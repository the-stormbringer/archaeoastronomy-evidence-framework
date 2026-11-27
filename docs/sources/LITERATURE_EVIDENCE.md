# Literature evidence used by the Nabta development case

Compiled November 27, 2026. This is a **referenced evidence digest**, not a full-text collection or a newly completed source audit. Statements below paraphrase published material as recorded in the project's existing source reviews; numerical values reproduce transcribed facts. There are no extended verbatim extracts. The review depth and unresolved premises remain as stated in the underlying records. W1 source adjudication is still open.

Citations use Chicago author–date and **printed** page locators. Full references are in the [Chicago bibliography](BIBLIOGRAPHY_CHICAGO.md); exact copy hashes/access locators are in the [catalogue](CATALOGUE.json). Primary publications are not included in the clone. The [dependency map](LITERATURE_DEPENDENCIES.md) identifies work that requires them. This digest points to evidence rather than replacing examination of a disputed passage.

## 1. Published coordinate observations and membership

**Source facts and scope.** The coordinate table in Wendorf and Malville (2001, 498, table 16.1) and the columns in Brophy and Rosen (2005, 16–17, table 1) are the basis of the numerical case. Our ledger contains 100 records: 25 entries in each of four documentary representations, including origins and missing coordinate pairs. They are not 100 separate monuments or four independent surveys.

| Ledger version | Published record represented | Use in our work |
|---|---|---|
| `WM2001_original` | Original 2001 table | Source-specific baseline |
| `BR2005_repeated_WM2001` | 2001 values repeated in 2005 | Detect transcription/representation differences; not independent survey evidence |
| `BR2005_QB2002` | 2002 satellite-derived column | Separate coordinate scenario |
| `BR2005_GPS2003` | 2003 GPS column | Separate coordinate scenario, preserving missingness |

The original origin is printed as latitude 22.5080 and longitude 30.7256. The same original-table records give A-4 as (22.5150, 30.7297), A-X as (22.5137, 30.7290), A-5 as (22.5134, 30.7291), and A-6 as (22.5132, 30.7290). These are printed decimal-degree representatives; datum and physical observation-point identity must not be inferred from precision alone (Wendorf and Malville 2001, 498).

Narrative feature descriptions and tabulated A1/A2 memberships differ; A-10 is described but lacks a coordinate in the older table. The ledger preserves 47 membership entries across two alternatives. Do not manufacture the missing coordinate or quietly select the alternative giving a preferred result (Wendorf and Malville 2001, 490–91, 498–500).

**Project use:** W1-01/02, E1–E3. Exact input files: [coordinate observations](../../data/source/source_coordinate_observations.csv), [membership alternatives](../../data/source/membership_scenarios.csv). Read-depth basis: [reconciliation decisions](../evidence/source_reconciliation-2026-10-22/DECISIONS.md), which records visual table checks. These are prior checks, not a fresh cell-by-cell verification in this digest.

## 2. Observation-point conventions and reductions

Brophy and Rosen discuss positioning GPS over an estimated centre and possible identification of different fragments. They distinguish image-position offset from relative geometry and present recalculated and combined-survey directions. Thus it would be incorrect to claim that their paper entirely ignores physical identification or observation-point definition (Brophy and Rosen 2005, 17–20, tables 1–2).

**Our calculation, not a quotation or author-method attribution:** spherical initial bearings followed by arithmetic means reproduce the six entries of the repeated-2001 direction column to its printed precision. This establishes a sufficient recipe, not the authors' exact implementation. The final combined-survey reduction is not thereby recovered. Our failed-combination screen is restricted to its declared tested family, not every conceivable reduction.

**Project use:** W1-05 and E3; [column reproduction](../evidence/source_reconciliation-2026-10-22/BR2005_WM_column_reproduction.csv), [method review](../evidence/analysis/geometry-comparison-2026-10-23/METHOD_REVIEW.md). Published directions are evidence to reconcile, not error-free targets to force a fit against.

## 3. Original reported directions and source-version differences

The Nature article reports three northern directions of 24.3°, 25°, and 28°, together with 90.02° and 126°. It describes the 1997 mapping as combining theodolite and differential GPS. Its printed origin uses a W longitude hemisphere, inconsistent with the stated Egyptian site; any E reinterpretation must be explicit. The five reported directions do not come with an established one-to-one crosswalk to all later six-group definitions (Malville et al. 1998, 489).

Later claim tables differ: the A2 direction is 28.1° in the 2007 table and 28.3° in the 2008 chapter. These must remain source-specific claims rather than being silently averaged or corrected (Malville et al. 2007, 5; Malville et al. 2008, 139). The 2015 table returns to 28.1° (Malville 2015, 1086).

