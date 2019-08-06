FROM python:3.6-stretch

ENV FLASK_ENV=development
ENV FLASK_APP=app.py

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY app.py /
COPY start_server.sh /
COPY app /app

ENTRYPOINT ["/start_server.sh"]