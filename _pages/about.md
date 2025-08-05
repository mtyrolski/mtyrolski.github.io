---
permalink: /
title: ""
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<!-- Custom Top Bar with Profile -->
<div style="display: flex; align-items: center; background-color: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 25px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); max-width: 1200px; margin-left: auto; margin-right: auto;">
  <div style="width: 100px; height: 100px; border-radius: 50%; overflow: hidden; margin-right: 20px; flex-shrink: 0;">
    <img src="../images/IMG_8383.JPEG" alt="Michał Tyrolski" style="width: 100%; height: 100%; object-fit: cover;">
  </div>
  <div>
    <h1 style="margin: 0; font-size: 1.7em;">Michał Tyrolski</h1>
    <p style="margin: 5px 0 0;">Senior AI Consultant at Ernst & Young / Independent Researcher</p>
    <div style="margin-top: 8px;">
      <a href="https://github.com/mtyrolski" style="margin-right: 10px;"><i class="fab fa-github"></i> GitHub</a>
      <a href="https://twitter.com/mtyrolski" style="margin-right: 10px;"><i class="fab fa-twitter"></i> Twitter</a>
      <a href="https://www.linkedin.com/in/michal-tyrolski/" style="margin-right: 10px;"><i class="fab fa-linkedin"></i> LinkedIn</a>
      <a href="../files/cv.pdf"><i class="fas fa-file-pdf"></i> CV</a>
    </div>
  </div>
</div>


I am **Michał Tyrolski**, a *Senior AI Consultant* at **Ernst & Young**. I hold an **M.Sc. in Machine Learning** (2023) and a **B.Sc. in Computer Science** (2021) from the **University of Warsaw**, where I was supervised by prof. Marek Cygan and prof. Piotr Miłoś.

My main research interests include **AI-based Planning**, **decision-making in complex environments**, **Meta-Reinforcement Learning**, and **Continual Learning**. Over the years, I’ve gained experience in both offline and online reinforcement learning, planning, efficient transformer architectures, and LLMs. I’ve also had the opportunity to be involved in AI projects at **Microsoft**, **Nvidia**, **Deepflare**, and **Samsung**.

I am an active member of the AI community, particularly with **ML in PL**, where I have been an organizer since 2020. In my free time, I enjoy mountain hiking and motorization.

You can view my [full CV here](../files/cv.pdf).


## Selected Publications

<style>
.publication-box {
  display: flex;
  align-items: center;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  background: #fafbfc;
  min-height: 150px;
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

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1200px; margin: 0 auto;">
{% for publication in site.publications %}
  <div class="publication-box">
    <div style="flex: 1; max-width: calc(100% - 170px);">
      <strong>{{ publication.title }}</strong><br>
      <em>{{ publication.venue }}</em><br>
      {% if publication.paperurl %}
        <a href="{{ publication.paperurl }}" class="paper-link">Paper</a>
      {% endif %}
      {% if publication.codeurl %}
        <a href="{{ publication.codeurl }}" class="paper-link">Code</a>
      {% endif %}
      {% if publication.websiteurl %}
        <a href="{{ publication.websiteurl }}" class="paper-link">Website</a>
      {% endif %}
      {% if publication.colaburl %}
        <a href="{{ publication.colaburl }}" class="paper-link">Colab</a>
      {% endif %}
      {% if publication.excerpt %}<br>{{ publication.excerpt }}{% endif %}
    </div>
    <div style="width: 150px; height: 150px; margin-left: 1.5rem; background: #eaeaea; border-radius: 6px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
      {% if publication.image %}
        <img src="{{ publication.image }}" alt="{{ publication.title }}" style="max-width: 100%; max-height: 100%; object-fit: cover; border-radius: 6px;" />
      {% else %}
        <span style="color: #aaa; font-size: 0.9em;">Image<br>Placeholder</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>


## Other Papers

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1200px; margin: 0 auto;">
{% for paper in site.other_papers %}
  <div class="publication-box">
    <div style="flex: 1; max-width: calc(100% - 170px);">
      <strong>{{ paper.title }}</strong><br>
      <em>{{ paper.venue }}</em><br>
      {% if paper.paperurl %}
        <a href="{{ paper.paperurl }}" class="paper-link">Paper</a>
      {% endif %}
      {% if paper.excerpt %}<br>{{ paper.excerpt }}{% endif %}
    </div>
    <div style="width: 150px; height: 150px; margin-left: 1.5rem; background: #eaeaea; border-radius: 6px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
      {% if paper.image %}
        <img src="{{ paper.image }}" alt="{{ paper.title }}" style="max-width: 100%; max-height: 100%; object-fit: cover; border-radius: 6px;" />
      {% else %}
        <span style="color: #aaa; font-size: 0.9em;">Image<br>Placeholder</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>


## Selected Projects

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1200px; margin: 0 auto;">
  <div style="border: 1px solid #1976d2; border-radius: 8px; padding: 1.5rem; background: #f5faff; box-shadow: 0 2px 8px rgba(25, 118, 210, 0.06);">
    <strong style="font-size: 1.2em; color: #1976d2;">CaRL Library: Combinatorial RL for planning</strong><br>
    <em>Lead author & maintainer</em><br>
    <div style="width: 100%; max-width: 420px; height: 180px; margin: 1.2em auto 0.7em auto; background: #e3eaf6; border-radius: 7px; display: flex; align-items: center; justify-content: center;">
      <img src="../images/planning.png" alt="CaRL Architecture" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 7px;" />
    </div>
    <p style="margin-top: 0.7em;">
      <b>CaRL</b> is an open-source library for scalable offline and online reinforcement/imitation learning in combinatorial planning problems.<br>
      <ul style="margin: 0.5em 0 0.5em 1.2em;">
        <li>Supports environments like <b>Sokoban</b>, <b>NPuzzle</b>, <b>Rubik</b>, and <b>INT</b>.</li>
        <li>Includes 35+ open-source models (Generator, Value, Policy, CLLP).</li>
        <li>Enables distributed experiments on SLURM clusters and local machines.</li>
        <li>Interactive Jupyter notebooks for research and reproducibility.</li>
        <li>Used in multiple peer-reviewed papers.</li>
      </ul>
      <b>Key features:</b> modular architecture, Hydra config extension, heterogeneous job support, remote deployment, and dataset demos.
    </p>
    <div style="margin-top: 0.7em;">
      <a href="https://github.com/mtyrolski/carl" style="display: inline-block; background: #1976d2; color: #fff; padding: 0.4em 1.2em; border-radius: 5px; text-decoration: none; font-weight: 600; margin-right: 0.7em; transition: background 0.2s;">GitHub Repo</a>
      <a href="https://arxiv.org/abs/2406.03361" style="display: inline-block; background: #c62828; color: #fff; padding: 0.4em 1.2em; border-radius: 5px; text-decoration: none; font-weight: 600; transition: background 0.2s;">Latest Paper</a>
    </div>
  </div>
</div>


