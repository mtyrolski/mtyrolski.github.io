---
title: "Resolution of Recursive Data Corruption to Transform T-cell Epitope Discovery"
collection: publications
permalink: /publication/2026-04-01-resolution-recursive-data-corruption
date: 2026-04-01
year: 2026
selected: true
selected_order: 1
homepage_group: preprints
publication_order: 5
authors: "G. Preibisch*, M. Tyrolski*, P. Kucharski, S. Giziński, P. Grzegorczyk, S. Moon, S. Kim, B. Zaro, A. Gambin"
venue: "bioRxiv preprint, 2026 · revised manuscript under review"
excerpt: "Predictor-dependent curation can preserve strong standard metrics while eroding genuine candidate-discovery performance; deepMHCflare reframes the problem as protein-centric learning-to-rank."
paperurl: "https://doi.org/10.64898/2026.03.30.710191"
paperlabel: "Paper"
citation: "Preibisch, G., Tyrolski, M., Kucharski, P., Giziński, S., Grzegorczyk, P., Moon, S., Kim, S., Zaro, B., & Gambin, A. (2026). Resolution of Recursive Data Corruption to Transform T-cell Epitope Discovery. bioRxiv 2026.03.30.710191. https://doi.org/10.64898/2026.03.30.710191"
image: "/images/publications/recursive_corruption.png"
---

{% include publication-figure.html alt="Recursive data corruption and deepMHCflare overview" %}

This preprint studies a feedback loop in immunopeptidomics: predictor-dependent labels and filtering can bias the data used to train and evaluate later models. Standard discrimination metrics can remain deceptively strong even as candidate-discovery performance deteriorates on predictor-independent data.

The work reframes epitope discovery as a protein-centric learning-to-rank problem and evaluates deepMHCflare using predictor-independent data. In prospective validation, deepMHCflare ranked peptide candidates from an existing scFv immunogen; it did not design the vaccine. Two of four nominated peptides elicited significant CD8+ TNF-α+ responses. A third candidate has independent support in previous literature but was not significant in this assay.

The revised manuscript is under review. It is not an accepted journal publication.
