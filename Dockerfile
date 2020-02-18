FROM python:3.8-slim

ARG REDIRECT_TYPE
ARG REDIRECT_TARGET

ENV APP_HOME /app
ENV REDIRECT_TYPE=$REDIRECT_TYPE
ENV REDIRECT_TARGET=$REDIRECT_TARGET

WORKDIR $APP_HOME
COPY redirect.py ./

RUN pip install Flask gunicorn

CMD exec gunicorn --log-level DEBUG --bind :$PORT --workers 1 --threads 8 redirect:app
