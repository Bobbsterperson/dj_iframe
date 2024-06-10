FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install pipenv

COPY Pipfile /code/
RUN pipenv install

COPY . /code/

EXPOSE 8000

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
