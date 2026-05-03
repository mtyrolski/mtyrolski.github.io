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
/* Homepage width tuning */
#main {
  width: 100% !important;
  max-width: none !important;
  padding-right: 0 !important;
  padding-left: 0 !important;
  box-sizing: border-box;
}
.masthead__inner-wrap {
  max-width: 810px !important;
  margin-right: auto !important;
  margin-left: auto !important;
}
.page {
  float: none !important;
  width: min(810px, calc(100% - 4rem)) !important;
  max-width: 810px !important;
  margin-right: auto !important;
  margin-left: auto !important;
  padding-right: 0 !important;
  padding-left: 0 !important;
  box-sizing: border-box;
}
.page__inner-wrap {
  max-width: none !important;
}
.page__content {
  width: 100%;
  max-width: none;
  margin: 0;
}

:root {
  --home-profile-bg: linear-gradient(180deg, #f8f9fa, #ffffff);
  --home-card-bg: #fafbfc;
  --home-card-bg-soft: #fbfcff;
  --home-card-bg-hover: #f0f6ff;
  --home-card-border: #e0e0e0;
  --home-card-border-soft: #e6eefc;
  --home-muted-text: #6b7280;
  --home-image-bg: #ffffff;
  --home-accent: #1976d2;
  --home-accent-hover: #1256a1;
  --home-danger: #c62828;
  --home-danger-hover: #9f1f1f;
  --home-shadow: rgba(16, 24, 40, 0.06);
}
html[data-theme="dark"] {
  --home-profile-bg: linear-gradient(180deg, #4f4f4f, #444);
  --home-card-bg: #3f3f3f;
  --home-card-bg-soft: #4a4a4a;
  --home-card-bg-hover: #425056;
  --home-card-border: #666;
  --home-card-border-soft: #5c6770;
  --home-muted-text: var(--global-text-color-light);
  --home-image-bg: #f7f7f7;
  --home-accent: var(--global-link-color);
  --home-accent-hover: var(--global-link-color-hover);
  --home-danger: #d85b5b;
  --home-danger-hover: #b84747;
  --home-shadow: rgba(0, 0, 0, 0.22);
}

/* Profile card styling */
.profile-card {
  display: flex;
  flex-direction: column;
  background: var(--home-profile-bg);
  border: 1px solid var(--home-card-border);
  border-radius: 14px;
  padding: 18px 20px;
  margin: 0 auto 28px auto;
  max-width: 810px;
  box-shadow: 0 6px 20px var(--home-shadow);
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
  border: 3px solid var(--global-bg-color);
  background: var(--home-card-bg-soft);
  flex-shrink: 0;
}
.profile-meta h1 {
  margin: 0;
  font-size: 1.9em;
  letter-spacing: -0.01em;
}
.profile-role {
  margin: 6px 0 0 0;
  color: var(--home-muted-text);
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
  background: var(--home-card-bg);
  color: var(--home-accent);
  border: 1px solid var(--home-card-border-soft);
  padding: 6px 10px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.1s;
}
.socials a:hover {
  background: var(--home-accent);
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
  background: var(--home-card-bg-soft);
  border: 1px solid var(--home-card-border-soft);
  border-left: 4px solid var(--home-accent);
  border-radius: 12px;
  padding: 14px 16px;
  transition: box-shadow 0.2s, transform 0.1s, border-color 0.2s;
}
.info-card:hover { box-shadow: 0 8px 18px rgba(25, 118, 210, 0.10); transform: translateY(-1px); border-color: var(--home-accent-hover); }
.info-card h3 { margin: 0 0 8px 0; font-size: 1.05em; }
.info-card ul { margin: 0; padding-left: 1.2rem; }
.info-card li { margin: 8px 0; }
.info-card li::marker { color: var(--home-accent); }
/* two-line item layout */
.item-title { font-weight: 600; line-height: 1.3; }
.item-date { font-size: 0.92em; color: var(--home-muted-text); margin-top: 2px; }
.item-subtext { font-size: 0.9em; color: var(--home-muted-text); margin-top: 1px; }

/* Inline date and place for Professional Experience */
.info-card.experience .item-date,
.info-card.experience .item-subtext {
  display: inline;
}
.info-card.experience .item-date::after {
  content: ' · ';
  color: var(--home-muted-text);
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
      <p class="profile-role">Senior AI Consultant at EY / Independent Researcher</p>
      <div class="socials">
        <a href="https://github.com/mtyrolski"><i class="fab fa-github"></i> <span>GitHub</span></a>
        <a href="https://twitter.com/mtyrolski"><i class="fab fa-twitter"></i> <span>Twitter</span></a>
        <a href="https://www.linkedin.com/in/mtyrolski/"><i class="fab fa-linkedin"></i> <span>LinkedIn</span></a>
        <a href="{{ site.author.googlescholar }}"><i class="ai ai-google-scholar"></i> <span>Scholar</span></a>
      </div>
    </div>
  </div>
  <div style="margin: 24px 0 0 0;">
    <span class="para-label">Profile</span> I am interested in building AI systems that can plan, adapt, and generalise in complex environments. My research focuses on <strong>AI planning</strong>, <strong>reinforcement learning</strong>, <strong>abstraction</strong>, and <strong>decision-making under distribution shift</strong>.<br><br>
    I hold an <strong>M.Sc. in Machine Learning</strong> (2023), supervised by Prof. <a href="https://www.mimuw.edu.pl/~pmilos/">Piotr Miłoś</a> and Prof. <a href="https://scholar.google.com/citations?hl=en&user=df8TSy4AAAAJ">Marek Cygan</a>, and a <strong>B.Sc. in Computer Science</strong> (2021), supervised by Prof. <a href="https://www.mimuw.edu.pl/~henrykm/resume.html">Henryk Michalewski</a> and Prof. <a href="https://scholar.google.com/citations?user=JWmiQR0AAAAJ&hl=en">Łukasz Kaiser</a>, both from the <a href="https://www.mimuw.edu.pl/en/"><strong>University of Warsaw, MIM Faculty</strong></a>. I currently work as a <em>Senior AI Consultant</em> at <strong>EY</strong> on agentic AI systems.<br><br> 

  </div>

</div>

<!-- Generic Actual Info -->
  <style>
  .para-label {
    display:inline-block;
    font-size:0.72em;
    letter-spacing:0.08em;
    text-transform:uppercase;
    background:var(--home-accent);
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

Alongside this, I have gained experience in research and engineering roles at NVIDIA, Microsoft, Samsung, DeepFlare, and EY. Since 2020, I have also been involved in the <a href="https://mlinpl.org/"><strong>ML in PL Association</strong></a>, supporting scientific programme activities and conference organisation across several editions, including its <a href="https://conference.mlinpl.org/2026/">upcoming 10th anniversary conference</a>.

You can view my [full CV here](../files/cv.pdf).


## Selected Publications

<style>
.publication-box {
  display: flex;
  align-items: stretch;
  gap: 0.8rem;
  border: 1px solid var(--home-card-border);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  background: var(--home-card-bg);
  min-height: 0;
  font-size: 1.04rem;
  line-height: 1.35;
  transition: background 0.2s, box-shadow 0.2s, border-color 0.2s;
}
.publication-box:hover {
  background: var(--home-card-bg-hover);
  box-shadow: 0 2px 8px rgba(30, 136, 229, 0.08);
  border-color: var(--home-accent);
}
.publication-box strong { font-size: 1.08em; }
.publication-box em { color: var(--home-muted-text); }
.publication-list,
.project-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 810px;
  margin: 0 auto;
}
.publication-content {
  flex: 1;
  min-width: 0;
}
.publication-excerpt {
  margin-top: 0.15em;
}
.publication-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  gap: 0.35rem;
  margin: 0.45em 0 0.4em;
}
.paper-link {
  display: inline-block;
  background: var(--home-danger);
  color: #fff;
  padding: 0.26em 0.7em;
  border-radius: 5px;
  text-decoration: none;
  font-weight: 600;
  margin: 0;
  font-size: 0.92em;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s;
}
.paper-link:hover {
  background: var(--global-bg-color);
  color: var(--home-danger);
  box-shadow: 0 0 0 2px var(--home-danger) inset;
}
.cite-button {
    display: inline-block;
    background: var(--home-accent);
    color: #fff;
    padding: 0.26em 0.7em;
    border-radius: 5px;
    text-decoration: none;
    font-weight: 600;
    margin: 0;
    cursor: pointer;
    transition: background 0.2s, box-shadow 0.2s;
  }
  .cite-button:hover {
    background: var(--home-accent-hover);
    box-shadow: 0 2px 8px rgba(25, 118, 210, 0.2);
  }
  .citation-details {
    margin: 0;
  }
  .citation-details[open] > .cite-button {
    background: var(--home-accent-hover);
  }
  .citation-box {
    background: var(--home-card-bg-soft);
    border: 1px solid var(--home-card-border);
    padding: 1em;
    border-radius: 8px;
    margin-top: 0.6em;
    font-family: monospace;
    white-space: pre-wrap;
  word-break: break-word;
  }
/* Publication image wrapper utility */
.pub-img-wrapper {
  width: 220px; min-height: 100%; margin-left: 0; flex: 0 0 220px; background: var(--home-image-bg); border-radius: 8px; display: flex; align-items: stretch; justify-content: center; overflow: hidden;
}
.pub-img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  padding: 4px;
  box-sizing: border-box;
  border-radius: 8px;
}
.pub-img-wrapper.small {
  width: 200px;
  flex-basis: 200px;
}
.project-box {
  display: flex;
  align-items: stretch;
  gap: 0.8rem;
  border: 1px solid var(--home-accent);
  border-radius: 8px;
  padding: 0.75rem 0.85rem;
  background: var(--home-card-bg);
  box-shadow: 0 2px 8px rgba(25, 118, 210, 0.06);
  font-size: 1.05rem;
  line-height: 1.35;
}
.project-title {
  font-size: 1.08em;
  color: var(--home-accent);
}
.project-content {
  flex: 1;
  min-width: 0;
}
.project-text {
  margin-top: 0.55em;
}
.project-text ul {
  margin: 0.45em 0 0 1.15em;
}
.project-text li {
  margin: 0.25em 0;
}
.project-media {
  width: 190px;
  min-height: 100%;
  flex: 0 0 190px;
  background: var(--home-image-bg);
  border-radius: 8px;
  display: flex;
  align-items: stretch;
  justify-content: center;
  overflow: hidden;
}
.project-media img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  padding: 4px;
  box-sizing: border-box;
  border-radius: 8px;
}
.project-links {
  margin-top: 0.55em;
}
.project-links a {
  display: inline-block;
  background: var(--home-accent);
  color: #fff;
  padding: 0.32em 0.85em;
  border-radius: 5px;
  text-decoration: none;
  font-weight: 600;
  margin: 0 0.35em 0.35em 0;
  font-size: 0.92em;
}
.project-links a.paper {
  background: var(--home-danger);
}
@media (max-width: 920px) {
  .page { width: calc(100% - 2rem) !important; }
  .publication-box { flex-direction: column; align-items: flex-start; padding: 0.95rem; }
  .pub-img-wrapper, .pub-img-wrapper.small { width: 100%; height: auto; flex-basis: auto; margin: 1rem 0 0 0; }
  .pub-img-wrapper img { width: 100%; height: auto; max-height: 320px; object-fit: contain; }
  .cite-button { width: auto; }
  .project-box { flex-direction: column; }
  .project-media { width: 100%; height: auto; flex-basis: auto; }
  .project-media img { width: 100%; max-height: 260px; }
}
@media (max-width: 520px) {
  .profile-card { padding: 16px 16px 22px; }
  .publication-box { padding: 0.85rem; }
  .pub-img-wrapper img { max-height: 260px; }
  .cite-button { padding: 0.45em 0.85em; font-size: 0.9em; }
}
@media (max-width: 380px) {
  .cite-button { width: 100%; text-align: center; }
}
</style>

