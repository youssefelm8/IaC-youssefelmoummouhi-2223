FROM python:latest 
RUN pip install flask
COPY ./static /home/docker_flask/static/
COPY ./templates /home/docker_flask/templates/
COPY ./flask_app.py /home/docker_flask/
EXPOSE 8008
CMD python /home/docker_flask/flask_app.py