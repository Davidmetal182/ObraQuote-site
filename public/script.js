'use strict';
(() => {
  document.getElementById('year').textContent = String(new Date().getFullYear());
  const form = document.getElementById('interest-form');
  const feedback = document.getElementById('form-feedback');
  const notice = document.getElementById('privacy-notice');
  const config = window.OBRAQUOTE_SITE_CONFIG || {};
  const whatsapp = String(config.whatsapp || '').replace(/\D/g, '');
  const email = String(config.email || '').trim();
  const validEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) && !email.endsWith('exemplo.com');
  const validWhatsApp = /^\d{12,15}$/.test(whatsapp);
  if (!validWhatsApp && !validEmail) {
    notice.textContent = 'Página em preparação: o canal de atendimento será ativado antes da divulgação pública.';
    notice.classList.add('needs-setup');
  } else if (validWhatsApp) {
    notice.textContent = 'Ao continuar, o WhatsApp abrirá com sua mensagem pronta. O site não guarda seus dados.';
  } else {
    notice.textContent = 'Ao continuar, seu aplicativo de e-mail abrirá um rascunho. Revise e clique em Enviar: o site não envia nem guarda seus dados.';
  }

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    feedback.classList.remove('success');
    if (!form.reportValidity()) return;
    if (!validWhatsApp && !validEmail) {
      feedback.textContent = 'O canal comercial ainda não foi configurado. Obrigado pelo interesse!';
      return;
    }
    const name = document.getElementById('interest-name').value.trim().slice(0, 80);
    const profession = document.getElementById('interest-profession').value.trim();
    const message = document.getElementById('interest-message').value.trim().slice(0, 280);
    const text = `Olá! Quero conhecer o teste gratuito do ObraQuote.\n\nNome: ${name}\nAtividade: ${profession}${message ? '\nDificuldade com orçamentos: ' + message : ''}\n\nVi a página de apresentação do ObraQuote.`;
    if (validWhatsApp) {
      const url = `https://wa.me/${whatsapp}?text=${encodeURIComponent(text)}`;
      window.location.assign(url);
      feedback.textContent = 'Abrindo WhatsApp...';
      feedback.classList.add('success');
    } else if (validEmail) {
      const url = `mailto:${email}?subject=${encodeURIComponent('Interesse no piloto ObraQuote')}&body=${encodeURIComponent(text)}`;
      window.location.assign(url);
      feedback.textContent = 'Confira seu aplicativo de e-mail e clique em Enviar. Se não abrir, use o endereço exibido abaixo.';
      feedback.classList.add('success');
    }
  });
})();
