(() => {
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.getElementById('primary-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      menu.classList.toggle('is-open', !expanded);
    });
  }

  const search = document.getElementById('speaker-search');
  const cards = [...document.querySelectorAll('[data-speaker-card]')];
  const status = document.getElementById('speaker-count');
  if (search && cards.length && status) {
    const update = () => {
      const query = search.value.trim().toLocaleLowerCase();
      let shown = 0;
      cards.forEach(card => {
        const match = !query || card.textContent.toLocaleLowerCase().includes(query);
        card.hidden = !match;
        if (match) shown += 1;
      });
      status.textContent = query ? `${shown} speaker${shown === 1 ? '' : 's'} match your search.` : `${cards.length} speakers listed.`;
    };
    search.addEventListener('input', update);
    update();
  }
})();
