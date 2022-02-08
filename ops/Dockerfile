FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /mydata/app
COPY requirements.txt ./
COPY ops/sources.list /etc/apt/sources.list
RUN  rm -Rf /var/lib/apt/lists/* && apt-get update && \
     pip3 config set global.index-url https://pypi.douban.com/simple/ && pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD python3 manage.py migrate --settings config.dev && \
    uwsgi -d --ini uwsgi.ini && \
    nohup & celery -A my_tasks.celery_instance worker -l info && \
    nohup & celery -A my_tasks.celery_instance beat -l info
