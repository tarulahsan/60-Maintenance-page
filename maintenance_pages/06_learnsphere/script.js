
const STORAGE_KEY = 'mp_target_06_learnsphere';
const DEFAULT_DAYS = 15;

function getParam(name) {
  const params = new URLSearchParams(window.location.search);
  return params.get(name);
}

function getStoredTarget() {
  try {
    const t = localStorage.getItem(STORAGE_KEY);
    if (!t) return null;
    const n = parseInt(t, 10);
    if (Number.isNaN(n)) return null;
    return n;
  } catch (e) {
    return null;
  }
}

function storeTarget(ts) {
  try { localStorage.setItem(STORAGE_KEY, String(ts)); } catch (e) {}
}

function resolveTarget() {
  const stored = getStoredTarget();
  if (stored) return stored;
  const dateStr = getParam('date');
  if (dateStr) {
    const t = Date.parse(dateStr);
    if (!Number.isNaN(t)) { storeTarget(t); return t; }
  }
  const daysParam = getParam('days');
  let days = DEFAULT_DAYS;
  if (daysParam && !Number.isNaN(parseInt(daysParam, 10))) days = parseInt(daysParam, 10);
  const target = Date.now() + days * 24 * 60 * 60 * 1000;
  storeTarget(target);
  return target;
}

function pad(n) { return String(n).padStart(2, '0'); }

function updateCountdown(targetTs) {
  const now = Date.now();
  let diff = Math.max(0, targetTs - now);
  const days = Math.floor(diff / (24*60*60*1000)); diff -= days * 24*60*60*1000;
  const hours = Math.floor(diff / (60*60*1000)); diff -= hours * 60*60*1000;
  const mins = Math.floor(diff / (60*1000)); diff -= mins * 60*1000;
  const secs = Math.floor(diff / 1000);

  document.getElementById('days').textContent = pad(days);
  document.getElementById('hours').textContent = pad(hours);
  document.getElementById('minutes').textContent = pad(mins);
  document.getElementById('seconds').textContent = pad(secs);

  const total = days*24*3600 + hours*3600 + mins*60 + secs;
  const initial = DEFAULT_DAYS * 24 * 3600;
  const ratio = Math.max(0.02, Math.min(1, 1 - total / initial));
  const bar = document.querySelector('.progress .bar');
  if (bar) bar.style.width = (ratio * 100).toFixed(1) + '%';
}

function resetCountdown(days) {
  const next = Date.now() + days * 24 * 60 * 60 * 1000;
  storeTarget(next);
  updateCountdown(next);
}

function setupEmailCapture() {
  const form = document.getElementById('notify-form');
  if (!form) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = form.querySelector('input[type=email]').value;
    form.querySelector('button').textContent = 'Added!';
    form.querySelector('button').disabled = true;
    try {
      const key = 'mp_emails_06_learnsphere';
      const list = JSON.parse(localStorage.getItem(key) || '[]');
      list.push({ email, ts: Date.now() });
      localStorage.setItem(key, JSON.stringify(list));
    } catch (err) {}
  });
}

document.addEventListener('DOMContentLoaded', () => {
  let target = resolveTarget();
  updateCountdown(target);
  setInterval(() => updateCountdown(target), 1000);
  document.querySelectorAll('[data-reset]')?.forEach(btn => {
    btn.addEventListener('click', () => { resetCountdown(parseInt(btn.getAttribute('data-reset'), 10) || 15); window.scrollTo({ top: 0, behavior: 'smooth' }); });
  });
  const y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
  setupEmailCapture();
});
