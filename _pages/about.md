---
permalink: /
title: ""
description: "Michał Tyrolski: research in AI planning, reinforcement learning, hierarchical reasoning, abstraction, and generalisation under distribution shift."
author_profile: false
page_class: home-page
redirect_from:
  - /about/
  - /about.html
---

<header class="home-profile">
  <div class="home-profile__header">
    <img class="home-profile__portrait" src="{{ '/images/mt_photo.png' | relative_url }}" alt="Michał Tyrolski">
    <div class="home-profile__meta">
      <h1>Michał Tyrolski</h1>
      <p class="home-profile__role">Senior AI Consultant at EY · AI planning and reinforcement learning</p>
      <nav class="socials home-socials" aria-label="Profile links">
        <a href="https://github.com/mtyrolski"><i class="fab fa-github" aria-hidden="true"></i> GitHub</a>
        <a href="https://twitter.com/mtyrolski"><i class="fab fa-twitter" aria-hidden="true"></i> Twitter</a>
        <a href="https://www.linkedin.com/in/mtyrolski/"><i class="fab fa-linkedin" aria-hidden="true"></i> LinkedIn</a>
        <a href="{{ site.author.googlescholar }}"><i class="ai ai-google-scholar" aria-hidden="true"></i> Scholar</a>
      </nav>
    </div>
  </div>

  <div class="home-profile__intro">
    <p>I am interested in building AI systems that can plan, adapt, and generalise in complex environments. My research focuses on <strong>AI planning</strong>, <strong>reinforcement learning</strong>, <strong>abstraction</strong>, and <strong>decision-making under distribution shift</strong>.</p>

    <p>I hold an <strong>MSc in Machine Learning</strong> (2023), supervised by Prof. <a href="https://www.mimuw.edu.pl/~pmilos/">Piotr Miłoś</a> and Prof. <a href="https://scholar.google.com/citations?hl=en&amp;user=df8TSy4AAAAJ">Marek Cygan</a>, and a <strong>BSc in Computer Science</strong> (2021), supervised by Prof. <a href="https://www.mimuw.edu.pl/~henrykm/resume.html">Henryk Michalewski</a> and Prof. <a href="https://scholar.google.com/citations?user=JWmiQR0AAAAJ&amp;hl=en">Łukasz Kaiser</a>, both from the <a href="https://www.mimuw.edu.pl/en/"><strong>University of Warsaw, MIM Faculty</strong></a>. I currently work as a <em>Senior AI Consultant</em> at <strong>EY</strong> on agentic AI systems.</p>
  </div>
</header>

<div class="home-intro">
  <p>My current research direction is <strong>adaptive planning in learned latent spaces</strong>: systems that adjust their planning horizon and level of abstraction to problem difficulty, progress, and changes in the environment.</p>

  <p>Alongside this, I have gained experience in research and engineering roles at NVIDIA, Microsoft, Samsung, DeepFlare, and EY. Since 2020, I have also been involved in the <a href="https://mlinpl.org/"><strong>ML in PL Association</strong></a>, supporting scientific programme activities and conference organisation across several editions.</p>

  <p>You can view my <a href="{{ '/files/cv.pdf' | relative_url }}">full CV here</a>.</p>
</div>

## Research

### Publications

<div class="research-list">
{% assign selected_publications = site.publications | where: "homepage_group", "publications" | sort: "selected_order" %}
{% for publication in selected_publications %}
  {% include publication-card.html publication=publication compact=true show_image=true %}
{% endfor %}
</div>

### Preprints

<div class="research-list">
{% assign preprints = site.publications | where: "homepage_group", "preprints" | sort: "selected_order" %}
{% for publication in preprints %}
  {% include publication-card.html publication=publication compact=true show_image=true %}
{% endfor %}
</div>

## Selected software

<ul class="software-list">
  <li><a href="https://deepflare.ai/">DeepFlare.ai</a> - contributed to an AI platform for in-silico immunogenicity prediction.</li>
  <li><a href="https://github.com/mtyrolski/CaRL">CaRL</a> - open-source framework for reproducible learning experiments in combinatorial planning.</li>
</ul>

<p class="small">More projects and open-source contributions are available on <a href="https://github.com/mtyrolski?tab=repositories">GitHub</a>.</p>

## Recognition and community

<ul class="recognition-list">
  <li><strong>ICLR 2023: Oral (top 5%)</strong> for <em>Fast and Precise: Adjusting Planning Horizon with Adaptive Subgoal Search</em>.</li>
  <li><strong>EEML 2025: Best Poster Award in Reinforcement Learning</strong> for <em>Hierarchical Search Landscapes</em>, continuing the study of hierarchical planning and generalisation.</li>
  <li>Long-term involvement with the <a href="https://mlinpl.org/">ML in PL Association</a>, including scientific programme work, conference organisation, and co-leadership.</li>
</ul>

## Contact

<p class="contact-actions">For any enquiries, <button class="contact-email" type="button" aria-describedby="contact-email-status">contact me by email</button>.</p>
<p id="contact-email-status" class="contact-status" role="status" aria-live="polite"></p>
