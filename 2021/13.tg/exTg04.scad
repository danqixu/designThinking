// Generated by SolidPython 1.1.1 on 2021-11-15 13:51:24
$fn = 50;


union() {
	cylinder(h = 0.2000000000, r = 1);
	rotate(a = [0, 0, 0]) {
		union() {
			translate(v = [2.5000000000, 0, 0]) {
				cylinder(h = 0.2000000000, r = 1);
			}
			translate(v = [0.4000000000, 0, 0]) {
				cube(size = [0.8000000000, 0.3000000000, 0.2000000000]);
			}
		}
	}
	rotate(a = [0, 0, 30]) {
		union() {
			translate(v = [2.5000000000, 0, 0.1000000000]) {
				cylinder(h = 0.2000000000, r = 1);
			}
			translate(v = [0.4000000000, 0, 0]) {
				cube(size = [0.8000000000, 0.3000000000, 0.2000000000]);
			}
		}
	}
	rotate(a = [0, 0, 60]) {
		union() {
			translate(v = [2.5000000000, 0, 0.2000000000]) {
				cylinder(h = 0.2000000000, r = 1);
			}
			translate(v = [0.4000000000, 0, 0]) {
				cube(size = [0.8000000000, 0.3000000000, 0.2000000000]);
			}
		}
	}
	rotate(a = [0, 0, 90]) {
		union() {
			translate(v = [2.5000000000, 0, 0.3000000000]) {
				cylinder(h = 0.2000000000, r = 1);
			}
			translate(v = [0.4000000000, 0, 0]) {
				cube(size = [0.8000000000, 0.3000000000, 0.2000000000]);
			}
		}
	}
	rotate(a = [0, 0, 120]) {
		union() {
			translate(v = [2.5000000000, 0, 0.4000000000]) {
				cylinder(h = 0.2000000000, r = 1);
			}
			translate(v = [0.4000000000, 0, 0]) {
				cube(size = [0.8000000000, 0.3000000000, 0.2000000000]);
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
# SolidPython example code 
# Brygg Ullmer, Clemson University
# Written 2021-10-28

from solid import *        # load in SolidPython/SCAD support code

outGeom = c1 = cylinder(r=1, h=.2)
count = 5; rot  = 0; rotIncr = 30
z = 0; dz = .1

s1 = cube([.8,.3,.2]) # s for feather "stem"
s2 = translate([.4,0,0])(s1)

for i in range(count):
  c2 = translate([2.5,0,z])(c1) + s2
  c3 = rotate([0,0,rot])(c2)
  outGeom += c3; rot += rotIncr; z += dz

radialSegments = 50; hdr = '$fn = %s;' % radialSegments # create a header for the export
scad_render_to_file(outGeom, 'exTg04.scad', file_header=hdr) # write the .scad file

### end ###

 
 
************************************************/
