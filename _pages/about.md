---
permalink: /
title: ""
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<!-- Custom Top Bar with Profile -->
<style>
/* Profile card styling */
.profile-card {
  display: flex;
  flex-direction: column;
  background: linear-gradient(180deg, #f8f9fa, #ffffff);
  border: 1px solid #e6e8eb;
  border-radius: 14px;
  padding: 18px 20px;
  margin: 0 auto 28px auto;
  max-width: 1500px;
  box-shadow: 0 6px 20px rgba(16, 24, 40, 0.06);
}
.profile-header {
  display: flex;
  align-items: center;
  gap: 24px;
}
.avatar {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 8px 30px rgba(0,0,0,0.10);
  border: 3px solid #fff;
  background: #eef2f7;
  flex-shrink: 0;
}
.profile-meta h1 {
  margin: 0;
  font-size: 1.9em;
  letter-spacing: -0.01em;
}
.profile-role {
  margin: 6px 0 0 0;
  color: #425466;
}
.socials {
  margin-top: 10px;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.socials a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #ffffff;
  color: #1976d2;
  border: 1px solid #dbe4ff;
  padding: 6px 10px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.1s;
}
.socials a:hover {
  background: #1976d2;
  color: #ffffff;
  box-shadow: 0 6px 16px rgba(25, 118, 210, 0.25);
  transform: translateY(-1px);
}
.info-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(240px, 1fr));
  gap: 16px;
  margin-top: 16px;
}
.info-card {
  background: #fbfcff;
  border: 1px solid #e6eefc;
  border-left: 4px solid #1976d2;
  border-radius: 12px;
  padding: 14px 16px;
  transition: box-shadow 0.2s, transform 0.1s, border-color 0.2s;
}
.info-card:hover { box-shadow: 0 8px 18px rgba(25, 118, 210, 0.10); transform: translateY(-1px); border-color: #1256a1; }
.info-card h3 { margin: 0 0 8px 0; font-size: 1.05em; }
.info-card ul { margin: 0; padding-left: 1.2rem; }
.info-card li { margin: 6px 0; }
.info-card li::marker { color: #1976d2; }

@media (max-width: 768px) {
  .profile-header { flex-direction: column; align-items: flex-start; }
  .avatar { width: 140px; height: 140px; }
  .info-grid { grid-template-columns: 1fr; }
}
</style>

<div class="profile-card">
  <div class="profile-header">
    <div class="avatar">
      <img src="../images/IMG_8383.JPEG" alt="Michał Tyrolski" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div class="profile-meta">
      <h1>Michał Tyrolski</h1>
      <p class="profile-role">Senior AI Consultant at Ernst & Young / Independent Researcher</p>
      <div class="socials">
        <a href="https://github.com/mtyrolski"><i class="fab fa-github"></i> <span>GitHub</span></a>
        <a href="https://twitter.com/mtyrolski"><i class="fab fa-twitter"></i> <span>Twitter</span></a>
        <a href="https://www.linkedin.com/in/michal-tyrolski/"><i class="fab fa-linkedin"></i> <span>LinkedIn</span></a>
        <a href="../files/cv.pdf"><i class="fas fa-file-pdf"></i> <span>CV</span></a>
      </div>
    </div>
  </div>
  <div class="info-grid">
    <div class="info-card">
      <h3>Professional Experience</h3>
      <ul>
  <li>2025–present — Senior AI Consultant IV, Ernst & Young (Warsaw)</li>
  <li>2022–2025 — Deep Learning Researcher, DeepFlare (Warsaw)</li>
  <li>07–10 2022 — Data Scientist Intern, Microsoft (Dublin)</li>
  <li>2021–2022 — Teaching Assistant, University of Warsaw (Warsaw)</li>
  <li>07–10 2021 — Deep Learning Intern, Nvidia (Warsaw)</li>
  <li>04–06 2021 — Software Engineering Intern, Microsoft (Dublin)</li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Education</h3>
      <ul>
  <li>2021–2023 — M.Sc. Machine Learning, University of Warsaw (honors)</li>
  <li>2018–2021 — B.Sc. Computer Science, University of Warsaw</li>
      </ul>
    </div>
  </div>
</div>


I am **Michał Tyrolski**, a *Senior AI Consultant* at **Ernst & Young**. I hold an **M.Sc. in Machine Learning** (2023), supervised by prof. Marek Cygan and prof. Piotr Miłoś, and a **B.Sc. in Computer Science** (2021), supervised by prof. Henryk Michalewski, both from the [**University of Warsaw**](https://www.mimuw.edu.pl/en/).

My main research interests include **AI-based Planning**, **decision-making in complex environments**, **Meta-Reinforcement Learning**, and **Continual Learning**. Over the years, I’ve gained experience in both offline and online reinforcement learning, planning, efficient transformer architectures, and LLMs. I’ve also had the opportunity to be involved in AI projects at **Microsoft**, **Nvidia**, **Deepflare**, and **Samsung**.

I am an active member of the AI community, particularly with [**ML in PL Association**](https://mlinpl.org/), where I have been an organizer since 2020. In my free time, I enjoy mountain hiking and motorization.

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

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1500px; margin: 0 auto;">
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
    <div style="width: 290px; height: 290px; margin-left: 2.5rem; background: #fafbfc; border-radius: 12px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
      {% if publication.image %}
        <img src="{{ publication.image }}" alt="{{ publication.title }}" style="max-width: 100%; max-height: 100%; object-fit: cover; border-radius: 12px;" />
      {% else %}
        <span style="color: #aaa; font-size: 1.2em;">Image<br>Placeholder</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>


## Other Papers

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1500px; margin: 0 auto;">
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
    <div style="width: 260px; height: 260px; margin-left: 2.5rem; background: #fafbfc; border-radius: 12px; display: flex; align-items: center; justify-content: center; overflow: hidden;">
      {% if paper.image %}
        <img src="{{ paper.image }}" alt="{{ paper.title }}" style="max-width: 100%; max-height: 100%; object-fit: cover; border-radius: 12px;" />
      {% else %}
        <span style="color: #aaa; font-size: 1.2em;">Image<br>Placeholder</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>


## Selected Projects

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1500px; margin: 0 auto;">
  <div style="border: 1px solid #1976d2; border-radius: 8px; padding: 1.5rem; background: #f5faff; box-shadow: 0 2px 8px rgba(25, 118, 210, 0.06);">
    <strong style="font-size: 1.2em; color: #1976d2;">CaRL Library: Combinatorial RL for planning</strong><br>
    <em>Lead author & maintainer</em><br>
    <div style="width: 100%; max-width: 600px; height: 320px; margin: 1.2em auto 0.7em auto; background: #fafbfc; border-radius: 14px; display: flex; align-items: center; justify-content: center;">
      <img src="../images/planning.png" alt="CaRL Architecture" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 14px;" />
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


