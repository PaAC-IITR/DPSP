from vpython import *
#GlowScript 3.1 VPython
from vpython import *
canvas(background=color.black, height=800, width = 1520)

s1 = sphere(pos=vector(-1e11,0,0), radius=1e10, color=color.white,make_trail=True, trail_type='curve', interval=1000)
s1.mass = 2e30
s1_axis = cylinder(pos= vector(-1e11,0,-3e10), axis = vector(0,0,6e10), radius=0.2e9, color = color.white, make_trail=True)
s1_jet = cone(pos = vector(-1.05e11,0, 4e10), axis = vector(0.05e11,0,-4.2e10), radius = 0.3e10, opacity = 0.5)
s1_jet_inv = cone(pos = vector(-.95e11,0, -4e10), axis = vector(-0.05e11,0,4.2e10), radius = 0.3e10, opacity=0.5)
#lamp1 = local_light(pos = vector(-1.05e11,0, 4e10), color= vector(1,1,1))
#lamp2 = local_light(pos = vector(-.95e11,0, -4e10), color= vector(1,1,1))
s1_planet = compound([s1,s1_axis, s1_jet, s1_jet_inv])
s1_planet.p = vector(0, -0.5e4, 0) * s1.mass


s2 = sphere(pos=vector(1.5e11,0,0), radius=0.5e10, color=color.green,make_trail=True, trail_type='curve', interval=1000)
s2_axis = cylinder(pos= vector(1.5e11,0,-3e10), axis = vector(0,0,6e10), radius=0.2e9, color = color.white,make_trail=True)
s2.mass = 1e30
s2_jet = cone(pos = vector(1.52e11,0, -2.5e10), axis = vector(-0.02e11,0,2.7e10), radius = 0.2e10, opacity=0.5)
s2_jet_inv = cone(pos = vector(1.48e11,0, 2.5e10), axis = vector(0.02e11,0,-2.7e10), radius = 0.2e10, opacity=0.5)
s2_planet = compound([s2,s2_axis, s2_jet, s2_jet_inv])
s2_planet.p = vector(0, 1.0e4, 0) * s2.mass

#centreofmass = sphere(pos=(s2.mass*s2.pos+s1.mass*s1.pos)/(s2.mass+s1.mass), radius=0.2e10, color=color.yellow, make_trail=True, trail_type='curve', interval=1000)
omega=0.1e-5
dt = 50

while True:
    rate(2000000000)
    r = s2_planet.pos - s1_planet.pos
    F = 6.67e-11*s1.mass*s2.mass*r.hat / mag(r)**2
    s1_planet.rotate(angle = omega*dt, axis=vector(0,0,1))
    s2_planet.rotate(angle = omega*dt, axis=vector(0,0,1))
    s1_planet.p  = s1_planet.p + F*dt
    s2_planet.p  = s2_planet.p - F*dt
    s1_planet.pos  = s1_planet.pos + (s1_planet.p/s1.mass) * dt
    s2_planet.pos = s2_planet.pos + (s2_planet.p/s2.mass) * dt
