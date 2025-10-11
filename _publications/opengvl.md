---
title: "OpenGVL: Benchmarking Visual Temporal Progress for Data Curation"
collection: publications
category: manuscripts
permalink: /publication/2025-09-30-opengvl
excerpt: "Benchmark and toolkit for evaluating VLMs' sense of progress in robotics via Value-Order Correlation (VOC); enables automated dataset curation from videos."
date: 2025-09-30
venue: "CoRL 2025 workshop"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2509.17321"
websiteurl: "https://huggingface.co/spaces/OpenGVL/OpenGVL"
colaburl: ""
codeurl: "https://github.com/budzianowski/opengvl"
citation: "Budzianowski, P., Wiśnios, E., Góral, G., Tyrolski, M., Kulakov, I., Petrenko, V., & Walas, K. (2025). OpenGVL - Benchmarking Visual Temporal Progress for Data Curation. arXiv:2509.17321."
image: "/images/publications/opengvl.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="OpenGVL" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

OpenGVL provides a benchmark and toolkit to evaluate how well vision–language models (VLMs) understand temporal progress in robotic tasks. It enables automatic annotation and curation of large-scale robotics datasets by predicting task completion from video frames, making it practical for data quality assessment and filtering.

We introduce Value-Order Correlation (VOC) — Spearman rank correlation between the model’s predicted progress ordering and the video’s true time order — to measure temporal understanding (higher is better; +1 perfect, 0 random, −1 reversed). The framework supports few-shot prompting with context episodes and includes contamination control via hidden tasks curated for evaluation.

Links:
- [Paper (arXiv)]({{ page.paperurl }})
- [Live Benchmark (HF Spaces)]({{ page.websiteurl }})
- [Code Repository]({{ page.codeurl }})
