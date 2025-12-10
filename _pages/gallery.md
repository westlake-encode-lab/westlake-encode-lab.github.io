---
layout: page
title: Gallery
permalink: /gallery/
description: Photos of ENCODE Lab activities and events.
nav: true
nav_order: 5
---

<style>
.gallery-vertical {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 2rem;
    max-width: 800px;
    margin: 0 auto;
}

.gallery-vertical .gallery-item {
    width: 100%;
}

.gallery-vertical .gallery-item img {
    width: 100%;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-vertical .gallery-item img:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.18);
}
</style>

## Lab Life

<div class="gallery-vertical">
    <div class="gallery-item">
        {% include figure.liquid path="assets/img/gallery/photo1.jpg" title="Photo 1" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="gallery-item">
        {% include figure.liquid path="assets/img/gallery/photo2.jpg" title="Photo 2" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
    <div class="gallery-item">
        {% include figure.liquid path="assets/img/gallery/photo3.jpg" title="Photo 3" class="img-fluid rounded z-depth-1" zoomable=true %}
    </div>
</div>
