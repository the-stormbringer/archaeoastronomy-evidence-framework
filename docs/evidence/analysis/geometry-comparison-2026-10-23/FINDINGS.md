> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../../../PROJECT_STATE.json) for current status.

# Geometry sensitivity milestone — 23 October 2026

## What was calculated

Four published coordinate versions, six groups and two Earth models were compared (48 records). The follow-up includes 12 sourcebook membership scenarios, 24 rounding scenarios and 96 origin-radius scenarios. Missing GPS coordinates remain missing. The source versions describe related evidence and are not independent samples.

## Main results

The sourcebook narrative membership for A2 gives 29.8051°, versus 28.7355° using its table membership: a difference of 1.0696°. This is a documentary-definition sensitivity, not measurement noise. The narrative A1 and C scenarios lack A-10 and C-6 coordinates in the original table; their partial means cannot stand in for complete rows.

| Group | Sampled rounding envelope width across complete table versions | Largest shift with a hypothetical 10 m origin displacement |
|---|---:|---:|
| A3 | 1.69–1.71° | 0.60° |
| A2 | 1.89–1.93° | 0.67° |
| A1 | 2.64–2.66° | 0.92° |
| B2 | 3.24–3.28° | 1.13° |
| B1 | 4.56–4.64° | 1.57° |
| C1 | 1.79–1.86° | 0.61° |

Rounding scenarios assume nearest rounding at the printed 0.0001° resolution. Each coordinate ranges over ±0.00005° in a finite grid. A single shared origin is used for all stones in each scenario; individual stone offsets can vary. This is an intentionally permissive coordinate-resolution diagnostic. It does not establish that all combinations are archaeologically possible, likely or compatible with original survey constraints.

Origin displacements use 1, 5, 10 and 25 m radii at 5° directional increments. These radii are hypothetical parameters, not inferred positional errors. Results for incomplete groups are retained in the data but excluded from the table above. C label identity remains unresolved even for complete printed tables.

## Validation

- All six BR2005 recalculated-WM means reproduced within the published 0.01° rounding.
- An independent spherical-bearing formula agrees to less than 1e-7°.
- Cardinal and oblique geodesic checks and a circular-wrap check passed.
- Refining each rounding-coordinate grid from three to five positions did not change sampled envelope endpoints. This is a convergence check, not a proof of global extrema.

## Scientific interpretation

Published coordinate precision alone can permit materially different reconstructed mean directions under the stated assumptions. Therefore close agreement with a proposed celestial direction must not be advertised as robust without specifying membership, origin and reduction method. The calculation does not show that the original survey was inaccurate: underlying unrounded measurements may have supported finer precision. It shows the limitations of reconstructing the result from the published numerical record.

The source spreads, membership changes, rounding envelopes and origin experiments are different diagnostics. They must not be added in quadrature or pooled as if independent error terms. No Gaussian standard deviation, confidence interval, probability of intentionality or construction date has been estimated.

## Next research gate

Before celestial-target tests: distinguish radial means from other defensible estimands, examine the BR2005 final combination method, and document a limited set of historical target claims with horizon/visibility/chronology assumptions. A bounded declination transformation can then show which geometric alternatives remain distinguishable. Independent construction dates are not available for individual rows; dates inferred by fitting stars cannot validate the same target fits.

No user input is needed for the next methods pass. Missing survey records may ultimately prevent unique reconstruction; the paper can report that limitation if it demonstrates a substantive consequence beyond earlier critiques. Novelty and publication readiness remain unestablished.


## Subsequent result: relative ordering

The shared-origin calculation now available in shared_origin_contrasts.csv avoids interpreting marginal overlap as loss of ordering. All complete northern table scenarios retain A3 < A2 < A1 across the sampled rounding grid. This does not transfer to untested identity/physical-position alternatives. See EVIDENCE_GATE.md for the updated scientific interpretation and 2025-source implications.
