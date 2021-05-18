FROM gcr.io/google_appengine/python:latest
WORKDIR /app
COPY requirement.txt /app
RUN pip install -r requirement.txt
EXPOSE 50051
COPY . /app
CMD ["python", "server/server.py"]
