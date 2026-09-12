# Table Reading, Block Counting, Instrument Comprehension

These three are speed tests, plain and simple. There isn't much to "know" — the real skill is reps until it's automatic. If you want the real look and feel of these, that's what OATTS is for.

## Table Reading — 40 items, 7 minutes (about 10.5 seconds each)

You'll see a large grid with an X-axis and a Y-axis. Each item gives you a coordinate pair, and you find the value in that cell.

How to work it:
1. Don't just "search around" the grid. Pick one axis to lock onto first — usually the top X scale is easiest.
2. Trace down the column, then across the row (or the reverse) — whichever order you pick, always do it the same way every time.
3. Read the value, mark your answer, move to the next one.
4. If you lose your place in a row, go back and restart from the axis rather than guessing a neighboring cell. Accuracy tends to fall apart when you rush the last 15 items — watch for that.

A way to practice: build a 20×20 spreadsheet of random two-digit numbers, and have a friend (or this app) fire coordinate pairs at you for 7 minutes straight.

Mistakes to watch for:
- Sign errors, if the table has negative axes.
- Being off by one column.
- Reading a (X,Y) prompt backwards as (Y,X).

## Block Counting — 30 items, 5 minutes

You'll see a pile of identical cubes drawn in 3D, with one target block marked. Depending on the item style, you either count how many blocks touch the target (sharing a full face — not just an edge or corner), or count the total number of blocks in the whole pile. Classic Form T items usually ask how many blocks touch a numbered one.

Rules to hold onto:
- Only **face-adjacent** blocks count as "touching."
- Hidden blocks still exist if the geometry of the stack requires them to be there for support. Assume there are no floating blocks and no unsupported cantilevers, unless the drawing actually shows them.
- Work it layer by layer: count blocks sharing a side in the target's own layer, then add one if there's a block directly above, and one more if there's a block directly below.

For counting the whole pile:
- Go layer by layer, starting from the top.
- Use the footprint to help. For example: a fully-populated 3×3 base, with a 2×2 layer on top of that, plus one block capping it, comes out to 9 + 4 + 1 = 14.

A way to practice with ASCII sketches:
```
Layer 3:     [A]
Layer 2:  [B][C]
Layer 1: [D][E][F]
```
If C is the target block here: it touches B (to the side), A (above), and E (below) — that's 3, unless D or F also happen to share a face with C (in this particular stack, they don't, since C sits on E only).

While you practice, mark a slash on scratch paper for each neighbor you've confirmed. It's faster than recounting from scratch every time.

## Instrument Comprehension — 25 items, 5 minutes

The full rules for reading the attitude indicator and heading indicator live in `AVIATION.md` — this is just the drill sequence.

Run this sequence until it's a reflex:
1. Bank side
2. Pitch: up, down, or level
3. Heading quadrant (start with N/E/S/W, then narrow it down)
4. Pick the silhouette

If two silhouettes match on both bank and heading, pitch is what tells them apart.

On the heading indicator, the nose points at the lubber line. If the card shows 135 lined up under the lubber, the airplane is pointed southeast.

One thing to watch: don't confuse the miniature-airplane symbol with "whichever way the horizon looks tilted." Use the official convention — read the sky/ground background on the attitude indicator for pitch and bank, and read the miniature airplane's wings specifically for bank.
