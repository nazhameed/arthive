'use strict';

document.addEventListener('click', function (e) {
  const link = e.target.closest('.open-artwork');
  if (!link) return;
  e.preventDefault();
  const img = document.getElementById('artworkModalImg');
  const title = document.getElementById('artworkModalLabel');
  if (!img || !title) return;
  img.src = link.getAttribute('data-img');
  img.alt = link.getAttribute('data-title') || '';
  title.textContent = link.getAttribute('data-title') || '';
});
