GlowScript 3.1 Vpython

canvas(background=color.black, height=800, width = 1520)
s1 = sphere(pos=vector(-1e11,0,0), radius=1e10, color=color.white,make_trail=True, trail_type='curve', interval=1000)

s1.mass = 2e30
s1.p = vector(0, -0.5e4, 0) * s1.mass

s2 = sphere(pos=vector(1.5e11,0,0), radius=0.5e10, color=color.green,make_trail=True, trail_type='curve', interval=1000)

s2.mass = 1e30
s2.p = vector(0, 1.0e4, 0) * s2.mass


dt = 10
while True:
    rate(2000000000)
    r = s2.pos - s1.pos
    F = 6.67e-11*s1.mass*s2.mass*r.hat / mag(r)**2
    
    s1.p  = s1.p + F*dt
    s2.p  = s2.p - F*dt
    s1.pos  = s1.pos + (s1.p/s1.mass) * dt
    s2.pos = s2.pos + (s2.p/s2.mass) * dt
   
    
