FROM python:3.8.2-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=myapp.py
EXPOSE 5000
CMD [ "python", "myapp.py" ]

# you should provide the enviroment value of DATABASE_URL