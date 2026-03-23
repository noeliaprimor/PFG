# Publicar el sitio web en Cloudflare Pages

## 1. Requisitos previos
- Cuenta de Cloudflare (gratuita).
- Cuenta de GitHub.
- Git instalado en tu máquina.
- El proyecto ya está en local.
- npm instalado.

## 2. Pasos para publicar en Cloudflare Pages

### Paso 1: Preparar el repositorio en GitHub
1. Ve a https://github.com/new
2. Crea un repositorio público (ej: `pfg-bigdata`)
3. Abre terminal en la raíz del proyecto:

```bash
cd /Users/noeliaprieto/PycharmProjects/PFG
git init
git add .
git commit -m "Publicación inicial del sitio educativo en Cloudflare"
git branch -M main
git remote add origin https://github.com/tu-usuario/pfg-bigdata.git
git push -u origin main
```

### Paso 2: Conectar GitHub con Cloudflare Pages
1. Ve a https://dash.cloudflare.com/
2. Inicia sesión (o crea cuenta gratuita si no tienes).
3. En el menú lateral, ve a **Pages**.
4. Haz clic en **Create a project**.
5. Selecciona **Connect to Git**.
6. Autoriza Cloudflare para acceder a tu GitHub.
7. Selecciona el repositorio `pfg-bigdata`.
8. Elige rama `main`.

### Paso 3: Configurar el Build
En Cloudflare Pages:
- **Build command:** `npm run build`
- **Build output directory:** `dist`
- **Root directory:** `/` (dejar vacío o por defecto)

### Paso 4: Agregar variables de entorno (si es necesario)
Deja vacío por ahora, ya que el proyecto no requiere variables.

### Paso 5: Desplegar
1. Haz clic en **Save and Deploy**.
2. Espera a que termine la compilación (2-5 minutos).
3. Accede a tu sitio en: `https://pfg-bigdata.pages.dev`

## 3. Actualizar contenido después de cambios
Cada vez que hagas cambios locales:

```bash
cd /Users/noeliaprieto/PycharmProjects/PFG
git add .
git commit -m "Descripción de los cambios realizados"
git push origin main
```

**Cloudflare Pages se redesplegará automáticamente en 1-2 minutos.**

## 4. Usar dominio personalizado (opcional)
Si tienes un dominio:

1. En Cloudflare Dashboard > Pages > Tu proyecto.
2. Ve a **Settings** > **Domains**.
3. Haz clic en **Add custom domain**.
4. Introduce tu dominio.
5. Sigue las instrucciones de configuración DNS.

## 5. Configuración recomendada

### Seguridad (Settings > Environment)
- **Secure Your Website:** Habilitar HTTPS (automático en Cloudflare).
- **Enforce SSL/TLS:** Full (strict).

### Caching
- **Cache Expiration:** 30 minutos para contenido estático.
- **Browser Cache TTL:** 4 horas.

### Redirecciones (si es necesario)
En **Settings > Redirects**, configura:
- `404.html` para páginas no encontradas.

## 6. Solución de problemas

### Error: "Failed: error occurred while running build command"
**Causa:** El archivo template en HtmlWebpackPlugin no existe.
**Solución ya aplicada:** Se cambió `'./modulo2.html'` a `'./index.html'` en webpack.config.prod.js.

Para verificar:
```bash
npm run build
```

Si sigue fallando, revisa que exista `index.html` en la raíz.

### Error: "404 Not Found"
1. Verifica que `index.html` está en la raíz.
2. Comprueba que el output directory en Cloudflare es `dist`.
3. Recarga la página (Ctrl+Shift+R).

### Las imágenes no se cargan
1. Verifica que las rutas usan `/img/` (absolutas).
2. Comprueba que la carpeta `img` está en GitHub.
3. Revisa el build local: `npm run build` y abre `dist/index.html`.

### Los estilos CSS no cargan
1. Revisa que los links en HTML usan `/css/` (rutas absolutas).
2. Verifica que `copy-webpack-plugin` está copiando `css/` a `dist/css`.
3. Revisa en las DevTools si hay errores CORS.

## 7. Automatización con GitHub Actions (incluida)
Se ha creado `.github/workflows/deploy-cloudflare.yml` que automatiza el despliegue.

Para usar:
1. En tu repositorio GitHub > **Settings > Secrets and variables > Actions**.
2. Añade dos secretos:
   - `CLOUDFLARE_API_TOKEN`: Token de tu cuenta Cloudflare.
   - `CLOUDFLARE_ACCOUNT_ID`: ID de tu cuenta.

3. Obtén estos en: https://dash.cloudflare.com/profile/api-tokens

## 8. Comparativa: GitHub Pages vs Cloudflare Pages

| Característica | GitHub Pages | Cloudflare Pages |
|---|---|---|
| Costo | Gratis | Gratis |
| CDN Global | No | Sí |
| Velocidad | Buena | Excelente |
| SSL/TLS | Automático | Automático |
| Dominio gratuito | Sí (.github.io) | No |
| Integración GitHub | Nativa | Excelente |
| Límite de tamaño | 1GB | Ilimitado |
| Funciones Serverless | No | Sí |

**Recomendación:** Cloudflare Pages es mejor para sitios con muchas imágenes y usuarios globales.

## 9. Monitoreo y Analytics
En Cloudflare Dashboard > Pages > Tu proyecto > **Analytics** puedes ver:
- Solicitudes totales.
- Errores 4xx y 5xx.
- Ancho de banda utilizado.
- Países de acceso.

## 10. Compartir el enlace
- Enlace público: `https://pfg-bigdata.pages.dev`
- O tu dominio personalizado.
- Funciona en cualquier dispositivo y navegador.
- Sin necesidad de instalar nada.

## 11. Notas de seguridad
- El contenido es público (cualquiera puede verlo).
- No subas archivos sensibles (credenciales, claves, etc.).
- Usa `.gitignore` para excluir:
  ```
  node_modules/
  .env
  .env.local
  dist/
  .DS_Store
  ```

## 12. Comandos útiles

```bash
# Instalar dependencias
npm install

# Build local para verificar
npm run build

# Ver resultado local (si tienes servidor)
npm start

# Ver contenido de dist/
ls -la dist/

# Limpiar y reinstalar
rm -rf node_modules dist
npm install
npm run build
```

## Contacto y soporte
- Docs Cloudflare Pages: https://developers.cloudflare.com/pages/
- Docs GitHub Pages: https://pages.github.com/
- Soporte Cloudflare: https://support.cloudflare.com/

