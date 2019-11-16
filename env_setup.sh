# File to setup the local settings for running dev horizon
export HORIZON_DOCKER_TAG=latest

export GUNICORN_PROC_NAME=horizon
export GUNICORN_BIND=0.0.0.0:8000
export GUNICORN_WORKER_CLASS=sync
export GUNICORN_WORKERS=4
export GUNICORN_MAX_REQUESTS=2000
export GUNICORN_MAX_REQUESTS_JITTER=37
export GUNICORN_TIMEOUT=30
export GUNICORN_GRACEFUL_TIMEOUT=30
export GUNICORN_ACCESSLOG=-
export GUNICORN_ACCESS_LOG_FORMAT='ACCESS: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
export GUNICORN_ERRORLOG=-
export GUNICORN_LOGLEVEL=info

# Read local env settings
if [ -f local_env_settings.sh ]; then
    . ./local_env_settings.sh
fi
