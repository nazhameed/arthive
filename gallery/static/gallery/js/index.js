'use strict';

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const authButtons = document.getElementById('auth-buttons');
  const container = document.querySelector('[data-active-form]');

  function showForm(form) {
    if (!loginForm || !registerForm || !authButtons) return;
    const isLogin = form === 'login';
    const shown = isLogin ? loginForm : registerForm;
    const hidden = isLogin ? registerForm : loginForm;

    shown.classList.remove('d-none');
    hidden.classList.add('d-none');
    authButtons.classList.add('d-none');

    // Scroll the revealed form into view and focus first input
    shown.scrollIntoView({ behavior: 'smooth', block: 'start' });
    const input = shown.querySelector('input, select, textarea, button');
    if (input) input.focus();
  }

  // Initialize from server-side active_form if present
  const initial = container ? container.getAttribute('data-active-form') : '';
  if (initial === 'login' || initial === 'register') {
    showForm(initial);
  }

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-form]');
    if (!btn) return;
    e.preventDefault();
    showForm(btn.getAttribute('data-form'));
  });
});
