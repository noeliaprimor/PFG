# ✅ Checklist: Desplegar en Cloudflare Pages

## ✨ Cambios ya realizados

- [x] **Corregido webpack.config.prod.js**
  - Cambié template de `'./modulo2.html'` a `'./index.html'`
  - Build compila correctamente ✅

- [x] **Creado wrangler.toml**
  - Configuración para Cloudflare Pages

- [x] **Creado .github/workflows/deploy-cloudflare.yml**
  - CI/CD automático (opcional)

- [x] **Creadas guías**
  - `GUIA_CLOUDFLARE_PAGES.md` (completa)
  - `SOLUCION_CLOUDFLARE.md` (resumen)

---

## 📋 Acciones que debes realizar

### **FASE 1: Preparar GitHub** (5 min)

- [ ] **1.1** Crear repositorio en GitHub
  - Ir a https://github.com/new
  - Nombre: `pfg-bigdata` (o el que prefieras)
  - Tipo: Public
  - Crear repositorio

- [ ] **1.2** Configurar Git localmente
  ```bash
  cd /Users/noeliaprieto/PycharmProjects/PFG
  git init
  git add .
  git commit -m "Publicación inicial - Correcciones webpack"
  git branch -M main
  git remote add origin https://github.com/TU-USUARIO/pfg-bigdata.git
  git push -u origin main
  ```

---

### **FASE 2: Conectar a Cloudflare Pages** (5 min)

- [ ] **2.1** Acceder a Cloudflare
  - Ir a https://dash.cloudflare.com/
  - Iniciar sesión o crear cuenta gratuita

- [ ] **2.2** Crear proyecto en Pages
  - Click en **Pages** (izquierda)
  - Click en **Create a project**
  - Seleccionar **Connect to Git**

- [ ] **2.3** Autorizar GitHub
  - Click en **Authorize Cloudflare**
  - Seleccionar tu usuario GitHub

- [ ] **2.4** Seleccionar repositorio
  - Elegir `pfg-bigdata`
  - Rama: `main`

- [ ] **2.5** Configurar Build
  - **Build command:** `npm run build`
  - **Build output directory:** `dist`
  - **Root directory:** (dejar vacío)

- [ ] **2.6** Desplegar
  - Click en **Save and Deploy**
  - Esperar 2-5 minutos

---

### **FASE 3: Verificar el despliegue** (2 min)

- [ ] **3.1** Obtener URL
  - Ir a la página del proyecto
  - La URL será algo como: `https://pfg-bigdata.pages.dev`

- [ ] **3.2** Probar el sitio
  - Abre la URL en navegador
  - Verifica que carga correctamente
  - Prueba navegación entre páginas
  - Verifica que cargan imágenes y estilos

- [ ] **3.3** Compartir
  - Copia el enlace
  - ¡Comparte tu sitio! 🎉

---

### **FASE 4: (OPCIONAL) Configurar CI/CD automático** (10 min)

- [ ] **4.1** Obtener credenciales Cloudflare
  - Ir a https://dash.cloudflare.com/profile/api-tokens
  - Crear token: "Create Token"
  - Usar template: "Edit Cloudflare Workers"
  - Copiar el token

- [ ] **4.2** Obtener Account ID
  - En Cloudflare Dashboard, esquina derecha
  - Buscar "Account ID"
  - Copiar valor

- [ ] **4.3** Agregar secretos a GitHub
  - Ir a GitHub > Tu repositorio
  - **Settings** > **Secrets and variables** > **Actions**
  - Crear secretos:
    ```
    CLOUDFLARE_API_TOKEN = [tu_token]
    CLOUDFLARE_ACCOUNT_ID = [tu_account_id]
    ```

- [ ] **4.4** Hacer un test
  - Edita un archivo localmente
  - `git add .`
  - `git commit -m "Test CI/CD"`
  - `git push origin main`
  - Verifica que se despliega automáticamente

---

## 🆘 Si algo sale mal

### Error: "Failed: error occurred while running build command"
✅ **Ya está solucionado** (webpack.config.prod.js fue corregido)

### Error: "404 Not Found"
1. Verifica que output directory en Cloudflare es `dist`
2. Recarga con `Ctrl+Shift+R` (caché)

### Las imágenes no cargan
1. Verifica rutas en HTML usan `/img/`
2. Confirma que carpeta `img` está en GitHub

### Los estilos CSS no cargan
1. Verifica que CSS usa `/css/` en HTML
2. Ejecuta localmente: `npm run build`
3. Abre `dist/index.html` para probar

---

## 📊 Estado actual del proyecto

```
✅ Webpack: Compilando correctamente
✅ Build output: 3.15 MB de assets
✅ index.html: Generado
✅ CSS: Copiado
✅ Imágenes: Copiadas
✅ Configuración Cloudflare: Lista
✅ Documentación: Completa
```

---

## 💡 Comandos útiles

```bash
# Build local
npm run build

# Ver contenido de dist
ls -lah dist/

# Limpiar y reconstruir
rm -rf dist
npm run build

# Ver git status
git status

# Ver commits
git log --oneline
```

---

## 📚 Documentación generada

| Archivo | Descripción |
|---|---|
| `GUIA_CLOUDFLARE_PAGES.md` | Guía completa con todos los pasos |
| `SOLUCION_CLOUDFLARE.md` | Resumen de los problemas solucionados |
| Este archivo | Checklist de acciones pendientes |

---

## 🎯 Próximo paso

**Comienza por la FASE 1** siguiendo el checklist arriba.

¿Preguntas? Revisar `GUIA_CLOUDFLARE_PAGES.md`

**¡Tu sitio estará en vivo en 15 minutos! 🚀**

