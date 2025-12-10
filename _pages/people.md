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
      <p class="profile-description">Assistant Professor <br> PhD NEU, MS & BS ZJU</p>
    </div>
  </div>
</div>

## Administrative & Research Staff
<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/xinjun_lin.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Xinjun Lin</h3>

      <div class="profile-social">
      <a href="mailto:linxinjun@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://instagram.com/sangwanlam7" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
    </div>
    <p class="profile-description">Administrative Assistant <br> MFA Goldsmiths, BA CAA <br> CSC Scholar 2022</p>
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
    <p class="profile-description">Postdoc Researcher <br> PhD SJTU <br> Since Jan 2025</p>
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
    <p class="profile-description">Postdoc Researcher <br> PhD SJTU <br> Since Feb 2025</p>
    </div>
  </div>
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
    <p class="profile-description">Research Assistant <br> MS CTBU, BS CTBU <br> Since Jun 2025</p>
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
    <p class="profile-description">Research Assistant <br> BE BIT <br> Since Oct 2025</p>
    </div>
  </div>
</div>

[//]: # (按照加入时间顺序排序)

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
    <p class="profile-description">Fall 2025 - <br> BS ZJU</p>
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
    <p class="profile-description">Fall 2025 - <br> BS XDU</p>
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
    <p class="profile-description">Fall 2025 - <br> BS BUPT</p>
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
    <p class="profile-description">Fall 2026 - <br> MS Beihang, BS NWPU</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/xueyi_chen.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Xueyi Chen</h3>

      <div class="profile-social">
      <a href="https://yige24.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:xueyi.chen.2024@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=SfLuBt8AAAAJ" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/YIGE24" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2026 - <br> MS CUHK, BS FZU</p>
    </div>
  </div>
</div>

## Visiting Students
<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/haolei_bai.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Haolei Bai</h3>

      <div class="profile-social">
      <a href="https://deadlykitten4.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:baih12264@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=CGh99DUAAAAJ&hl=zh-CN" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/deadlykitten4" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">MS NTU <br> Since Jan 2025</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/zefang_wang.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Zefang Wang</h3>

      <div class="profile-social">
      <a href="https://aden9460.github.io/Zefang-Wang/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:wangzefang@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=95e7tCgAAAAJ&hl=zh-CN&authuser=2" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/aden9460" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">MS ZJU <br> Since Mar 2025</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/siyong_jian.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Siyong Jian</h3>

      <div class="profile-social">
      <a href="https://syjmelody.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:syjian5@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://github.com/syjmelody" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">MS NJU <br> Since Feb 2025</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/wenjie_du.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Wenjie Du</h3>

      <div class="profile-social">
      <a href="https://kurt232.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:duwenjie@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?hl=en&user=ZxqE25EAAAAJ" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/kurt232" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">BS SCU <br> Since Jul 2025</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/boya_liao.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Boya Liao</h3>

      <div class="profile-social">
      <a href="https://boyaliao.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:bursonliao@gmail.com" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?user=xdWZc2YAAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/BoyaLiao" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">MS ZJU <br> Since Jul 2025</p>
    </div>
  </div>
</div>

## Undergraduate Students

<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/junhan_zhu.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Junhan Zhu</h3>

      <div class="profile-social">
      <a href="https://alrightlone.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:zhujunhan@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://scholar.google.com/citations?hl=en&user=kWEQRU0AAAAJ" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
      <a href="https://github.com/Alrightlone" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2023 - <br> EIE</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/zhenyu_xv.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Zhenyu Xu</h3>

      <div class="profile-social">
      <a href="https://xzy8806-beep.github.io/zhenyuxu/" title="Homepage"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:xuzhenyu@westlake.edu.cn" title="email"><i class="fa-solid fa-envelope"></i></a>
      <a href="https://github.com/xzy8806-beep/zhenyuxu" title="GitHub"><i class="fa-brands fa-github"></i></a>
    </div>
    <p class="profile-description">Fall 2025 - <br> AI</p>
    </div>
  </div>
</div>

## Alumni
<div class="profile-grid grid-3-col">
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/hanzhang_shen.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Hanzhang Shen</h3>

      <div class="profile-social">
      <a href="https://hanzhangshen03.github.io" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS Cambridge <br> SWE Intern at Meta</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/kejia_zhang.png" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Kejia Zhang</h3>

      <div class="profile-social">
      <a href="https://kejiazhang-robust.github.io/homepage" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">MS Xiamen Univ</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/lingcheng_kong.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Lingcheng Kong</h3>

      <div class="profile-social">
      <a href="https://www.linkedin.com/in/lingcheng-kong-443624303" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
    </div>
    <p class="profile-description">BS HKUST</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/rongfu_bai.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Rongfu Bai</h3>

      <div class="profile-social">
      <a href="https://www.linkedin.com/in/brf7" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
    </div>
    <p class="profile-description">BS XJTU</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/yufan_zhou.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Yufan Zhou</h3>

      <div class="profile-social">
      <a href="https://wiserzhou.github.io" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS HIT</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/zhenyu_sun.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Zhenyu Sun</h3>

      <div class="profile-social">
      <a href="https://zhenyusun-walker.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS SCUT</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/sicheng_feng.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Sicheng Feng</h3>

      <div class="profile-social">
      <a href="https://fscdc.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS NKU</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/zhenxin_ai.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Zhenxin Ai</h3>

      <div class="profile-social">
      <a href="https://ai-kunkun.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS JXUST</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/kaiwen_tuo.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Kaiwen Tuo</h3>

      <div class="profile-social">
      <a href="https://cfintech.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS Tongji</p>
    </div>
  </div>
  <div class="profile-item">
    <img class="profile-image" src="../assets/img/people/jiaxuan_ren.jpg" alt="Profile"/>
    <div class="profile-content">

      <h3 class="profile-name">Jiaxuan Ren</h3>

      <div class="profile-social">
      <a href="https://xuan9-9.github.io/" title="Homepage"><i class="fa-solid fa-house"></i></a>
    </div>
    <p class="profile-description">BS UESTC</p>
    </div>
  </div>
</div>

### Others

- **[Huixing Zhu](https://wuyulunbizhouojielun.github.io/)**: BS ZJU
- **[Qitong Wang](https://wang-qitong.github.io/)**: BS TJUT
- **Haoyu Shen**
- **Xianzu Wu**
- **Fan Wu**
