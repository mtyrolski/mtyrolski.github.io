---
title: "Adjusting Planning Horizon with Adaptive Subgoal Search"
collection: publications
category: manuscripts
permalink: /publication/2023-01-01-adjusting-planning-horizon
excerpt: "AdaSubS adaptively adjusts the planning horizon by generating diverse subgoals and swiftly filtering unreachable ones, combining efficiency and fine-grained control on tasks like Sokoban, Rubik's Cube, and INT."
date: 2023-06-01
venue: "ICLR 2023 (Top-5%, Oral)"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2206.00702"
websiteurl: "https://sites.google.com/view/adaptivesubgoalsearch/"
colaburl: "https://colab.research.google.com/drive/1qdHaTSegZRHMy6nRHXXFjY0DjKSTZQ0x?usp=sharing"
codeurl: "https://github.com/AdaptiveSubgoalSearch/adaptive_subs"
citation: "Zawalski, M., Tyrolski, M., Czechowski, K., Odrzygóźdź, T., Stachura, D., Piękos, P., Wu, Y., Kuciński, Ł. and Miłoś, P., 2022. Fast and precise: Adjusting planning horizon with adaptive subgoal search. arXiv preprint arXiv:2206.00702."
image: "/images/publications/adasubs.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="Adjusting Planning Horizon with Adaptive Subgoal Search" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

Complex reasoning problems contain states that vary in the computational cost required to determine a good action plan. Taking advantage of this property, we propose Adaptive Subgoal Search (AdaSubS), a search method that adaptively adjusts the planning horizon. To this end, AdaSubS generates diverse sets of subgoals at different distances. A verification mechanism is employed to filter out unreachable subgoals swiftly, allowing to focus on feasible further subgoals. In this way, AdaSubS benefits from the efficiency of planning with longer subgoals and the fine control with the shorter ones, and thus scales well to difficult planning problems.

We show that AdaSubS significantly surpasses hierarchical planning algorithms on three complex reasoning tasks: Sokoban, the Rubik's Cube, and inequality proving benchmark INT.

**Links:**
- [Paper (PDF)]({{ page.paperurl }})
- [Project Website]({{ page.websiteurl }})
- [Google Colab Demo]({{ page.colaburl }})
- [Code Repository]({{ page.codeurl }})
