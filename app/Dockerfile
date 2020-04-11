FROM python:3.8.2-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh", "start.sh" ]

# enviroment value of DATABASE_URL must be provided!!!
# remember that you should run alembic upgrade head to initialize the database!!!
# BASE_URL is required.
# PLAYLIST_ID is required if you don't provide it in args