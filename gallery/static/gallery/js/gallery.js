'use strict';

document.addEventListener('click', function (e) {
  const imageTrigger = e.target.closest('.open-artwork-image');
  const actionsTrigger = e.target.closest('.open-artwork-actions');

  if (imageTrigger) {
    e.preventDefault();
    const imgEl = document.getElementById('artworkImageModalImg');
    const titleEl = document.getElementById('artworkImageModalTitle');
    const dateEl = document.getElementById('artworkImageModalDate');
    const descEl = document.getElementById('artworkImageModalDesc');
    const editEl = document.getElementById('artworkImageModalEdit');

    const img = imageTrigger.getAttribute('data-img');
    const title = imageTrigger.getAttribute('data-title') || '';
    let date = imageTrigger.getAttribute('data-date') || '';
    const desc = imageTrigger.getAttribute('data-desc') || '';
    const editHref = imageTrigger.getAttribute('data-edit') || '#';

    // Fallback: pull date from the card if not provided
    if (!date) {
      const card = imageTrigger.closest('.honeycomb-media');
      const dateNode = card ? card.querySelector('.honeycomb-date') : null;
      if (dateNode) date = dateNode.textContent.trim();
    }

    if (imgEl) { imgEl.src = img; imgEl.alt = title; }
    if (titleEl) { titleEl.textContent = title; }
    if (dateEl) {
      dateEl.textContent = date || '';
      if (date) { dateEl.classList.remove('d-none'); } else { dateEl.classList.add('d-none'); }
    }
    if (descEl) {
      descEl.textContent = desc;
      if (desc.trim()) { descEl.classList.remove('d-none'); } else { descEl.classList.add('d-none'); }
    }
    if (editEl) { editEl.href = editHref; editEl.classList.toggle('d-none', editHref === '#'); }
    return;
  }

  if (actionsTrigger) {
    e.preventDefault();
    const titleEl = document.getElementById('artworkActionsTitle');
    const editEl = document.getElementById('artworkEditLink');
    const deleteEl = document.getElementById('artworkDeleteLink');

    const title = actionsTrigger.getAttribute('data-title') || '';
    const editHref = actionsTrigger.getAttribute('data-edit');
    const deleteHref = actionsTrigger.getAttribute('data-delete');

    if (titleEl) { titleEl.textContent = title; }
    if (editEl && editHref) { editEl.href = editHref; }
    if (deleteEl && deleteHref) { deleteEl.href = deleteHref; }
  }
});
