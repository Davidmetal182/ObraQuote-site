'use strict';
// O formulario HTML usa envio POST nativo pelo Netlify Forms.
// Nao interceptar o submit com mailto: ou links para navegadores.
(() => {
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
