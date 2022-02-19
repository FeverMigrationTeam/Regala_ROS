FROM python:3
WORKDIR /app
ADD . app
RUN apt-get update && apt-get install -y default-mysql-client && apt-get install redis-server; exit 0
RUN pip install -r requirements.txt
CMD ["uwsgi", "uwsgi.ini"]
