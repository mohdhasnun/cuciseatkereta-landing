(() => {
  const track = document.querySelector('#ulasan .testi-grid');
  const controls = document.querySelector('.review-controls');
  if (!track || !controls) return;
  const cards = [...track.querySelectorAll('.testi-card')];
  controls.hidden = false;
  track.setAttribute('tabindex', '0');
  track.setAttribute('aria-label', 'Ulasan pelanggan; tatal kiri atau kanan untuk membaca semua ulasan');
  const move = direction => {
    const gap = Number.parseFloat(getComputedStyle(track).columnGap) || 0;
    const step = cards[0].getBoundingClientRect().width + gap;
    const max = Math.max(0, track.scrollWidth - track.clientWidth);
    let next = track.scrollLeft + direction * step;
    if (next > max + 2) next = 0;
    else if (next < -2) next = max;
    track.scrollTo({left: Math.min(max, Math.max(0, next)), behavior: 'auto'});
  };
  controls.querySelector('[data-review-prev]').addEventListener('click', () => move(-1));
  controls.querySelector('[data-review-next]').addEventListener('click', () => move(1));
  track.addEventListener('keydown', event => {
    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      event.preventDefault();
      move(event.key === 'ArrowLeft' ? -1 : 1);
    }
  });
})();
