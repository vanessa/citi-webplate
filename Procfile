release: python manage.py migrate
web: gunicorn {{ project_name }}.wsgi --log-file -
worker: python manage.py runworker