---
title: "Hierarchical Transformers Are More Efficient Language Models"
collection: publications
category: manuscripts
permalink: /publication/2022-01-01-hierarchical-transformers
excerpt: "Hourglass adds downsampling and upsampling to Transformers for more efficient long-sequence modeling; evaluated on ImageNet32 and enwik8."
date: 2022-07-01
venue: "NAACL 2022"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2110.13711"
citation: "Nawrot, P., Tworkowski, S., Tyrolski, M., Kaiser, Ł., Wu, Y., Szegedy, C., & Michalewski, H. (2022). Hierarchical transformers are more efficient language models. Findings of the Association for Computational Linguistics: NAACL 2022, 1559-1571."
image: "/images/publications/hierarchical_transformers.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="Hierarchical Transformers Are More Efficient Language Models" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

Hourglass is a hierarchical Transformer with downsampling and upsampling layers. It studies how explicit hierarchy can reduce computation in long-sequence modeling.

The model is evaluated on ImageNet32 and enwik8, where it improves efficiency relative to standard Transformer baselines.

**Links:**
- [Paper (PDF)]({{ page.paperurl }})
