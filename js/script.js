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

// Llamar una vez al cargar (si los elementos ya están presentes)
document.addEventListener('DOMContentLoaded', updateTitleAndFooter);

// MENU Y SUBMENÚS

document.addEventListener("DOMContentLoaded", function() {
  const menuModulo = `
      <div class="menu-section">
        <nav class="nav">

            <input type="checkbox" id="nav_checkbox" class="nav_checkbox">

            <label for="nav_checkbox" class="nav_toggle">

              <svg class="menu" viewBox="0 0 448 512" width="100">
                <path d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z" />
              </svg>
              <svg class="close" viewBox="0 0 384 512" width="100">
                <path d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.2 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.2 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z" />
              </svg>

            </label>

            <ul class="nav_menu">
              <li><a href="../index.html">Inicio</a></li>
              <li><a href="#">Accede al Tema <i class="fa-solid fa-caret-down" style="padding-left: 5px; color: #ffffff;"></i></a>

                <ul class="submenu">
                <li>
                  <a href="#">Módulo 1 <i class="fa-solid fa-caret-right" style="padding-left: 5px; color: #ffffff;"></i></a>
                         <ul class="submenu">
                               <li><a href="../modulo1/modulo1/tema1.html">Tema 1</a></li>
                                <li><a href="../modulo1/modulo1/tema2.html">Tema 2</a></li>
                               <li><a href="../modulo1/modulo1/tema3.html">Tema 3</a></li>
                           </ul>
                </li>
                <li>
                    <a href="#">Módulo 2 <i class="fa-solid fa-caret-right" style="padding-left: 5px; color: #ffffff;"></i></a>
                    <ul class="submenu">
                            <li><a href="../modulo2/tema1.html">Tema 1</a></li>
                            <li><a href="../modulo2/tema2.html">Tema 2</a></li>
                            <li><a href="../modulo2/tema3.html">Tema 3</a></li>
                    </ul>
                </li>
                <li><a href="../preparacion/index.html">Preparación del Entorno</a></li>
                 <li><a href="../modulo1/modulo1/index.html">Tema 1</a></li>
                  <li><a href="../modulo2/modulo2.html">Tema 2</a></li>
                  <li><a href="../modulo3/modulo3.html">Tema 3</a></li>
                  <li><a href="../modulo4/index.html">Tema 4</a></li>
                </ul>
              </li>
            </ul>
          </nav>
  `;
  document.getElementById('menumodulo').innerHTML = menuModulo;
});

document.addEventListener("DOMContentLoaded", function() {

  const menuPrincipal = `
      <div class="menu-section">
        <nav class="nav">

            <input type="checkbox" id="nav_checkbox" class="nav_checkbox">

            <label for="nav_checkbox" class="nav_toggle">

              <svg class="menu" viewBox="0 0 448 512" width="100">
                <path d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z" />
              </svg>
              <svg class="close" viewBox="0 0 384 512" width="100">
                <path d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.2 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.2 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z" />
              </svg>

            </label>

            <ul class="nav_menu">
              <li><a href="../index.html">Inicio</a></li>
              <li><a href="#">Accede al Tema <i class="fa-solid fa-caret-down" style="padding-left: 5px; color: #ffffff;"></i></a>
                <ul class="submenu">
                  <li><a href="../../preparacion/index.html">Preparación del Entorno</a></li>
                  <li><a href="../modulo1/modulo1/index.html">Tema 1</a></li>
                  <li><a href="../../modulo2/index.html">Tema 2</a></li>
                  <li><a href="../../modulo3/index.html">Tema 3</a></li>
                  <li><a href="../../modulo4/index.html">Tema 4</a></li>
                </ul>
              </li>
            </ul>
          </nav>
    </div>
  `;

  document.getElementById('menuprincipal').innerHTML = menuPrincipal;
});



