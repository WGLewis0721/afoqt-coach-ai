# Aviation Information + Instrument Comprehension

Feeds Pilot and ABM. AI is the one rated subtest you can study as knowledge. IC is a visual skill with a short rule set.

## Four forces
In steady straight-and-level unaccelerated flight:
- Lift = Weight
- Thrust = Drag

Lift acts perpendicular to the relative wind (approximately upward in level flight).
Weight acts toward Earth through the center of gravity.
Thrust acts generally forward along the engine/prop axis.
Drag acts opposite to the flight path.

## How a wing makes lift
Two complementary descriptions:
1. Bernoulli: faster airflow over the curved upper surface → lower pressure above the wing.
2. Newton: wing deflects air downward; equal-and-opposite reaction is lift.

Angle of attack (AoA) is the angle between the chord line and the relative wind. Increase AoA → more lift, up to the critical AoA. Beyond critical AoA → stall. A stall is an aerodynamic event, not an engine failure. An airplane can stall at any airspeed/attitude if AoA is too high.

## Three axes and primary flight controls

| Control | Surface | Axis | Motion |
|---------|---------|------|--------|
| Ailerons | trailing edge of wings, differential | Longitudinal (nose-to-tail) | Roll / bank |
| Elevator (or stab) | horizontal tail | Lateral (wingtip-to-wingtip) | Pitch (nose up/down) |
| Rudder | vertical tail | Vertical | Yaw (nose left/right) |

Secondary / high-lift / drag:
- Flaps: increase camber (and often area) → more lift and more drag. Used for takeoff/landing to fly slower.
- Slats/slots: energize boundary layer at high AoA.
- Spoilers: dump lift, add drag.
- Trim tabs: hold a control surface so the pilot does not fight constant pressure.

Adverse yaw: downward aileron creates more lift AND more induced drag, yawing the nose away from the roll. Rudder coordinates the turn.

## Stability
- Positive static stability: displaced, tends to return.
- Longitudinal stability: pitch; related to CG vs center of lift / tail volume. Aft CG reduces stability and can make recovery ugly.
- Lateral stability: roll; dihedral helps.
- Directional stability: yaw; vertical stabilizer weathervanes the nose into the relative wind.

## Aircraft structure vocab
- Fuselage: body
- Empennage: tail assembly
- Wing spar, ribs, skin
- Landing gear: tricycle (nosewheel) vs tailwheel
- Propeller: accelerating a slipstream; also a spinning airfoil
- Jet engine: intake → compressor → combustor → turbine → exhaust
- Pitot tube: ram (dynamic) pressure for airspeed
- Static port: ambient pressure for altimeter, VSI, and airspeed's static side

## Airspeeds
- IAS — indicated airspeed (what the ASI shows)
- CAS — calibrated (IAS corrected for instrument/position error)
- TAS — true (CAS corrected for altitude/temperature; TAS increases with altitude for a given IAS)
- GS — groundspeed (TAS plus/minus wind)

ASI color arcs (typical light airplane):
- White: flap operating range (Vs0 to Vfe)
- Green: normal operating (Vs1 to Vno)
- Yellow: caution (Vno to Vne)
- Red line: Vne never-exceed

## Pitot-static instruments
- Airspeed indicator: dynamic − static
- Altimeter: static pressure vs aneroid; set Kollsman window to current altimeter setting (inHg) for MSL approximation
- VSI / vertical speed: rate of static pressure change

Pitot block + open static: ASI fails toward zero in level flight (classic). Know that a blocked static system lies to altimeter and VSI.

Altimeter setting: 29.92 inHg is standard. Higher pressure setting → higher indicated altitude. "High to low, look out below" when flying toward lower pressure or colder air without updating.

## Gyro instruments
Gyros use rigidity in space and precession.
- Attitude indicator (AI / artificial horizon): bank + pitch. The horizon bar stays gyro-stable; the miniature airplane moves with the airframe in the display convention used on the test.
- Heading indicator (DI): gyro compass card; must be aligned with the magnetic compass periodically because of precession.
- Turn coordinator / turn-and-slip: rate of roll/turn + ball (coordination). Ball toward the inside = slip; toward the outside = skid. "Step on the ball."

