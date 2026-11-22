> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../PROJECT_STATE.json) for current status.

# Nabta Playa project orientation

Reviewed 19 October 2026. This is an orientation record, not a revised research result or an implementation plan.

## Scope and boundary

The user requested a thorough orientation and explicitly asked that research work not begin. This pass read the existing drafts, scripts, CSVs, GIS metadata, saved figures, and selected photographs. No project analysis scripts were executed, astronomical calculations rerun, online catalogue queries made, dependencies installed, or legacy files edited. Temporary document renders and photograph previews were used for inspection. This note is the only new project artifact.

The NotebookLM videos are excluded. The presentation will be supplied later if needed; its absence does not prevent understanding the project. The separately archived `~/Coding_Projects/archive/mc_fixed` is excluded from the research baseline and was not used to choose methods or results.

## Project purpose and current state

The core question is whether the geometry of the Nabta Playa megalithic rows can be reconstructed reproducibly from published coordinate datasets, with uncertainty quantified before assigning astronomical meanings.

The main geometric study compares six named rows, A3, A2, A1, B2, B1, and C1, associated with Complex Structure A. Three coordinate versions are represented: Wendorf/Malville legacy coordinates, QuickBird 2002, and Brophy/Rosen GPS 2003. The scripts fit line axes using PCA/SVD after projection into UTM zone 36N, then calculate perpendicular scatter, leave-one-out sensitivity, bootstrap dispersion, and cross-dataset differences.

A later exploratory branch adds a DEM-derived horizon, solstitial sunrise calculations, a Gaia stellar survey, candidate matching, SIMBAD identifications, constellation grouping, and statistical tests. The written report is primarily about geometry and explicitly defers celestial attribution; the later scripts and saved graphics make stronger astronomical claims.

There is substantial source material and a recoverable computational history. There is not yet one internally consistent, validated chain from source coordinates to publishable conclusions. Several concrete inconsistencies below affect both the geometry and later astronomy. Existing numerical outputs are historical artifacts until those issues are addressed under a future instruction.

## Workspace and provenance

The fresh project is `~/Research_Projects/nabta/`. Everything inherited is under `legacy/`:

| Location | Role |
|---|---|
| `legacy/MC/` | Complete copy of the original `~/MC` directory, including code, data, images, environment, and photo archive |
| `legacy/Documents/` | Report PDF, editable interim report, expanded research notes, and the Wendorf/Schild source volume |
| `legacy/home_gis/` | Calendar point, reference points, and the loose projected DEM originally in the home directory |

The preceding copy operation verified 24,700 regular files by SHA-256 and four symlink targets, totalling 8,625,851,957 bytes. Those counts describe the inherited snapshot, including the Python environment. Originals were retained. No Git repository, dependency lock, formal project README, or test suite was found in the research materials outside bundled dependencies.

### Written outputs

| File | Content and status |
|---|---|
| `legacy/Documents/Nabta Playa Report.pdf` | Ten-page report titled “Digital Reconstruction and Statistical Re-evaluation of the Nabta Playa Megalithic Alignments.” Names Ahmed A. Ezzat, the Megalithic Culture course, and Professor Nelson J. Almeida. Contains background, methods, discussion, references, and two figures. PDF metadata records export on 11 January 2026; the cover says December 19th without a year. |
| `legacy/Documents/Prelem Report data.docx` | Approximately 2,100-word “Geometric Reassessment … (Interim Report).” More explicit about alignment membership and tabulated results than the PDF. It is an editable earlier/interim text, not an exact Word source of the PDF. |
| `legacy/Documents/Preliminary.docx` | Expanded literature extraction and planning notes, including site and feature nomenclature. Contains conversational/generated text and should not be treated as a checked bibliography or authoritative transcription. |
| `legacy/MC/Preliminary.docx` | Shorter version of the literature notes, approximately 3,500 words. Preserved separately because its contents differ. |

The report PDF was read in full through text extraction; its two figure pages were also inspected visually. Figure 1 is a line plot despite a caption describing bars and vertical summary markers. The report's claims of orientation families around 25° and 90° are not established by the six-row saved PCA table: that table contains no measured row around 90°. The later matcher separately inserts a manual 90° target.

### Source material and spatial assets

