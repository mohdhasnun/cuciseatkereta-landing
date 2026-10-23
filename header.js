(() => {
  const header = document.querySelector('.site-header');
  const toggle = header.querySelector('.header-toggle');
  const links = header.querySelector('.nav-links');
  const compact = matchMedia('(max-width:1100px)');
  links.id = 'header-links';
  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Tutup menu' : 'Buka menu');
    toggle.title = open ? 'Tutup menu' : 'Buka menu';
    toggle.firstElementChild.textContent = open ? '\u00d7' : '\u2630';
    links.classList.toggle('is-open', open);
  };
  header.classList.add('menu-ready');
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  links.addEventListener('click', (event) => {
    if (compact.matches && event.target.closest('a')) {
      setOpen(false);
      toggle.focus({ preventScroll: true });
    }
  });
  header.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  compact.addEventListener('change', () => setOpen(false));
})();
