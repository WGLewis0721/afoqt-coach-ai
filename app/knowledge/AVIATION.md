# Aviation Information + Instrument Comprehension

Quick context: this material feeds the Pilot and ABM composites. Aviation Information (AI) is the one rated-track subtest that's really just knowledge you can study directly. Instrument Comprehension (IC) is more of a visual skill, but it runs on a short, learnable rule set.

## The four forces on an airplane

In steady, straight-and-level, unaccelerated flight, two pairs of forces balance out:
- Lift = Weight
- Thrust = Drag

Lift acts perpendicular to the "relative wind" (in level flight, that's roughly straight up). Weight pulls toward the Earth through the aircraft's center of gravity. Thrust pushes generally forward, along the engine or propeller's axis. Drag pushes backward, opposite the direction of flight.

## How a wing actually makes lift

Two ways to explain the same thing:
1. **Bernoulli's explanation**: air moves faster over the wing's curved upper surface, which lowers the pressure above the wing.
2. **Newton's explanation**: the wing pushes air downward, and the equal-and-opposite reaction pushes the wing (and plane) up.

Angle of attack (AoA) is the angle between the wing's chord line and the relative wind. Increasing AoA increases lift — right up until you hit the critical AoA, at which point you get a stall. A stall is an aerodynamic event (the wing stops producing enough lift), not an engine problem — and here's a common misconception worth clearing up: a plane can stall at any airspeed or any attitude, as long as the AoA gets too high.

## The three axes and the primary flight controls

| Control | Surface | Axis | Motion |
|---------|---------|------|--------|
| Ailerons | trailing edge of wings, differential | Longitudinal (nose-to-tail) | Roll / bank |
| Elevator (or stab) | horizontal tail | Lateral (wingtip-to-wingtip) | Pitch (nose up/down) |
| Rudder | vertical tail | Vertical | Yaw (nose left/right) |

Secondary controls that add lift or drag:
- Flaps: increase the wing's camber (and often its area), adding both lift and drag. Used on takeoff and landing so the plane can fly slower.
- Slats/slots: keep airflow attached at high angles of attack.
- Spoilers: dump lift and add drag on purpose.
- Trim tabs: hold a control surface in position so the pilot isn't fighting constant pressure the whole flight.

Adverse yaw: when you bank, the aileron that goes down creates more lift *and* more induced drag on that wing, which yaws the nose away from the direction you're rolling. That's what the rudder is for — coordinating the turn.

## Stability

- Positive static stability: if something displaces the aircraft, it tends to return to where it was.
- Longitudinal stability (pitch): depends on the center of gravity relative to the center of lift, and the tail's leverage (tail volume). An aft CG makes the plane less stable and can make recovery from upsets uglier.
- Lateral stability (roll): dihedral (the upward angle of the wings) helps here.
- Directional stability (yaw): the vertical stabilizer acts like a weathervane, pointing the nose into the relative wind.

## Aircraft parts, in plain terms

- Fuselage: the body of the plane.
- Empennage: the whole tail assembly.
- Wing spar, ribs, skin: the wing's internal skeleton and covering.
- Landing gear: tricycle (nosewheel up front) vs. tailwheel.
- Propeller: works by accelerating a slipstream of air — it's essentially a spinning airfoil.
- Jet engine, in order: intake → compressor → combustor → turbine → exhaust.
- Pitot tube: measures ram (dynamic) pressure, used for airspeed.
- Static port: measures ambient pressure, feeding the altimeter, the VSI, and the static side of the airspeed indicator.

## Airspeeds — know the difference

- **IAS** — indicated airspeed: whatever the instrument shows.
- **CAS** — calibrated airspeed: IAS corrected for instrument and position error.
- **TAS** — true airspeed: CAS corrected for altitude and temperature. For a given IAS, TAS actually increases as you climb.
- **GS** — groundspeed: TAS adjusted for wind.

Typical light-airplane airspeed indicator color arcs:
- White: flap operating range (Vs0 to Vfe)
- Green: normal operating range (Vs1 to Vno)
- Yellow: caution range (Vno to Vne)
- Red line: Vne, the never-exceed speed

## Pitot-static instruments

- Airspeed indicator: reads the difference between dynamic and static pressure.
- Altimeter: compares static pressure against an internal aneroid; you set the Kollsman window to the current altimeter setting (in inHg) to read altitude above mean sea level.
- VSI (vertical speed indicator): reads the rate at which static pressure is changing.

Worth remembering: a blocked pitot tube with an open static port makes the airspeed indicator drift toward zero in level flight — a classic failure. And a blocked static system will lie to you on both the altimeter and the VSI.

On altimeter settings: 29.92 inHg is standard. A higher pressure setting on the Kollsman window shows a higher indicated altitude. The old memory aid still holds: "high to low, look out below" — meaning if you fly toward lower pressure or colder air without updating your setting, your true altitude is lower than what's indicated.

## Gyro instruments

Gyroscopic instruments rely on two properties: rigidity in space, and precession.

- Attitude indicator (AI, or "artificial horizon"): shows bank and pitch. The horizon bar itself stays gyro-stable; in this test's display convention, the little miniature airplane symbol moves with the actual airframe.
- Heading indicator (DI): a gyro-stabilized compass card. It has to be re-aligned with the magnetic compass periodically, because of precession drift.
- Turn coordinator / turn-and-slip indicator: shows rate of roll/turn, plus a ball that shows coordination. Ball toward the inside of the turn = slip; toward the outside = skid. The saying is "step on the ball" to fix it.

Magnetic compass errors worth naming:
- **Variation**: the difference between magnetic north and true north (shown on charts as isogonic lines).
- **Deviation**: errors caused by the aircraft's own magnetism.
- **Dip errors**: remembered as ANDS — Accelerate North, Decelerate South (in the Northern Hemisphere).
- **Turning errors**: remembered as UNOS — Undershoot North, Overshoot South (in the Northern Hemisphere).

## How to actually work Instrument Comprehension questions (this part matters)

You'll be shown an attitude indicator and a heading indicator (sometimes a simple compass rose too), and you need to pick the airplane silhouette that matches both the pitch/bank AND the heading.

The steps that work:
1. **Read the bank first.** The bank index on the attitude indicator shows left or right bank — match the wing-low side.
2. **Read the pitch.** Nose up means more brown (ground) below the horizon and less than half the window in blue/sky, using the standard display: blue (sky) up top, brown (earth) below. Nose down means more brown fills the window.
3. **Read the heading.** The "lubber line" shows the direction the nose is pointing.
4. **Combine all three.** For example: a plane banked right, nose up, heading 090 is a climbing right turn toward east.
5. **Eliminate fast.** Cross out any answer choice that gets the bank side wrong first — that alone knocks out most of the wrong options in about a second.

Heading numbers to know: 000/360 is north, 090 is east, 180 is south, 270 is west.

It helps to sketch this out while you practice:
```
   blue
  ------- horizon
   brown
```

The bank scale at the top of the attitude indicator has tick marks at 10°, 20°, 30°, and 60°.

One more thing: this section gives you 25 items in 5 minutes. That's not enough time to think it through carefully — you need this to become reflexive through repetition.

## Airports and traffic patterns

- A runway's number is just its magnetic heading, rounded to the nearest 10°, with the last zero dropped. So a heading of 268° becomes Runway 27. The opposite end of that same runway differs by 18 (so 27 and 09 are the reciprocal ends of the same strip).
- Left traffic is the standard pattern unless published otherwise. The pattern legs, in order: upwind, crosswind, downwind, base, final.
- A wind sock points **downwind** — it's blown in the direction the wind is going. Aircraft land into the wind.
- Runway markings to know: threshold, centerline, and displaced threshold (pavement before the threshold that's not usable for landing).
- Light gun signals from the tower, if radios are out:
  - Steady green (in air): cleared to land
  - Flashing green (in air): return for landing
  - Steady red (in air): give way, continue circling
  - Flashing red (in air): airport unsafe, do not land
  - Flashing white (in air): return to starting point
  - Alternating red/green: exercise extreme caution
- On the ground: steady green means taxi; flashing green means taxi clear of the runway; steady red means stop; flashing red means taxi clear of the runway; flashing white means return to start.

## Airspace, at a glance

- Class B: the big, busy airports — ATC clearance required.
- Class C: has approach control; typically needs two-way radio and a transponder squawk.
- Class D: towered, needs two-way radio.
- Class E: controlled airspace for en-route flying or transitions.
- Class G: uncontrolled.
- Restricted / MOA / prohibited: prohibited means a hard no, always. Restricted airspace needs permission when it's "hot" (active).

VFR weather minimums shift depending on the airspace and altitude. If it's tested, the typical numbers for Class D/E below 10,000 feet are: 3 statute miles visibility, and staying 500 feet below / 1,000 feet above / 2,000 feet horizontally from clouds.

Flight categories by ceiling and visibility:
- VFR: ceiling above 3,000 feet AGL and visibility above 5 statute miles
- MVFR: ceiling 1,000–3,000 feet, or visibility 3–5 statute miles
- IFR: ceiling 500 to under 1,000 feet, or visibility 1 to under 3 statute miles
- LIFR: ceiling under 500 feet, or visibility under 1 statute mile

## Weather worth knowing for this test

- **Cold front**: steep and fast-moving, can bring thunderstorms and a wind shift; after it passes, expect cooler and drier air.
- **Warm front**: shallow and slow, tends to bring widespread stratus clouds and rain; after it passes, expect warmer and more humid air.
- **Stationary and occluded fronts**: just know the names and that they exist.
- **Thunderstorm stages**: cumulus stage (updrafts building), mature stage (updrafts and downdrafts together, with rain and lightning — the most violent stage), and dissipating stage (mostly downdrafts).
- **Wind shear / microburst**: especially dangerous during an approach to land.
- **Icing**: structural ice needs both visible moisture and freezing temperatures to form. Carburetor ice, on the other hand, can form in warmer air if the humidity is high enough.
- **Density altitude**: high heat, high elevation, and high humidity all make performance worse — longer takeoff rolls, weaker climb.
- **Fog types**: radiation fog (clear night, light wind), advection fog (warm moist air moving over a cooler surface), upslope fog, and steam fog.

## Helicopters (lighter coverage)

Helicopters get their lift from the spinning rotor disk. The cyclic control tilts the disk to choose direction; the collective changes all the blades' pitch together to climb or descend (power); the pedals counter engine torque and control yaw. Things like translating tendency, ETL, and retreating blade stall are more advanced topics — for this test, just know that the tail rotor's job is fighting torque.

## Basic navigation

- Latitude: 0–90°, measured in parallels, north or south of the equator.
- Longitude: 0–180°, measured in meridians, east or west of the prime meridian.
- Magnetic vs. true heading: true plus variation gives magnetic. The old memory trick is "east is least, west is best," meaning magnetic = true minus east variation.
- 1 nautical mile equals 1 minute of latitude, which is about 6,076 feet. 1 knot equals 1 nautical mile per hour.

## A little history and trivia that sometimes shows up

The Wright brothers made the first powered, controlled flight in 1903. The jet age followed after World War II. Know the difference between fixed-wing and rotary-wing aircraft. And remember: a glider has lift, drag, and weight acting on it, but no thrust — it's unpowered.
