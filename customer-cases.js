(() => {
  const root = document.querySelector('[data-case-carousel]');
  if (!root) return;
  const slides = [...root.querySelectorAll('.customer-case')];
  const dots = [...root.querySelectorAll('.case-dot')];
  const status = root.querySelector('[data-case-status]');
  let current = 0;
  // Reserve the tallest story at this width so controls stay in place.
  function sizeSlides() {
    slides.forEach(slide => { slide.style.minHeight = ''; slide.hidden = false; });
    const height = Math.max(...slides.map(slide => slide.getBoundingClientRect().height));
    slides.forEach((slide, i) => { slide.style.minHeight = `${height}px`; slide.hidden = i !== current; });
  }
  function show(index, announce = true) {
    current = (index + slides.length) % slides.length;
    slides.forEach((slide, i) => {
      slide.hidden = i !== current;
      if (i !== current) slide.querySelectorAll('video').forEach(video => video.pause());
    });
    dots.forEach((dot, i) => dot.setAttribute('aria-current', String(i === current)));
    if (announce) status.textContent = `Kes ${current + 1} daripada ${slides.length}: ${slides[current].querySelector('h3').textContent}`;
  }
  root.querySelector('[data-case-prev]').addEventListener('click', () => show(current - 1));
  root.querySelector('[data-case-next]').addEventListener('click', () => show(current + 1));
  dots.forEach((dot, i) => dot.addEventListener('click', () => show(i)));
  root.addEventListener('keydown', event => {
    if (event.target.closest('video,a,input')) return;
    const actions = { ArrowLeft: current - 1, ArrowRight: current + 1, Home: 0, End: slides.length - 1 };
    if (!(event.key in actions)) return;
    event.preventDefault();
    show(actions[event.key]);
  });
  root.querySelectorAll('.case-compare').forEach(compare => {
    const range = compare.querySelector('input[type="range"]');
    const update = () => {
      compare.style.setProperty('--reveal', `${range.value}%`);
      range.setAttribute('aria-valuetext', `${range.value}% gambar sebelum ditunjukkan`);
    };
    range.addEventListener('input', update);
    update();
  });
  const video = root.querySelector('video');
  const play = root.querySelector('.case-play');
  play.addEventListener('click', async () => {
    if (!video.getAttribute('src')) video.src = video.dataset.src;
    video.controls = true;
    play.hidden = true;
    try { await video.play(); video.focus(); }
    catch { play.hidden = false; }
  });
  root.querySelector('.cases-controls').hidden = false;
  show(0, false);
  sizeSlides();
  let resizeFrame;
  window.addEventListener('resize', () => {
    cancelAnimationFrame(resizeFrame);
    resizeFrame = requestAnimationFrame(sizeSlides);
  });
  if (document.fonts) document.fonts.ready.then(sizeSlides);
})();
