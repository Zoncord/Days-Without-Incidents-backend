FROM python:3.9-alpine
MAINTAINER Firsov Kirill <kirill.firsov@zoncord.tech>
WORKDIR .

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

RUN pip install 'poetry'

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD python manage.py migrate
CMD python manage.py collectstatic
