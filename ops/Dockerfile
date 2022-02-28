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
    cp -r ops/supervisor /etc/supervisor && \
    echo_supervisord_conf > /etc/supervisor/supervisord.conf && \
    supervisord && \
    supervisorctl reread && \
    supervisorctl update
