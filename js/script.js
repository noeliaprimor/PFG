// Función segura para actualizar título y pie de página cuando los elementos existen
function updateTitleAndFooter() {
  try {
    var tituloElement = document.getElementById("titulo");
    if (tituloElement) {
      tituloElement.innerHTML = "Infraestruras computacionales para procesamiento de datos masivos";
      tituloElement.style.cursor = "pointer";
    }
    var tituloPElement = document.getElementById("tituloP");
    if (tituloPElement) {
      tituloPElement.innerHTML = "PFG - Noelia Prieto Morales";
    }
    var footerElement = document.getElementById("piePagina");
    if (footerElement) {
      footerElement.innerHTML = "&copy; 2026 PFG Noelia Prieto Morales. Todos los derechos reservados.";
    }
  } catch (e) {
    // no-op
  }
}

function siteUrl(sitePath) {
  if (!sitePath || /^(?:https?:|mailto:|tel:|#)/.test(sitePath)) return sitePath;
  if (window.location.protocol !== 'file:') return sitePath;

  var cleanPath = sitePath.replace(/^\/+/, '') || 'index.html';
  var currentPath = window.location.pathname || '';
  var marker = '/PFG/';
  var relativeCurrent = currentPath;
  var markerIndex = currentPath.indexOf(marker);
  if (markerIndex !== -1) {
    relativeCurrent = currentPath.slice(markerIndex + marker.length);
  }

  var depth = relativeCurrent.split('/').slice(0, -1).filter(Boolean).length;
  return (depth ? '../'.repeat(depth) : './') + cleanPath;
}

// Llamar una vez al cargar (si los elementos ya están presentes)
document.addEventListener('DOMContentLoaded', updateTitleAndFooter);

// MENU Y SUBMENÚS (generación estática de HTML en elementos con id menuprincipal / menumodulo)
document.addEventListener("DOMContentLoaded", function() {
  try {
    var el = document.getElementById('menumodulo');
    if (el) {
      el.innerHTML = `
      <div class="menu-section">
        <nav class="nav">
            <input type="checkbox" id="nav_checkbox" class="nav_checkbox">
            <label for="nav_checkbox" class="nav_toggle">
              <svg class="menu" viewBox="0 0 448 512" width="100"><path d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z"/></svg>
              <svg class="close" viewBox="0 0 384 512" width="100"><path d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.2 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.2 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z"/></svg>
            </label>
            <ul class="nav_menu">
              <li><a href="${siteUrl('/index.html')}">Inicio</a></li>
              <li><a href="#">Módulos</a>
                <ul class="submenu">
                  <li><a href="${siteUrl('/modulo2/modulo2.html')}">Módulo 2</a></li>
                  <li><a href="${siteUrl('/modulo3/modulo3.html')}">Módulo 3</a></li>
                </ul>
              </li>
            </ul>
        </nav>
      </div>`;
    }
  } catch (e) { /* ignore */ }
});

// Manejo simple de submenús (accesible y sin dependencia del índice dinámico)
document.addEventListener('click', function (e) {
  // Oculta submenus si se hace click fuera
  var submenus = document.querySelectorAll('.submenu');
  submenus.forEach(function(s){
    if (!s.contains(e.target)) s.style.display = 'none';
  });
});

document.addEventListener('DOMContentLoaded', function(){
  var items = document.querySelectorAll('nav li');
  items.forEach(function(it){
    it.addEventListener('click', function(ev){
      ev.stopPropagation();
      var submenu = this.querySelector('.submenu');
      if (submenu) {
        ev.preventDefault();
        submenu.style.display = (submenu.style.display === 'block') ? 'none' : 'block';
      }
    });
  });
});

// COPIAR CONTENIDO CELDA CÓDIGO (mantener utilidad)
function copyCode(nom_element, nom_Cell) {
    var codeElement = document.getElementById(nom_element);
    if (!codeElement) return; // seguridad
    var codigoSinEspacios = eliminarEspaciosIzquierda(codeElement.textContent);
    var tempElement = document.createElement('textarea');
    tempElement.value = codigoSinEspacios;
    document.body.appendChild(tempElement);
    tempElement.select();
    document.execCommand('copy');
    document.body.removeChild(tempElement);
    var codeCell = document.querySelector("#" + nom_Cell);
    if (!codeCell) return;
    var codeCellRect = codeCell.getBoundingClientRect();
    var topPosition = codeCellRect.top + window.scrollY;
    var leftPosition = codeCellRect.left + window.scrollX;
    mostrarAviso(topPosition + 5, leftPosition + 10);
}

function eliminarEspaciosIzquierda(codigo) {
  const lineas = codigo.split('\n');
  if (lineas[0] && lineas[0].trim() === '') lineas.shift();
  if (lineas.length && lineas[lineas.length - 1].trim() === '') lineas.pop();
  let minIndent = Infinity;
  lineas.forEach(linea => {
      const espaciosInicio = /^[ \t]*/.exec(linea)[0].length;
      if (espaciosInicio > 0 && espaciosInicio < minIndent) minIndent = espaciosInicio;
  });
  if (!isFinite(minIndent)) minIndent = 0;
  const codigoSinEspacios = lineas.map(linea => {
      const espaciosInicio = /^[ \t]*/.exec(linea)[0].length;
      return espaciosInicio >= minIndent ? linea.substring(minIndent) : linea;
  });
  return codigoSinEspacios.join('\n');
}

function mostrarAviso(top, left) {
  var aviso = document.createElement('div');
  aviso.innerHTML = 'Código copiado al portapapeles.';
  aviso.style.backgroundColor = '#80d182';
  aviso.style.padding = '10px';
  aviso.style.position = 'absolute';
  aviso.style.top = top + 'px';
  aviso.style.left = left + 'px';
  aviso.style.border = '1px solid #ccc';
  aviso.style.borderRadius = '5px';
  aviso.style.fontSize = 'small';
  document.body.appendChild(aviso);
  setTimeout(function() { document.body.removeChild(aviso); }, 2000);
}

// BOTÓN IR ARRIBA (jQuery sigue en el proyecto)
if (window.jQuery) {
  $(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 150) {
            $('#scroll').fadeIn();
        } else {
            $('#scroll').fadeOut();
        }
    });
    $('#scroll').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
  });
}

// Incluir header/footer desde /partials en todas las páginas excepto las que están bajo /modulo1
document.addEventListener('DOMContentLoaded', function () {
  try {
    var path = window.location.pathname || '/';
    var normalized = path.replace(/\/+$/g, '');
    if (normalized.indexOf('/modulo1') === 0) return;
    function fetchAndInsert(url, selector, position) {
      if (document.querySelector(selector)) {
        updateTitleAndFooter();
        return;
      }
      fetch(siteUrl(url), { cache: 'no-store' }).then(function (res) { if (!res.ok) return; return res.text(); }).then(function (html) {
        if (!html) return;
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var node = doc.querySelector(selector);
        if (!node) return;
        var imported = document.importNode(node, true);
        var existing = document.querySelector(selector);
        if (existing) existing.parentNode.replaceChild(imported, existing); else if (position === 'prepend') document.body.insertBefore(imported, document.body.firstChild); else document.body.appendChild(imported);
        updateTitleAndFooter();
      }).catch(function (err) { console.warn('No se pudo cargar ' + url + ':', err); });
    }
    fetchAndInsert('/partials/header.html', 'header', 'prepend');
    fetchAndInsert('/partials/footer.html', 'footer', 'append');
  } catch (e) { console.error('Error al incluir partials:', e); }
});
