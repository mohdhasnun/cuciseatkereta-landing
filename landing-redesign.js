(() => {
  const track = document.querySelector('#ulasan .testi-grid');
  const controls = document.querySelector('.review-controls');
  if (!track || !controls) return;
  const cards = [...track.querySelectorAll('.testi-card')];
  controls.hidden = false;
  track.setAttribute('tabindex', '0');
  track.setAttribute('aria-label', 'Ulasan pelanggan; tatal kiri atau kanan untuk membaca semua ulasan');
  const move = direction => {
    const step = cards[0].getBoundingClientRect().width + 12;
    const current = Math.round(track.scrollLeft / step);
    const next = (current + direction + cards.length) % cards.length;
    track.scrollTo({left: next * step, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
  };
  controls.querySelector('[data-review-prev]').addEventListener('click', () => move(-1));
  controls.querySelector('[data-review-next]').addEventListener('click', () => move(1));
})();
