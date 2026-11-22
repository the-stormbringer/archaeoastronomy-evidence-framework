> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../../../../PROJECT_STATE.json) for current status.

# Map and catalogue audit — 24 October 2026

The user-supplied 470-page PDF clears the durable-copy access dependency. Checksums and offsets are in ../acquisition.json. Printed page + 2 = local PDF page for the pages used here.

## Reproducible extraction

Run `python3 map_catalogue_audit.py` from agent_artifacts (script resolves its own paths). It extracts red filled drawing paths in the ten Sector C cells identified for B1/B2 in chapter 7, using the vector grid on Fig. 2.4, printed p. 28 / PDF p. 30. There are 25 vertical and 35 horizontal grid boundaries, defining 24 lettered rows and 34 numbered columns. Assignment uses each path bounding-box centre. It yields 28 paths: six in B2 cells and 22 in B1 cells. The review overlay was visually checked against the source on 24 October.

These are drawing objects, not an archaeological inventory or surveyed point dataset. One path can represent a fragment or drawing symbol; several fragments can belong to one stone; a centre near a cell boundary can be assigned differently by another rule. No old B-1–B-7 identity is assigned. No georeferencing, true azimuth, ancient position or survey-error estimate is derived.

## Catalogue cross-check

Visually inspected full pages:

- Printed p. 408 / PDF p. 410: Sector C row n, columns 19–21, with another outline beyond the right boundary towards n/22. This supports the location of the B2 sequence, but does not label the older individual coordinate-table IDs.
- Printed p. 413 / PDF p. 415: Sector C row o, columns 23–24, containing multiple separate outlines.
- Printed p. 414 / PDF p. 416: Sector C row o, columns 25–27, with a larger fragment cluster in column 26 and other outlines on either side.
- Printed p. 381 / PDF p. 383: Sector B a-prime/19 contains multiple outlines. This is relevant to the chapter 7 A8 location spanning a-prime and b-prime/19; it does not establish which outline corresponds to the old numerical coordinate.

Contact sheets of printed pp. 381–422 were used only to locate relevant pages, not to certify every label or object. The catalogue key on printed p. 379 identifies capital letters as sectors and lower-case letters/numbers as squares. Its sector B is not the historical alignment-group B.

## Consequence for the reconstruction

The old coordinate ledger and the later mapped outlines have different observational units. Counting outlined fragments and comparing that count directly with old coordinate rows would be invalid. A defensible crosswalk needs: historical ID, later cell and object, observation date, point definition (base, fragment centre, group representative), and evidence that the position represents the intended ancient feature. Unresolved entries stay unresolved.

The map scale is available, but grid size and reference-north conversion are not assumed. Catalogue geometry can support a conditional drawing-space reconstruction after point definitions are explicit; it cannot by itself supply unrounded original survey measurements or ancient stone positions.

Next: reconcile A identities and selected B catalogue features against historical source figures; record candidate alternatives rather than silently choosing a nearest neighbour. Historical-table sensitivity results remain valid within their existing stated scope.

## Text-versus-map representation check

Chapter 7 printed p. 142 describes two pieces in n/19, five fragments in o/25, fifteen in o/26, and six in o/27. The selected red map paths number 1, 3, 9 and 4 respectively. Thus even within this single volume the red path count is not interchangeable with the textual fragment inventory. This may reflect drawing generalisation, compound paths or different recording detail; it is not evidence of lost stones or a demonstrated textual error. The discrepancy was found by comparing the complete chapter 7 description with the extracted map and relevant catalogue drawings, not by assuming that every outlined path is one archaeological object.

B_identity_candidates.csv records all ten cells, reported units, map-path counts and catalogue locators. For n/22 the locator is the unlabelled continuation beyond the n/21 panel boundary on p. 408; its square attribution comes from chapter 7 and the general map, not a printed catalogue n/22 heading. Page 406 / PDF 408 was subsequently inspected at full size: its sector C, row m, column 18 labels and single drawn outline are confirmed. No historical coordinate IDs have been silently filled.
