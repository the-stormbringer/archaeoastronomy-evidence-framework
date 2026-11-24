# Citation and referencing convention

Use **Chicago Manual of Style, 18th edition, author–date** for current research writing. This fits the scientific draft's author/year citations. Do not mix it with numbered notes-and-bibliography. Historical evidence notes retain their original citation strings; stable catalogue identifiers link them to the current reference list.

- Text: `(Brophy and Rosen 2005, 17–20)`; narrative: `Malville et al. (2007, 5)`; chapter: `(Wendorf and Malville 2001, 498, table 16.1)`.
- For more than two authors, use the first surname plus `et al.` in text. In references list up to six authors; for more than six, list the first three followed by `et al.`. Preserve source-author order; invert only the first personal name.
- Alphabetize the reference list by author, then order an author's works chronologically. Repeat names rather than replacing them with a dash. Use letter suffixes only when author/year collisions require them.
- Give article/chapter titles in quotation marks, journal/book titles in italics, volume/issue, pages or article number, and DOI as an HTTPS link. Cite chapter authors for chapter-specific evidence; do not substitute the volume editor for them.
- Use **printed pages** in citations. Store PDF page index and local file SHA-256 separately in the evidence record. Example: printed p.85 corresponds to PDF p.87 in the held 2025 monograph. Do not treat those page numbers as interchangeable.
- A quotation or close factual attribution needs a pinpoint locator and read-depth record. A bibliography entry or downloaded PDF does not establish that it was read. Do not make the reference list appear to support an unread claim.
- Cite original publications for observations and our versioned ledger/code for transformations. Distinguish the printed source's claim from our conditional calculation. Catalogue IDs such as `BR2005_GPS2003` are dataset identifiers, not formatted literature citations.
- For inaccessible literature, identify the consulted secondary source: for example, “Wendorf et al. (1992–1993), discussed in Malville et al. (2008, 131).” Do not imply first-hand reading or invent a quotation/page within the unavailable article.
- Use issue years consistently: Silva's skyscapeR notice is 2021 (online 2022); Zotti et al. is 2020 (online 2021). Acquisition IDs remain stable. See reference-specific metadata notes rather than silently changing historical records.

The canonical human-readable list is [BIBLIOGRAPHY_CHICAGO.md](BIBLIOGRAPHY_CHICAGO.md); [REFERENCES.json](REFERENCES.json) supplies stable keys, text labels, formatted references and qualifications. [CATALOGUE.json](CATALOGUE.json) maps local source holdings to those keys. Supplements and duplicate editions/copies do not automatically create independent references. Cite Kuper and Kröpelin's supplement as `(Kuper and Kröpelin 2006, supporting online material, [verified locator])`; replace the bracketed instruction with a checked locator before use.

This is a working reference list, not journal acceptance. Metadata exceptions and incomplete procurement entries remain visible. The missing Sahara paper's year span is retained from the project record pending direct verification. The full bibliography includes conditional literature; the manuscript's own list includes only its cited subset.

Style authority: [Chicago's author–date quick guide](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-2.html) and [18th-edition changes](https://www.chicagomanualofstyle.org/help-tools/what-s-new.html). Metadata check date: November 24, 2026. DOI-generated formatting was treated as a draft and corrected against held publications where it conflicted; it was not accepted automatically.

The [metadata-check record](METADATA_CHECK.json) distinguishes successful DOI retrievals, rate-limited requests and primary-page checks. Formatted entries are reviewed working references, not a claim of independently verified completeness for every field.