- `legacy/Documents/Holocene Settlement of the Egyptian Sahara_ Volume 1_ The Archaeology of Nabta Playa.pdf` is the substantial primary source volume. This pass located its role but did not conduct a fresh literature review or independently verify every extracted table and claim against the volume.
- `legacy/MC/P1T1/` contains four extracted CSVs: the Wendorf/Malville alignment table, the three-version Brophy/Rosen coordinate table, and Malville 2007/2015 target and chronology summaries.
- `legacy/MC/WS2001/` preserves figure PDFs for 14.1, 14.3, 16.1, and 16.17, extracted images, two photographs, georeferenced versions of 16.1 and 16.17, and QGIS control-point files.
- `WS2001/digitizer.py` is a PyQt6/OpenCV point-picking utility with manual and blob-centroid options. `DGI1.json` records 25 manual pixel points and an absolute original image path. These are image coordinates, not a documented independent survey of geographic stone positions.
- `legacy/MC/PG/` contains a ZIP with 623 HEIC photographs and an extracted collection of 623 HEIC files. Three samples from the beginning, middle, and end show overlapping views of a reconstructed stone circle in a museum/garden setting. Their EXIF dates are 7 December 2025, using an iPhone 13 at 4032 × 3024. Identification with the relocated calendar circle is a contextual inference; this is not evidence of an in-situ survey at Nabta Playa. No photogrammetry model, camera solution, point cloud, or mesh was found in the inventory.
- Maps include `Prelim Geometry.png`, `report_exp.png`, and `presentetion small dem.png`, with world files for the first two. The last is a terrain/alignment map, not a deck.

### GIS structure

`legacy/MC/nabta_phase1_geometry.qgz` uses a project CRS of EPSG:4326 and contains 16 layer references, with no saved print layouts. Coordinate layers are read directly from `P1T1/brophy_rosen_coords.csv`. Spatial analysis scripts explicitly use EPSG:32636.

| Asset | Inspected state |
|---|---|
| `Contours.gpkg` | 336 contour features, EPSG:4326 |
| `P_Allignment.gpkg` | Seven features, EPSG:4326 |
| `alignments_leg.gpkg` | Six features, EPSG:4326 |
| `alignments_qb.gpkg` | Empty feature table |
| `home_gis/Calendar Prelem.shp` | One point |
| `home_gis/Reference.shp` | Four points |
| `MC/dem.tif` | 45 × 77 cells, geographic CRS; small local clip |
| `MC/dem_expanded.tif` | 351 × 182 cells, geographic CRS |
| `MC/handoff/code/data/dem_utm36n.tif` | 348 × 198 cells, EPSG:32636, about 29.06 m cells; rectangular footprint about 10.1 × 5.75 km |
| `MC/handoff/code/data/archive/dem_utm36n_clipped.tif` | Older 44 × 80 cell projected clip at 30 m |

The QGIS project is not fully portable in its current copied layout. It references `../Calendar Prelem.shp`, `../Reference.shp`, and `../DEM_UTM.tif`, which originally resolved from `~/MC` into home. The copied files now live in `legacy/home_gis/`, not the paths those references expect. It also references an absolute temporary terrain-ruggedness raster under `/tmp/processing_…/OUTPUT.tif` and a Google Maps XYZ service. These references were inspected as XML; QGIS was not opened and the network layer was not fetched.

An additional `~/ROI.shp` family referenced by QGIS remains outside the copied snapshot. Read-only inspection found zero polygon features. It was identified during this orientation and was not copied or modified because the instruction was to start no further work.

## Pipeline and surviving outputs

Paths below are relative to `legacy/MC/handoff/code/`. These describe code and saved artifacts, not a verified execution order.

