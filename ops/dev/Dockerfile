FROM django

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . .
CMD python3 manage.py migrate --settings config.dev && \
    uwsgi -d --ini uwsgi.ini && \
    nohup & celery -A my_async_tasks.celery_instance worker -l info && \
    nohup & celery -A my_async_tasks.celery_instance beat -l info
