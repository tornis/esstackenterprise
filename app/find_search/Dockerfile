FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev postgresql-dev
RUN mkdir /opt/find_search
COPY . /opt/find_search/
WORKDIR /opt/find_search
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .build-deps
ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]



