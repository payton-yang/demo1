FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY ops/sources.list /etc/apt/sources.list
RUN  rm -Rf /var/lib/apt/lists/* && apt-get update && \
     pip config set global.index-url https://pypi.douban.com/simple/ && \
     pip install --no-cache-dir -r requirements.txt
COPY . .
CMD python manage.py migrate --settings config.prod && \
    cp ops/supervisor /etc/supervisor && \
    supervisord -c /etc/supervisor/supervisord.conf && \
    supervisorctl reread && \
    supervisorctl update
