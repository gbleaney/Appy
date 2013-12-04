##Get Python 2.7
<http://python.org>

##Navigate to this folder in cmd or terminal  
    cd appy_server

##Install modules
    pip install -r requirements.txt

##Run database migrations
    python manage.py syncdb
    python manage.py migrate appy

##Run server 
	python manage.py runserver
	<http://localhost:8000>