FROM python:3.12.4-bookworm

# RUN pip3 install pipenv

# ENV PROJECT_DIR /usr/src/flaskbookapi

WORKDIR /workspace

# COPY Pipfile .
# COPY Pipfile.lock .
COPY . .

RUN pip install -r requirements.txt
ENV CONNECTION_STRING=foo

# RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

# CMD python api.py --host 0.0.0.0
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]