| Stage | Script or input | Surviving artifact |
|---|---|---|
| Source coordinates | `data/BR_leg.geojson`, `BR_QB.geojson`, `BR_field.geojson` | Each has 25 feature records: Complex A plus 24 stones. GPS 2003 has null geometries for B-2 and C-2. Coordinates match the three source columns in role; full source accuracy has not been revalidated. |
| Geometry | `01_load_and_inspect.py` | `outputs/pca/alignment_results_by_dataset.csv`: 18 solutions; six-row summary; two-row omission log |
| Terrain horizon | `02_horizon_profiles.py` | `outputs/horizon_profile.csv`: 720 bearings at 0.5° intervals, saved altitudes about 0.0113°–2.0392° |
| Solar comparison | `03_solar_calibration.py` | Five solstice rows for astronomical years −6500, −6000, −5500, −5000, −4500; saved DEM-minus-flat shift about 0.221° |
| Horizon sampling | `03a_quantify_horizon_impact.py` | `outputs/horizon_alts.txt`, using hard-coded literature-like target bearings rather than dynamically loading the PCA fits |
| Stellar survey | `04_stellar_survey.py` | `outputs/ancient_stellar_survey.csv`: 254 rows; saved classifications 239 rise/set, 12 never rise, three circumpolar; these classifications are not validated results |
| Stellar matching | `05_stellar_alignment_test.py` | 132 rows, 35 unique star IDs, 44 distinct star/target/event combinations, three tested epochs; all rows labelled `STRONG (All 3)` |
| Names | `06_identify_candidates.py` | The same 132 rows with SIMBAD common identifiers added |
| Sky map | `06b_visualize_sky_map.py` | `outputs/sky_map_visualization.png` exists |
| POV illustration | `06c_pov_sky_simulation.py` | Script exists; its named `outputs/simulation_sky_view_5000BCE.png` is absent |
| Constellation test | `07_symbolic_pattern_test.py` | `outputs/final_constellation_report.csv`: 24 rows |
| Statistical stress test | `08_statistical_stress_testing.py` | Script exists; named final text report and Monte Carlo plot are absent |
| Slide graphics | `untitled2.py` | Three PNGs: geometric uncertainty, horizon profile, and constellation significance |

The `overview/` directory is a handoff bundle rather than a separate authoritative run. Its three GeoJSONs and DEM are byte-identical to their `data/` counterparts. `overview/project_files.txt` embeds CSVs and code, including copies of scripts 01–07 matching the standalone versions, plus an additional `stress_test.py` that has no standalone counterpart. That embedded script is another exploratory statistics implementation, not proof that the final stress test ran.

There are parallel result branches under `outputs/clip error/` and `outputs/mag 2.5/`, including a 15-row brighter-star candidate run. Their names suggest revisions/sensitivity exploration, but no run manifest explains their lineage. Older `pca_by_dataset_available.csv`, `pca_by_dataset_harmonized.csv`, and `data/archive/pca_alignment_azimuths_by_dataset.csv` contain zero-point solutions and empty estimates, consistent with unresolved identifier matching in those versions.

### Timeline visible in the files

- 7 December 2025: sampled museum-circle photographs.
- December 2025: literature extraction, GIS preparation, source figures, and early empty PCA tables.
- 5 January 2026: saved nonempty PCA results and geometry summaries.
- 11 January: export of the written report PDF.
- 13–14 January: editable interim report and expanded notes saved; Gaia survey script appears in this period.
- 17 January: saved solar/horizon/stellar products, candidate naming, and constellation report.
- 18–19 January: stress-test code and three slide graphics; no corresponding final stress-test artifacts located.

Modification dates indicate sequence, not successful executions or approved scientific decisions.

## Findings that affect interpretation

These are observations from static code and artifact inspection. No fixes or replacement results were produced.

### 1. Stone identities and alignment membership conflict

`P1T1/nabta_alignment_table.csv` assigns B2 to B-1/B-2/B-3/B-4 and B1 to B-5/B-6/B-7. Script 01 lines 46–52 instead assigns B2 to B-1/B-4/B-5/B-6 and B1 to B-2/B-3/B-7. The editable interim report follows the script membership. Older archived PCA tables use still another membership version.

The alignment-table CSV also ends with C-8, whereas the Brophy/Rosen table and working GeoJSONs use C-6. Some C-row coordinates differ between the extracted tables as well. These are unadjudicated source/transcription differences. The script's chosen memberships cannot yet be assumed to represent the primary publication correctly.

### 2. The geometry implementation does not consistently treat axes as axes

Script 01 lines 58–93 treats azimuths on a 360° circle. The PCA singular vector has an arbitrary sign; opposite vectors represent the same line. Leave-one-out comparison and bootstrap circular statistics do not reconcile that 180° ambiguity. Bootstrap resampling can also produce repeated-point or rank-deficient samples, with no explicit rejection or diagnostic.

