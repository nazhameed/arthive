'use strict';

document.addEventListener('click', function (e) {
  const imageTrigger = e.target.closest('.open-artwork-image');
  const actionsTrigger = e.target.closest('.open-artwork-actions');

  if (imageTrigger) {
    e.preventDefault();
    const imgEl = document.getElementById('artworkImageModalImg');
    const img = imageTrigger.getAttribute('data-img');
    const title = imageTrigger.getAttribute('data-title') || '';
    if (imgEl) { imgEl.src = img; imgEl.alt = title; }
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
