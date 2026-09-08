---
title: "Hierarchical Transformers Are More Efficient Language Models"
collection: publications
permalink: /publication/2022-01-01-hierarchical-transformers
date: 2022-07-01
year: 2022
selected: true
selected_order: 3
homepage_group: publications
publication_order: 3
authors: "P. Nawrot*, S. Tworkowski*, M. Tyrolski, Ł. Kaiser, Y. Wu, C. Szegedy, H. Michalewski"
venue: "Findings of NAACL 2022"
excerpt: "Hourglass introduces explicit downsampling and upsampling into a Transformer, studying hierarchical abstraction as a route to more efficient long-sequence modelling."
paperurl: "https://aclanthology.org/2022.findings-naacl.117/"
paperlabel: "ACL Anthology"
citation: "Nawrot, P., Tworkowski, S., Tyrolski, M., Kaiser, Ł., Wu, Y., Szegedy, C., & Michalewski, H. (2022). Hierarchical Transformers Are More Efficient Language Models. Findings of the Association for Computational Linguistics: NAACL 2022, 1559–1571. https://doi.org/10.18653/v1/2022.findings-naacl.117"
image: "/images/publications/hierarchical_transformers.png"
---

{% include publication-figure.html alt="Hourglass hierarchical Transformer architecture" %}

Hourglass is a hierarchical Transformer that shortens and expands intermediate representations using explicit downsampling and upsampling layers. It studies how hierarchy can reduce computation while retaining long-range sequence modelling capacity.

The model improves efficiency over standard Transformer baselines on ImageNet32 generation and the enwik8 language-modelling benchmark.
