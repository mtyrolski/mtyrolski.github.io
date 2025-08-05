---
title: "What Matters in Hierarchical Search for Combinatorial Problems?"
collection: publications
category: manuscripts
permalink: /publication/2024-01-01-what-matters-hierarchical-search
excerpt: "Comprehensive analysis of key properties influencing hierarchical search in combinatorial reasoning, with guidelines for robust comparisons and future algorithm design."
date: 2024-06-01
venue: "ICLR 2024 (Generative Models for Decision Making)"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2406.03361"
codeurl: "https://github.com/mtyrolski/CaRL"
citation: "Zawalski, M., Góral, G., Tyrolski, M., Wiśnios, E., Budrowski, F., Cygan, M., Kuciński, Ł. and Miłoś, P., 2024. What Matters in Hierarchical Search for Combinatorial Reasoning Problems?. arXiv preprint arXiv:2406.03361."
image: "/images/publications/what_matters.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="What Matters in Hierarchical Search" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

Combinatorial problems, particularly the notorious NP-hard tasks, remain a significant challenge for AI research. A common approach to addressing them combines search with heuristics learned from demonstrations. Recently, hierarchical planning has emerged as a powerful framework in this context, enabling agents to decompose complex problems into manageable subgoals. However, the foundations of this approach, particularly the behavior and limitations of learned heuristics, remain underexplored.

We identify key characteristics whose presence favors the choice of hierarchical search methods: hard-to-learn value functions, complex action spaces, presence of dead ends in the environment, or training data collected from diverse sources. Through in-depth empirical analysis, we establish that hierarchical search methods consistently outperform standard search methods across these dimensions, and we formulate insights for future research. On the practical side, we also propose a set of evaluation guidelines to enable meaningful comparisons between methods and reassess the state-of-the-art algorithms.

**Links:**
- [Paper (PDF)]({{ page.paperurl }})
- [Code (CaRL Library)]({{ page.codeurl }})
