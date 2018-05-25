Docker image for running Flask Application.

Using this image :-

docker run -d -p 5000:5000 -v %cd%:/app vishal97/flask

Execute the above command from the root directory of the project having app.py . Port 5000 is exposed by the container.