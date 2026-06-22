---
layout: about
title: Home
permalink: /
subtitle:

profile:
  align: right
  image: lab.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <center>ENCODE Lab Family</center>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

**About Us:** <br>
The <span style="color: var(--global-theme-color); font-weight: 500">ENCODE Lab</span> (**E**fficient **N**eural **CO**mputing and **DE**sign) is led by Dr. [Huan Wang](https://huanwang.tech/), a Tenure-Track Assistant Professor in the School of Engineering at [Westlake University](https://en.westlake.edu.cn/faculty/huan-wang.html). We focus on building efficient and reliable AI systems that are scalable and self-improving, driving both theoretical innovation and practical impact.

**Research Focus:** <br>
Our research centers on **Efficient AI**, **Multimodal AI**, and **Generative AI**.

**Join Us:** <br>
We are actively recruiting **Ph.D. students**, **Research Assistants**, **Visiting Students**, and **Postdocs**. Please read the [Admission Guide](/assets/pdf/admission.pdf){:target="_blank"} for openings and how to apply, and email us at [encodelab@westlake.edu.cn](mailto:encodelab@westlake.edu.cn).

<style>
  .sponsors {
    margin: 2.5rem 0 0.5rem;
    text-align: center;
  }
  .sponsors-title {
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--global-text-color-light);
    margin-bottom: 1.1rem;
  }
  .sponsors-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 1rem 1.25rem;
    margin-bottom: 1.1rem;
  }
  .sponsors-row:last-child {
    margin-bottom: 0;
  }
  /* White card behind each logo so it stays readable in both light and dark mode. */
  .sponsor-item {
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fff;
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 10px;
    padding: 0.55rem 1.1rem;
    box-shadow: var(--card-shadow);
    transition: var(--card-transition);
  }
  .sponsor-item:hover {
    transform: var(--card-lift);
    box-shadow: var(--card-shadow-hover);
  }
  .sponsor-item img {
    height: 38px;
    width: auto;
    max-width: 180px;
    object-fit: contain;
    display: block;
  }
  @media (max-width: 576px) {
    .sponsor-item img {
      height: 30px;
      max-width: 135px;
    }
  }
</style>

<div class="sponsors">
  <p class="sponsors-title">Funding &amp; Sponsors</p>
  <div class="sponsors-row">
    <a class="sponsor-item" href="https://www.nsfc.gov.cn/" target="_blank" rel="noopener" title="国家自然科学基金委员会">
      <img src="/assets/img/sponsors/nsfc.png" alt="National Natural Science Foundation of China" />
    </a>
    <a class="sponsor-item" href="https://kjt.zj.gov.cn/" target="_blank" rel="noopener" title="浙江省科学技术厅">
      <img src="/assets/img/sponsors/zjst.png" alt="Zhejiang Provincial Department of Science and Technology" />
    </a>
    <a class="sponsor-item" href="https://www.caai.cn/" target="_blank" rel="noopener" title="中国人工智能学会">
      <img src="/assets/img/sponsors/caai.png" alt="Chinese Association for Artificial Intelligence" />
    </a>
  </div>
  <div class="sponsors-row">
    <a class="sponsor-item" href="https://www.antgroup.com/" target="_blank" rel="noopener" title="蚂蚁集团">
      <img src="/assets/img/sponsors/ant.png" alt="Ant Group" />
    </a>
    <a class="sponsor-item" href="https://www.alibabacloud.com/" target="_blank" rel="noopener" title="阿里云">
      <img src="/assets/img/sponsors/alicloud.png" alt="Alibaba Cloud" />
    </a>
  </div>
</div>