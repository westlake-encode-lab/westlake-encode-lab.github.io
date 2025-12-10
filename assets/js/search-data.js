// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-people",
          title: "People",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/people/";
          },
        },{id: "nav-gallery",
          title: "Gallery",
          description: "Photos of ENCODE Lab activities and events.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/gallery/";
          },
        },{id: "news-new-start-our-lab-is-established-prof-huan-wang-joins-westlake-university-as-a-tenure-track-assistant-professor",
          title: '[New Start] Our lab is established! Prof. Huan Wang joins Westlake University as...',
          description: "",
          section: "News",},{id: "news-eccv-39-24-our-paper-on-efficient-video-sci-snapshot-compressive-imaging-via-network-quantization-has-been-accepted-to-eccv-24-as-an-oral-presentation-congrats-to-miao-arxiv-code",
          title: '[ECCV&amp;#39;24] Our paper on efficient video SCI (Snapshot Compressive Imaging) via network quantization...',
          description: "",
          section: "News",},{id: "news-mm-39-24-we-present-the-first-real-time-on-device-video-sci-snapshot-compressive-imaging-framework-through-dedicated-network-design-and-distillation-based-training-congrats-to-miao-arxiv-code",
          title: '[MM&amp;#39;24] We present the first real-time, on-device video SCI (Snapshot Compressive Imaging) framework...',
          description: "",
          section: "News",},{id: "news-cvpr-39-25-dycoke-has-been-accepted-to-cvpr-25-congrats-to-keda-dycoke-is-a-training-free-plug-and-play-token-compression-method-for-fast-video-llms-achieving-1-5x-inference-speedup-and-1-4x-memory-reduction-with-no-performance-loss-arxiv-code",
          title: '[CVPR&amp;#39;25] DyCoke has been accepted to CVPR’25! Congrats to Keda! DyCoke is a...',
          description: "",
          section: "News",},{id: "news-iccv-39-25-our-paper-on-efficient-robot-manipulation-has-been-accepted-to-iccv-25-congrats-to-yiming-arxiv",
          title: '[ICCV&amp;#39;25] Our paper on efficient robot manipulation has been accepted to ICCV’25. Congrats...',
          description: "",
          section: "News",},{id: "news-award-congrats-to-our-phd-student-keda-tao-on-receiving-the-2025-westlake-university-xinrui-award-西湖大学博士研究生新锐奖-only-2-recipients-in-ai-among-all-the-2025-fall-phd-students-in-school-of-engineering",
          title: '[Award] Congrats to our PhD student Keda Tao on receiving the “2025 Westlake...',
          description: "",
          section: "News",},{id: "news-mm-39-25-our-paper-on-efficient-video-diffusion-models-via-network-pruning-has-been-accepted-to-mm-25-congrats-to-yiming-arxiv",
          title: '[MM&amp;#39;25] Our paper on efficient video diffusion models via network pruning has been...',
          description: "",
          section: "News",},{id: "news-preprint-we-are-excited-to-present-the-first-systematic-survey-on-multimodal-long-context-token-compression-methods-arxiv-code",
          title: '[Preprint] We are excited to present the first systematic survey on multimodal long-context...',
          description: "",
          section: "News",},{id: "news-services-prof-huan-wang-will-serve-as-an-area-chair-for-aaai-2026-iclr-2026-and-cvpr-2026",
          title: '[Services] Prof. Huan Wang will serve as an Area Chair for AAAI 2026,...',
          description: "",
          section: "News",},{id: "news-neurips-39-25-four-papers-accepted-to-neurips-2025-in-the-field-of-efficient-and-reliable-ai-congrats-to-our-students-and-collaborators-three-papers-from-our-lab-holitom-a-top-performing-video-llm-token-compression-method-that-maintains-99-1-performance-while-reducing-flops-to-just-6-9-and-it-s-training-free-arxiv-code-webpage-poison-as-cure-is-adversarial-visual-noise-always-harmful-like-poison-we-show-it-can-actually-cure-the-hallucination-problem-in-vlms-arxiv-code-webpage-freqexit-a-dynamic-inference-framework-for-visual-autoregressive-var-models-via-early-exit-with-novel-frequency-aware-guidance-openreview-code-webpage",
          title: '[NeurIPS&amp;#39;25] Four papers accepted to NeurIPS 2025 in the field of efficient and...',
          description: "",
          section: "News",},{id: "news-preprint-obs-diff-the-first-paper-led-by-a-westlake-undergraduate-in-our-lab-junhan-zhu-class-of-2023-led-this-work-on-one-shot-pruning-for-diffusion-models-congrats-arxiv",
          title: '[Preprint] OBS-Diff: The first paper led by a Westlake undergraduate in our lab!...',
          description: "",
          section: "News",},{id: "news-funds-we-received-a-research-grant-from-caai-ant-group-caai-蚂蚁科研基金-thank-you-caai-and-ant-group",
          title: '[Funds] We received a research grant from CAAI-Ant Group (CAAI-蚂蚁科研基金). Thank you, CAAI...',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%77%61%6E%67%68%75%61%6E@%77%65%73%74%6C%61%6B%65.%65%64%75.%63%6E", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/westlake-encode-lab", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
