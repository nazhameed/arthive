'use strict';

document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const authButtons = document.getElementById('auth-buttons');

  function showForm(form) {
    if (!loginForm || !registerForm || !authButtons) return;
    const isLogin = form === 'login';
    loginForm.classList.toggle('d-none', !isLogin);
    registerForm.classList.toggle('d-none', isLogin);
    authButtons.classList.add('d-none');
    // Focus the first input in the shown form
    const input = (isLogin ? loginForm : registerForm).querySelector('input, select, textarea, button');
    if (input) input.focus();
  }

  document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-form]');
    if (!btn) return;
    e.preventDefault();
    showForm(btn.getAttribute('data-form'));
  });
});
