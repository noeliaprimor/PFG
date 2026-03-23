# Publicar el sitio web en GitHub Pages

## 1. Requisitos previos
- Cuenta de GitHub (gratuita).
- Git instalado en tu máquina.
- El proyecto ya está en local.

## 2. Pasos para publicar en GitHub Pages

### Paso 1: Crear un repositorio en GitHub
1. Ve a https://github.com/new
2. Nombre del repositorio: `nombre-usuario.github.io` (reemplaza `nombre-usuario` por tu usuario de GitHub).
3. Descripción (opcional): "Plataforma educativa de Big Data y Apache Spark".
4. Selecciona `Public`.
5. Haz clic en `Create repository`.

### Paso 2: Configurar Git en tu proyecto local
Abre terminal en la raíz del proyecto (`/Users/noeliaprieto/PycharmProjects/PFG`):

```bash
git init
git add .
git commit -m "Publicación inicial del sitio educativo PFG"
```

### Paso 3: Conectar con el repositorio remoto
```bash
git remote add origin https://github.com/nombre-usuario/nombre-usuario.github.io.git
git branch -M main
git push -u origin main
```

(Reemplaza `nombre-usuario` con tu usuario de GitHub).

### Paso 4: Verificar la publicación
- Espera 2-5 minutos.
- Abre: `https://nombre-usuario.github.io`
- Verás tu sitio web en vivo.

## 3. Actualizar contenido después de cambios
Cada vez que hagas cambios locales:

```bash
git add .
git commit -m "Descripción de los cambios realizados"
git push origin main
```

## 4. Alternativa: Repositorio con nombre personalizado
Si prefieres otro nombre de repositorio (ej: `pfg-bigdata`):

1. Crea el repositorio con ese nombre.
2. En GitHub, ve a `Settings` > `Pages`.
3. Selecciona `Deploy from a branch`.
4. Elige rama `main` y carpeta `root (/)`.
5. Tu sitio estará en: `https://nombre-usuario.github.io/pfg-bigdata`

## 5. Configuración recomendada de GitHub Pages

### En Settings > Pages:
- Source: Deploy from a branch.
- Branch: `main` / `/(root)`.
- Enforce HTTPS: activado.

### En Settings > General:
- Template: ninguno.
- Default branch: `main`.

## 6. Solución de problemas comunes

### Problema: "404 Not Found"
- Verifica que `index.html` esté en la raíz del proyecto.
- Comprueba que la rama es `main` (no `master`).
- Espera 5 minutos y recarga (cache).

### Problema: Estilos CSS no cargan
- Revisa rutas absolutas en `index.html` (deben empezar con `/`).
- Verifica que todos los archivos están en GitHub (`git status`).

### Problema: Imágenes no se ven
- Comprueba que rutas en HTML usan `/img/` (absolutas).
- Confirma que la carpeta `img/` está en GitHub.

## 7. Automatización con GitHub Actions (opcional)
Si usas webpack u otro build:

Crea archivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/
```

## 8. Dominio personalizado (opcional)
Si tienes dominio propio:

1. En tu proveedor de dominio, añade registros DNS:
   ```
   Tipo A: 185.199.108.153
   Tipo A: 185.199.109.153
   Tipo A: 185.199.110.153
   Tipo A: 185.199.111.153
   ```

2. En GitHub > Settings > Pages > Custom domain: introduce tu dominio.

3. Espera validación (puede tardar 24h).

## 9. Compartir el enlace
- Enlace público: `https://nombre-usuario.github.io`
- Funciona en cualquier dispositivo y navegador.
- Sin necesidad de instalar nada en el lado del usuario.

## 10. Notas de seguridad
- El contenido es público (cualquiera puede verlo).
- No subas archivos sensibles (credenciales, claves, etc.).
- Usa `.gitignore` para excluir:
  ```
  node_modules/
  .env
  .env.local
  dist/
  ```


