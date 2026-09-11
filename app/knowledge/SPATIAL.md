# Table Reading, Block Counting, Instrument Comprehension

These are speed tests. Knowledge is small. Reps are everything. Official look-and-feel: OATTS.

## Table Reading — 40 items, 7 minutes (~10.5 sec)

A large grid. X along one axis, Y along the other. Each item gives a coordinate pair. You find the cell value.

Method:
1. Do not "search around." Pick the axis that is easier to lock (usually the top X scale).
2. Drop a finger/pencil mentally down the column, then across the row — or the reverse, but always the same order.
3. Read the value. Mark. Next.
4. If you lose the row, restart from the axis. Guessing a neighbor is common; accuracy collapses when you rush the last 15.

Practice: make a 20×20 spreadsheet of random two-digit numbers. Have the app (or a friend) fire coordinate pairs at you for 7 minutes.

Common errors:
- Sign errors if the table has negative axes
- Off-by-one column
- Reading the prompt as (Y,X) instead of (X,Y)

## Block Counting — 30 items, 5 minutes

A pile of identical cubes is drawn in 3D. A target block is marked. Count how many blocks touch the target (shared face, not just an edge or corner) — OR count how many blocks are in the pile, depending on the item style. Form T items classically ask how many blocks touch a numbered block.

Rules:
- Only FACE-adjacent counts for "touching" items.
- Hidden blocks still exist if the stack geometry requires them. Assume no floating blocks and no unsupported cantilevers unless the drawing shows them.
- Work by layers: how many in the target's layer sharing a side, plus one above if occupied, plus one below if occupied.

Counting the whole pile:
- Count layer by layer from the top.
- Use the footprint. If a 3×3 base is fully populated and there is a 2×2 on top plus one cap, that is 9+4+1=14.

ASCII practice idea:
```
Layer 3:     [A]
Layer 2:  [B][C]
Layer 1: [D][E][F]
```
If C is the target: touches B (side), A (above), E (below). That is 3 unless D/F also share a face with C (they do not in this stack if C sits on E only).

Draw slashes on scratch paper for each confirmed neighbor. Do not recount from scratch if you can avoid it.

## Instrument Comprehension — 25 items, 5 minutes

See AVIATION.md for the AI + HI reading rules.

Drill sequence until it is a reflex:
1. Bank side
2. Pitch up/down/level
3. Heading quadrant (N/E/S/W then refine)
4. Select silhouette

If two silhouettes share bank and heading, pitch is the discriminator.

Heading indicator: the nose is at the lubber line. If the card shows 135 under the lubber, the airplane is pointing southeast.

Do not confuse the test's miniature-airplane symbol with "which way the horizon tilts." Use the official convention: sky/ground on the attitude indicator, wings of the miniature airplane for bank.
