---
layout: page
permalink: /talks/
title: Talks
description: Invited talks and seminars at ENCODE Lab
nav: true
nav_order: 5
---

<style>
  /* ---- Talk cards ---- */
  .talk-item {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    gap: 1.5rem;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    background: var(--global-card-bg-color);
    border: 1px solid var(--global-divider-color);
    border-radius: var(--card-radius);
    box-shadow: var(--card-shadow);
    transition: var(--card-transition);
  }

  .talk-item:hover {
    transform: var(--card-lift);
    box-shadow: var(--card-shadow-hover);
  }

  /* Highlight upcoming talks with an accent + badge */
  .talk-item.upcoming {
    border-left: 4px solid var(--global-theme-color);
  }

  .talk-item.upcoming .talk-title::before {
    content: "UPCOMING";
    display: inline-block;
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: #fff;
    background: var(--global-theme-color);
    border-radius: 999px;
    padding: 0.16rem 0.6rem;
    margin-right: 0.55rem;
    vertical-align: middle;
  }

  .talk-image {
    width: 96px;
    min-width: 96px;
    height: 96px;
    object-fit: cover;
    border-radius: 50%;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15);
  }

  .talk-content {
    flex: 1;
    min-width: 0;
  }

  .talk-title {
    font-size: 1.18rem;
    font-weight: 700;
    line-height: 1.35;
    margin: 0 0 0.4rem 0;
    color: var(--global-theme-color);
  }

  .talk-speaker {
    font-size: 1rem;
    font-weight: 600;
    margin: 0.2rem 0;
    color: var(--global-text-color);
  }

  .talk-affiliation {
    font-size: 0.9rem;
    color: var(--global-text-color-light);
    margin: 0.1rem 0 0.6rem 0;
  }

  .talk-date,
  .talk-meta {
    font-size: 0.85rem;
    color: var(--global-text-color-light);
    margin: 0.28rem 0;
  }

  .talk-date i,
  .talk-meta i {
    color: var(--global-theme-color);
    width: 1rem;
    margin-right: 0.45rem;
    text-align: center;
  }

  .talk-abstract {
    font-size: 0.9rem;
    line-height: 1.65;
    margin: 0.8rem 0 0.25rem 0;
    color: var(--global-text-color);
  }

  /* Pill-shaped link buttons */
  .talk-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 0.85rem;
  }

  .talk-links a {
    font-size: 0.82rem;
    color: var(--global-theme-color);
    border: 1px solid var(--global-divider-color);
    border-radius: 999px;
    padding: 0.28rem 0.85rem;
    text-decoration: none;
    transition: background 0.2s ease, color 0.2s ease, border-color 0.2s ease;
  }

  .talk-links a:hover {
    background: var(--global-theme-color);
    border-color: var(--global-theme-color);
    color: #fff;
  }

  @media (max-width: 576px) {
    .talk-item {
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 1.25rem;
    }

    .talk-item.upcoming {
      border-left: none;
      border-top: 4px solid var(--global-theme-color);
    }

    .talk-links {
      justify-content: center;
    }
  }
</style>

## Upcoming Talks

<div class="talk-item upcoming">
  <img class="talk-image" src="../assets/img/talks/xilin_chen.png" alt="Xilin Chen"/>
  <div class="talk-content">
    <h3 class="talk-title">On the Transfer and Development of Embodied Intelligent Systems</h3>
    <p class="talk-speaker">Xilin Chen, Professor</p>
    <p class="talk-affiliation">Institute of Computing Technology, Chinese Academy of Sciences</p>
    <p class="talk-date"><i class="fa-regular fa-calendar"></i> June 23, 2026, 14:00-15:30</p>
    <p class="talk-meta"><i class="fa-solid fa-location-dot"></i> E10-215, Yungu Campus</p>
    <p class="talk-meta"><i class="fa-solid fa-user"></i> Host: Huan Wang</p>
    <p class="talk-meta"><i class="fa-solid fa-microphone"></i> Westlake AI Forum (8th) &middot; Language: Chinese</p>
    <p class="talk-abstract">
      Embodied intelligence is a bridge and engineering path connecting the physical and mental worlds, and has become an important means for exploring intelligence and its applications. However, the field faces challenges such as a wide variety of embodiments and highly task-dependent settings, which often lead to dependency and over-specialization that constrain progress. The key to overcoming these limitations lies in cross-embodiment transferability and cross-task developmental growth. This talk explores these problems, proposing hierarchical task decomposition and language–embodiment adaptation for transferability, and continual learning for growth. We present recent work probing the feasibility of these ideas, and outline open problems and future directions worth attention.
    </p>
    <div class="talk-links">
      <a href="http://vipl.ict.ac.cn/people/xlchen/" title="Homepage"><i class="fa-solid fa-house"></i> Homepage</a>
    </div>
  </div>
</div>

---

## Past Talks