<div class="publication-list">
{% assign pubs_sorted = site.publications | sort: 'date' | reverse %}
{% for publication in pubs_sorted %}
  <div class="publication-box">
    <div class="publication-content">
      <strong>{{ publication.title }}</strong><br>
      <em>{{ publication.venue }}</em><br>
      <div class="publication-actions">
        {% if publication.paperurl and publication.paperurl != blank %}
          <a href="{{ publication.paperurl }}" class="paper-link">{{ publication.paperlabel | default: "Paper" }}</a>
        {% endif %}
        {% if publication.codeurl and publication.codeurl != blank %}
          <a href="{{ publication.codeurl }}" class="paper-link">{{ publication.codelabel | default: "Code" }}</a>
        {% endif %}
        {% if publication.websiteurl and publication.websiteurl != blank %}
          <a href="{{ publication.websiteurl }}" class="paper-link">{{ publication.websitelabel | default: "Website" }}</a>
        {% endif %}
        {% if publication.colaburl and publication.colaburl != blank %}
          <a href="{{ publication.colaburl }}" class="paper-link">Colab</a>
        {% endif %}
        {% if publication.citation and publication.citation != blank %}
          <details class="citation-details" id="cite-{{ publication.title | slugify }}">
            <summary class="cite-button" style="list-style:none;">Cite</summary>
            <div class="citation-box">{{ publication.citation }}</div>
          </details>
        {% endif %}
      </div>
      {% if publication.excerpt %}<div class="publication-excerpt">{{ publication.excerpt }}</div>{% endif %}
    </div>
  <div class="pub-img-wrapper">
      {% if publication.image %}
        <img src="{{ publication.image }}" alt="{{ publication.title }}" />
      {% else %}
        <span style="color: #aaa; font-size: 1.2em;">Image<br>Placeholder</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>


