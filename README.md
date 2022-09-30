# Run app localy
=> flask run

# Build with docker
=> docker build -t rest-apis-flask-python .

-t : tags

After that you will find images in docker desktop 
and you could run it on the docker desktop app
or by commande line 
=> docker run -p 5002:5000 rest-apis-flask-python

add '-d' to run it in the background to not use anoter terminal

# Install all dependencies
pip install -r requirements.txt