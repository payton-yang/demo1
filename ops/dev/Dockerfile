FROM django

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . .
CMD python3 manage.py migrate --settings config.dev && \
    python3 manage.py collectstatic --settings config.dev && \
    uwsgi --ini uwsgi.ini && \
    celery -A my_async_tasks.celery_instance worker -l info && \
    celery -A my_async_tasks.celery_instance beat -l info
