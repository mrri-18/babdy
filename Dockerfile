FROM python:3.9.0


WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/mrri-18/babdy.git

WORKDIR /home/babdy/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-w%rd#b%^86a5&dre9)wal^$f(gy&qm_i3zzd8hu+79+l!v300i" > .env

RUN echo yes | python manage.py collectstatic

EXPOSE 8000

CMD ["bash","-c","python manage.py migrate --settings=babdmay.settings.deploy && gunicorn babdmay.wsgi --env DJANGO_SETTINGS_MODULE=babdmay.settings.deploy --bind 0.0.0.0:8000"]

