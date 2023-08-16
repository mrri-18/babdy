FROM python:3.9.0


WORKDIR /home/

RUN git clone https://github.com/mrri-18/babdy.git

WORKDIR /home/babdy/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-w%rd#b%^86a5&dre9)wal^$f(gy&qm_i3zzd8hu+79+l!v300i" > .env

RUN python manage.py migrate

RUN echo yes | python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn","babdmay.wsgi","--bind","0.0.0.0:8000"]

