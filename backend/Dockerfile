FROM python:3.7.5-slim-buster

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY backend/. .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8001 --access-logfile - "cow_say.app:create_app()"
