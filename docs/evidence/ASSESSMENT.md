> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../PROJECT_STATE.json) for current status.

# Nabta Playa: research assessment and route to a defensible paper

**19 October 2026 · Internal research assessment, not a submission manuscript**

This report assesses the inherited concepts, data, methods, outputs, and publication prospects. It incorporates the user's intention to publish a first case study and then a larger study establishing a repeatable framework. The enduring objective is recorded in [RESEARCH_CHARTER.md](../RESEARCH_CHARTER.md).

## 1. Overall judgment

The project has a worthwhile archaeological question and enough surviving material to support a serious reanalysis. It is currently a recoverable exploratory study, not a nearly finished paper awaiting editing. Its principal weakness is the chain connecting archaeological features to measurements and measurements to interpretations. Several computational errors then compound that conceptual problem.

The strongest prospective contribution is **an auditable assessment of what fragmentary, rounded, and sometimes conflicting published spatial evidence can establish about astronomical alignment claims**. Nabta Playa could demonstrate how to distinguish robust findings from results that depend on source choice, feature definition, observer position, or astronomical assumptions. That would be more substantial than a new collection of possible star matches.

The original geometric question remains useful. However, a free line fitted through a cluster of stones and a sightline from Complex Structure A are different measurements. The project sometimes treats them as interchangeable. A diagnostic comparison shows that this distinction changes the apparent stability of A3 dramatically. It could become a central finding of the case study, subject to full source adjudication and uncertainty analysis.

The inherited stellar candidates, epoch-robustness labels, and constellation significance results cannot presently support a paper. They contain target-overwriting, missing-coordinate, reference-frame, event-validity, and counting problems. Fixing their code alone would still leave unresolved archaeological selection, chronology, visibility, and multiple-testing questions.

My recommended first paper is a **source-critical reassessment of the identifiability of published Nabta alignment hypotheses**, with astronomical tests included only where the underlying archaeological and geometric evidence supports them. Here, *identifiability* means whether the available evidence can distinguish one proposed interpretation from plausible alternatives. A finding that a particular claim cannot be resolved from the published coordinates can be valuable, provided the limitation is demonstrated and matters archaeologically.

## 2. What was left behind

The inherited snapshot is preserved under `legacy/`. [ORIENTATION.md](ORIENTATION.md) contains the detailed inventory and initial static inspection. This assessment supersedes its provisional interpretation where primary-source checks or new diagnostics provide better evidence; it does not replace the historical files.

| Component | What survives | Assessment |
|---|---|---|
| Research writing | Ten-page course report PDF, editable interim geometric report, two versions of literature notes | A recoverable argument and useful context; inconsistent numerical claims and unverified bibliography require reconstruction |
| Primary evidence | Wendorf/Schild source volume, extracted figures, coordinate tables, georeferencing control points | The most valuable foundation; provenance and disagreements must be made explicit |
| Spatial working material | Three coordinate versions, six named rows, QGIS project, GeoPackages, DEMs | Enough for a documented desktop case study; not a new field survey |
| Geometric analysis | PCA/SVD script, 18 dataset-row solutions, six-row summary, omission records | Useful exploratory diagnostics, with invalid uncertainty handling and mismatched feature definitions |
| Astronomy | Horizon, solar and stellar scripts, catalog extract, candidate and constellation tables | An exploratory branch with inference-invalidating errors |
| Validation | Stress-test code and an alternate embedded implementation | No completed, defensible end-to-end validation result located |
| Photography | 623 HEIC images plus their archive | Sampled images show a reconstructed circle in a museum/garden setting; no reconstructed 3D model was found |
| Reproducibility | Copied virtual environment, ephemeris, scripts and duplicate handoff bundles | Substantial recoverability, but no authoritative run manifest, dependency lock, or complete portable execution chain |

The report PDF is titled *Digital Reconstruction and Statistical Re-evaluation of the Nabta Playa Megalithic Alignments*. Its export metadata is 11 January 2026. Most surviving astronomy products follow the geometric draft; later figures make stronger claims than the draft's cautious deferral of celestial attribution. Modification dates suggest this sequence but do not certify successful runs.

The missing presentation is not a blocker. The NotebookLM videos are excluded as requested. `Coding_Projects/archive/mc_fixed` is excluded from the research baseline. The photography is not evidence for original in-situ orientation unless its relationship to the original arrangement is independently established.

### What this project is—and the limits of that description

It is a secondary-data investigation of published megalith locations, their possible geometric organization, and the consequences for astronomical interpretations. It could become a methodological case study in evidence quality and inference.

It has not established a new survey, a complete digital reconstruction of the prehistoric landscape, a validated photogrammetric model, a reliable identification of intended celestial targets, a date for construction derived independently of those targets, or a validated general framework. The saved figures do not establish these achievements merely because they look finished.

The project also does not encompass every Nabta astronomical claim. The radiating megalith rows, the small calendar circle, orientations of individual slabs, complex structures, and burial orientations are different archaeological units. They require different data and models. A manual 61.8° calendar target does not make the circle an independently measured part of the six-row study.

## 3. The research questions worth retaining

I recommend organizing the first study around four questions, in dependency order:

