FROM python

WORKDIR /app

COPY . .

RUN pip install -r ./crud/requirements.txt

WORKDIR /app/crud

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]