document.addEventListener("DOMContentLoaded", function () {
    //Elementos de menú con submenú
    var menuItems = document.querySelectorAll('nav li');

    // Agrega un evento de clic al documento para ocultar todos los submenús
    document.addEventListener('click', function () {
      hideAllSubmenus();
    });

    // Itera sobre cada elemento de menú
    menuItems.forEach(function (menuItem) {
      // Agrega un evento de clic a cada elemento de menú para evitar que se propague el clic al documento
      menuItem.addEventListener('click', function (event) {
        event.stopPropagation(); // Evita que el clic se propague al documento

        // Oculta todos los submenús
        hideAllSubmenus();

        // Muestra el submenú correspondiente al elemento de menú actual
        var submenu = this.querySelector('.submenu');
        if (submenu) {
          // Evitar la acción por defecto del enlace (href="#") que puede cambiar el fragmento y cerrar el menú
          event.preventDefault();
          submenu.style.display = (submenu.style.display === 'block') ? 'none' : 'block';
        }
      });
    });

    // Oculta todos los submenús
    function hideAllSubmenus() {
      var submenus = document.querySelectorAll('.submenu');
      submenus.forEach(function (submenu) {
        submenu.style.display = 'none';
      });
    }



  });

// VER/OCULTAR ÍNDICE EN CADA LECCIÓN (registro seguro)
document.addEventListener('DOMContentLoaded', function () {
  try {
    var toggleBtn = document.getElementById('toggle-index');
    if (!toggleBtn) return; // no hay botón en esta página

    toggleBtn.addEventListener('click', function () {
      var indexContainer = document.getElementById('index-container');
      if (!indexContainer) return;

      if (indexContainer.classList.contains('hidden')) {
        indexContainer.classList.remove('hidden');
        toggleBtn.innerHTML = 'Ocultar Índice <i class="fa-solid fa-caret-up" style="padding-left: 5px; color: #004d35;"></i>';
      } else {
        indexContainer.classList.add('hidden');
        toggleBtn.innerHTML = 'Mostrar Índice <i class="fa-solid fa-caret-down" style="padding-left: 5px; color: #004d35;"></i>';
      }
    }, false);
  } catch (e) {
    console.warn('toggle-index listener error:', e);
  }
});

// Registro robusto por delegación para el botón toggle-index (funciona aunque el botón se añada dinámicamente)
if (!window.__indexToggleSetup) {
  window.__indexToggleSetup = true;
  document.addEventListener('click', function (event) {
    var btn = event.target.closest && event.target.closest('#toggle-index');
    if (!btn) return;
    try {
      var indexContainer = document.getElementById('index-container');
      if (!indexContainer) return;
      if (indexContainer.classList.contains('hidden')) {
        indexContainer.classList.remove('hidden');
        btn.innerHTML = 'Ocultar Índice <i class="fa-solid fa-caret-up" style="padding-left: 5px; color: #004d35;"></i>';
      } else {
        indexContainer.classList.add('hidden');
        btn.innerHTML = 'Mostrar Índice <i class="fa-solid fa-caret-down" style="padding-left: 5px; color: #004d35;"></i>';
      }
    } catch (e) {
      console.warn('Error al alternar índice:', e);
    }
  }, false);
}

// COPIAR CONTENIDO CELDA CÓDIGO
function copyCode(nom_element, nom_Cell) {
    // Seleccionar el contenido del elemento pre y eliminar espacios en blanco a la izquierda
    var codeElement = document.getElementById(nom_element);
    var codigoSinEspacios = eliminarEspaciosIzquierda(codeElement.textContent);

    // Crear un elemento temporal para contener el código sin espacios
    var tempElement = document.createElement('textarea');
    tempElement.value = codigoSinEspacios;
    document.body.appendChild(tempElement);

    // Seleccionar y copiar el contenido del elemento temporal
    tempElement.select();
    document.execCommand('copy');

    // Eliminar el elemento temporal
    document.body.removeChild(tempElement);

    // Obtener la posición de la celda de código
    var codeCell = document.querySelector("#" + nom_Cell);
    var codeCellRect = codeCell.getBoundingClientRect();
    var topPosition = codeCellRect.top + window.scrollY;
    var leftPosition = codeCellRect.left + window.scrollX;

    // Mostrar el aviso junto a la celda de código
    mostrarAviso(topPosition + 5, leftPosition + 10);
}

