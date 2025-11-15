// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('theme-toggle');
  const html = document.documentElement;
  const setTheme = (theme) => {
    html.setAttribute('data-bs-theme', theme);
    localStorage.setItem('theme', theme);
    toggle.querySelector('.light').classList.toggle('d-none', theme === 'dark');
    toggle.querySelector('.dark').classList.toggle('d-none', theme === 'light');
  };
  const saved = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  setTheme(saved);
  toggle.addEventListener('click', () => setTheme(html.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark'));
});