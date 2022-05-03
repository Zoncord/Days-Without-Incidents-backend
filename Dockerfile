FROM python:3.6

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
WORKDIR .
COPY poetry.lock pyproject.toml
RUN poetry install --no-dev

CMD ["python", "manage.py", 'runserver']