Saved bootstrap standard deviations are commonly around 100°–180°, and the geometric slide plots those values directly as error bars. They cannot be read as validated uncertainty estimates for line axes. The PDF describes modulo-180° handling, but the surviving script does not implement that description.

The code measures orientation in projected UTM coordinates while the drafts call it true-north azimuth. No explicit grid-to-true-north conversion appears in the geometry script. The desired convention remains unresolved. PCA is also not intrinsically resistant to outliers, despite the interim report's wording.

### 3. The report and saved geometry disagree in material details

The saved C1 summary reports mean direction 314.18°, cross-dataset maximum difference 5.40°, and mean perpendicular RMS 21.06 m. The interim draft instead gives approximately 314.2°, 2.85°, and 13 m. A3 is described as unreliable in the interim draft, whereas the PDF generalizes about A1–A3 clustering near 25°. The PDF's recurring 90° family lacks a corresponding measured row in the saved six-alignment table.

GPS 2003 B1 uses only two points after the missing B-2 record is removed; its almost-zero perpendicular RMS is a property of a two-point fit, not independent evidence of high construction precision. Its leave-one-out value is blank. Repeated survey versions of the same physical row also cannot automatically be counted as independent monuments in significance tests.

### 4. The horizon does not cover the requested 20 km search

Script 02 requests a 20 km horizon radius, but its input raster covers only about 10.1 × 5.75 km in total. The code discards out-of-raster samples and uses whatever portion remains, without reporting actual coverage by bearing. Thus the saved result is a horizon estimate from a limited raster, not a demonstrated 20 km horizon.

The model uses the observer's raster-cell elevation without an explicit eye height, nearest-neighbour terrain sampling, and no explicit curvature/refraction treatment in the terrain-ray calculation. The modern DEM's relationship to the ancient landscape is not established. `slide2_horizon_profile.png` clips the vertical display at 1.5° despite the saved profile extending beyond 2°.

### 5. Stellar coordinate information is lost between stages

Script 04 exports only `Gaia_ID`, `Name`, `Mag`, `Ancient_Dec`, `Dist_to_Pole_Deg`, and `Status`. It does not export right ascension, proper motion, parallax, radial velocity, or the original reference-epoch information needed downstream.

Script 05 lines 208–214 expects modern or ancient RA, proper motion, and parallax, and silently substitutes zero for absent fields. Its fallback passes a calendar year such as −5000 as a numeric `Star` epoch. The bundled Skyfield source stores numeric epochs as Julian-date values, not calendar years. The visualization scripts also expect `Ancient_RA`, which is absent from the saved survey; one sky-map expression evaluates that missing-column fallback even when looking for a modern RA column.

Both the survey and matcher call `.radec()` without an epoch argument and use its declination for ancient-pole/horizon reasoning. The locally bundled Skyfield 1.53 documentation/source states that this returns ICRF coordinates; coordinates referred to the equator/equinox of the observation date require an epoch argument. This is a concrete reference-frame mismatch, not evidence that ancient precession has been validated. The current “strong across three epochs” labels should not be interpreted as proven millennial stability.

### 6. The stellar matcher overwrites most measured targets

Script 05 lines 77–101 names targets using only the `dataset` column and stores them in a dictionary. Each dataset's six alignment rows overwrite the same key; the final row is C1. The saved candidate table confirms only `PCA: legacy` at 311.35°, `PCA: quickbird` at 316.75°, and `PCA: gps2003` at 314.43° survive as measured targets.

The other targets are manually inserted 61.8°, 90°, 0°, and 180°; the saved matches have hits for the first three. The candidate output therefore is not a search over all six physical rows. The solver also clips out-of-domain rise/set expressions instead of explicitly excluding impossible horizon crossings, uses only a single horizon-update step, and compares azimuths with an ordinary absolute difference near the 0° boundary.

### 7. Solar refraction is claimed more broadly than implemented