## Other Papers

<div class="publication-list">
{% for paper in site.other_papers %}
  <div class="publication-box">
    <div class="publication-content">
      <strong>{{ paper.title }}</strong><br>
      <em>{{ paper.venue }}</em><br>
      <div class="publication-actions">
        {% if paper.paperurl and paper.paperurl != blank %}
          <a href="{{ paper.paperurl }}" class="paper-link">Paper</a>
        {% endif %}
        {% if paper.citation and paper.citation != blank %}
          <details class="citation-details" id="cite-{{ paper.title | slugify }}">
            <summary class="cite-button" style="list-style:none;">Cite</summary>
            <div class="citation-box">{{ paper.citation }}</div>
          </details>
        {% endif %}
      </div>
      {% if paper.excerpt %}<div class="publication-excerpt">{{ paper.excerpt }}</div>{% endif %}
    </div>
  <div class="pub-img-wrapper small">
      {% if paper.image %}
        <img src="{{ paper.image }}" alt="{{ paper.title }}" />
      {% else %}
        <span style="color: #aaa; font-size: 1.2em;">Image<br>Placeholder</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>


## Selected Projects

<div class="project-list">
  <div class="project-box">
    <div class="project-content">
      <strong class="project-title">CaRL Library: Combinatorial RL for Planning</strong><br>
      <div class="project-text">
        <b>CaRL</b> is an open-source library for offline and online reinforcement/imitation learning in combinatorial planning.
      </div>
      <div class="project-links">
        <a href="https://github.com/mtyrolski/carl">GitHub Repo</a>
        <a href="https://arxiv.org/abs/2406.03361" class="paper">Latest Paper</a>
      </div>
    </div>
    <div class="project-media">
      <img src="../images/planning.png" alt="CaRL Architecture" />
    </div>
  </div>
  <div class="project-box">
    <div class="project-content">
      <strong class="project-title">Todoist Assistant</strong><br>
      <div class="project-text">
        Local-first Todoist dashboard and automation toolkit with optional summaries and read-only chat over cached activity.
      </div>
      <div class="project-links">
        <a href="https://github.com/mtyrolski/todoist-assistant">GitHub Repo</a>
      </div>
    </div>
    <div class="project-media">
      <img src="../images/projects/todoist-assistant.png" alt="Todoist Assistant logo" />
    </div>
  </div>
</div>
