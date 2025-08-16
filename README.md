
# IgnitedIndians — Django + DRF Starter (Oracle Cloud Ready)
- Django + DRF (API: `/api/products/`, `/api/health/`)
- Templates: Home, About, Contact, Products
- Docker Compose: Django (Gunicorn) + Postgres + Nginx
- GitHub Actions: deploy to Oracle VM via SSH

## Local Run
```bash
cp .env.example .env
docker compose -f docker/docker-compose.yml up -d --build
# Open http://localhost
# API: http://localhost/api/health/
```

## GitHub
```bash
git init && git add . && git commit -m "init: django starter"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## Oracle VM (one-time)
```bash
sudo apt update && sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker $USER && newgrp docker
mkdir -p ~/ignited && cd ~/ignited
```

Add repo Secrets: ORACLE_HOST, ORACLE_USER, ORACLE_SSH_KEY, ORACLE_DEPLOY_PATH
Push to main → auto deploy.

## Domain
Point A record of ignitedindians.com to your VM IP.
For HTTPS, install certbot and update nginx (we can do this next).
