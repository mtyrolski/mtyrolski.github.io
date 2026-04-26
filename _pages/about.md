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
.info-card li { margin: 8px 0; }
.info-card li::marker { color: #1976d2; }
/* two-line item layout */
.item-title { font-weight: 600; line-height: 1.3; }
.item-date { font-size: 0.92em; color: #6b7280; margin-top: 2px; }
.item-subtext { font-size: 0.9em; color: #7a7f8a; margin-top: 1px; }

/* Inline date and place for Professional Experience */
.info-card.experience .item-date,
.info-card.experience .item-subtext {
  display: inline;
}
.info-card.experience .item-date::after {
  content: ' · ';
  color: #6b7280;
  margin: 0 4px;
}
.info-card.experience .item-subtext { margin: 0; }

@media (max-width: 768px) {
  .profile-header { flex-direction: column; align-items: flex-start; }
  .avatar { width: 140px; height: 140px; }
  .info-grid { grid-template-columns: 1fr; }
}
</style>


<div class="profile-card">
  <div class="profile-header">
    <div class="avatar">
    <img src="../images/mt_photo.png" alt="Michał Tyrolski" style="width: 100%; height: 100%; object-fit: cover; object-position: center 40%;">
    </div>
    <div class="profile-meta">
      <h1>Michał Tyrolski</h1>
      <p class="profile-role">Senior AI Consultant at Ernst & Young / Independent Researcher</p>
      <div class="socials">
        <a href="https://github.com/mtyrolski"><i class="fab fa-github"></i> <span>GitHub</span></a>
        <a href="https://twitter.com/mtyrolski"><i class="fab fa-twitter"></i> <span>Twitter</span></a>
        <a href="https://www.linkedin.com/in/mtyrolski/"><i class="fab fa-linkedin"></i> <span>LinkedIn</span></a>
        <a href="{{ site.author.googlescholar }}"><i class="ai ai-google-scholar"></i> <span>Scholar</span></a>
      </div>
    </div>
  </div>
  <div style="margin: 24px 0 0 0;">
    <span class="para-label">Profile</span> My name is <strong>Michał Tyrolski</strong>. I’m a <em>Senior AI Consultant</em> at <strong>Ernst & Young</strong>, where I work on Agentic AI systems. I hold an <strong>M.Sc. in Machine Learning</strong> (2023), supervised by Prof. <a href="https://www.mimuw.edu.pl/~pmilos/">Piotr Miłoś</a> and Prof. <a href="https://scholar.google.com/citations?hl=en&user=df8TSy4AAAAJ">Marek Cygan</a>, and a <strong>B.Sc. in Computer Science</strong> (2021), supervised by Prof. <a href="https://www.mimuw.edu.pl/~henrykm/resume.html">Henryk Michalewski</a> and Prof. <a href="https://scholar.google.com/citations?user=JWmiQR0AAAAJ&hl=en">Łukasz Kaiser</a>. Both degrees are from the <a href="https://www.mimuw.edu.pl/en/"><strong>University of Warsaw, MIM Faculty</strong></a>.<br><br>
    <span class="para-label">Research Focus</span> My research interests lie at the intersection of <strong>AI-based Planning</strong>, <strong>decision-making in complex environments</strong>, and <strong>Reinforcement Learning</strong>. I study how intelligent agents can select useful abstractions, adapt their planning horizon, and generalise under distribution shift across diverse problem settings.<br><br> 

  </div>

</div>

<!-- Generic Actual Info -->
  <style>
  .para-label {
    display:inline-block;
    font-size:0.72em;
    letter-spacing:0.08em;
    text-transform:uppercase;
    background:#1976d2;
    color:#fff;
    padding:3px 7px 2px;
    border-radius:5px;
    font-weight:600;
    margin-right:8px;
    line-height:1;
    position:relative;
    top:-2px;
    box-shadow:0 2px 4px rgba(25,118,210,0.25);
  }
  @media (max-width:600px){
    .para-label{font-size:0.65em; margin-right:6px;}
  }
  </style>

My broader experience spans research and engineering across large-scale machine learning, distributed systems, scientific AI, and applied intelligent systems through work with NVIDIA, Microsoft, Samsung, DeepFlare, and Ernst & Young. I am an active member of the broader AI community, particularly through the <a href="https://mlinpl.org/"><strong>ML in PL Association</strong></a>, a non-profit supporting the machine learning community in Poland and across Central & Eastern Europe. Since 2020, I have contributed to scientific programme activities and conference organisation across multiple editions, including the upcoming <a href="https://conference.mlinpl.org/2026/">10th anniversary conference</a>.


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
.cite-button {
    display: inline-block;
    background: #1976d2;
    color: #fff;
    padding: 0.4em 1em;
    border-radius: 5px;
    text-decoration: none;
    font-weight: 600;
    margin: 0.5em 0;
    cursor: pointer;
    transition: background 0.2s, box-shadow 0.2s;
  }
  .cite-button:hover {
    background: #1256a1;
    box-shadow: 0 2px 8px rgba(25, 118, 210, 0.2);
  }
  .citation-details {
    margin-top: 0.4em;
  }
  .citation-details[open] > .cite-button {
    background: #1256a1;
  }
  .citation-box {
    background: #f8f9fa;
    border: 1px solid #e0e0e0;
    padding: 1em;
    border-radius: 8px;
    margin-top: 0.6em;
    font-family: monospace;
    white-space: pre-wrap;
  word-break: break-word;
  }
/* Publication image wrapper utility */
.pub-img-wrapper {
  width: 290px; height: 290px; margin-left: 2.5rem; background: #fafbfc; border-radius: 12px; display: flex; align-items: center; justify-content: center; overflow: hidden;
}
.pub-img-wrapper.small { width: 260px; height: 260px; }
@media (max-width: 920px) {
  .publication-box { flex-direction: column; align-items: flex-start; padding: 1.1rem 1.1rem 1.25rem; }
  .pub-img-wrapper, .pub-img-wrapper.small { width: 100%; height: auto; margin: 1rem 0 0 0; }
  .pub-img-wrapper img { width: 100%; height: auto; max-height: 320px; object-fit: contain; }
  .publication-box > div:first-child { max-width: 100% !important; }
  .cite-button { width: auto; }
}
@media (max-width: 520px) {
  .profile-card { padding: 16px 16px 22px; }
  .publication-box { padding: 0.95rem 0.95rem 1.1rem; }
  .pub-img-wrapper img { max-height: 260px; }
  .cite-button { padding: 0.45em 0.85em; font-size: 0.9em; }
}
@media (max-width: 380px) {
  .cite-button { width: 100%; text-align: center; }
}
</style>

<div style="display: flex; flex-direction: column; gap: 1.5rem; max-width: 1500px; margin: 0 auto;">
{% assign pubs_sorted = site.publications | sort: 'date' | reverse %}
{% for publication in pubs_sorted %}
  <div class="publication-box">
    <div style="flex: 1; max-width: calc(100% - 170px);">
      <strong>{{ publication.title }}</strong><br>
      <em>{{ publication.venue }}</em><br>
      {% if publication.paperurl and publication.paperurl != blank %}
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
      {% if publication.citation and publication.citation != blank %}
        <details class="citation-details" id="cite-{{ publication.title | slugify }}">
          <summary class="cite-button" style="list-style:none;">Cite</summary>
          <div class="citation-box">{{ publication.citation }}</div>
        </details>
      {% endif %}
    </div>
  <div class="pub-img-wrapper">
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
      {% if paper.paperurl and paper.paperurl != blank %}
        <a href="{{ paper.paperurl }}" class="paper-link">Paper</a>
      {% endif %}
      {% if paper.excerpt %}<br>{{ paper.excerpt }}{% endif %}
      {% if paper.citation and paper.citation != blank %}
        <details class="citation-details" id="cite-{{ paper.title | slugify }}">
          <summary class="cite-button" style="list-style:none;">Cite</summary>
          <div class="citation-box">{{ paper.citation }}</div>
        </details>
      {% endif %}
    </div>
  <div class="pub-img-wrapper small">
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
    <strong style="font-size: 1.2em; color: #1976d2;">OpenGVL: Benchmarking Visual Temporal Progress for Data Curation</strong><br>
    <em>Co-author & contributor</em><br>
    <div style="width: 100%; max-width: 600px; height: 320px; margin: 1.2em auto 0.7em auto; background: #fafbfc; border-radius: 14px; display: flex; align-items: center; justify-content: center;">
      <img src="../images/publications/opengvl.png" alt="OpenGVL" style="max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 14px;" />
    </div>
    <p style="margin-top: 0.7em;">
      <b>OpenGVL</b> is an open benchmark and toolkit for measuring how well vision–language models understand <b>temporal task progress</b> in robotics, enabling <b>automatic dataset curation</b> by predicting per-frame completion from videos.
      <ul style="margin: 0.5em 0 0.5em 1.2em;">
        <li><b>Problem:</b> Equip robots with a sense of progress for better learning and decision-making.</li>
        <li><b>Metric (VOC):</b> Value‑Order Correlation - Spearman rank correlation between predicted progress ordering and true time order.</li>
        <li><b>Few‑shot prompting:</b> Uses ordered context episodes to guide predictions on shuffled frames.</li>
        <li><b>Contamination control:</b> Hidden tasks with curated demos; 100% completion rate datasets used for evaluation.</li>
        <li><b>Unified interface:</b> Standardized prompts, data loaders, and configs (Hydra) across open and closed VLMs.</li>
      </ul>
    </p>
    <div style="margin-top: 0.7em;">
      <a href="https://github.com/budzianowski/opengvl" style="display: inline-block; background: #1976d2; color: #fff; padding: 0.4em 1.2em; border-radius: 5px; text-decoration: none; font-weight: 600; margin-right: 0.7em; transition: background 0.2s;">GitHub Repo</a>
      <a href="https://huggingface.co/spaces/OpenGVL/OpenGVL" style="display: inline-block; background: #1976d2; color: #fff; padding: 0.4em 1.2em; border-radius: 5px; text-decoration: none; font-weight: 600; margin-right: 0.7em; transition: background 0.2s;">Live Benchmark</a>
      <a href="https://arxiv.org/abs/2509.17321" style="display: inline-block; background: #c62828; color: #fff; padding: 0.4em 1.2em; border-radius: 5px; text-decoration: none; font-weight: 600; transition: background 0.2s;">arXiv</a>
    </div>
  </div>
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

