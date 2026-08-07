// Staged reveal for the newest poem card.
// Up to four stages fade in one after another, each after its own delay
// (in milliseconds) counted from page load:
//   1) banner  (e.g. "HAPPY BIRTHDAY") -- only if the poem has one
//   2) title   (the h2 + date)
//   3) first   (the first paragraph of the poem)
//   4) rest    (everything else + photos, all together -- nothing
//               further is staged after this point)

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".reveal-card").forEach((card) => {
    const delays = {
      banner: parseInt(card.dataset.delayBanner || "0", 10),
      title: parseInt(card.dataset.delayTitle || "0", 10),
      first: parseInt(card.dataset.delayFirst || "0", 10),
      rest: parseInt(card.dataset.delayRest || "0", 10),
    };

    card.querySelectorAll(".reveal-stage").forEach((el) => {
      const stage = el.dataset.stage;
      const delay = delays[stage] ?? 0;
      setTimeout(() => el.classList.add("visible"), delay);
    });
  });
});
