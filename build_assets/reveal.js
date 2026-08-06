// Staged reveal for the newest poem card.
// The title and date show immediately (they're plain HTML, not staged).
// Elements marked .reveal-stage fade in one at a time, after the delay
// (in milliseconds) set on the card via data-first-delay / data-rest-delay.

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".reveal-card").forEach((card) => {
    const firstDelay = parseInt(card.dataset.firstDelay || "2500", 10);
    const restDelay = parseInt(card.dataset.restDelay || "6000", 10);

    const firstStage = card.querySelector('[data-stage="first"]');
    const restStage = card.querySelector('[data-stage="rest"]');

    if (firstStage) {
      setTimeout(() => firstStage.classList.add("visible"), firstDelay);
    }
    if (restStage) {
      setTimeout(() => restStage.classList.add("visible"), restDelay);
    }
  });
});
