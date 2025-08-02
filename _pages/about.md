---
permalink: /
title: "Michał Tyrolski - AI Researcher"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am **Michał Tyrolski**, a *Senior AI Consultant* at **Ernst & Young**. I hold an **M.Sc. in Machine Learning** (2023) and a **B.Sc. in Computer Science** (2021) from the **University of Warsaw**, where I was supervised by prof. Marek Cygan and prof. Piotr Miłoś.

My research focuses on **Multi-Agent Systems**, **Meta-RL**, **AI-based Planning**, and **decision-making in complex environments**. My expertise includes offline and online reinforcement learning, planning, efficient transformers, and LLMs. I have contributed to AI projects at **Microsoft**, **Nvidia**, **Deepflare**, and **Samsung**.

I am an active member of the AI community, particularly with **ML in PL**, where I have been an organizer since 2020. In my free time, I enjoy mountain hiking and motorization.

You can view my [full CV here](../files/cv.pdf).

---

## Selected Publications

<div style="display: flex; flex-direction: column; gap: 1.5rem;">
{% for publication in site.publications %}
  <div style="display: flex; align-items: center; border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; background: #fafbfc; min-height: 120px;">
    <div style="flex: 1;">
      <strong>{{ publication.title }}</strong><br>
      <em>{{ publication.venue }}, {{ publication.pub_date | date: '%Y' }}</em><br>
      {% if publication.paperurl %}<a href="{{ publication.paperurl }}">Paper</a>{% endif %}
      {% if publication.excerpt %}<br>{{ publication.excerpt }}{% endif %}
    </div>
    <div style="width: 100px; height: 100px; margin-left: 1.5rem; background: #eaeaea; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: #aaa; font-size: 0.9em;">
      <span>Image<br>Placeholder</span>
    </div>
  </div>
{% endfor %}
</div>

---

## Selected Projects

<div style="display: flex; flex-direction: column; gap: 1.5rem;">
  <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; background: #fafbfc;">
    <strong>Multi-Agent RL for Smart Grids</strong><br>
    <em>EY, 2024</em><br>
    Developed a scalable reinforcement learning system for optimizing energy distribution in smart grids, reducing costs and improving reliability.
  </div>
  <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; background: #fafbfc;">
    <strong>Efficient Transformer Architectures</strong><br>
    <em>University of Warsaw, 2023</em><br>
    Researched and implemented efficient transformer models for NLP tasks, achieving state-of-the-art results with reduced computational resources.
  </div>
  <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 1rem; background: #fafbfc;">
    <strong>AI-based Medical Diagnostics</strong><br>
    <em>Deepflare, 2022</em><br>
    Built deep learning pipelines for medical image analysis, supporting early disease detection and clinical decision-making.
  </div>
</div>

---

