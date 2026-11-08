A fully 3D-printed 1/16 scale RC drift car, designed in Fusion 360 around a brushless motor, a printed gear drivetrain and a servo-steered front end. Everything except the electronics, bearings, shafts and pinion is printed in ABS.

<img width="1175" height="925" alt="Screenshot 2026-11-08 180758" src="https://github.com/user-attachments/assets/4e7a0d31-9356-4a5b-8a24-9b3dae2eeb33" />
<img width="1342" height="934" alt="Screenshot 2026-11-08 173655" src="https://github.com/user-attachments/assets/e7e99339-5ffe-4da1-b9b3-41e23dbf1068" />
<img width="1239" height="914" alt="Screenshot 2026-11-08 173633" src="https://github.com/user-attachments/assets/06afe149-0200-442b-b310-f4ac43966150" />

How it works
Power: Surpass Hobby 2847 4300KV brushless motor, a 35A ESC and a 2S 7.4V 18650 battery pack.
Drivetrain: The motor's 18-tooth metal pinion (module 0.6) drives a printed 68-tooth spur gear, a 3.78:1 reduction. The spur gear is on a drive shaft that runs along the car to a pair of printed 24-tooth bevel gears. They turn the drive through 90° onto a solid rear axle running on two 608 bearings.
Steering: An S0017M servo drives both front wheels through a servo horn and a link. The front wheels are on printed knuckles with 608 bearings.
Wheels: Printed 55 mm wheels with rubber-style tyres. The rear wheels are wider than the front ones so the car slides easily.
Size: About 180 mm wheelbase and 148 mm wide.
Design notes
Gear ratio: I worked it out from the motor's KV, the battery voltage and the wheel size. Without a limit it would be far too fast for a car this size, so the plan is to cap the throttle on the first runs.
Printed gears: Both gear sets are modelled with backlash for ABS shrinkage (0.25 mm on the spur gear, 0.3 mm on the bevels). I estimated the load on the spur gear teeth at about 14 N at peak, which gives a bending stress of about 9 MPa. That's about a factor of 2 under what ABS can take, so I keep a spare.
Bevel gears: The two gears are identical and their cone tips meet at one point on the axle line. Mounts are slotted so I can shim them in and out.
Fit checks: I imported models of the motor, servo, bearings and battery into the assembly and ran Fusion's interference check.
Files
RC drift car.f3d Fusion 360 model
STL/ printable parts
Parts
Qty	Part
1	Surpass Hobby 2847 4300KV brushless motor
1	Surpass Hobby 35A ESC
1	S0017M servo
1	2S 7.4V 18650 battery pack (1500 mAh)
1	18-tooth metal pinion, module 0.6
6+	608zz bearings
2	Steel shafts for the drive shaft and rear axle
-	M2 and M3 screws, nuts, ABS filament
Status
Designed and checked in CAD. Next up is printing, testing the steering and the gear mesh, and adding a body shell.
