---
title: "Hierarchical Transformers Are More Efficient Language Models"
collection: publications
category: manuscripts
permalink: /publication/2022-01-01-hierarchical-transformers
excerpt: "Hourglass: a hierarchical Transformer with down/upsampling layers that improves long-sequence modeling efficiency; SOTA on ImageNet32 and strong enwik8 performance."
date: 2022-07-01
venue: "NAACL 2022"
slidesurl: ""
paperurl: "https://arxiv.org/abs/2110.13711"
citation: "Nawrot, P., Tworkowski, S., Tyrolski, M., Kaiser, Ł., Wu, Y., Szegedy, C., & Michalewski, H. (2021). Hierarchical transformers are more efficient language models. arXiv preprint arXiv:2110.13711."
image: "/images/publications/hierarchical_transformers.png"
---

{% if page.image %}
<img src="{{ page.image }}" alt="Hierarchical Transformers Are More Efficient Language Models" style="max-width: 420px; border-radius: 8px; margin-bottom: 1em;" />
{% endif %}

Transformer models yield impressive results on many NLP and sequence modeling tasks. Remarkably, Transformers can handle long sequences which allows them to produce long coherent outputs: full paragraphs produced by GPT-3 or well-structured images produced by DALL-E. These large language models are impressive but also very inefficient and costly, which limits their applications and accessibility.

We postulate that having an explicit hierarchical architecture is the key to Transformers that efficiently handle long sequences. To verify this claim, we first study different ways to downsample and upsample activations in Transformers so as to make them hierarchical. We use the best performing upsampling and downsampling layers to create **Hourglass** - a hierarchical Transformer language model. Hourglass improves upon the Transformer baseline given the same amount of computation and can yield the same results as Transformers more efficiently. In particular, Hourglass sets new state-of-the-art for Transformer models on the ImageNet32 generation task and improves language modeling efficiency on the widely studied enwik8 benchmark.

**Links:**
- [Paper (PDF)]({{ page.paperurl }})
