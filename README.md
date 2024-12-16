# prandtlAirfoils
Aerodynamic analysis on all airfoils used in the Prandtl investigation.


To do:
Insert benchmark results with NACA 23012
 - Abbot & von Doenhoff windtunnel
 - Then XFOIL
 - Then CFD
 - Then write up this results
 - Benchmark this profile against Abbot and von Doenhoff and try to match as close as possible, by tripping the flow and trying everything to match.

Then proceed to the following tasks:



HQ profiles:

Digitize and smooth the profiles in XFoil.
Digitize all aero data on these profiles for comparison.
Rerun all the aero data for these profiles and compare with the measured and designed lift, drag and Cp data.
Use these profiles as examples of how to make laminar flow profiles that have reflex.



Prandtl profiles:

Analyze the profiles for the operating conditions of the full scale aircraft.
Also trip the flow early to see how turbulence increases drag.

Then run these profiles at low Reynolds number as achieved with the small model.  Assume fully turbulent flows by tripping the flow immediately.  See how the drag increases and try to match the drag to the worked back drag from flight test.  Therefore work out the CD for the whole wing and apply a 2D to 3D adjustment and then see how close it is.  Also the Reynolds numbers are very low for the model.  This might also bring down L/D.  Use this to try and explain maybe the poor performance of the model aircraft.

Then do CFD on all the profiles and see how closely it matches with the XFoil results.
Use OpenFoam.

Write up the results as a report.





Analyse HQ36 and document with XFOIL
Analyse Prandtl root and tip and document with XFOIL
Write LaTeX macro to plot drag polar.
CFD all profiles.  Use OpenFoam
Also plot over windtunnel results of the HQ profiles and the NACA23012
Compare windtunnel, CFD and XFOIL.  Check how close predictions are.