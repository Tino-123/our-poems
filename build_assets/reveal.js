// Staged reveal for the newest poem card.
// Up to three stages fade in one after another, each after its own delay
// (in milliseconds) counted from page load:
//   1) banner   (e.g. "HAPPY BIRTHDAY") -- only if the poem has one
//   2) title    (the h2 + date)
//   3) body     (the full poem text + photos, all together -- nothing
//                further is staged after this point)

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".reveal-card").forEach((card) => {
    const delays = {
      banner: parseInt(card.dataset.delayBanner || "0", 10),
      title: parseInt(card.dataset.delayTitle || "0", 10),
      body: parseInt(card.dataset.delayBody || "0", 10),
    };

    card.querySelectorAll(".reveal-stage").forEach((el) => {
      const stage = el.dataset.stage;
      const delay = delays[stage] ?? 0;
      setTimeout(() => el.classList.add("visible"), delay);
    });
  });
});
