#Install bundle from Docker registry with Flask, UWSGI and NGINX (Alpine Linux based and Python v.3.8).
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
COPY ./app /app
#Install bash shell and nano.
RUN apk --update add bash nano
#Set up environment variables for serve static content by NGINX (images, styles and more).
ENV STATIC_URL /static
ENV STATIC_PATH /app/app/static
#Install required python packages from requirements file.
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt