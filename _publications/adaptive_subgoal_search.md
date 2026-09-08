---
title: "Fast and Precise: Adjusting Planning Horizon with Adaptive Subgoal Search"
collection: publications
permalink: /publication/2023-01-01-adjusting-planning-horizon
date: 2023-05-01
year: 2023
selected: true
selected_order: 1
homepage_group: publications
publication_order: 1
authors: "M. Zawalski*, K. Czechowski*, M. Tyrolski*, T. Odrzygóźdź, P. Piękos, D. Stachura, Ł. Kuciński, Y. Wu, P. Miłoś"
venue: "ICLR 2023 · Oral"
excerpt: "Adaptive Subgoal Search adjusts its planning horizon to local problem difficulty by combining subgoals at several temporal distances with reachability verification."
paperurl: "https://openreview.net/forum?id=7JsGYvjE88d"
paperlabel: "OpenReview"
websiteurl: "https://sites.google.com/view/adaptivesubgoalsearch/"
websitelabel: "Project"
colaburl: "https://colab.research.google.com/drive/1qdHaTSegZRHMy6nRHXXFjY0DjKSTZQ0x?usp=sharing"
codeurl: "https://github.com/AdaptiveSubgoalSearch/adaptive_subs"
citation: "Zawalski, M., Czechowski, K., Tyrolski, M., Odrzygóźdź, T., Piękos, P., Stachura, D., Kuciński, Ł., Wu, Y., & Miłoś, P. (2023). Fast and Precise: Adjusting Planning Horizon with Adaptive Subgoal Search. International Conference on Learning Representations."
image: "/images/publications/adasubs.png"
---

{% include publication-figure.html alt="Adaptive Subgoal Search planning diagram" %}

Adaptive Subgoal Search (AdaSubS) addresses the fact that states within one problem can require different amounts of look-ahead. It generates candidate subgoals at several distances and uses reachability verification to filter infeasible states, moving between longer and shorter planning horizons as needed.

The method was evaluated on Sokoban, the Rubik's Cube, and the INT inequality-proving benchmark. This work formed the central research contribution of my MSc and established the adaptive-planning direction that I continue to pursue.
