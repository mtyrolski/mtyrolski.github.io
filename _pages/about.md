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

<!-- Citation toggle handled with <details> for GitHub Pages compatibility (no inline JS needed) -->

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
  <div class="info-card experience">
      <h3>Professional Experience</h3>
      <ul>
        <li>
          <div class="item-title">Senior AI Consultant IV, Ernst & Young</div>
          <div class="item-date">2025 — present</div>
          <div class="item-subtext">Warsaw, Poland</div>
        </li>
        <li>
          <div class="item-title">Deep Learning Researcher, DeepFlare</div>
          <div class="item-date">2022 — 2025</div>
          <div class="item-subtext">Warsaw, Poland</div>
        </li>
        <li>
          <div class="item-title">Data Scientist Intern, Microsoft</div>
          <div class="item-date">Jul 2022 — Oct 2022</div>
          <div class="item-subtext">Dublin, Ireland</div>
        </li>
        <li>
          <div class="item-title">Teaching Assistant, Uni of Warsaw</div>
          <div class="item-date">2021 — 2022</div>
          <div class="item-subtext">Warsaw, Poland</div>
        </li>
        <li>
          <div class="item-title">Deep Learning Intern, Nvidia</div>
          <div class="item-date">Jul 2021 — Oct 2021</div>
          <div class="item-subtext">Warsaw, Poland</div>
        </li>
        <li>
          <div class="item-title">Software Engineering Intern, Microsoft</div>
          <div class="item-date">Apr 2021 — Jun 2021</div>
          <div class="item-subtext">Dublin, Ireland</div>
        </li>
        <li>
          <div class="item-title">Deep Learning Intern, Nvidia</div>
          <div class="item-date">Jun 2020 — Sep 2020</div>
          <div class="item-subtext">Warsaw, Poland</div>
        </li>
        <li>
          <div class="item-title">Software Developer Intern AI, Samsung</div>
          <div class="item-date">Jul 2019 — Sep 2019</div>
          <div class="item-subtext">Warsaw, Poland</div>
        </li>
      </ul>
    </div>
    <div class="info-card">
      <h3>Education</h3>
      <ul>
        <li>
          <div class="item-title">M.Sc. Machine Learning, University of Warsaw</div>
          <div class="item-date">Warsaw, Poland 2021 — 2023</div>
          <div class="item-subtext">top 5% students · graduated with honors</div>
          <div class="key-activities">
            <strong>Key activities:</strong>
            <ul>
              <li>ICLR A* oral top-5%, onsite presentation on reinforcement learning, first such paper from Poland</li>
              <li>Co-led ML in PL Conference 2021,</li>
            </ul>
          </div>
        </li>
        <li>
          <div class="item-title">B.Sc. Computer Science, University of Warsaw</div>
          <div class="item-date">Warsaw, Poland 2018 — 2021</div>
          <div class="item-subtext">top 5% students</div>
          <div class="key-activities">
            <strong>Key activities:</strong>
            <ul>
              <li>Published paper on efficient transformers with Google Research.</li>
              <li>President, Machine Learning Society at UW.</li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
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

  <span class="para-label">Profile</span> I am **Michał Tyrolski**, a *Senior AI Consultant* at **Ernst & Young**. I hold an **M.Sc. in Machine Learning** (2023), supervised by prof. [Marek Cygan](https://scholar.google.com/citations?hl=en&user=df8TSy4AAAAJ) and prof. [Piotr Miłoś](https://www.mimuw.edu.pl/~pmilos/), and a **B.Sc. in Computer Science** (2021), supervised by prof. [Henryk Michalewski](https://www.mimuw.edu.pl/~henrykm/resume.html) and prof. [Łukasz Kaiser](https://scholar.google.com/citations?user=JWmiQR0AAAAJ&hl=en), both from the [**University of Warsaw, MIM Faculty**](https://www.mimuw.edu.pl/en/).


<!-- Research Interests -->
<span class="para-label">Research Focus</span> My research interests lie at the intersection of **AI-based Planning**, **decision-making in complex environments**, and **Reinforcement Learning**. I am driven by the challenge of advancing the reasoning capabilities of AI algorithms and exploring the strategic thinking that emerges within Game Intelligence. To further pursue this direction, I have recently begun delving in **Meta-RL**, and **Continual Learning** to develop algorithms **capable of solving problem instances** under, broadly speaking, **heavy domain shifts** across different axes.

<!-- Techniczne skille + experience  + doświadczenie przy różnych googlach nie googlach -->
<span class="para-label">Computer Science Background</span> My experience spans the **entire AI stack**: from **low-level C++/CUDA engineering** ([NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)) and **scalable distributed systems** ([Microsoft Omex](https://github.com/microsoft/Omex)), through **MLOps** and **ML library development** ([**CaRL**: Deep RL library calibrated for planning and search](https://github.com/mtyrolski/carl)), to advanced **applied & research innovation** across industry and academia. I have worked on **deep learning for vaccine discovery** (DeepFlare), **3D computer vision algorithms** (Samsung), and built my own **fastest model parallelism algorithm** at the time for extremely large **NLP models** (NVIDIA). I was the first **Microsoft Ireland** intern to have a paper accepted at **[MLADS](https://mymlads.microsoft.com/)** on explainable AI. My bachelor’s thesis with **Google Research** set **state-of-the-art benchmarks** for [efficient transformers](https://arxiv.org/abs/2110.13711) in long-sequence prediction. During my master’s, I developed **Adaptive Subgoal Search (AdaSubS)**, a novel search algorithm for efficient reinforcement learning under low computational budgets—presented onsite as an **ICLR 2023 Top-5% Oral** (first such achievement from Poland). Most recently, my research on **hierarchical search landscapes** was awarded **Best Poster at [EEML 2025](https://www.eeml.eu/)**.


<!-- Community Contribution -->
<span class="para-label">Community</span> I am an active member of the AI community, particularly within the [**ML in PL Association**](https://mlinpl.org/), a non-profit advancing the machine learning community in Poland and across Central & Eastern Europe. Since 2020, I have served as **Scientific Program Officer** across six annual editions—curating a high-impact invited speaker lineup—and had the honor to be **co-Leader** of the [**ML in PL 2021 Conference**](https://conference2021.mlinpl.org/). In my free time, I enjoy mountain hiking and motorization.



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
      {% if publication.citation %}
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
      {% if paper.paperurl %}
        <a href="{{ paper.paperurl }}" class="paper-link">Paper</a>
      {% endif %}
      {% if paper.excerpt %}<br>{{ paper.excerpt }}{% endif %}
      {% if paper.citation %}
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