// ELIMINAR LOS ESPACIOS EN BLANCO
// FUNCIÓN AUXILIAR DE COPYCODE
function eliminarEspaciosIzquierda(codigo) {
  // Dividir el código en líneas
  const lineas = codigo.split('\n');

  // Eliminar la primera línea en blanco, si existe
  if (lineas[0].trim() === '') {
      lineas.shift();
  }

  // Eliminar la última línea en blanco, si existe
  if (lineas[lineas.length - 1].trim() === '') {
      lineas.pop();
  }

  // Encontrar la cantidad mínima de espacios en blanco en la identación
  let minIndent = Infinity;
  lineas.forEach(linea => {
      const espaciosInicio = /^[ \t]*/.exec(linea)[0].length;
      if (espaciosInicio > 0 && espaciosInicio < minIndent) {
          minIndent = espaciosInicio;
      }
  });

  // Eliminar espacios en blanco a la izquierda de cada línea, solo si hay una identación
  const codigoSinEspacios = lineas.map(linea => {
      const espaciosInicio = /^[ \t]*/.exec(linea)[0].length;
      return espaciosInicio >= minIndent ? linea.substring(minIndent) : linea;
  });

  // Unir las líneas de nuevo en un solo string
  return codigoSinEspacios.join('\n');
}

  // FUNCIÓN AVISO COPIAR CÓDIGO
  // AUXILIAR DE COPYCODE
  function mostrarAviso(top, left) {
    // Crear un elemento de aviso
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

    // Agregar el aviso al cuerpo del documento
    document.body.appendChild(aviso);

    // Desaparecer el aviso después de 5 segundos
    setTimeout(function() {
      document.body.removeChild(aviso);
    }, 2000);
  }

// BOTÓN IR ARRIBA
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

document.addEventListener("DOMContentLoaded", function() {
  var dropdown = document.querySelector('.dropdown');
  var submenu = document.querySelector('.submenu');

  // Asegurarse de que ambos existen antes de registrar listeners
  if (dropdown && submenu) {
    // Ejemplo: Muestra el submenú con JS al pasar el mouse
    dropdown.addEventListener('mouseover', function() {
      submenu.style.display = 'block';
    });

    // Ejemplo: Oculta el submenú con JS al quitar el mouse
    dropdown.addEventListener('mouseout', function() {
      submenu.style.display = 'none';
    });
  }
});

// Incluir header/footer desde /partials en todas las páginas excepto las que están bajo /modulo1
document.addEventListener('DOMContentLoaded', function () {
  try {
    var path = window.location.pathname || '/';
    // Normalizar: eliminar trailing slash para la comprobación
    var normalized = path.replace(/\/+$|^\\/g, '/');
    if (normalized.indexOf('/modulo1') === 0) {
      // No inyectar en las páginas de modulo1
      return;
    }

    function fetchAndInsert(url, selector, position) {
      fetch(url, { cache: 'no-store' }).then(function (res) {
        if (!res.ok) return; return res.text();
      }).then(function (html) {
        if (!html) return;
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var node = doc.querySelector(selector);
        if (!node) return;
        // Import the node into the current document (to avoid issues with ownerDocument)
        var imported = document.importNode(node, true);
        var existing = document.querySelector(selector);
        if (existing) {
          existing.parentNode.replaceChild(imported, existing);
        } else {
          if (position === 'prepend') {
            document.body.insertBefore(imported, document.body.firstChild);
          } else {
            document.body.appendChild(imported);
          }
        }
        // Actualizar título y pie de página después de insertar partials
        updateTitleAndFooter();
      }).catch(function (err) {
        console.warn('No se pudo cargar ' + url + ':', err);
      });
    }

    // Insertar header (reemplaza o inserta al principio)
    fetchAndInsert('/partials/header.html', 'header', 'prepend');
    // Insertar footer (reemplaza o inserta al final)
    fetchAndInsert('/partials/footer.html', 'footer', 'append');
  } catch (e) {
    console.error('Error al incluir partials:', e);
  }
});

