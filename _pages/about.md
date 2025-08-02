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

<style>
.publication-box {
  display: flex;
  align-items: center;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1rem;
  background: #fafbfc;
  min-height: 120px;
  transition: background 0.2s, box-shadow 0.2s, border-color 0.2s;
}
.publication-box:hover {
  background: #f0f6ff;
  box-shadow: 0 2px 8px rgba(30, 136, 229, 0.08);
  border-color: #90caf9;
}
.paper-link {
  display: inline-block;
  background: #c62828;
  color: #fff;
  padding: 0.4em 1em;
  border-radius: 5px;
  text-decoration: none;
  font-weight: 600;
  margin: 0.5em 0 0.2em 0;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s;
}
.paper-link:hover {
  background: #fff;
  color: #c62828;
  box-shadow: 0 0 0 2px #c62828 inset;
}
</style>

<div style="display: flex; flex-direction: column; gap: 1.5rem;">
{% for publication in site.publications %}
  <div class="publication-box">
    <div style="flex: 1;">
      <strong>{{ publication.title }}</strong><br>
      <em>{{ publication.venue }}, {{ publication.pub_date | date: '%Y' }}</em><br>
      {% if publication.paperurl %}
        <a href="{{ publication.paperurl }}" class="paper-link">Paper</a>
      {% endif %}
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

