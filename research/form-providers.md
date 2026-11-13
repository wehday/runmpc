# Form providers for Submission and Interest registration

Research for [#3](https://gitea.wehday.com/wehday/run-mpc/issues/3), part of #1.

**Question.** Which form provider fits two public forms on a static site (Cloudflare Pages): a Submission form and an Interest registration form? Options: Typeform, Tally, Formspree, plain `mailto:`.

**Constraints from GLOSSARY.md.** A Submission is a request to add an Item. It is not an Item until accepted. An Interest registration is a request to hear when community accounts open. Every Submission also counts as an Interest registration, so whatever we pick has to put both kinds of record in one place and label each with its kind.

All sources accessed 2026-11-13. Numbers come from vendor pages and can change without notice. Footnotes point to the Sources section.

## Comparison

| | Typeform | Tally | Formspree | `mailto:` |
|---|---|---|---|---|
| Free responses / month | **10, shared across all forms** [T1][T2]. At the limit, forms go private until the next billing month [T2] | Unlimited, subject to fair use [L1][L2]. Fair-use examples of "extensive usage" start at 50,000 submissions/month [L2] | **50** [F1][F2] | No limit. Each one is an email |
| Free forms | Unlimited [T1] | Unlimited [L1][L7] | Unlimited [F1][F2] | n/a |
| Cheapest paid tier | Basic $39/mo or $28/mo yearly, 100 responses [T3] | Pro $24/mo [L1] | Personal $15/mo or $10/mo yearly, 200 submissions [F1] | n/a |
| Data export (free) | Spreadsheet export of responses [T2] (help page, see note 1) | CSV download from the Submissions tab. Google Sheets sync is free [L7][L1] | **No.** Export is listed only on paid plans [F1][F5]. Dashboard shows the last 30 days [F2] | Whatever your mailbox exports |
| Email notification to owner (free) | Not confirmed for free. Pricing lists "email notifications" without saying which tiers [T3]. Respondent follow-up emails are paid [T2] | Yes, self notifications [L1][L3]. Respondent emails are Pro [L3] | Yes, up to 2 linked addresses [F1][F2]. Autoresponses are paid [F1] | The email is the notification |
| Consent checkbox | "Legal" question type: explicit accept or decline [T2] | Checkbox block, which the docs name as usable for consent [L4] | Any HTML checkbox. You write the form markup yourself | No form controls. Consent would have to be implied by the act of sending |
| UK GDPR: where data is stored | AWS, main servers in Virginia, USA. EU hosting (Frankfurt) only on Enterprise / Growth Custom, and not for existing accounts [T4][T5] | Europe: Google Cloud Belgium, Cloudflare EU. Email notifications go through SendGrid (US) [L5] | AWS, hosted in the US [F3]. Privacy policy names no region or sub-processors [F4] | Your mail provider |
| UK GDPR: DPA | Public DPA is written for Enterprise plans and takes effect on signature [T6]. Help pages say the Privacy Policy covers GDPR duties for other plans (see note 1) | DPA comes with the Terms. Professional users accept it at sign-up, no signature needed [L5][L6] | No DPA found. Security page says it relies on SCCs as a processor [F3]. Privacy policy does not mention a DPA or SCCs [F4] | None needed with a third-party form vendor. The mail provider's own terms apply |
| UK transfer basis | US: needs the UK Extension (data bridge) or the DPA's UK Addendum [T6][U1] | EEA has full UK adequacy [U1]. US sub-processors are opt-in features [L5] | US: SCCs claimed [F3]. No UK Addendum or IDTA found | n/a |
| Embed vs link-out | Inline, full page, popup, slider, popover, side tab. Not embeddable on non-HTTPS pages [T7] | Standard and popup embeds on free, or link-out [L3] | Your own HTML `<form>` posts to the endpoint (native, no iframe) [F6] | Link only. Opens the visitor's mail client |
| Spam protection (free) | Not confirmed for free | reCAPTCHA v2, free for all users [L8] | Built-in filtering ("Formshield") and reCAPTCHA [F1]. `_gotcha` honeypot on all plans [F7]. Custom honeypot and spam rules are paid [F1] | None. RFC 6068 warns that `mailto:` links on public pages expose the address to harvesting [M1] |
| Tag a record as Submission or Interest registration | URL parameters (formerly Hidden Fields) are a free feature [T8] | Hidden fields, free, filled from URL params [L9] | Hidden `<input>` in our own markup, or the `data` option on the JS client [F6] | Fixed `subject=` / `body=` in the link [M1]. The sender can edit it, so it is not reliable |
| Branding on free | Typeform branding; removal from Plus [T3] | "Made with Tally"; removal is Pro [L1] | None. It is our markup | None |

## Which options meet the constraints

These findings are not a decision.

- **Typeform: fails the volume constraint.** Ten responses a month across both forms is not enough for a public launch. Default data storage is in the US, and EU hosting is only on Enterprise. Meeting the constraints would mean paying at least $28-39/mo for 100 responses.
- **Tally: meets every constraint on the free tier.** Responses are effectively unlimited, CSV export is free, data is stored in the EU, the DPA comes with the Terms, reCAPTCHA is free, and hidden fields are free. Two catches: the free forms carry Tally branding, and notification emails go through SendGrid in the US. The GDPR page lists that as an opt-in sub-processor, so it belongs in our privacy notice.
- **Formspree: works at low volume. Weakest GDPR position.** It is the only option where the form is our own native HTML, which keeps it on-brand. But the free tier has 50 submissions a month, no export, and only 30 days of visible history. Data is stored in the US and we found no published DPA or UK transfer document. Personal ($10-15/mo) adds export and 200 submissions.
- **`mailto:`: no vendor and no DPA, but no structure.** We get no consent checkbox, no spam protection, and no reliable tagging (the sender can edit the subject). The address is exposed to harvesters, and we would have to copy records into a list by hand. It is fine as a stopgap. It does not give a list we can export when accounts open.

## Tagging: one store, two kinds

The glossary rule "a Submission also counts as an Interest registration" holds on every form option if both forms write to the same place:

1. **Two forms with a hidden `kind` field.** Use `kind=submission` and `kind=interest`. Each form's link or embed sets it through URL parameters: Typeform URL parameters [T8], Tally hidden fields [L9], a Formspree hidden input [F6]. On Tally, both forms can sync to the same Google Sheet [L1], which gives one list. On Formspree, both forms can post to the same form endpoint, so one submission log holds both kinds.
2. **One form with a branch.** An opening question ("Suggest an Item" or "Just notify me") sends the person down a different path. Every respondent leaves an email and a consent tick, so every Submission is automatically an Interest registration. The branch answer is the tag.

Either way, the Interest registration list is "all rows with consent = yes", whatever their `kind`.

## Notes

1. **Typeform help centre blocked direct fetch.** `help.typeform.com` returned HTTP 403 to our fetcher. Typeform's own search index was used for [T2] and [T4] instead, and the 10-response figure is also confirmed on `typeform.com/platform-overview` [T1]. Community posts mention a legacy free tier of 100 responses a month per form. Typeform staff say that is the old plan. New accounts get 10.
2. **Formspree's legal pages are thin.** The privacy policy names no hosting region, sub-processors, DPA, or SCCs [F4]. Only the security page mentions AWS US and SCCs [F3]. If Formspree is shortlisted, ask team@formspree.io for a DPA before going live.
3. **UK adequacy.** The UK treats all EEA states as adequate. The US has partial adequacy, covering only organisations certified under the UK Extension to the EU-US Data Privacy Framework [U1]. Tally's EU storage needs no transfer mechanism. Typeform and Formspree (US) need either DPF certification or SCCs plus the UK Addendum or an IDTA. We did not check either company's DPF certification status.
4. **Not checked:** Typeform's free-plan reCAPTCHA and owner notifications. A Tally comparison page claims reCAPTCHA is $79/mo on Typeform, but that is a competitor's claim, not a primary source. Whether Tally's checkbox block can be marked required is also unchecked: the input-blocks page does not say [L4].

## Sources

All accessed 2026-11-13.

- [T1] Typeform, Platform overview (FAQ: "up to 10 responses per month"). https://www.typeform.com/platform-overview
- [T2] Typeform Help Center, Free plan. https://help.typeform.com/hc/en-us/articles/360032972852-Free-plan (403 to direct fetch, content via search index). Also: Updates to your Free plan, https://help.typeform.com/hc/en-us/articles/18480888260756-Updates-to-your-Free-plan
- [T3] Typeform, Plans & Pricing. https://www.typeform.com/pricing
- [T4] Typeform Help Center, What happens to my data? https://help.typeform.com/hc/en-us/articles/360029581691-What-happens-to-my-data (via search index)
- [T5] Typeform Developers, Interacting with the EU Responses Data Center. https://www.typeform.com/developers/get-started/responses-data-center/
- [T6] Typeform, Data Processing Agreement. https://www.typeform.com/dpa
- [T7] Typeform Developers, Embed. https://www.typeform.com/developers/embed/
- [T8] Typeform Help Center, Using URL parameters (formerly Hidden Fields). https://help.typeform.com/hc/en-us/articles/360052676612-Using-URL-parameters-formerly-Hidden-Fields (via search index)
- [L1] Tally, Pricing. https://tally.so/pricing
- [L2] Tally, Fair use policy. https://tally.so/help/fair-use-policy
- [L3] Tally, Features. https://tally.so/features
- [L4] Tally, Input blocks. https://tally.so/help/input-blocks
- [L5] Tally, GDPR (storage location, sub-processors, DPA). https://tally.so/help/gdpr
- [L6] Tally, Data Processing Agreement. https://tally.so/help/data-processing-agreement
- [L7] Tally, FAQ. https://tally.so/help/faq
- [L8] Tally, Block spam with reCAPTCHA. https://tally.so/help/recaptcha
- [L9] Tally, Hidden fields. https://tally.so/help/hidden-fields
- [F1] Formspree, Plans. https://formspree.io/plans
- [F2] Formspree Docs, Account limits. https://help.formspree.io/articles/account-management/account-limits
- [F3] Formspree, Security. https://formspree.io/security/
- [F4] Formspree, Privacy Policy. https://formspree.io/legal/privacy-policy/
- [F5] Formspree Docs, Exporting submissions. https://help.formspree.io/hc/en-us/articles/4415183464979-Exporting-Submissions
- [F6] Formspree Docs, Submit forms with JavaScript (AJAX). https://help.formspree.io/hc/en-us/articles/360013470814-Submit-forms-with-JavaScript-AJAX
- [F7] Formspree Docs, Honeypot spam filtering. https://help.formspree.io/articles/building-your-form/honeypot-spam-filtering/
- [M1] RFC 6068, The 'mailto' URI Scheme (section 2 hfields, section 7 security considerations). https://www.rfc-editor.org/rfc/rfc6068
- [U1] ICO, Is the restricted transfer covered by adequacy regulations? https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/international-transfers/adequacy-regulations/is-the-restricted-transfer-covered-by-adequacy-regulations/