<div class="talk-item">
  <img class="talk-image" src="../assets/img/talks/disheng_liu.jpg" alt="Disheng Liu"/>
  <div class="talk-content">
    <h3 class="talk-title">Spatial Intelligence in Vision-Language Models: What It Is, What Works, and What's Next</h3>
    <p class="talk-speaker">Disheng Liu, Ph.D. Candidate</p>
    <p class="talk-affiliation">Case Western Reserve University</p>
    <p class="talk-date"><i class="fa-regular fa-calendar"></i> December 30, 2025, 11:00-12:00</p>
    <p class="talk-meta"><i class="fa-solid fa-location-dot"></i> Tencent Meeting 682-127-813</p>
    <p class="talk-meta"><i class="fa-solid fa-user"></i> Host: Huan Wang</p>
    <p class="talk-abstract">
      Vision-Language Models (VLMs) have achieved remarkable success but exhibit a fundamental deficiency in spatial intelligence, a critical capability for progress in embodied AI, autonomous driving, and spatially coherent generation. This talk provides a systematic review that spans the foundations of spatial intelligence in VLMs, root causes of spatial limitations, enhancement methodologies, evaluation protocols, and real-world applications.
    </p>
    <div class="talk-links">
      <a href="https://dishengll.github.io/" title="Homepage"><i class="fa-solid fa-house"></i> Homepage</a>
    </div>
  </div>
</div>

<div class="talk-item">
  <img class="talk-image" src="../assets/img/talks/yi_ma.png" alt="Yi Ma"/>
  <div class="talk-content">
    <h3 class="talk-title">Pursuing the Nature of Intelligence</h3>
    <p class="talk-speaker">Yi Ma, Chair Professor</p>
    <p class="talk-affiliation">School of CDS, Hong Kong University & EECS Department, UC Berkeley</p>
    <p class="talk-date"><i class="fa-regular fa-calendar"></i> October 14, 2025, 15:30-17:00</p>
    <p class="talk-meta"><i class="fa-solid fa-location-dot"></i> E10-201, Yungu Campus</p>
    <p class="talk-meta"><i class="fa-solid fa-user"></i> Host: Huan Wang, Yandong Wen</p>
    <p class="talk-abstract">
      In this talk, we will try to clarify different levels and mechanisms of intelligence from historical, scientific, mathematical, and computational perspective. From the evolution of intelligence in nature, from phylogenetic, to ontogenetic, societal, and to scientific intelligence, we will try to shed light on how to understand the true nature of the seemingly dramatic advancements in the technologies of machine intelligence in the past decade. We achieve this goal by developing a principled mathematical framework to explain deductively the practices of deep learning from the first principle of pursuing low-dimensional distributions.
    </p>
    <div class="talk-links">
      <a href="https://people.eecs.berkeley.edu/~yima/" title="Homepage"><i class="fa-solid fa-house"></i> Homepage</a>
    </div>
  </div>
</div>

<div class="talk-item">
  <img class="talk-image" src="../assets/img/talks/yiyi_liao.png" alt="Yiyi Liao"/>
  <div class="talk-content">
    <h3 class="talk-title">3D Generative Models through the Lens of Coordinate Systems</h3>
    <p class="talk-speaker">Yiyi Liao, Assistant Professor</p>
    <p class="talk-affiliation">Zhejiang University</p>
    <p class="talk-date"><i class="fa-regular fa-calendar"></i> September 4, 2025, 16:00-17:00</p>
    <p class="talk-meta"><i class="fa-solid fa-location-dot"></i> Room E10-215, 2F, Yungu Campus</p>
    <p class="talk-meta"><i class="fa-solid fa-user"></i> Host: Huan Wang</p>
    <p class="talk-abstract">
      3D content offers advantages such as real-time interactivity and plays an important role in AR/VR applications, where both generation and compression are critical for practical use. This talk explores 3D content generation from the perspective of coordinate systems, highlighting the distinctions and applications of absolute, observer, and intrinsic coordinates. We present object generation methods developed in the intrinsic coordinate system and scene generation approaches formulated in the observer coordinate system, providing a structured view of how coordinate choices shape 3D generative modeling.
    </p>
    <div class="talk-links">
      <a href="https://yiyiliao.github.io/" title="Homepage"><i class="fa-solid fa-house"></i> Homepage</a>
    </div>
  </div>
</div>

<div class="talk-item">
  <img class="talk-image" src="../assets/img/talks/ming_hsuan_yang.jpg" alt="Ming-Hsuan Yang"/>
  <div class="talk-content">
    <h3 class="talk-title">Recent Results on Multimodal Foundation Models</h3>
    <p class="talk-speaker">Ming-Hsuan Yang, Professor</p>
    <p class="talk-affiliation">University of California, Merced</p>
    <p class="talk-date"><i class="fa-regular fa-calendar"></i> August 9, 2025, 13:30-14:00</p>
    <p class="talk-meta"><i class="fa-solid fa-user"></i> Host: Huan Wang</p>
    <p class="talk-abstract">
      Recent advances in vision and language models have significantly improved visual understanding and generation tasks. In this talk, I will present our latest research on designing effective tokenizers for transformers and our efforts to adapt frozen large language models for diverse vision tasks. These tasks include visual classification, video-text retrieval, visual captioning, visual question answering, visual grounding, video generation, stylization, outpainting, and video-to-audio conversion. If time permits, I will also discuss our recent findings on learning diffusion models and dynamic 3D vision.
    </p>
    <div class="talk-links">
      <a href="https://faculty.ucmerced.edu/mhyang/" title="Homepage"><i class="fa-solid fa-house"></i> Homepage</a>
    </div>
  </div>
</div>