**Project use:** W1-02/05, historical selection record and published-claim provenance. See [supplied-source reconciliation](../evidence/source_reconciliation-2026-10-22/SUPPLIED_SOURCE_RECONCILIATION.md) and [claim ledger](../../data/source/published_claims.csv). This does not establish five-versus-six physical identity equivalence.

## 4. Published stellar target dates

The following ranges reproduce seven date-bearing rows in the 2007 table, with its BC convention retained. They are astronomical associations reported by the authors, **not independently measured construction dates** (Malville et al. 2007, 5).

| Alignment | Target as reported | Published range (BC) |
|---|---|---:|
| A3 | Arcturus | 4530–4320 |
| A2 | Arcturus | 4220–4020 |
| A1 | Arcturus | 3810–3630 |
| B2 | Alnilam | 4340–4150 |
| B2 | Sirius | 3700–3430 |
| B1 | Sirius | 4640–4400 |
| B1 | α Centauri | 4500–4260 |

The table also includes a B2 winter-solstice claim without a numerical date range. Do not insert a date for that row. Later BP-labelled ranges are retained in their own fields; an observed arithmetic offset between sources does not justify silently changing the conventions.

**Project use:** W1-05 and conditional chronology comparisons; [complete published claims](../../data/source/published_claims.csv), [date-label comparison](../../data/reference/analysis/identity-chronology-2026-10-24/date_label_comparison.csv). No fresh stellar calculation is implied.

## 5. Later physical identities and map limits

The 2025 alignment descriptions assign both A-X and A-4 to square r/20, and both A-5 and A-6 to x/20. The text also locates A-10's embedded base at j’/17. This provides documentary identity/condition evidence, not unrounded survey coordinates (Schild 2025, 140–41).

The r/20 and x/20 assignments were independently revisited by the lead agent on November 23, as documented in the [source spot-check](../audits/2026-11-23-SOURCE_CHECK.md). That single source review did **not** establish map scale, the correspondence of older coordinate representatives to later descriptions, or ancient original positions. Two workers reviewing the derivative ledger are not two independent primary-page confirmations.

Descriptions of displacement, erosion/creep and fragment conditions constrain physical reconstruction. The later mapping account concerns specific surveys and transformations; precision stated for another surveyed feature cannot simply be assigned to every radial row (Schild 2025, 23–24, 139–42).

**Project use:** W1-03/04 and E4; [identity crosswalk](../evidence/source_reconciliation-2026-10-22/monograph2025/alignment_A_identity.csv), [map audit](../evidence/source_reconciliation-2026-10-22/monograph2025/map_audit/README.md). Map path centres are drawing observations, not stone survey points. No nearest-angle/proximity rule settles identity.

## 6. Contextual radiocarbon measurements and discrepancies

The sourcebook reports DRI-3358 as 4800 ±85 radiocarbon BP in table 3.1, but as 4800 ±80 in the Structure E discussion. These are conflicting reports of the same sample, not two independent dates. The sourcebook also lists CAMS-17287 at 6000 ±60 BP for a calendar-circle hearth and CAMS-17289 at 6470 ±270 BP for another monument. None is a direct date for installation of an individual A/B/C row (Wendorf and Schild 2001, 54, 517).

The circa-4800 BC interpretation for Complex A is conditioned in the discussion on its role in the stellar alignments, so it cannot independently validate those same astronomical associations. Relative sequencing and that absolute interpretation must be separated (Wendorf and Schild 2001, 520).

Malville's figure shows five quarry-labelled values, 5600 ±40, 5530 ±40, 5460 ±40, 5450 ±40 and 5470 ±40 BP. Figure labels alone do not identify laboratory context or independent events. The Ring Hill entries must not be pooled with quarry values merely because they occur in the same illustration (Malville 2015, 1087, fig. 89.9).

**Project use:** W1-05; [chronology evidence](../evidence/source_reconciliation-2026-10-22/chronology_evidence.csv). No recalibration was performed by compiling this digest, and reported uncertainties retain their source qualifications.

## 7. Quarry chronology in the 2025 volume

The quarry chapter supplies laboratory IDs and contexts. For example, Poz-7818 (5530 ±40 BP), Poz-73203 (5580 ±40 BP), and Poz-7917 (5600 ±40 BP) are all assigned to Trench 1, Unit 5 Upper, Hearth 1 at E-04-4. Treating them as three independent construction episodes would discard their common context (Królik et al. 2025, 87).

The chapter discusses quarrying/installation broadly around 4600–4200/4100 BC while leaving undated pits and possible later extraction. Occupation/fill of a quarry depression does not necessarily date extraction of a particular slab. The sixteen transcribed determinations include older results and context-reporting discrepancies; they must not be trimmed into one preferred construction estimate (Królik et al. 2025, 87–105, especially 101–5).

