FROM python:3.8

WORKDIR /wct-api

COPY . /wct-api
COPY pyproject.toml /wct-api
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["python", "manage.py", "start-server"]

EXPOSE 8000