Script 03 does calculate solstice times and solar semidiameter, but its final `.altaz()` calls omit atmospheric parameters. The bundled Skyfield implementation documents that these calls do not apply atmospheric refraction by default. A fixed −0.8333° threshold is used only to locate an approximate sunrise before the later scan. The heading's “Dynamic Refraction” claim is therefore not supported by the final crossing calculation.

The solar CSV explicitly labels astronomical year −5000 as 5001 BCE. Other scripts/comments call −5000 “5000 BCE.” The notes also mix BP, uncalibrated radiocarbon dates, and BCE labels without a consistent documented conversion/calibration convention. Epoch and chronology assumptions are not settled.

### 8. Constellation significance counts repeated epochs as separate stars

Script 07 uses row counts per target and constellation in a hypergeometric test, even though the same star/event recurs once per epoch. For example, the saved Gemini row has nine hits but lists only three distinct stars. The code supplies approximate hand-written constellation populations, often defaults to eight, and uses all 254 survey rows as the population, including rows labelled never rising.

Some nine-hit groups therefore exceed their assumed eight-star population, producing a zero probability from an impossible count. Other zero values may be rounded small numbers; they cannot all be interpreted as extreme scientific significance. There is no visible correction for searching many stars, targets, epochs, tolerances, and constellation groups.

The slide script replaces saved zero p-values with `1e-10`, displays a significance of 10, and labels repeated hits as “Stars.” These are visualization choices, not additional statistical evidence. Modern constellation abbreviations are used as categories; a cultural connection to Neolithic groupings is not demonstrated.

### 9. The final stress-test stage is unfinished in the surviving record

Script 08 imports `kuipertest` and `watson_williams_test` from `astropy.stats`. Inspection of the bundled Astropy 7.2.0 source found the API `kuiper` and no definitions with those two imported names. This is a static incompatibility with the copied environment; no import test was run.

Even apart from execution, its Monte Carlo “sky” is selected from previously successful matches and its “site pattern” from those same matches. That conditions the null on the discoveries it is intended to assess. It also groups stellar hits near the calendar-circle axis as a “solar” population. Such labels do not establish separate solar and stellar uses of the monument.

The named final report and Monte Carlo distribution PNG are absent. An alternate stress-test implementation survives only inside the overview text bundle. Neither source file is a completed validation result.

## Runtime and reproducibility status

The inherited `handoff/Astro/` is a Python 3.13.5 virtual environment. Its configuration and executable-script shebangs still point to `/home/stormbringer/MC/handoff/Astro`. It has been preserved as evidence, not activated or certified portable.

Selected installed versions read from package metadata: NumPy 2.3.5, pandas 2.3.3, GeoPandas 1.1.1, rasterio 1.4.4, pyproj 3.7.2, SciPy 1.16.3, Matplotlib 3.10.8, Skyfield 1.53, Astropy 7.2.0, astroquery 0.4.11, and jplephem 2.23. This is an environment snapshot, not a dependency specification.

The `de441.bsp` file is approximately 3.31 GB. It was preserved, but its kernel coverage/provenance was not independently checked in this pass. Scripts use working-directory-relative paths. Script 01 writes to `outputs/`, whereas later stages read geometry from `outputs/pca/`; the manual move or run-history step between those paths is undocumented.

Running the existing scripts is not a read-only inspection: several overwrite saved outputs, the Gaia stage queries a remote catalogue, SIMBAD identification makes remote requests, and ephemeris-loading fallbacks may fetch files. None of those actions occurred during orientation.

## What remains open for the user's next directive

The central research intention is clear; the intended final contribution and accepted methods still need the user's orientation. Questions retained for later, not treated as permission to start work:

- Is the publishable study primarily geometric reconstruction and uncertainty, or should it also test specific archaeological astronomy hypotheses?
- Which primary source definitions govern stone identities, row memberships, the observer/origin, and the archaeological date window?
- Was there an intentional reason to change B-row memberships or C-stone labels between the source extraction and scripts?
- What was the intended use of the museum-circle photography: illustration, photogrammetry, geometry comparison, or something else?
- Are any later datasets, accepted corrections, notebooks, field notes, or source scans missing from this inherited snapshot?
- What venue, length, and contribution were originally intended for publication?

No answer has been inferred from generated prose or a “final” filename. The project is oriented and remains awaiting direction. No repair, reanalysis, manuscript revision, or new research has begun.
