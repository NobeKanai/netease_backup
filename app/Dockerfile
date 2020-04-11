FROM python:3.8.2-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]

# enviroment value of DATABASE_URL must be provided!!!
# remember that you should run alembic upgrade head to initialize the database!!!
