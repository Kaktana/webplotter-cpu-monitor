FROM python:3.6

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pipenv
RUN pipenv install --deploy --system && pip uninstall -y pipenv
COPY . .
CMD python main.py


