"use strict";

initializeTheme();
initializeSearch();
initializeDialogs();
initializePublicationFilters();
initializeGallery();

function initializeTheme() {
  const documentRoot = document.documentElement;
  const themeButton = document.querySelector("#theme");

  function applyTheme(value) {
    const dark = value === "dark";
    documentRoot.dataset.theme = dark ? "dark" : "light";
    themeButton.title = dark ? "Use light theme" : "Use dark theme";
    themeButton.setAttribute("aria-label", themeButton.title);
  }

  applyTheme(documentRoot.dataset.theme);
  themeButton.addEventListener("click", () => {
    const choice = documentRoot.dataset.theme === "dark" ? "light" : "dark";
    try {
      localStorage.setItem("theme", choice);
    } catch (error) {
      if (error.name !== "SecurityError" && error.name !== "QuotaExceededError") {
        throw error;
      }
      console.warn("Theme preference could not be saved. Applying it to this page.", error);
    }
    applyTheme(choice);
  });
  document.querySelector(".tools").hidden = false;
}

function initializeSearch() {
  const searchDialog = document.querySelector("#site-search");
  const searchInput = document.querySelector("#search-query");
  const searchResults = document.querySelector("#search-results");

  function renderResults() {
    const terms = searchInput.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    const matches = window.labSearch.filter((record) => {
      if (!terms.length) {
        return record.kind === "Page";
      }
      const text = [record.kind, record.title, record.keywords].join(" ").toLowerCase();
      return terms.every((term) => text.includes(term));
    });
    searchResults.replaceChildren();
    for (const record of matches) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = /^(?:https:\/\/|mailto:)/.test(record.url)
        ? record.url
        : document.documentElement.dataset.root + record.url;
      const kind = document.createElement("small");
      kind.textContent = record.kind;
      link.append(kind, record.title);
      item.append(link);
      searchResults.append(item);
    }
    const message = matches.length ? `${matches.length} results` : "No matching results.";
    document.querySelector("#search-status").textContent = message;
    if (!matches.length) {
      searchResults.textContent = message;
    }
  }

  function openSearch() {
    if (document.querySelector("dialog[open]")) {
      return;
    }
    searchInput.value = "";
    renderResults();
    searchDialog.showModal();
    searchInput.focus();
  }

  document.querySelector("#search-open").addEventListener("click", openSearch);
  searchInput.addEventListener("input", renderResults);
  searchResults.addEventListener("click", (event) => {
    if (event.target.closest("a")) {
      searchDialog.close();
    }
  });
  document.addEventListener("keydown", (event) => {
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openSearch();
    }
  });
}

function initializeDialogs() {
  for (const dialog of document.querySelectorAll("dialog")) {
    dialog.querySelector("[data-close]").addEventListener("click", () => dialog.close());
    dialog.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !event.isComposing) {
        event.preventDefault();
        dialog.close();
      }
    });
    dialog.addEventListener("click", (event) => {
      const bounds = dialog.getBoundingClientRect();
      const outside =
        event.clientX < bounds.left ||
        event.clientX > bounds.right ||
        event.clientY < bounds.top ||
        event.clientY > bounds.bottom;
      if (event.target === dialog && outside) {
        dialog.close();
      }
    });
  }
}

function initializePublicationFilters() {
  const controls = document.querySelector(".pub-controls");
  if (!controls) {
    return;
  }
  controls.hidden = false;
  const searchInput = controls.querySelector("#filter");
  const collectionInput = controls.querySelector("#collection");
  const yearInput = controls.querySelector("#pub-year");
  if (new URLSearchParams(location.search).get("view") === "selected") {
    collectionInput.value = "selected";
  }
  const rows = [...document.querySelectorAll(".paper")].map((paper) => ({
    paper,
    text: ["h3", ".authors", ".venue", ".venue-name"]
      .map((selector) => paper.querySelector(selector).textContent)
      .join(" ")
      .toLowerCase(),
  }));

  function filterPapers() {
    const terms = searchInput.value.trim().toLowerCase().split(/\s+/);
    let count = 0;
    for (const { paper, text } of rows) {
      const matchesText = terms.every((term) => text.includes(term));
      const matchesYear = yearInput.value === "all" || paper.dataset.year === yearInput.value;
      const matchesCollection = collectionInput.value !== "selected" || paper.dataset.selected === "1";
      paper.hidden = !(matchesText && matchesYear && matchesCollection);
      if (!paper.hidden) {
        count++;
      }
    }
    document.querySelector("#pub-count").textContent = `${count} ${count === 1 ? "publication" : "publications"}`;
    document.querySelector("#no-papers").hidden = count > 0;
    for (const group of document.querySelectorAll(".year-group")) {
      group.hidden = !group.querySelector(".paper:not([hidden])");
    }
  }

  function resetFilters() {
    searchInput.value = "";
    collectionInput.value = "all";
    yearInput.value = "all";
    filterPapers();
  }

  function revealLinkedPaper() {
    const paper = document.getElementById(location.hash.slice(1));
    if (!paper?.classList.contains("paper") || !paper.hidden) {
      return;
    }
    resetFilters();
    paper.scrollIntoView({ block: "start" });
  }

  for (const input of [searchInput, collectionInput, yearInput]) {
    input.addEventListener("input", filterPapers);
  }
  controls.querySelector("#reset-filters").addEventListener("click", () => {
    resetFilters();
    searchInput.focus();
  });
  filterPapers();
  revealLinkedPaper();
  window.addEventListener("hashchange", revealLinkedPaper);
  document.querySelector("#search-results").addEventListener("click", (event) => {
    if (event.target.closest("a")?.href === location.href) {
      revealLinkedPaper();
    }
  });
}

function initializeGallery() {
  const lightbox = document.querySelector("#lightbox");
  const photos = [...document.querySelectorAll("[data-photo]")];
  if (!lightbox || !photos.length) {
    return;
  }
  const counter = document.querySelector("#photo-count");
  const originalLink = document.querySelector("#photo-original");
  const previousButton = document.querySelector("#previous");
  const nextButton = document.querySelector("#next");
  let currentIndex = 0;

  function showPhoto(index) {
    currentIndex = (index + photos.length) % photos.length;
    const photo = photos[currentIndex];
    const image = lightbox.querySelector("img");
    image.src = photo.href;
    image.alt = photo.querySelector("img").alt;
    document.querySelector("#photo-title").textContent = image.alt;
    counter.textContent = `${currentIndex + 1} / ${photos.length}`;
    counter.setAttribute("aria-label", `Photo ${currentIndex + 1} of ${photos.length}`);
    originalLink.href = photo.href;
  }

  photos.forEach((photo, index) => {
    photo.setAttribute("aria-haspopup", "dialog");
    photo.addEventListener("click", (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
        return;
      }
      event.preventDefault();
      showPhoto(index);
      lightbox.showModal();
    });
  });
  previousButton.disabled = photos.length < 2;
  nextButton.disabled = photos.length < 2;
  previousButton.addEventListener("click", () => showPhoto(currentIndex - 1));
  nextButton.addEventListener("click", () => showPhoto(currentIndex + 1));
  lightbox.addEventListener("keydown", (event) => {
    if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") {
      return;
    }
    event.preventDefault();
    showPhoto(currentIndex + (event.key === "ArrowLeft" ? -1 : 1));
  });
}
