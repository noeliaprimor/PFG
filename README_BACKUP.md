# Backup automático con Git

Este repositorio incluye un script simple para hacer copias de seguridad automáticas a un remoto GitHub u otro servidor Git.

Qué hace
- Comprime (no hace compresión explícita) y comete todos los cambios en el repositorio.
- Empuja (push) al remote y branch configurados.

Archivo principal:
- `scripts/auto_backup.sh` — script bash que hace commit y push automático.

Cómo configurarlo
1. Añade un remote apuntando a tu repositorio GitHub (ejemplo):

   git remote add origin git@github.com:TU_USUARIO/TU_REPO.git

2. (Opcional) cambia el branch por defecto si tu repo usa `main` o `master`:

   export GIT_BRANCH=main

3. Probar manualmente:

   bash scripts/auto_backup.sh

Ejecución periódica
- Opción A — Cron (simple):
  - Edita la tabla de cron: `crontab -e`
  - Añade una línea para ejecutar cada 15 minutos por ejemplo:

    */15 * * * * cd /var/www/PFG && /bin/bash scripts/auto_backup.sh >> /var/log/pfg_autobackup.log 2>&1

- Opción B — systemd timer (más robusto):
  - Crear un unit y un timer en `/etc/systemd/system/` (ejemplo en README adicional).

Notas de seguridad
- No incluyas credenciales en el repo.
- Para push vía SSH, configura la clave SSH del servidor/usuario que ejecuta el cron.
- Para grandes ficheros binarios considera usar Git LFS o excluirlos en `.gitignore`.
