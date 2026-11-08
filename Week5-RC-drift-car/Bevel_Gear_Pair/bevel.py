import math, sys
from build123d import *

def profile_pts(m, z, add, ded, backlash):
    rp = m*z/2; rb = rp*math.cos(math.radians(20)); ra = rp+add; rf = rp-ded
    inv = lambda a: math.tan(a)-a
    ap = math.radians(20)
    def half(r):
        a = math.acos(min(1.0, rb/r))
        return math.pi/(2*z)+inv(ap)-inv(a)-(backlash/2)/rp
    r0 = max(rf, rb)
    rs = [r0+(ra-r0)*k/6 for k in range(7)]
    pts=[]
    for i in range(z):
        phi = 2*math.pi*i/z
        seq=[(rf,phi-half(rs[0]))]+[(r,phi-half(r)) for r in rs]+[(r,phi+half(r)) for r in reversed(rs)]+[(rf,phi+half(rs[0]))]
        for r,t in seq:
            p=(r*math.cos(t), r*math.sin(t))
            if not pts or math.dist(p,pts[-1])>1e-3: pts.append(p)
    if math.dist(pts[0],pts[-1])<1e-3: pts.pop()
    return pts

def bevel_gear(m=1.0, z=24, face=5.5, bore=4.3, backlash=0.3, hub_d=14.0, hub_h=6.0):
    d = math.pi/4                       # 45 deg pitch cone (1:1 miter pair)
    rp = m*z/2; Re = rp/math.sin(d)
    s = (Re-face)/Re
    pts = profile_pts(m, z, m*math.cos(d), 1.25*m*math.cos(d), backlash)
    H = rp/math.tan(d)                  # apex height above big end plane
    z_small = H*(1-s)
    big = Face(Wire.make_polygon([Vector(x,y,0) for x,y in pts], close=True))
    small = Face(Wire.make_polygon([Vector(x*s,y*s,z_small) for x,y in pts], close=True))
    g = loft([big, small], ruled=True)
    g += Pos(0,0,-hub_h/2)*Cylinder(hub_d/2, hub_h)       # hub below the wide end
    g -= Cylinder(bore/2, 60)
    # M3 set screw (radial) + nut trap in the hub
    g -= Pos(0,0,-hub_h/2)*(Rot(Y=90)*Cylinder(1.7, hub_d+2))
    g -= Pos(0,0,-hub_h/2)*Pos(0,3.6,0)*Box(5.7,2.6,5.8)
    return g, dict(rp=rp, Re=Re, s=s, z_small=z_small, od=2*(rp+m*math.cos(d)))

if __name__=="__main__":
    g,info = bevel_gear()
    print(info, g.volume/1000, g.is_valid)
    bb=g.bounding_box(); print(bb.size)
    export_stl(g,"Bevel_Gear_24T.stl"); export_step(g,"Bevel_Gear_24T.step")
