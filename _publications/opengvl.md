---
title: "OpenGVL: Benchmarking Visual Temporal Progress for Data Curation"
collection: publications
category: manuscripts
permalink: /publication/2025-09-30-opengvl
excerpt: "Benchmark, toolkit, and live leaderboard for evaluating VLM temporal progress estimation in robotics videos; supports automated dataset curation."
date: 2025-09-30
venue: "CoRL 2025 workshop"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2509.17321"
paperlabel: "arXiv"
websiteurl: "https://huggingface.co/spaces/OpenGVL/OpenGVL"
websitelabel: "Live Benchmark"
colaburl: ""
codeurl: "https://github.com/budzianowski/opengvl"
codelabel: "GitHub Repo"
citation: "Budzianowski, P., Wiśnios, E., Tyrolski, M., Góral, G., Kulakov, I., Petrenko, V., & Walas, K. (2025). OpenGVL--Benchmarking Visual Temporal Progress for Data Curation. arXiv preprint arXiv:2509.17321."
image: "/images/publications/opengvl.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="OpenGVL" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

OpenGVL evaluates how vision-language models estimate temporal progress in robotics videos. It supports automated dataset curation by predicting task completion from video frames.

The benchmark uses Value-Order Correlation (VOC), a rank correlation between predicted progress and true time order. It includes shared prompts, data loaders, configs, and hidden tasks for contamination control.

Links:
- [Paper (arXiv)]({{ page.paperurl }})
- [Live Benchmark (HF Spaces)]({{ page.websiteurl }})
- [Code Repository]({{ page.codeurl }})
