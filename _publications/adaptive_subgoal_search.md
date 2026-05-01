---
title: "Adjusting Planning Horizon with Adaptive Subgoal Search"
collection: publications
category: manuscripts
permalink: /publication/2023-01-01-adjusting-planning-horizon
excerpt: "AdaSubS adjusts planning horizon using generated subgoals and reachability filtering; evaluated on Sokoban, Rubik's Cube, and INT."
date: 2023-06-01
venue: "ICLR 2023 (Top-5%, Oral)"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2206.00702"
websiteurl: "https://sites.google.com/view/adaptivesubgoalsearch/"
colaburl: "https://colab.research.google.com/drive/1qdHaTSegZRHMy6nRHXXFjY0DjKSTZQ0x?usp=sharing"
codeurl: "https://github.com/AdaptiveSubgoalSearch/adaptive_subs"
citation: "Zawalski, M., Tyrolski, M., Czechowski, K., Odrzygóźdź, T., Stachura, D., Piękos, P., Wu, Y., Kuciński, Ł., & Miłoś, P. (2022). Fast and precise: Adjusting planning horizon with adaptive subgoal search. arXiv preprint arXiv:2206.00702."
image: "/images/publications/adasubs.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="Adjusting Planning Horizon with Adaptive Subgoal Search" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

Adaptive Subgoal Search (AdaSubS) adjusts the planning horizon by generating candidate subgoals at multiple distances and filtering unreachable states. The method targets complex reasoning tasks where states vary in planning difficulty.

AdaSubS is evaluated on Sokoban, the Rubik's Cube, and INT.

**Links:**
- [Paper (PDF)]({{ page.paperurl }})
- [Project Website]({{ page.websiteurl }})
- [Google Colab Demo]({{ page.colaburl }})
- [Code Repository]({{ page.codeurl }})
