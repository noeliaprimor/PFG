/* Carga fragmentos HTML en elementos con data-include="ruta" */

document.addEventListener('DOMContentLoaded', function () {
  const includes = Array.from(document.querySelectorAll('[data-include]'));
  if (!includes.length) return;

  Promise.all(includes.map(el => {
    const url = el.getAttribute('data-include');
    return fetch(url)
      .then(res => {
        if (!res.ok) throw new Error('No se pudo cargar ' + url);
        return res.text();
      })
      .then(html => {
        el.innerHTML = html;
        // ejecutar scripts internos del fragmento (si existen)
        el.querySelectorAll('script').forEach(oldScript => {
          const s = document.createElement('script');
          if (oldScript.src) s.src = oldScript.src;
          else s.textContent = oldScript.textContent;
          document.body.appendChild(s).parentNode.removeChild(s);
        });
      })
      .catch(err => console.error(err));
  }));
});
