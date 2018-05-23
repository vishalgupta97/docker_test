FROM python

RUN pip install flask

# copy all files to /app
#ADD . /app

WORKDIR /app
# expose port
EXPOSE 5000

# run python
ENTRYPOINT python app.py

#For building
#docker build -t flaskt .
#docker run -d --name flaskt -p 5006:5000 -v %cd%:/app flaskt