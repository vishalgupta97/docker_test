FROM python

RUN pip install flask

# copy all files to /app
ADD https://raw.githubusercontent.com/juniorojha/docker-session/master/flask/app.py /app/

#WORKDIR /app
# expose port
EXPOSE 5000

# run python
ENTRYPOINT ["python", "/app/app.py"]