Magnetic compass errors (know the names):
- Variation: magnetic vs true north (charted isogonic lines)
- Deviation: aircraft magnetism
- Dip errors: ANDS (Accelerate North, Decelerate South in the Northern Hemisphere)
- Turning errors: UNOS (Undershoot North, Overshoot South) in the Northern Hemisphere

## Instrument Comprehension method (critical)

You will see an attitude indicator and a heading indicator (and sometimes a simple compass rose) and must pick the airplane silhouette that matches both pitch/bank AND heading.

Rules:
1. Read bank first. The AI bank index shows left or right bank. Match wing-low side.
2. Read pitch. Nose up = ground below horizon in the window more than half (standard display: brown/earth down, blue/sky up). Nose down = more brown.
3. Read heading. The lubber line is the nose direction.
4. Combine. A plane banked right, nose up, heading 090 is a climbing right turn toward east.
5. Kill any choice that gets bank side wrong first — that eliminates most options in one second.

Heading numbers: 000/360 north, 090 east, 180 south, 270 west.

Practice by sketching:
```
   blue
  ------- horizon
   brown
```
Bank hash on the top of the AI: tick marks 10°, 20°, 30°, 60°.

This subtest is 25 items in 5 minutes. You must be automatic.

## Airport and traffic
- Runway number = magnetic heading rounded to nearest 10°, drop a zero. Heading 268° → Runway 27. Reciprocal differs by 18 (27 ↔ 09).
- Left traffic is standard unless published otherwise. Pattern: upwind, crosswind, downwind, base, final.
- Wind sock points downwind (the sock is blown toward the direction the wind is going). Land into the wind.
- Threshold markings, centerline, displaced threshold (pavement before threshold not for landing).
- Light gun signals (tower no-radio):
  - Steady green (air): cleared to land
  - Flashing green (air): return for landing
  - Steady red (air): give way / continue circling
  - Flashing red (air): airport unsafe, do not land
  - Flashing white (air): return to starting point
  - Alternating red/green: exercise extreme caution
- Ground: steady green taxi; flashing green taxi clear of runway; steady red stop; flashing red taxi clear of runway; flashing white return to start.

## Airspace (high level)
- Class B: big airports, ATC clearance required.
- Class C: approach control, two-way radio + squawk typically.
- Class D: towered, two-way radio.
- Class E: controlled en route / transition.
- Class G: uncontrolled.
- Restricted / MOA / prohibited: know that prohibited is a hard no; restricted needs permission when hot.

VFR weather minimums vary by airspace and altitude; if tested, typical Class D/E below 10,000: 3 SM vis, 500 below / 1000 above / 2000 horizontal from clouds.

Flight categories:
- VFR: ceiling > 3000 AGL and vis > 5 SM
- MVFR: 1000–3000 or 3–5 SM
- IFR: 500–<1000 or 1–<3 SM
- LIFR: <500 or <1 SM

## Weather that matters on AI
- Cold front: steep, fast, possible thunderstorms, wind shift, after passage cooler/drier.
- Warm front: shallow, widespread stratus/rain, after passage warmer/more humid.
- Stationary / occluded: know the names.
- Thunderstorm stages: cumulus (updrafts), mature (updraft + downdraft, rain, lightning — most violent), dissipating (downdrafts).
- Wind shear / microburst: dangerous on approach.
- Icing: structural ice needs visible moisture + freezing temperature. Carb ice can occur in warmer moist air with high humidity.
- Density altitude: high heat, high elevation, high humidity → worse performance (longer takeoff, reduced climb).
- Fog types: radiation (clear night, light wind), advection (warm moist air over cool surface), upslope, steam.

## Rotary wing (light coverage)
Helicopters: lift from rotor disk. Cyclic tilts the disk (direction), collective changes blade pitch collectively (climb/descend / power), pedals counter torque (yaw). Translating tendency, ETL, retreating blade stall are advanced — know torque and that the tail rotor fights torque.

## Basic nav
- Latitude: 0–90, parallels, north/south of equator.
- Longitude: 0–180, meridians, east/west of prime meridian.
- Magnetic vs true: true + variation (east is least, west is best — "East is least, west is best" means magnetic = true − east variation).
- 1 nautical mile = 1 minute of latitude ≈ 6076 ft. 1 knot = 1 NM/hour.

## History / systems trivia that sometimes appears
Wright 1903 powered controlled flight. Jet age after WWII. Know fixed-wing vs rotary. Know that a glider has lift and drag and weight but no thrust (unpowered).
