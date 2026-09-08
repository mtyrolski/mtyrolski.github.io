---
title: "What Matters in Hierarchical Search for Combinatorial Reasoning Problems?"
collection: publications
permalink: /publication/2024-01-01-what-matters-hierarchical-search
date: 2024-06-05
year: 2024
selected: true
selected_order: 2
homepage_group: publications
publication_order: 2
authors: "M. Zawalski, G. Góral, M. Tyrolski, E. Wiśnios, F. Budrowski, M. Cygan, Ł. Kuciński, P. Miłoś"
venue: "ICLR 2024 · Generative Models for Decision Making Workshop"
excerpt: "A controlled study of when hierarchical search helps: difficult value functions, complex action spaces, dead ends, heterogeneous demonstrations, and distribution shift."
paperurl: "https://arxiv.org/abs/2406.03361"
codeurl: "https://github.com/mtyrolski/CaRL"
citation: "Zawalski, M., Góral, G., Tyrolski, M., Wiśnios, E., Budrowski, F., Cygan, M., Kuciński, Ł., & Miłoś, P. (2024). What Matters in Hierarchical Search for Combinatorial Reasoning Problems? Generative Models for Decision Making Workshop at ICLR 2024."
image: "/images/publications/what-matters.png"
---

{% include publication-figure.html alt="Hierarchical and low-level search comparison" %}

This work asks when hierarchical search is preferable to planning directly with atomic actions. Controlled experiments isolate several relevant conditions: inaccurate value functions, complex action spaces, dead ends, heterogeneous training data, and out-of-distribution tasks.

The paper also proposes a consistent methodology for comparing hierarchical and low-level planners. The accompanying CaRL framework supports these reproducible comparisons.
