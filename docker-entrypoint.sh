#!/bin/sh
set -eu
python manage.py migrate --noinput
if [ -n "${DJANGO_SUPERUSER_USERNAME:-}" ] && [ -n "${DJANGO_SUPERUSER_EMAIL:-}" ] && [ -n "${DJANGO_SUPERUSER_PASSWORD:-}" ]; then
  python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); u,c=U.objects.get_or_create(username='${DJANGO_SUPERUSER_USERNAME}', defaults={'email':'${DJANGO_SUPERUSER_EMAIL}'}); u.email='${DJANGO_SUPERUSER_EMAIL}'; u.is_staff=True; u.is_superuser=True; u.set_password('${DJANGO_SUPERUSER_PASSWORD}'); u.save()"
fi
exec "$@"
