---
layout: page
title: Gallery
permalink: /gallery/
description: Photos of ENCODE Lab activities and events.
nav: true
nav_order: 6
---

<style>
  .gallery-vertical {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.75rem;
    max-width: 820px;
    margin: 1rem auto 0;
  }

  .gallery-vertical .gallery-item {
    width: 100%;
  }

  /* Softer rounding, layered shadow, and a gentle lift on hover. */
  .gallery-vertical .gallery-item img {
    width: 100%;
    border-radius: 14px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }

  .gallery-vertical .gallery-item img:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.2);
  }
</style>

## Lab Life

{%- comment -%} Auto-discover every image in assets/img/gallery/ — drop a photo in the folder and it shows up here, no edits needed. The .webp filter skips imagemagick's generated responsive variants. {%- endcomment -%}
{% assign gallery_photos = site.static_files | where_exp: "f", "f.path contains '/assets/img/gallery/' and f.extname != '.webp'" | sort: "path" %}

<div class="gallery-vertical">
  {% for photo in gallery_photos %}
    {% assign photo_path = photo.path | remove_first: "/" %}
    <div class="gallery-item">
      {% include figure.liquid path=photo_path class="img-fluid" zoomable=true %}
    </div>
  {% endfor %}
</div>
