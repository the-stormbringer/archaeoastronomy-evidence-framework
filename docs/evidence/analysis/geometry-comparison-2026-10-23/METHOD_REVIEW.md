> Historical evidence record. Dates and acquisition statements below describe the original review; use [current project state](../../../PROJECT_STATE.json) for current status.

# Reduction-method and celestial-coordinate review — 23 October 2026

## Published reduction

Brophy and Rosen 2005 p.17 defines the recalculated WM2001 directions as simple averages of individual stone azimuths from Complex A. Our six-value reproduction validates that specific column. Pages 18–20 distinguish absolute satellite geolocation from within-image relative positions, report an approximately 12 m east–west offset, and attribute the final directions to ground GPS plus corrected satellite positions. The checked passages do not provide an explicit weighting/reduction algorithm sufficient to reproduce the final column from rounded coordinates alone.

`combination_family_check.csv` tests one narrowly defined family: any nonnegative weighted average of the two row means reconstructed from printed QB2002/GPS2003 coordinates. A3, A2, A1 and B1 have complete rows in both datasets; their published final means lie outside the attainable range under both spherical and assumed-WGS84 calculations. Distances beyond the nearest endpoint are 0.18–0.32° for the sphere and 0.31–0.45° for WGS84. Therefore that family does not reproduce the final column. This does not refute a calculation with unrounded positions, different point weights, an alternative origin, or additional reduction steps. B2 and C contain missing GPS coordinates and cannot serve as equivalent full-row tests.

A common Cartesian translation of all points, including the origin, leaves relative vectors unchanged. Consequently, adding the reported image offset is not by itself a substantive explanation for different radial bearings. Applying corrections to only selected points would require documentary justification.

Malville et al. 2007 p.5 describes combining two GPS datasets and satellite results, plus refraction/extinction and a level physical horizon. The stated ±0.6° encompasses fragmentation and irregularity; it is not specified as a Gaussian standard deviation. Reconstructing their exact combined reduction remains open. We must not equate a conveniently close reconstructed number with a verified method.

## What direction is being estimated?

The historical numerical reproduction uses the arithmetic mean of stone-to-origin bearings. A circular mean is a useful wrap-safe alternative but is a change of estimator, not an automatic correction to the original. Fitting a free line through the stones addresses their longitudinal axis; it does not estimate the same radial sightline. A line constrained to pass through Complex A introduces different distance weighting and must be justified separately. Preserve these distinctions before considering model comparison.

## Bounded celestial transformation

`method_gate.py` implements sin(delta)=sin(latitude)sin(altitude)+cos(latitude)cos(altitude)cos(azimuth), the geometrical transformation in Silva 2020 equation 1. Cardinal identity checks pass. `declination_scenarios.csv` contains 72 transformations of the prior rounding envelopes at geometric altitudes 0°, 1° and 2° using source-specific latitudes. Altitudes are hypothetical scenarios, not reconstructed prehistoric horizons. Neither refraction nor extinction is modelled. A geometric altitude is not interchangeable with an observed physical horizon or first-visibility threshold.

The transform carries documentary resolution into celestial-coordinate resolution. It cannot identify a star, recover a construction date, demonstrate first visibility, or measure intention. Target-date fitting is deferred until the available archaeological and methodological evidence is reconciled. Source lookup found a potentially decisive 2025 monograph; its numerical content must be checked before representing older-record gaps as current gaps.

## New source review priorities

- *The Megaliths of Nabta Playa* (2025), ISBN 978-83-68122-15-2, edited by Romuald Schild with Agnieszka Czekaj-Zastawny and Halina Królik. Publisher contents list measurements/maps, alignments, quarries, radiocarbon summary and a stone catalogue. Institutional repository identifies open access and CC BY 4.0. Full-text acquisition is currently being attempted, not completed.
  - https://ksiegarnia.iaepan.edu.pl/pl/p/The-Megaliths-of-Nabta-Playa/829
  - https://rcin.org.pl/dlibra/publication/284542/edition/247676?language=en
  - https://polona.pl/preview/bb144248-9617-45fa-87a5-8777f3e2a2a1
- Haynie 2014, *Nabta Playa in the Development of Science and Technology*, Technology & Innovation 16:63–73, DOI 10.3727/194982414X13971392823433. Candidate comparator; full text not obtained. Haynie's accessible 2015 paper cites it as an earlier unified-design interpretation; do not infer its full methods from that citation.
- Haynie 2015, *A Great Comet and Ceremonial Site Development at Nabta Playa*, MAA15(1):127–134. Publisher PDF available; broader interpretation is a hypothesis, not archaeological confirmation. https://www.maajournal.com/index.php/maa/article/download/185/139/262
- Beyene 2025, DOI 10.33552/OAJAA.2025.06.000628, publisher text inspected at screening level. Calendar-circle interpretation, outside the present radial core. Inclusion is not endorsement of the claimed cultural or astronomical connections.

This was a focused update, not a systematic novelty review. Broad claims that coordinate reassessment or probabilistic archaeoastronomy are new remain excluded. Search-result upload dates for older journal archives must not replace the issue's publication year.
