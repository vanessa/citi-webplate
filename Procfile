release: bash ./deploy-tasks.sh
web: gunicorn {{ project_name }}.wsgi --log-file -
worker: python manage.py runworker