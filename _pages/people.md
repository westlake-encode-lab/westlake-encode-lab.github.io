---
layout: page
permalink: /people/
title: People
description:
nav: true
nav_order: 2
---

<!-- 通用样式定义 -->
<style>
.profile-grid {
  display: grid;
  gap: 1.5rem 1rem;
  padding: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

.profile-item {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  text-align: left;
  padding: 0.5rem;
  height: fit-content;
  width: 100%;
  color: var(--global-text-color);
  gap: 0.75rem;
}

.profile-image {
  width: 100px;
  min-width: 100px;
  aspect-ratio: 3/4;
  height: auto;
  object-fit: cover;
  border-radius: 10px;
}

.profile-content {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  flex: 1;
}

.profile-name {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 0.3rem 0;
  color: var(--global-theme-color);
}

.profile-social {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin: 0.3rem 0;
}

.profile-social a {
  color: var(--global-text-color);
}

.profile-social a:hover {
  color: var(--global-theme-color);
}

.profile-description {
  font-size: 0.85rem;
  line-height: 1.4;
  margin: 0.3rem 0 0 0;
  color: var(--global-text-color-light);
}

/* 响应式布局类 */
.grid-1-col { grid-template-columns: repeat(1, 1fr); }
.grid-2-col { grid-template-columns: repeat(2, 1fr); }
.grid-3-col { grid-template-columns: repeat(3, 1fr); }
.grid-4-col { grid-template-columns: repeat(4, 1fr); }

@media (max-width: 992px) {
  .grid-4-col {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 768px) {
  .grid-3-col, .grid-4-col {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .profile-grid {
    grid-template-columns: repeat(1, 1fr) !important;
  }
}

/* 纯文字列表样式 */
.text-list {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0;
  columns: 2;
  column-gap: 2rem;
}

.text-list li {
  padding: 0.35rem 0;
  font-size: 0.95rem;
  break-inside: avoid;
}

.text-list li .dest {
  color: var(--global-text-color-light);
  font-size: 0.85rem;
}

@media (max-width: 576px) {
  .text-list {
    columns: 1;
  }
}
</style>

## Principal Investigator
<div class="profile-grid grid-1-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/huan_wang.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Huan Wang</h3>

      <div class="profile-social">
        <a href="https://huanwang.tech/" title="Homepage"><i class="fa-solid fa-house"></i></a>
        <a href="mailto:wanghuan@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
        <a href="https://scholar.google.com/citations?user=0-On0y4AAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
        <a href="https://github.com/mingsun-tse" title="GitHub"><i class="fa-brands fa-github"></i></a>
        <a href="https://www.linkedin.com/in/huanwangx" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
        <a href="https://twitter.com/huanwangx" title="X"><i class="fa-brands fa-x-twitter"></i></a>
      </div>
      <p class="profile-description">Assistant Professor <br> PhD@NEU, MS&BS@ZJU</p>
    </div>
  </div>
</div>

## Administrative & Postdoc Staff
<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/xinjun_lin.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Xinjun Lin</h3>

      <div class="profile-social">
      <a href="mailto:linxinjun@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
    </div>
    <p class="profile-description">Administrative Assistant <br> MFA@Goldsmiths, BA@CAA</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/ying_li.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Ying Li</h3>

      <div class="profile-social">
      <a href="https://neuraliying.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:liying06@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=jIkHgFAAAAAJ&hl" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
    </div>
    <p class="profile-description">Postdoc Researcher <br> PhD@SJTU, Since Jan 2025</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/simin_xu.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Simin Xu</h3>

      <div class="profile-social">
      <a href="https://simmy-x.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:xusimin@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com.hk/citations?user=-9lGlGwAAAAJ&hl=zh-CN" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/Simmy-X" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Postdoc Researcher <br> PhD@SJTU, Since Feb 2025</p>
    </div>
  </div>
</div>

## PhD Students

<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/kele_shao.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Kele Shao</h3>

      <div class="profile-social">
      <a href="https://cokeshao.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:shaokele@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=f4-ER1kAAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/cokeshao" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2025 - <br> BS@ZJU</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/keda_tao.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Keda Tao</h3>

      <div class="profile-social">
      <a href="https://kd-tao.github.io" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:KD.TAO@outlook.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=ek8xaLUAAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/KD-TAO" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2025 - <br> BS@XDU</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/hesong_wang.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Hesong Wang</h3>

      <div class="profile-social">
      <a href="https://viridisgreen.github.io" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:viridisgreen27@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://github.com/viridisGreen" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2025 - <br> BS@BUPT</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/mingluo_su.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Mingluo Su</h3>

      <div class="profile-social">
      <a href="https://sunshine-0903.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:mingluosu0903@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com.hk/citations?user=OEGnyD8AAAAJ&hl=zh-CN" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/sunshine-0903" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2026 - <br> MS@Beihang <br> BS@NWPU</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/xueyi_chen.png" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Xueyi Chen</h3>

      <div class="profile-social">
      <a href="https://yige24.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:xueyi.chen.2024@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=SfLuBt8AAAAJ" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/YIGE24" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2026 - <br> MS@CUHK <br> BS@FZU</p>
    </div>
  </div>
</div>

## Research Assistants
<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/xin_jin.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Xin Jin</h3>

      <div class="profile-social">
      <a href="https://jinxins.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:jinxin86@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=v3OwxWIAAAAJ&hl=zh-CN" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/JinXins" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">MS&BS@CTBU <br> Since Jun 2025</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/chun_yang.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Chun Yang</h3>

      <div class="profile-social">
      <a href="https://chuny9743.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:yangchun@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?hl=zh-CN&user=D_pszsIAAAAJ" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/chuny9743" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">BS@BIT <br> Since Oct 2025</p>
    </div>
  </div>
</div>

<ul class="text-list">
  <li><strong>Shikang Zhang</strong></li>
  <li><strong>Jinhao Sheng</strong></li>
</ul>

## Visiting Students

<ul class="text-list">
  <li><strong>Youssef Ahmed</strong> <span class="dest">BS@Westlake</span></li>
  <li><strong><a href="https://deadlykitten4.github.io/">Haolei Bai</a></strong> <span class="dest">MS@NTU</span></li>
  <li><strong>Wenrui Bao</strong> <span class="dest">MS@NTU</span></li>
  <li><strong>Zixu Wang</strong></li>
  <li><strong>Yikai Yang</strong> <span class="dest">MS@ZJU</span></li>
  <li><strong><a href="https://pillor9.github.io/">Yuhua Zheng</a></strong> <span class="dest">BS@ZJU</span></li>
  <li><strong>Wenxi Zhu</strong> <span class="dest">BS@Westlake</span></li>
</ul>

## Alumni

<ul class="text-list">
  <li><strong><a href="https://ai-kunkun.github.io/">Zhenxin Ai</a></strong> <span class="dest">BS@JXUST</span></li>
  <li><strong>Rongfu Bai</strong> <span class="dest">BS@XJTU</span></li>
  <li><strong><a href="https://kurt232.github.io/">Wenjie Du</a></strong> <span class="dest">BS@SCU → MS@NTU</span></li>
  <li><strong><a href="https://fscdc.github.io/">Sicheng Feng</a></strong> <span class="dest">BS@NKU → PhD@NUS</span></li>
  <li><strong><a href="https://syjmelody.github.io/">Siyong Jian</a></strong> <span class="dest">MS@NJU</span></li>
  <li><strong><a href="https://www.linkedin.com/in/lingcheng-kong-443624303">Lingcheng Kong</a></strong> <span class="dest">BS@HKUST</span></li>
  <li><strong><a href="https://hp-l33.github.io/">Haopeng Li</a></strong> <span class="dest">BS@BUPT → MS@HKUST(GZ)</span></li>
  <li><strong><a href="https://boyaliao.github.io/">Boya Liao</a></strong> <span class="dest">MS@ZJU → PhD@UMN</span></li>
  <li><strong><a href="https://ddsacu.github.io/">Zhizhen Pan</a></strong> <span class="dest">BS@BUPT</span></li>
  <li><strong><a href="https://xuan9-9.github.io/">Jiaxuan Ren</a></strong> <span class="dest">BS@UESTC</span></li>
  <li><strong><a href="https://hanzhangshen03.github.io">Hanzhang Shen</a></strong> <span class="dest">BS@Cambridge</span></li>
  <li><strong>Haoyu Shen</strong></li>
  <li><strong><a href="https://zhenyusun-walker.github.io/">Zhenyu Sun</a></strong> <span class="dest">BS@SCUT → PhD@SJTU</span></li>
  <li><strong><a href="https://cfintech.github.io/">Kaiwen Tuo</a></strong> <span class="dest">BS@Tongji → PhD@HKUST</span></li>
  <li><strong><a href="https://aden9460.github.io/Zefang-Wang/">Zefang Wang</a></strong> <span class="dest">MS@ZJU</span></li>
  <li><strong>Qitong Wang</strong></li>
  <li><strong>Fan Wu</strong></li>
  <li><strong><a href="https://xianzuwu.github.io/">Xianzu Wu</a></strong></li>
  <li><strong><a href="https://jiaxu0123.github.io/jiaxu/">Jia Xu</a></strong> <span class="dest">BS@BIT</span></li>
  <li><strong><a href="https://wiserzhou.github.io">Yufan Zhou</a></strong> <span class="dest">BS@HIT</span></li>
  <li><strong><a href="https://alrightlone.github.io/">Junhan Zhu</a></strong> <span class="dest">BS@Westlake</span></li>
  <li><strong><a href="https://wuyulunbizhouojielun.github.io/">Huixing Zhu</a></strong> <span class="dest">BS@ZJU → MS@ZJU</span></li>
</ul>
