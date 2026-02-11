# systemd timer example for automated backup

Create these files as root (example names):

`/etc/systemd/system/pfg-autobackup.service`:

```
[Unit]
Description=PFG auto backup (git commit & push)

[Service]
Type=oneshot
WorkingDirectory=/var/www/PFG
ExecStart=/bin/bash /var/www/PFG/scripts/auto_backup.sh

[Install]
WantedBy=multi-user.target
```

`/etc/systemd/system/pfg-autobackup.timer`:

```
[Unit]
Description=Run PFG backup every 15 minutes

[Timer]
OnBootSec=5min
OnUnitActiveSec=15min
Persistent=true

[Install]
WantedBy=timers.target
```

Commands to enable:

```
sudo systemctl daemon-reload
sudo systemctl enable --now pfg-autobackup.timer
sudo systemctl status pfg-autobackup.timer
```

Notes:
- Ensure the service runs as a user that has SSH keys configured (if pushing via SSH).
- Logs go to `journalctl -u pfg-autobackup.service`.
