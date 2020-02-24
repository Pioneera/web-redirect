FROM python:3.8-slim

ARG REDIRECT_TYPE
ARG REDIRECT_TARGET
ARG GA

ENV APP_HOME /app
ENV REDIRECT_TYPE=$REDIRECT_TYPE
ENV REDIRECT_TARGET=$REDIRECT_TARGET
ENV GA=$GA

WORKDIR $APP_HOME
COPY redirect.py ./

RUN pip install Flask gunicorn pyga

CMD exec gunicorn --log-level info --bind :$PORT --workers 1 --threads 8 redirect:app