**Our inference boundary:** comparing a target-fit range with these proposed windows is a conditional compatibility screen. Non-overlap does not by itself reject a target; overlap duration is not a target probability or posterior construction date.

**Project use:** W1-05; [seven E-04-4 records](../evidence/source_reconciliation-2026-10-22/monograph2025/quarry_E04_4.csv), [all sixteen records](../evidence/source_reconciliation-2026-10-22/monograph2025/quarry_all16.csv), [context reconciliation](../evidence/source_reconciliation-2026-10-22/monograph2025/README.md).

## 8. Calendar-circle reassessment: separate scope

Iwaniszewski contrasts the Nature direction with a broader viewing direction in the archaeological source and discusses zenith-passage sunrise as an alternative interpretation. A viewing aperture is not automatically a Gaussian measurement error. The tabulated 4890 BCE sunrise directions are model outputs under particular assumptions, not observed stone bearings (Iwaniszewski 2021, 12, table 1).

The 2009 conference contribution was published in 2021 proceedings. It is no longer an inaccessible manuscript in the owner's library, but it concerns E-92-9 and does not replace the radial-row survey. Hearth chronology and construction inference remain distinct.

**Project use:** optional calendar-circle branch only; [reassessment record](../evidence/source_reconciliation-2026-10-22/SUPPLIED_SOURCE_RECONCILIATION.md). Its inclusion does not open E6 automatically.

## 9. Direct predecessors and methodological dependence

| Literature | Information used and read-depth basis | Consequence for this project |
|---|---|---|
| Haynie (2014, 63–73, figs. 1–3) | Full-text project review records stellar reassessment, inconsistency/visibility discussion, alternative targets and chronological context. Figure 2 derives from coordinates supplied by Malville; a complete numerical input table is not supplied there | Recalculation or proposing other stars is not our novelty. Do not digitize the schematic into asserted original survey data. See [review](../evidence/source_reconciliation-2026-10-22/haynie2014/REVIEW.md) |
| Silva (2017, 93–111) | Reviewed abstract, simulation discussion and conclusion compare accuracy/precision of alignment inference methods and discuss uncertainty limitations | Do not claim invention of uncertainty analysis or assume a single target/known feature without argument |
| Silva (2020, secs. 2–3) | Reviewed methods concern orientation distributions, celestial transformation and significance/null-model questions for identified features | Our prior question is evidence/feature definition; no superiority or performance advantage is established without a fair benchmark |
| Silva (2021, 325–26) | Complete software notice describes skyscapeR's reduction/analysis capabilities | Software integration itself is not a novel contribution; notice claims are not an independent benchmark of the installed code |

These are focused comparisons, not an exhaustive novelty review. See [prior-work assessment](../manuscript/PRIOR_WORK_COMPARISON.md). W1-06 still requires a documented search and claim-specific inclusion/exclusion record.

## 10. Conditional methods, not adopted evidence

Efron (1979), Golub and Van Loan (1980), and Phipson and Smyth (2010) are potential foundations for resampling, fitting and simulation-based testing. Their presence in the library does not establish that those procedures suit a tiny dependent selected-feature sample. Reimer et al. (2020) supplies a calibration framework, not missing site association. Precession/corrigendum, stellar catalogue, ephemeris, terrain and visibility sources become operative only after the relevant branch is justified. The [literature-dependency guide](LITERATURE_DEPENDENCIES.md) names each and its access/implementation limits.

## 11. What comes from our analysis, not from the cited literature

The source-specific numerical reproductions, restricted-combination tests, point/identity compatibility screens, contextual date-overlap calculations and continuous rounding-domain ordering are project-derived results. Cite their versioned code/tables **alongside** the input literature, not as statements made by the original authors. All remain subject to current premises, W1–W4 review and the documented hosted reproducibility failure.

In particular, the northern A3 < A2 < A1 enclosure is conditional on historical table membership, a spherical model and the specified rounding domains with a shared origin. It does not establish original stone placement or astronomical intention. The [claim register](../evidence/analysis/case-study-2026-10-24/CLAIMS.md), [pipeline contract](../../data/pipeline.json) and [hosted failure evidence](../validation/hosted-2026-11-24/README.md) preserve the exact scope and execution limits.

The unavailable Sahara article limits first-hand discovery-history claims; no additional unrounded survey records or contact are available from the owner. These are explicit bounds on the case study, not invitations to manufacture observations. Nothing in this digest establishes a unique target, construction chronology, probability of intentionality or validated general framework.