1. **Source reconstruction:** Which stones, coordinates, origins, memberships, and published bearings belong to each historical claim? Which differences are transcription errors, publication discrepancies, or genuine measurement differences?
2. **Geometric robustness:** How do defensible feature definitions and uncertainty assumptions change estimated directions and their resolution?
3. **Astronomical discriminability:** Within archaeologically supported date and visibility scenarios, which published hypotheses are compatible, incompatible, or indistinguishable using these data?
4. **Methodological value:** What explicit decisions and validation procedures prevent misleading certainty, and which are likely to transfer to another archaeological dataset?

These questions can yield a useful paper without discovering a new stellar target. A general search over bright stars can remain an exploratory supplement if needed; it should not determine the main argument retrospectively.

The archaeological significance is not merely whether a number matches a star. It concerns what can be inferred about the organization of a ceremonial landscape, the plausibility of proposed observation practices, and the evidential basis for claims about repeated orientation or changing targets. Continuity with later Egyptian traditions is a separate historical hypothesis, not a consequence of an azimuth match.

## 4. Primary sources change the interpretation

### 4.1 Source disagreement must be separated from extraction error

The source volume's chapter 16, *The Megalithic Alignments*, gives Table 16.1 on printed p. 498. Visual inspection confirms that C-8, C-1 longitude 30.7333, and C-3 latitude 22.5025 occur in that original table. Differences from the later Brophy/Rosen coordinate table therefore cannot simply be blamed on this project's extraction. The chapter's A-row narrative also differs from its tabulated nomenclature: its descriptions associate A-4/A-5 with A2 and A-6–A-10 with A1, whereas the working tabular scheme uses A-0/A-4/A-X and A-5–A-9. This needs a source identity concordance, not an undocumented rename.

The B-row discrepancy is more direct. The chapter's descriptions and table assign B-1 through B-4 to B2, and B-5 through B-7 to B1. The surviving script instead mixes those groups. Unless an independent justification is recovered, its B-row results do not measure the published groups.

