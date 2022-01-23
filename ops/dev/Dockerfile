FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list && rm -Rf /var/lib/apt/lists/* && apt-get update
RUN pip3 config set global.index-url https://pypi.douban.com/simple/ && pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD python3 manage.py migrate --settings config.dev && \
    python3 manage.py runserver 0.0.0.0:8000 --settings config.dev
