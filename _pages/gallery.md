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
    gap: 2rem;
    max-width: 800px;
    margin: 0 auto;
}

.gallery-vertical .gallery-item {
    width: 100%;
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
