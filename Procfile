release: python manage.py migrate
api: gunicorn backend.wsgi --log-file -
web: node server.js
