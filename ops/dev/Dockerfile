FROM django

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY . .
CMD python3 manage.py migrate --settings config.dev && \
    mkdir static && python3 manage.py collectstatic --settings config.dev && \
    uwsgi --ini uwsgi.ini