A separate project transcription error is confirmed in GPS 2003 A-7: Brophy/Rosen Table 1 prints latitude 22.5131 and longitude 30.7289, while the local CSV/GeoJSON use 22.5130 and 30.7288. The printed table also distinguishes the three coordinate versions. See the [primary article](https://www.maajournal.com/index.php/maa/article/download/82/57/108) and [local table image (local archive)](../LOCAL_ARCHIVE.md).

No legacy records have been silently corrected. Future accepted data should preserve the original value, the proposed correction, the evidence, and its approval status as separate fields.

### 4.2 The historical literature already revised the hypotheses

The 2001 chapter frames the rows as radiating from Complex Structure A. Brophy and Rosen's 2005 reanalysis explicitly calculates bearings from that origin and describes averaging individual stone bearings. It already questions agreement between published coordinates and published alignment angles. A new paper cannot claim that noticing such discrepancies is itself novel. [Brophy and Rosen, 2005](https://www.maajournal.com/index.php/maa/article/download/82/57/108).

The 2007 reassessment is especially important: it interprets five alignments, changes the northern stellar candidate to Arcturus, and declines to interpret the southern C alignment because its stones lie on dunes and may not preserve an original alignment. It estimates a megalith period approximately 4500–3600 BC from archaeological associations, uses a flat physical horizon because ancient dunes are uncertain, and adopts ±0.6° orientation uncertainty. These are published positions to evaluate, not values automatically adopted here. [Malville et al., 2007, original article scan](https://www.eixdelmon.com/wp-content/papercite-data/pdf/McKMahilleSchildWendorfEtAl2007.pdf).

This creates a particularly serious mismatch: the current stellar matcher retains only C1 from the six measured rows, while a later primary interpretation explicitly questions C's archaeological status. That does not prohibit studying C1. It makes C1 an explicit contested-feature scenario rather than an unquestioned astronomical monument.

The 2015 handbook entry is a later synthesis with another presentation of chronology and targets. Its publisher abstract and bibliography were checked; its full text was not available in this assessment. The inherited 2015 CSV is therefore not treated as independently verified. The 2007 journal article and the similarly titled 2008 book chapter must also remain separate bibliography entries. [Malville, 2015, publisher record](https://link.springer.com/rwe/10.1007/978-1-4614-6141-8_101).

### 4.3 Chronology is an input, not a reward for a good match

The working epochs −6500 to −4500 are not, by themselves, a justified construction window. The source literature contains distinct site phases, indirect dates, dated associated features, and astronomical date estimates. These must not be collapsed into one range.

A chronological evidence table should record sample identifier, material, context, laboratory age/error where available, calibration status, calibration method, and the strength of its association with the feature under study. A date near a monument is not automatically its construction date. A date inferred by aligning a star cannot then independently validate that same alignment.

Use one documented convention for astronomical years and historical BCE labels: astronomical year −5000 is 5001 BCE. Distinguish calendrical BP, conventional radiocarbon BP, calibrated years, and BCE. Recalibration requires original measurements and appropriate contextual decisions; subtracting a fixed offset from all reported numbers is inadequate.

## 5. Geometry: the most consequential methodological correction

### 5.1 Define the quantity before choosing the estimator

| Quantity | Question answered | Necessary qualification |
|---|---|---|
| Free fitted line through row stones | What axis best describes this cluster's shape? | An undirected axis; does not assume an observer at Complex A |
| Bearings from Complex A to individual stones | In which directions are these stones seen from a specified origin? | A directed sightline model; origin position and stone extent matter |
| Line constrained through Complex A | What common radial line best fits the group? | Different weighting and residual model from averaging bearings |
| Free line including Complex A as one extra point | What line fits the combined point set? | Not equivalent to fixing an observer; the origin is given a particular statistical weight |
| Physical aperture or viewing corridor | What range of directions could an observer use? | Requires stone shapes, observer location/height, and a defensible reconstruction |

There is no universal best choice. The published hypothesis determines the relevant quantity. Free PCA can be a useful diagnostic of row shape while being the wrong primary estimator for a ray from Complex A. Model choice must not be made by selecting whichever result matches a preferred star.

### 5.2 Isolated diagnostics demonstrate the effect

The new [geometry diagnostics (local archive)](../LOCAL_ARCHIVE.md) operate on inherited coordinates without executing or modifying the old analysis. They assume WGS84, use local geodesic bearings/distances, and compare definitions. They are diagnostic calculations, not accepted archaeological measurements; source identities and errors remain unresolved.

For A3, using the same three inherited row stones:

| Coordinate version | Free row axis, degrees modulo 180 | Mean directed bearing from Complex A, degrees |
|---|---:|---:|
| Legacy | 169.36 | 26.97 |
| QuickBird | 34.55 | 26.31 |
| GPS 2003 | 31.09 | 26.42 |

The free axes differ by as much as about 45.19° under axial comparison. The origin-to-stone mean bearings span about 0.66°. The stones occupy only about 39–44 m internally, roughly 0.93–0.98 km from the origin. A short cluster's own direction is much more sensitive to small coordinate changes than its direction from a distant origin. **An unstable free axis does not establish an unstable radial sightline.** Conversely, stable radial bearings do not prove intentional astronomical observation.

Changing only B membership to the primary table grouping moves the inherited legacy B2 free axis from 107.75° to 118.06°, and B1 from 110.14° to 115.93° in the same diagnostic convention. These are substantial changes before astronomy is considered. The isolated A-7 correction changes the GPS A1 free axis by about 0.35°; it has not been applied to legacy data. Full comparisons are in [estimand and membership diagnostics (local archive)](../LOCAL_ARCHIVE.md) and [source discrepancy scenarios (local archive)](../LOCAL_ARCHIVE.md).

### 5.3 Precision in the files is not precision on the ground

The published coordinate precision is generally four decimal places. At the site, 0.0001° corresponds to approximately 10.29 m east–west and 11.07 m north–south. Reporting orientations to hundredths of a degree cannot recover information lost through rounding. Survey accuracy, identification of fragment centers, and map registration add further uncertainty.

A 10,000-draw sensitivity calculation perturbed coordinates independently within ±0.00005° rounding cells, with a single shared origin per draw. For QuickBird A3, the central 95% of changes in the free axis span approximately −12.0° to +12.6°, versus about −0.40° to +0.39° for the origin-bearing mean. These are **conditional rounding-scenario ranges**, not confidence intervals, bounds on all errors, or evidence that the assumed rounding model is historically correct. The point is how strongly the quantity being measured affects sensitivity. [Rounding diagnostics (local archive)](../LOCAL_ARCHIVE.md).

The inherited script also reports projected UTM grid bearings as if they were true-north bearings. Diagnostic grid convergence near Complex A is approximately −0.87°; computed free grid axes are about 0.87° greater than the corresponding local true axes here. Any correction must be implemented with a tested convention, not inserted by intuition. That difference matters when discussing sub-degree agreement.

### 5.4 Resampling and uncertainty need redesign

PCA singular vectors have arbitrary sign: an axis at θ is the same axis at θ+180°. The old leave-one-out and bootstrap calculations use directional rather than consistently axial comparisons. Their roughly 100–180° bootstrap dispersions are not usable line-orientation uncertainty estimates.

Small groups cause an additional problem even after sign handling is corrected. For three points, an ordinary size-three bootstrap has 27 ordered resamples: three contain one distinct point and 18 contain only two. A two-point group has zero variance in half its bootstrap resamples. The diagnostic enumerates these cases explicitly. Discarding degenerate draws can clarify a diagnostic but does not automatically make the remaining distribution a valid confidence interval. [Bootstrap diagnostics (local archive)](../LOCAL_ARCHIVE.md).

Use leave-one-stone-out analyses to report leverage and sensitivity. Use a justified measurement-error model for positional uncertainty. Model missingness and alternative memberships explicitly. Do not treat resampling a small fixed archaeological group as a universal substitute for known survey errors. PCA is also not intrinsically resistant to outliers.

### 5.5 Three coordinate versions are not 18 independent monuments

Repeated measurements of the same physical stones provide information about measurement differences, not independent replication of the cultural act. Shared origins, source lineage, image registration, common shifts, and fragment identification induce dependencies. A common translation can leave internal geometry unchanged; a common rotation changes orientation. A model that perturbs every coordinate independently can misrepresent both effects.

Future comparisons should separate matched-stone comparisons from all-available-point analyses, because the GPS version lacks B-2 and C-2. Do not pool the three versions as exchangeable observations until their relationship is justified. A small sample and substantial shared assumptions limit the strength of population-level conclusions.

The georeferenced source figures are also not independent confirmations: their control points include positions matching the GPS 2003 table. Measuring a figure after registering it to those coordinates inherits that information. The figure can assist identity checking, but independent accuracy would require documented transformations and withheld checks, not agreement with the same control data.

## 6. Astronomy and terrain: what survives scrutiny

The modular idea—geometry, horizon, celestial predictions, then hypothesis assessment—is sensible. Its present interfaces and assumptions are not reliable enough to support the saved claims. Detailed code references and diagnostics are in the [astronomy and statistics audit (local archive)](../LOCAL_ARCHIVE.md).

| Problem | Verified evidence | Required consequence |
|---|---|---|
| Incomplete horizon coverage | Code requests 20 km; the raster is only about 10.1 × 5.75 km and out-of-bounds samples are silently dropped | Report actual coverage by bearing and establish an adequate terrain domain before interpreting horizon effects |
| Unspecified ancient observing conditions | No explicit eye height in terrain rays; modern DEM, nearest-neighbor sampling, no explicit terrain curvature/refraction model | Construct defensible scenarios and assess their effect at the precision needed for the question |
| Solar refraction claim exceeds implementation | Final `altaz()` calls omit atmospheric parameters; fixed −0.8333° is used only in initial bracketing | Recompute a clearly specified event, including solar limb and atmospheric assumptions consistently |
| Lost stellar astrometry | Export has ID, magnitude, declination and status, but omits RA, proper motion, parallax and reference epoch required downstream | Preserve a full validated catalog schema; fail on required missing data rather than substituting zero |
| Wrong reference frame for ancient-pole reasoning | `.radec()` is called without a date-equator epoch | Recompute with a consistent ancient reference frame or validated direct topocentric calculation |
| Wrong numeric epoch meaning | A negative calendar year is supplied as a numeric `Star` epoch | Supply the documented time representation; test the conversion |
| Targets overwritten | Dictionary keys contain only dataset, so each row replaces its predecessor | Use stable physical-feature and source-version identifiers; verify all intended targets survive |
| Impossible events manufactured | Out-of-range cosine values are clipped instead of rejecting non-crossing objects | Explicitly classify possible crossings; never turn a circumpolar object into a synthetic rising event |
| Incomplete bright-star population | Saved 254-star sample has brightest G ≈ 1.94 despite an upper cutoff G < 3.5 | Audit completeness and photometric selection; do not treat it as the complete visible sky |
| Unvalidated millennial stability | All 132 matches are labelled strong across three epochs, with rounded position spans only 0–0.01° | Withdraw those labels; repeated faulty predictions are not robustness evidence |

The software contracts are explicit: Skyfield's default RA/declination coordinates use fixed ICRS axes, while a supplied epoch requests equator/equinox coordinates for that date. Atmospheric refraction is also opt-in for `altaz()`. These are direct implementation errors, not disagreements over archaeological interpretation. [Skyfield coordinates](https://rhodesmill.org/skyfield/coordinates.html), [position API](https://rhodesmill.org/skyfield/api-position.html).

Gaia's astrometric bright limit is material to this particular query. A positive-parallax filter adds another selection rule. A defensible naked-eye target population needs a documented completeness strategy, cross-identifications, and a brightness definition appropriate to the observation being modeled. A Gaia G cutoff is not automatically a visual-magnitude or human-detectability threshold. [ESA Gaia DR3 contents](https://www.cosmos.esa.int/web/gaia/dr3).

The local DE441 kernel does cover the ancient epochs requested by the scripts; that specific concern has been resolved through header inspection. Coverage does not certify the entire astronomical model. Long-term precession, stellar motion, reference frames, time conventions, and visibility remain separate issues. An isolated comparison of the bundled precession calculation with ERFA's long-term model found rotation differences of about 0.061° at astronomical year −5000 and 0.195° at −6500. These are model differences, not corrected alignment azimuths or calibrated error bars. They warrant an independent benchmark over the actual research date range. [Diagnostic record (local archive)](../LOCAL_ARCHIVE.md), [ERFA implementation](https://raw.githubusercontent.com/liberfa/erfa/master/src/ltp.c).

The highest priority is still the basic geometry and frame errors, not increasingly elaborate atmospheric modeling. Once those are fixed, build an uncertainty budget to determine which secondary effects can change the conclusion. Do not invest heavily in a sub-degree sky calculation if the feature's origin, identity, or orientation is uncertain by several degrees.

### Visibility is a different question from geometric crossing

A star crossing the mathematical horizon is not necessarily visible. Extinction, brightness, twilight, dust, local horizon, and the observing event matter. Heliacal rising requires a model involving the Sun and first visibility; it is not ordinary daily rising. An upper-limb solar event differs from a point-source stellar event. The 2001 source chapter already discusses extinction, so this is a substantive part of the historical hypotheses rather than an optional refinement.

Likewise, a modern DEM cannot establish the prehistoric dune horizon. It can constrain topography or support sensitivity scenarios, but its date, source, resolution, vertical datum, interpolation, and uncertainty must be stated. A present-day horizon and an archaeological horizon should remain separate products.

## 7. Statistical inference needs reconstruction, not a new test name

### 7.1 Why the current significance results fail

The 132 saved matches reduce to 44 unique star–target–event combinations and 35 stars. Epoch repetitions are model evaluations, not additional observations. In the constellation table, nine Gemini hits represent three stars; some groups exceed the manually assumed constellation population. The hypergeometric model can consequently return zero because its supplied count is impossible. Other probabilities are rounded to zero. The plot then substitutes 10⁻¹⁰ for saved zeros, displaying a significance level unsupported by the stored calculation.

Even deduplicating the table would not repair the model. Stars in a constellation are spatially clustered and do not constitute exchangeable draws from a uniform star population for this alignment search. The constellation populations are approximate, the eligible sky is incomplete, and the analysis searches many features and choices. Modern constellation membership also supplies no independent evidence of Neolithic categories.

The stress-test stage is unfinished: isolated inspection confirms that its two named Astropy imports are unavailable in the preserved version. More fundamentally, its null “sky” is selected from successful matches, and its site pattern is derived from the same successes. That conditions the comparison on the discoveries it purports to assess. It also treats repeated survey solutions as additional monuments. Neither a repaired import nor more Monte Carlo iterations would fix these problems.

### 7.2 Keep the inferential levels separate

The logical sequence should be:

**Documented feature → measured geometry → physically possible observation → compatibility with a stated hypothesis → evidence relative to alternatives → archaeological interpretation.**

Each step needs its own evidence. A compatible azimuth does not establish intentionality. Rejecting a uniform-orientation model does not establish an astronomical cause. Failure to reject with a small sample does not establish randomness. Statistical significance does not identify a particular cultural meaning. [American Statistical Association statement on p-values](https://www.amstat.org/docs/default-source/amstat-documents/p-valuestatement.pdf).

For a specified direction and geometric horizon altitude, the implied celestial declination provides a useful intermediate quantity:

`sin(δ) = sin(φ) sin(h) + cos(φ) cos(h) cos(A)`

Here φ is site latitude, h is the consistently defined geometric altitude, and A is true azimuth measured from north. Propagate the joint uncertainty rather than inserting a nominal angle alone. Limb and refraction conventions must first be translated into the corresponding geometric event. The resulting overlap with a candidate's declination indicates compatibility under assumptions; it is not a probability of prehistoric intent.

### 7.3 Choose a null for a precise question

| Proposed design | What it could assess | What it cannot establish automatically |
|---|---|---|
| Predetermined published target and feature | Angular mismatch or compatibility over an independently supported date range | Unique identification, cultural meaning, or chance probability without further assumptions |
| Rotation of the entire physical pattern | Unusual absolute orientation relative to a complete prespecified sky, conditional on the existing internal pattern | That the rows themselves are non-accidental; that uniform rotation is plausible under terrain constraints |
| Landscape/construction-constrained model | Compatibility relative to a specified non-astronomical placement process | Validity of that process unless independently supported and checked |
| Spatial simulation with row detection repeated | Frequency of comparable geometry and matches after the same selection procedure | Reconstruction of undocumented historical selection without an eligible feature universe |
| Independent prospective case | Whether the frozen procedure transfers to different evidence | Universal applicability after one success |

A rotation test should preserve relevant within-site dependence and evaluate the horizon at the new bearings. The full eligible geometry and sky belong in the comparison, not only successful matches. If features, origins, or memberships were selected because they looked promising, that selection must be reproduced in each simulated dataset, addressed by a justified selective-inference procedure, or tested on genuinely independent evidence. Otherwise restrict the result to descriptive compatibility, without a calibrated chance or intentionality claim; merely conditioning on the selected set does not repair selection bias.

Multiplicity includes stars, events, both ends of axes, observer positions, rows, dates, membership choices, tolerances, magnitude thresholds, and constellation groupings. Correcting a handful of final p-values cannot account for an unrecorded search. Prefer a small, source-justified primary hypothesis set. Where broad exploration is useful, report the search space and calibrate the complete search statistic.

For an appropriate finite randomized test, report the number of simulations, exceedance count, seed, and Monte Carlo uncertainty; a calculation such as `(b+1)/(B+1)` prevents impossible claims of zero probability when its assumptions apply. With 10,000 simulations this convention cannot resolve probabilities below roughly 0.0001. No arbitrary replacement of zero by 10⁻¹⁰ is acceptable. [Phipson and Smyth, 2010](https://gksmyth.github.io/pubs/PermPValuesPreprint.pdf).

### 7.4 Retrospective development must remain visible

Nabta is already explored material. The outcomes have influenced choices. A frozen and transparent reanalysis can substantially improve it, but cannot retroactively make its discovery history prospective. A claim register should distinguish hypotheses taken from published literature, hypotheses developed during this project, and validation checks specified afterward.

The second study is the opportunity to test a frozen protocol on evidence not used to develop it. That distinction should be designed now, not added in the discussion after another round of exploration.

## 8. Disposition of the existing outputs

| Output or claim | Present disposition | Requirement for future use |
|---|---|---|
| Primary figures and coordinate transcriptions | Preserve as source evidence | Cell-by-cell audit and identity/provenance ledger |
| Six-row geometry table | Exploratory historical result | Recompute after membership, estimand, north convention, missingness and uncertainty decisions |
| A3 instability | Retain as a question about the free-axis estimator | Do not generalize it to all origin-based sightline models |
| C1 summary | Historical values disagree with draft | Regenerate from one accepted run and treat archaeological status explicitly |
| “25° and 90° orientation families” | Unsupported by the saved six-row geometry as presented | Identify the actual measured features and their source definitions; a manual 90° target is not a fitted row |
| Bootstrap uncertainty figure | Retire from evidential use | Replace with appropriate axial and measurement-model diagnostics |
| Horizon figure and ~0.221° solar shift | Exploratory output | Validate coverage, event model, observer and landscape assumptions; remove plot clipping |
| Stellar match table and “STRONG” labels | Retire as scientific conclusions | Recompute from full astrometry and validated geometry/events |
| Constellation significance table/plot | Retire the analysis and its claimed inference | A different, archaeologically justified question and calibrated design would be needed |
| Sky map | Illustration of uncertain provenance | Regenerate from validated coordinates and distinguish illustration from evidence |
| Stress-test script | Unfinished prototype | Replace with a specified, validated inferential design |
| Current prose | Useful history and rough structure | Rewrite around accepted research questions and generated results |

The saved C1 summary gives mean directional representation 314.18°, maximum cross-dataset difference 5.40°, and mean RMS 21.06 m; the interim draft instead gives approximately 2.85° and 13 m for the latter two. Those are manuscript-to-output inconsistencies, not new research findings. The nearly zero RMS of the inherited two-point GPS B1 fit is mathematical inevitability, not construction precision. The horizon slide caps its vertical axis below the saved maximum. Such issues illustrate why future figures and tables must be generated from a single authoritative result set.

## 9. Where a contribution to the field could lie

Uncertainty propagation and quantitative assessment of orientations are established topics. Silva's 2020 paper already develops a probabilistic framework, transforms orientation distributions into celestial coordinates, and evaluates significance with archaeological applications. Its methods and examples are essential comparators. [Silva, 2020](https://eprints.bournemouth.ac.uk/33905/7/1-s2.0-S0305440320300601-main.pdf).

Software integration is also not an empty niche: skyscapeR provides data reduction, visualization, and analysis for this field. The project should compare or reuse suitable existing components rather than claim novelty from combining GIS, astronomy, and statistics. [skyscapeR repository](https://github.com/stonexsky/skyscapeR).

The promising increment is an operational treatment of **source conflict and limits of inference before astronomical attribution**. That would connect several elements which must be demonstrated together:

- A traceable ledger separates what the source prints from what the analyst infers or corrects.
- Feature definitions determine the quantity measured, and alternatives are evaluated explicitly.
- Correlated measurement error, coordinate rounding, source disagreement, and physical ambiguity remain distinguishable.
- Sensitivity analysis identifies which assumptions control the archaeological conclusion.
- Calibrated decision rules allow an unresolved result when the evidence lacks discrimination.
- A portable protocol is tested against existing methods and on independent material.

This is a proposed contribution, not an established priority claim. The literature search was focused rather than a systematic proof that no equivalent approach exists. Before making novelty claims, construct a comparison matrix covering source provenance, geometry models, positional uncertainty, observer uncertainty, horizon/chronology, selection adjustment, simulation calibration, and external validation. Identify the actual gap and demonstrate why filling it changes an inference.

The conceptual value should be expressed in archaeological terms: for example, showing when apparent disagreement between publications comes from different quantities being measured; when rounded coordinates can or cannot discriminate proposed celestial targets; or when a stronger dataset is necessary. A well-engineered reproduction of known calculations is useful infrastructure, but it becomes a substantive paper only when it answers a consequential question or establishes a demonstrable methodological improvement.

## 10. Recommended first paper

**Working question:** What can published spatial evidence establish about astronomical alignments at Nabta Playa, and which interpretations survive explicit source and model uncertainty?

**Provisional title:** *What can published coordinates establish about Nabta Playa's megalithic alignments? A source-critical uncertainty analysis.*

The paper should have a bounded core: the published radiating rows, their source history, and a limited set of historically stated hypotheses. The calendar circle should be a separate module only if its original geometry and observation model are sufficiently documented. Do not bundle museum photogrammetry, unrestricted sky searches, a new chronology, and a generalized framework into one small case study.

The minimum substantive result is not merely a cleaned dataset. It is a reproducible demonstration of how specific defensible decisions alter—or fail to alter—the inference, together with the archaeological consequence. Three outcomes are possible:

| Outcome after validated analysis | Defensible paper emphasis |
|---|---|
| A published association survives reasonable alternatives | State its compatibility and the degree of discrimination, while retaining alternative causes and cultural limits |
| An association is incompatible under the supported evidence | Explain the source/model reason and the exact claim affected; do not generalize to all Nabta astronomy |
| Several interpretations remain indistinguishable | Quantify the information limit, identify the evidence needed to resolve it, and validate the method's ability to recognize that limit |

None is guaranteed to be novel or sufficient for acceptance. Each can support a useful paper if its question, evidence, and methodological increment are strong enough.

### Suggested manuscript architecture

1. Archaeological problem and the changing published claims.
2. Source corpus, feature identities, preservation/context, and chronology.
3. Measurement definitions and uncertainty assumptions.
4. Validation and comparison with existing approaches.
5. Results: source differences, geometric sensitivity, and bounded astronomical tests.
6. Interpretation: what is supported, contradicted, or unresolved and why.
7. Transferable lessons and explicitly limited scope.

Useful main figures would be a source/feature map distinguishing origin rays from free axes; a source-lineage diagram; a scenario comparison of orientation estimates; and, where justified, uncertainty-aware compatibility against specified targets. A claim-by-scenario table may communicate more than a crowded sky chart. The full source ledger, diagnostics, candidate universe, and run manifest belong in supplements.

### Venue fit

The **Journal of Skyscape Archaeology** is a plausible first choice if the central result is an archaeologically grounded reassessment of Nabta interpretations. Its submission page describes peer review; exact current format and policies should be checked when the manuscript is ready. This is a fit recommendation, not an editorial judgment. [JSA submissions](https://journal.equinoxpub.com/JSA/about/submissions).

The **Journal of Computer Applications in Archaeology** is a plausible alternative if the validated computational method and transferable case-study procedure become the central contribution. Its society's scope explicitly includes spatial analysis, statistics, digital reconstruction, and case studies applying established methods to archaeological questions. [CAA journal scope](https://sites.caa-international.org/main/journal/).

**Journal of Archaeological Science: Reports** is a more conditional option. A co-editor's guide emphasizes clear archaeological questions and wider relevance, and cautions about small-sample case studies. The scientific and archaeological contribution would need to justify this dataset's size. That guide also sets restrictive expectations around generative AI use; the final venue's current policies must govern manuscript preparation and disclosure. This internal AI-assisted assessment is not submission-ready authorship or a substitute for human responsibility for the research. [Ellery Frahm's editorial guide](https://www.elleryfrahm.com/jasrep).

Venue selection should follow the actual result and contribution. No submission, correspondence, or publication action has been taken.

## 11. What would make the second study a framework test

The larger study should test transferability, not merely add stars, more output plots, or a second application tuned after inspection. Before inspecting its astronomical outcomes, freeze the first study's reusable protocol and define what counts as success, failure, and an unresolved case.

Choose new material for data suitability and methodological contrast, rather than a reputation for impressive astronomical alignments. Useful contrasts include better versus poorer survey precision, different feature geometry, different horizon complexity, different preservation, or a larger independently documented set of structures. The date range and archaeological interpretation should be independently constrained. A second case with several independently sampled units may offer stronger validation than one more small monument group.

The protocol should specify the eligible features, exclusion rules, measurement models, candidate hypotheses, uncertainty inputs, primary statistics, and decision rules. Record deviations before interpreting their consequences. Where feasible, separate feature extraction from astronomical matching and keep some cases or outcomes held out until the method is frozen.

Assess four properties: reproducibility of the computations; reproducibility of analyst decisions; statistical calibration; and archaeological usefulness. Two analysts should be able to follow the same source rules without silently defining different objects. Synthetic null and injected-signal datasets should establish false-positive behavior, power, interval coverage where claimed, and the conditions producing unresolved results. Comparisons with existing methods should show whether the added procedures improve reliability rather than merely increase complexity.

One additional case can demonstrate successful transfer to that setting. Generality across the field requires variation in the relevant conditions and clear boundaries of applicability. A framework should document when it should not be used or when available evidence is insufficient.

## 12. Work required, in order

This is a proposed research program. The assessment has not implemented these repairs or generated replacement astronomical results.

| Stage | Work and deliverable | Exit condition |
|---|---|---|
| 1. Establish the evidential baseline | Source ledger, feature concordance, claim/chronology register, checked coordinate tables and documented unresolved alternatives | Every included feature and hypothesis has a traceable definition; uncertainty is not hidden in silent corrections |
| 2. Freeze the first-study design | Primary questions, estimands, observer models, eligible target set, chronology, scenario policy and exploratory boundaries | Models are justified by evidence rather than favorable outcomes |
| 3. Rebuild the minimal analytical core | Separate accepted-data workspace, validated geometry, explicit schemas, north conventions, missing-data handling | Independent geometric benchmarks and invariance checks pass |
| 4. Establish astronomical adequacy where needed | Complete catalog strategy, reference frames, dates, event solver, terrain coverage and visibility scenarios | Relevant predictions agree with independent benchmarks within a justified tolerance |
| 5. Calibrate inference | Realistic rounding/error/membership simulations, complete selection-aware nulls if used, power and false-positive checks | The method performs as claimed and reports limits honestly |
| 6. Run and interpret Nabta | Versioned scenario results and claim disposition table, including adverse and unresolved outcomes | Each conclusion survives its stated checks or is explicitly conditional |
| 7. Prepare publication package | Manuscript, generated figures/tables, reproducible supplement, rights-cleared materials and external critique | A reader can reproduce central results and assess the archaeological argument |
| 8. Freeze and test transfer | Prospective second-study protocol and independent data selection | The extension tests declared capabilities instead of tuning itself to another desired finding |

### Immediate priorities

The first work package should be the **source and claim ledger plus a minimal geometric comparison**. It should resolve the A/B/C identity issues as far as the evidence permits, retain alternatives where necessary, and compare the historical bearing definitions with free-axis diagnostics. That is the shortest route to deciding what the paper can credibly ask.

After that, choose a small published hypothesis set and evaluate whether available spatial and chronological resolution is sufficient. Only then decide how much astronomical infrastructure is justified. Building a broad search engine first would create more unvalidated outputs without resolving the main uncertainty.

Potentially useful new evidence includes unrounded survey coordinates, original mapping/registration metadata, field records clarifying fragment identities and observation points, and source-specific chronology. Contacting researchers or archives is a possible later step, not something performed here. New fieldwork is not automatically required for a desktop evidence-limit study; it may be essential if the intended claim demands precision or landscape reconstruction unavailable in publications.

### A practical publication-readiness test

The case study is ready to become a submission only when all of the following are true:

- The archaeological units and the hypotheses being tested are explicit and source-supported.
- The central data have been audited; unresolved source conflicts remain visible.
- The measurement definitions actually correspond to those hypotheses.
- Appropriate uncertainty and dependence are carried through to the conclusion.
- Astronomy, visibility and chronology are adequate for the particular claim, with independent checks.
- Any significance statement evaluates the relevant selection process and has demonstrated calibration.
- The paper adds a result or methodological insight beyond existing reanalyses and frameworks.
- The central results are reproducible from a versioned package and accurately represented in the text and figures.
- An archaeologically informed reader and a quantitative reviewer have challenged the argument before submission.

There is no honest percentage-complete estimate at present: source adjudication and model choice may change the research question. The surviving archive saves substantial recovery work, but the inferential foundation still needs rebuilding.

## 13. Reproducibility and evidence-management requirements

Keep `legacy/` immutable as the inherited record. Future work should separate raw source transcriptions, adjudicated data, analysis code, run configurations, generated outputs, and manuscript assets. Preserve source versions rather than overwriting them. A compact claim register should link each proposed sentence or numerical conclusion to its input records, method, run, uncertainty assumptions, and disposition.

The reproducible package should contain stable identifiers, units and coordinate conventions; schema validation; source and transformation metadata; environment versions; random seeds; and checksums/run manifests. Generate paper tables and figure labels directly from accepted outputs. Record errors and exclusions as structured outputs, not only console messages. Missing astrometry or absent terrain coverage should stop the dependent analysis or produce an explicit incomplete status.

The copied virtual environment is evidence of the old setup, not a portable dependency specification. Its configuration records Python 3.13.5, but an isolated diagnostic invocation resolves to Python 3.13.15 on this laptop; that drift itself illustrates why executable and package versions must be recorded per run. Scripts contain original absolute paths and inconsistent input/output locations. The QGIS project also has broken home-relative and temporary-file references. These need repair in a new working version before anyone can claim clean reproducibility.

Do not redistribute the whole 8.6 GB inherited snapshot as a publication supplement. A useful research package contains the necessary derived data and code, lawful source-access instructions, and documented access to large dependencies. The source book, satellite imagery, and reproduced figures require appropriate rights handling. Preserve AI-assisted code and prose provenance where relevant, verify every source and claim, and disclose assistance according to the chosen venue. Authorship and responsibility remain human research decisions.

## 14. Assessment scope and supporting evidence

This pass combines inspection of the inherited documents, data, source figures, scripts and outputs; targeted primary-literature checks; official software documentation; and isolated diagnostic calculations. It did not run the inherited pipeline, overwrite its outputs, query a new stellar catalog, repair research code in `legacy/`, complete new field measurements, or produce validated replacement astronomical conclusions.

The assessment is thorough for the recovered materials, but it is not a systematic literature review or a complete independent replication. The 2015 chapter's full text remains a source-access gap. Original field precision, several identity relationships, ancient observing conditions, and any unrecorded analysis decisions remain open. The new numerical diagnostics deliberately expose sensitivity rather than establish final answers.

Supporting notes and evidence:

- [Initial orientation and inventory](ORIENTATION.md).
- [Geometry and primary-source audit (local archive)](../LOCAL_ARCHIVE.md), with [executable diagnostics (local archive)](../LOCAL_ARCHIVE.md) and [metadata (local archive)](../LOCAL_ARCHIVE.md).
- [Astronomy and statistics audit (local archive)](../LOCAL_ARCHIVE.md), with [artifact diagnostic record (local archive)](../LOCAL_ARCHIVE.md).
- [Literature and contribution assessment (local archive)](../LOCAL_ARCHIVE.md).

The strategic recommendation is to make the first paper establish **what can be inferred, under which assumptions, and at what resolution**, and make the second study test whether that discipline travels. That is a credible route toward the user's larger objective: a solid contribution to the field, regardless of whether any particular Nabta stellar interpretation survives.
