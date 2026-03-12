/* Carga fragmentos HTML en elementos con data-include="ruta" */
document.addEventListener('DOMContentLoaded', function () {
  var includeNodes = document.querySelectorAll('[data-include]');

  includeNodes.forEach(function (node) {
    var url = node.getAttribute('data-include');
    if (!url) return;

    // header/footer ya los gestiona script.js de forma centralizada
    if (url.indexOf('/partials/header.html') !== -1 || url.indexOf('/partials/footer.html') !== -1) {
      return;
    }

    fetch(url, { cache: 'no-store' })
      .then(function (res) {
        if (!res.ok) throw new Error('No se pudo cargar ' + url);
        return res.text();
      })
      .then(function (html) {
        node.innerHTML = html;
      })
      .catch(function (err) {
        console.warn('Error en data-include (' + url + '):', err);
      });
  });
});
