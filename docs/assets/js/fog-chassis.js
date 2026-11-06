/* SF Fog RFC — shared chassis behaviour: rotating background + Progress Pride chapter menu.
   Extracted from docs/index.html sections 1–2. */
(function () {
      // 1. AUTO-ROTATING RANDOM BACKGROUND IMAGE POOL
      const bgPool = [
        'assets/img/panels/fog-waiver-1-welcome.jpg',
        'assets/img/panels/fog-waiver-2-contact.jpg',
        'assets/img/panels/fog-waiver-3-waiver.jpg',
        'assets/img/panels/fog-waiver-4-sign.jpg',
        'assets/img/panels/old-picks/fog-waiver-welcome.jpg',
        'assets/img/panels/old-picks/fog-waiver-contact.jpg',
        'assets/img/panels/old-picks/fog-waiver-waiver.jpg',
        'assets/img/panels/old-picks/fog-waiver-sign.jpg'
      ];

      const layerA = document.getElementById('fog-bg-a');
      const layerB = document.getElementById('fog-bg-b');
      let activeLayer = 'a';
      let poolIndex = Math.floor(Math.random() * bgPool.length);

      bgPool.forEach(function(src) {
        const img = new Image();
        img.src = src;
      });

      function crossfadeNext() {
        poolIndex = (poolIndex + 1) % bgPool.length;
        const nextSrc = bgPool[poolIndex];

        if (activeLayer === 'a') {
          layerB.style.backgroundImage = 'url("' + nextSrc + '")';
          layerB.classList.add('active');
          layerA.classList.remove('active');
          activeLayer = 'b';
        } else {
          layerA.style.backgroundImage = 'url("' + nextSrc + '")';
          layerA.classList.add('active');
          layerB.classList.remove('active');
          activeLayer = 'a';
        }
      }

      if (layerA) {
        layerA.style.backgroundImage = 'url("' + bgPool[poolIndex] + '")';
      }

      const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (!prefersReducedMotion) {
        setInterval(crossfadeNext, 7000);
      }

      // 2. DRUPAL PROGRESS PRIDE CHAPTER MENU (fog-pride-menu)
      const stripContainer = document.querySelector('[data-component="fog-pride-menu"]');
      const siteHeader = document.getElementById('site-header');
      const stripToggle = document.getElementById('progress-strip-toggle');
      const stripDrawer = document.getElementById('pride-chapter-drawer');
      const stripBackdrop = document.getElementById('pride-backdrop');
      const drawerClose = document.getElementById('pride-drawer-close');
      const segButtons = stripContainer ? Array.from(stripContainer.querySelectorAll('.fog-window-progress-strip__seg')) : [];

      function syncDrawerTop() {
        if (!stripDrawer || !siteHeader) return;
        const bottom = Math.round(siteHeader.getBoundingClientRect().bottom);
        stripDrawer.style.top = bottom + 'px';
        stripDrawer.style.maxHeight = 'calc(100vh - ' + (bottom + 12) + 'px)';
      }

      function togglePrideDrawer(open) {
        if (!stripDrawer || !stripToggle) return;
        const isCurrentlyOpen = !stripDrawer.hidden;
        const shouldOpen = open !== undefined ? open : !isCurrentlyOpen;
        if (shouldOpen) syncDrawerTop();
        stripDrawer.hidden = !shouldOpen;
        if (stripBackdrop) stripBackdrop.hidden = !shouldOpen;
        stripToggle.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
        segButtons.forEach(function(btn) {
          btn.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
        });
      }

      window.addEventListener('resize', function() {
        if (stripDrawer && !stripDrawer.hidden) syncDrawerTop();
      });

      if (stripToggle) {
        stripToggle.addEventListener('click', function(e) {
          e.stopPropagation();
          togglePrideDrawer();
        });
      }

      if (drawerClose) {
        drawerClose.addEventListener('click', function(e) {
          e.stopPropagation();
          togglePrideDrawer(false);
          if (stripToggle) stripToggle.focus();
        });
      }

      if (stripBackdrop) {
        stripBackdrop.addEventListener('click', function() {
          togglePrideDrawer(false);
        });
      }

      segButtons.forEach(function(seg) {
        seg.addEventListener('click', function(e) {
          e.stopPropagation();
          const chapter = seg.getAttribute('data-chapter');
          togglePrideDrawer(true);
          const card = document.querySelector('[data-chapter-target="' + chapter + '"]');
          if (card) {
            card.scrollIntoView({ behavior: prefersReducedMotion ? 'auto' : 'smooth', block: 'nearest' });
            card.style.outline = '2px solid #24A0F1';
            setTimeout(function() {
              card.style.outline = 'none';
            }, 2000);
          }
        });
      });

      document.addEventListener('click', function(e) {
        if (stripDrawer && !stripDrawer.hidden && !stripDrawer.contains(e.target) && e.target !== stripToggle && (!stripToggle || !stripToggle.contains(e.target))) {
          togglePrideDrawer(false);
        }
      });

})();
