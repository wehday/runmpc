# Gitea-GitHub mirroring and Cloudflare Pages deploy

Research for [#4](https://gitea.wehday.com/wehday/run-mpc/issues/4) (part of #1). All sources accessed 2026-11-13. Gitea findings checked against the instance version reported by `GET /api/v1/version`: **28.2.0**. Source-code citations are pinned to tag `v28.2.0` of go-gitea/gitea.

This note lays out options. It does not pick one.

## Short answer

- **True two-way mirroring is not something Gitea or GitHub do natively.** Gitea has pull mirrors (read-only copies of a remote) and push mirrors (force-push of everything to a remote). GitHub has no built-in mirror feature at all. One Gitea repo *can* be a pull mirror and also carry push mirrors, but that is a one-way chain, not two-way sync.
- **Cloudflare Pages can deploy without GitHub.** Pages Git integration supports only GitHub and GitLab (cloud, not self-hosted), so Gitea cannot connect directly. Direct Upload via `wrangler pages deploy` from a Gitea Actions runner is a documented path.
- **Free tier is ample for a static catalogue** (static requests free and unlimited, 20,000 files, 25 MiB per file). runmpc.com is already registered at Cloudflare with Cloudflare nameservers, so the apex-domain requirement is already met.

## 1. Gitea mirroring

### Pull mirror (remote to Gitea)

- Created only through **New Migration** with "This repository will be a mirror" ticked. "You can only set up pull mirroring for repos that don't exist yet on your instance." ([docs.gitea.com/usage/repo-mirror](https://docs.gitea.com/usage/repo-mirror))
- So `wehday/run-mpc`, which already exists, **cannot be converted into a pull mirror**. It would need to be recreated as a new migration.
- **Read-only.** Gitea rejects pushes to a mirror repo over SSH (`"Mirror Repository %s is read-only"`, [routers/private/serv.go#L172](https://github.com/go-gitea/gitea/blob/v28.2.0/routers/private/serv.go#L172)) and over HTTP (`"mirror repository is read-only"`, [routers/web/repo/githttp.go#L201](https://github.com/go-gitea/gitea/blob/v28.2.0/routers/web/repo/githttp.go#L201)). Issues, PRs etc. still live on Gitea, but code changes must land on the upstream.
- **Sync mechanics:** `git fetch --tags [--prune] <remote>` ([services/mirror/mirror_pull.go#L126](https://github.com/go-gitea/gitea/blob/v28.2.0/services/mirror/mirror_pull.go#L124)). Upstream state wins.
- A pull mirror can be converted to a normal repo later (settings "convert"), which ends mirroring.

### Push mirror (Gitea to remote)

- Added to any existing repo under Settings > Repository > Mirror Settings. For GitHub: create the target repo first ("GitHub does not support creating repositories by pushing to the remote"), use `https://github.com/<owner>/<repo>.git`, GitHub username, and a PAT with `public_repo` scope (plus `workflow` if the repo contains GitHub Actions workflow files). ([docs.gitea.com/usage/repo-mirror](https://docs.gitea.com/usage/repo-mirror))
- **SSH push mirrors are not supported**: "Currently Gitea supports no ssh push mirrors." HTTPS + token only. (same page)
- **Overwrites the remote**: "This will force push to the remote repository. This will overwrite any changes in the remote repository!" (same page). Code confirms `Force: true, Mirror: true` ([services/mirror/mirror_push.go#L158-L162](https://github.com/go-gitea/gitea/blob/v28.2.0/services/mirror/mirror_push.go#L158-L162)), i.e. `git push --mirror --force`: branches/tags absent on Gitea are deleted on GitHub, and any commit made directly on GitHub is discarded on next sync.
- **"Sync when commits are pushed"** option (Gitea 1.18+) pushes immediately on each push instead of waiting for the interval.
- LFS objects are pushed too when LFS is enabled ([mirror_push.go#L150](https://github.com/go-gitea/gitea/blob/v28.2.0/services/mirror/mirror_push.go#L150)).

### Can one repo be both?

- **Yes, mechanically.** The push-mirror table and "add" form render for any repo, including pull mirrors; the only gates are `DISABLE_NEW_PUSH` and archived status ([templates/repo/settings/options.tmpl#L199-L257](https://github.com/go-gitea/gitea/blob/v28.2.0/templates/repo/settings/options.tmpl#L199-L257), [routers/web/repo/setting/setting.go#L494](https://github.com/go-gitea/gitea/blob/v28.2.0/routers/web/repo/setting/setting.go#L494)).
- **But that is a chain (A to Gitea to B), not two-way.** If Gitea pulls from GitHub and also push-mirrors to GitHub, the push mirror would force-push Gitea's (possibly stale) copy over GitHub, discarding new GitHub commits that the pull has not fetched yet. Docs do not discuss this; the risk follows from the force-push behaviour above.

### Sync intervals (instance-level config)

From `app.example.ini` at v28.2.0 ([custom/conf/app.example.ini](https://github.com/go-gitea/gitea/blob/v28.2.0/custom/conf/app.example.ini), `[mirror]` and `[cron.update_mirrors]`):

| Setting | Default | Meaning |
|---|---|---|
| `[mirror] DEFAULT_INTERVAL` | `8h` | Default per-mirror interval |
| `[mirror] MIN_INTERVAL` | `10m` | Floor for per-mirror interval (code clamps to >= 1m) |
| `[cron.update_mirrors] SCHEDULE` | `@every 10m` | How often the scheduler queues due mirrors |
| `PULL_LIMIT` / `PUSH_LIMIT` | `50` | Mirrors queued per run |

Per-mirror intervals are editable in the UI. Interval `0` disables periodic sync ([options/locale/locale_en-US.json#L1011](https://github.com/go-gitea/gitea/blob/v28.2.0/options/locale/locale_en-US.json#L1011)). The homelab instance's actual values were not checked (needs server config access).

### GitHub side

GitHub has no pull-mirror feature. Its docs describe mirroring as a manual `git clone --mirror` then periodic `git fetch -p origin && git push --mirror`, noting local refs are "overwritten each time you fetch". ([docs.github.com: Duplicating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository))

### Viable mirroring options

| Option | How | Writable on | Conflict behaviour | Notes |
|---|---|---|---|---|
| **M1. Gitea canonical, push mirror to GitHub** | Push mirror with "sync on commit" | Gitea only (GitHub is a read-only copy by convention) | Anything pushed/merged on GitHub is overwritten | Native, zero code. GitHub PRs from others would need to be re-applied on Gitea. |
| **M2. GitHub canonical, Gitea pull mirror** | Recreate `wehday/run-mpc` as a migration with mirror ticked | GitHub only (Gitea rejects pushes) | Upstream wins | Existing Gitea issues (#1-#4 etc.) would not carry over to a recreated repo automatically. Gitea Actions on a mirror repo: not verified. Min 10m lag unless synced manually. |
| **M3. Scripted two-way sync** | CI job(s) on each side that fetch the other and push with a normal (non-force) push, e.g. Gitea Actions on push + GitHub Actions on push, or a cron | Both | Non-fast-forward pushes fail; someone has to merge/rebase by hand. Must avoid ping-pong loops (skip if refs already equal). | Not a Gitea feature; custom maintenance. Do not combine with a force push mirror. |
| **M4. Push to both from the client** | `git remote set-url --add --push origin <github-url>` so one `git push` hits both | Both, as long as everyone pushes this way | Second push rejects if remotes diverged | Purely local git config; Web UI merges on either side bypass it. |

## 2. Cloudflare Pages

### Git integration

- "Cloudflare supports connecting Cloudflare Pages to your GitHub and GitLab repositories." "Pages does not currently support connecting self-hosted instances of GitHub or GitLab." Other providers or self-hosted instances should start with a Direct Upload project. ([developers.cloudflare.com/pages/configuration/git-integration](https://developers.cloudflare.com/pages/configuration/git-integration/))
- **Gitea cannot connect directly.** Git integration would need the GitHub copy (options M1-M4).
- **Lock-in both ways:** "If you deploy using the Git integration, you cannot switch to Direct Upload later." (same page) and a Direct Upload project "cannot switch to Git integration later" ([direct-upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)). Changing method means a new Pages project (custom domain can be moved).
- With M1 (force-push mirror) feeding a Git-integrated project, Cloudflare would build from GitHub, so deploys depend on the mirror having synced.

### Direct Upload from CI (`wrangler pages deploy`)

- API token: Custom Token with **Account > Cloudflare Pages > Edit**. Env vars `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Command: `npx wrangler pages deploy <DIRECTORY> --project-name=<PROJECT_NAME>`. Wrangler needs Node 16.17.0+. ([use-direct-upload-with-continuous-integration](https://developers.cloudflare.com/pages/how-to/use-direct-upload-with-continuous-integration/))
- Tokens can be limited to the specific account, given an expiry, and IP-filtered ([create-token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)). IP filtering to the homelab's egress IP is possible.
- Flags: `--branch`, `--commit-hash`, `--commit-message`, `--commit-dirty`; project production branch set with `wrangler pages project create <name> --production-branch` ([wrangler pages commands](https://developers.cloudflare.com/workers/wrangler/commands/pages/)).
- Direct Upload projects have no production-branch control in the dashboard; it is set at creation by Wrangler or changed via the Update Project API ([direct-upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)).
- **On Gitea Actions:** `uses:` accepts absolute URLs to any git host, and bare action names fetch from GitHub by default unless `DEFAULT_ACTIONS_URL = self`. GitHub-only permission scopes such as `deployments` are not supported and `environment` is ignored ([docs.gitea.com/usage/actions/comparison](https://docs.gitea.com/usage/actions/comparison)). So Cloudflare's sample workflow (`cloudflare/wrangler-action` with `permissions: deployments: write` and `gitHubToken`) needs those lines dropped, or a plain `run: npx wrangler pages deploy ...` step on a runner image with Node.
- No GitHub account or repo is needed for this path.

### Preview deployments

- Every deployment gets `<hash>.<project>.pages.dev`; branch deployments also get an alias `<branch>.<project>.pages.dev` (lowercased, non-alphanumerics to hyphens). Previews are public by default; Cloudflare Access can restrict `*.<project>.pages.dev` previews to the account. ([preview-deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/))
- With Direct Upload, a deploy whose `--branch` differs from the production branch is a preview ([direct-upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)). So a Gitea Actions job on PR branches passing `--branch=${branch}` gives per-branch previews.
- Automatic PR comments with preview links are a Git-integration feature; with Direct Upload, the CI job would need to post the URL itself.

### Free-tier limits ([limits](https://developers.cloudflare.com/pages/platform/limits/))

| Limit | Free |
|---|---|
| Builds per month | 500 |
| Concurrent builds | 1 |
| Build timeout | 20 min |
| Files per site | 20,000 |
| Max file size | 25 MiB |
| Custom domains per project | 100 |
| Projects per account | 100 |
| `_headers` rules | 100 |
| `_redirects` | 2,000 static + 100 dynamic |
| Preview deployments | Unlimited |

- "On both free and paid plans, requests to static assets are free and unlimited." Pages Functions requests count against the Workers Free daily quota. ([functions/pricing](https://developers.cloudflare.com/pages/functions/pricing/))
- The limits page ties the build limits to Cloudflare's own build pipeline (pushes to a Git repo). It does not say whether Direct Upload deploys count toward the 500/month. Inference: they likely don't, since no build runs on Cloudflare, but this is not confirmed in docs.
- Drag-and-drop dashboard uploads are capped at 1,000 files; Wrangler uploads at 20,000 ([direct-upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)).

### Custom domain (runmpc.com)

- **Apex domain requires the domain to be a Cloudflare zone** with Cloudflare nameservers; Cloudflare then creates the record. Subdomains (e.g. `www`) can use an external CNAME to `<project>.pages.dev` without the zone being on Cloudflare. ([custom-domains](https://developers.cloudflare.com/pages/configuration/custom-domains/))
- The domain must be added under the Pages project's **Custom domains** first. A manual CNAME without that association fails to resolve (522). (same page)
- **Current state:** `dig NS runmpc.com` returns `cullen.ns.cloudflare.com` / `natasha.ns.cloudflare.com`, and WHOIS registrar is Cloudflare, Inc. (checked 2026-11-13). The apex requirement is already met.
- The `*.pages.dev` production URL can be redirected to the custom domain with a Bulk Redirect (same page).

## 3. Combined options

| | Mirroring | Deploy | GitHub needed for deploy? | Trade-off |
|---|---|---|---|---|
| **A** | None, or M1 for visibility | Gitea Actions + `wrangler pages deploy` | No | Fewest moving parts; deploy depends on homelab runner being up; preview links not auto-commented. |
| **B** | M1 (Gitea to GitHub push mirror) | Pages Git integration on GitHub repo | Yes | Cloudflare builds/previews/PR comments for free; GitHub becomes read-only; deploy lags on mirror sync if "sync on commit" is off. |
| **C** | M2 (GitHub canonical, Gitea pull mirror) | Pages Git integration on GitHub | Yes | Gitea becomes a read-only backup; existing Gitea repo would be recreated. |
| **D** | M3 or M4 (scripted/client two-way) | Either A or B | Depends | Meets "both ways" literally; needs custom sync and manual conflict handling. |

## Open questions for the owner

1. Which side should accept writes (pushes, merged PRs)? This decides M1 vs M2 vs M3/M4.
2. Is the homelab runner's availability acceptable as a deploy dependency (option A), or should Cloudflare build (B/C)?
3. Are public preview URLs acceptable, or should Cloudflare Access protect them?
4. Unverified: current `[mirror]` interval settings on gitea.wehday.com, and whether Gitea Actions runs on a pull-mirror repo.
