"""RunMPC 'Sine' logo — final master geometry as filled outlines (no strokes, no text).
Construction: monoline lowercase on x-height 100, stroke w (default 22), butt terminals,
circular arcs only, 1.5-unit overshoot on round forms. All sub-paths wound clockwise and
united with the nonzero rule; counters are counter-clockwise sub-paths (real holes)."""
import math, sys
INK='#0E0E12'; ACC='#FF4B2B'; WHITE='#FFFFFF'
O=1.5  # overshoot
def f(v): v=round(v,2); return (f'{v:.2f}').rstrip('0').rstrip('.') if v!=int(v) else str(int(v))
def pt(cx,cy,r,a): return cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a))
def vline(x,y0,y1,h): return f'M{f(x-h)} {f(y0)}H{f(x+h)}V{f(y1)}H{f(x-h)}Z'
def band(cx,cy,r,a0,a1,h):
    R,ri=r+h,r-h; large=1 if (a1-a0)>180 else 0
    (x0,y0),(x1,y1)=pt(cx,cy,R,a0),pt(cx,cy,R,a1); (x2,y2),(x3,y3)=pt(cx,cy,ri,a1),pt(cx,cy,ri,a0)
    return f'M{f(x0)} {f(y0)}A{f(R)} {f(R)} 0 {large} 1 {f(x1)} {f(y1)}L{f(x2)} {f(y2)}A{f(ri)} {f(ri)} 0 {large} 0 {f(x3)} {f(y3)}Z'
def ring(cx,cy,r,h):
    R,ri=r+h,r-h
    return (f'M{f(cx-R)} {f(cy)}A{f(R)} {f(R)} 0 1 1 {f(cx+R)} {f(cy)}A{f(R)} {f(R)} 0 1 1 {f(cx-R)} {f(cy)}Z'
            f'M{f(cx-ri)} {f(cy)}A{f(ri)} {f(ri)} 0 1 0 {f(cx+ri)} {f(cy)}A{f(ri)} {f(ri)} 0 1 0 {f(cx-ri)} {f(cy)}Z')
def glyph(ch,x,w):
    """returns (d, ink_right) for a glyph whose stem centreline sits at x"""
    h=w/2
    if ch=='r':
        ra=40; cy=ra+h-O
        return vline(x,0,100,h)+band(x+ra,cy,ra,180,270,h), x+ra
    if ch=='W':  # the 'un' sine wave
        rr=30; yb=100+O-rr-h; yt=-O+rr+h
        d=vline(x,0,yb,h)+band(x+rr,yb,rr,0,180,h)+vline(x+2*rr,yt,yb,h)+band(x+3*rr,yt,rr,180,360,h)+vline(x+4*rr,yt,100,h)
        return d, x+4*rr+h
    if ch=='m':
        rm=27; cy=-O+rm+h
        d=vline(x,0,100,h)+band(x+rm,cy,rm,180,360,h)+vline(x+2*rm,cy,100,h)+band(x+3*rm,cy,rm,180,360,h)+vline(x+4*rm,cy,100,h)
        return d, x+4*rm+h
    if ch=='p':
        rp=50+O-h
        return vline(x,0,135,h)+ring(x+rp,50,rp,h), x+2*rp+h
    if ch=='c':
        rp=50+O-h; cx=x+rp
        return band(cx,50,rp,45,315,h), cx+(rp+h)*math.cos(math.radians(45))
GAPS={('r','W'):12,('W','m'):20,('m','p'):20,('p','c'):15}
def wordmark(w=22,word="rWmpc"):
    """returns list of (d, role) and ink bbox"""
    h=w/2; out=[]; cursor=0; prev=None
    for ch in word:
        gap=GAPS.get((prev,ch),0) if prev else 0
        x=cursor+gap+h
        d,right=glyph(ch,x,w); out.append((d,'acc' if ch=='W' else 'ink')); cursor=right; prev=ch
    return out,(0,-O,cursor,135)
def symbol(w=22):
    d,right=glyph('W',w/2,w); return [(d,'acc')],(0,-O,right,100+O)
def place(parts,bbox,s,tx,ty,cols):
    x0,y0,_,_=bbox; o=''
    for role in ('ink','acc'):
        ds=''.join(d for d,r in parts if r==role)
        if ds: o+=f'<path fill="{cols[role]}" d="{ds}"/>'
    return f'<g transform="translate({f(tx-x0*s)} {f(ty-y0*s)}) scale({f(s)})">{o}</g>'
def svg(vw,vh,body,title):
    vw,vh=math.ceil(vw),math.ceil(vh)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(vw)} {f(vh)}" width="{f(vw)}" height="{f(vh)}" role="img" aria-labelledby="t">'
            f'<title id="t">{title}</title>{body}</svg>\n')
def write(name,s): open(name,'w').write(s)
COL={'color':{'ink':INK,'acc':ACC},'black':{'ink':'#000000','acc':'#000000'},'white':{'ink':WHITE,'acc':WHITE},'reversed':{'ink':WHITE,'acc':ACC}}
def build():
    pad=24
    for var,cols in COL.items():
        w=21.3 if var in ('white','reversed') else 22   # thinner on dark: irradiation correction
        # wordmark (primary horizontal), height 256
        parts,bb=wordmark(w); bw,bh=bb[2]-bb[0],bb[3]-bb[1]; s=(256-2*pad)/bh
        write(f'runmpc-wordmark-{var}.svg',svg(bw*s+2*pad,256,place(parts,bb,s,pad,pad,cols),'RunMPC logo'))
        # symbol (the sine), 256 square, optical centre 2% high
        parts,bb=symbol(w); bw,bh=bb[2]-bb[0],bb[3]-bb[1]; s=(256*0.74)/bw
        write(f'runmpc-symbol-{var}.svg',svg(256,256,place(parts,bb,s,(256-bw*s)/2,(256-bh*s)/2-5,cols),'RunMPC symbol'))
        # stacked: symbol over wordmark
        sp,sbb=symbol(w); wp,wbb=wordmark(w); ws=1.0; ww=(wbb[2]-wbb[0])*ws; wh=(wbb[3]-wbb[1])*ws
        ss=ww*0.42/(sbb[2]-sbb[0]); sw=(sbb[2]-sbb[0])*ss; sh=(sbb[3]-sbb[1])*ss; gap=44
        W_=ww+2*pad*2; H_=sh+gap+wh+2*pad*2
        body=place(sp,sbb,ss,(W_-sw)/2,pad*2,cols)+place(wp,wbb,ws,(W_-ww)/2,pad*2+sh+gap,cols)
        write(f'runmpc-stacked-{var}.svg',svg(W_,H_,body,'RunMPC logo stacked'))
    # small-size cut: heavier, for 16-32 px (favicon source)
    parts,bb=symbol(27); bw,bh=bb[2]-bb[0],bb[3]-bb[1]; s=(256*0.84)/bw
    write('runmpc-symbol-small.svg',svg(256,256,place(parts,bb,s,(256-bw*s)/2,(256-bh*s)/2-4,COL['color']),'RunMPC symbol small'))
build()
