FROM python:3.8.3-alpine3.10

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY frontend/. .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "cow_say.app:create_app()"
