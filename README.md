#Profiles REST API
Course code.
vagrant up
vagrant ssh
To install venv
vagrant@ubuntu-bionic:~$ cd /vagrant/
vagrant@ubuntu-bionic:/vagrant$ python -m venv ~/env
vagrant@ubuntu-bionic:/vagrant$ source ~/env/bin/activate
(env) vagrant@ubuntu-bionic:/vagrant$ pip install -r requirements.txt

(env) vagrant@ubuntu-bionic:/vagrant$ django-admin.py startproject profiles_project .
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py startapp profiles_api
(env) vagrant@ubuntu-bionic:/vagrant$
(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py runserver 0.0.0.0:8000
Django version 2.2, using settings 'profiles_project.settings'
Starting development server at http://0.0.0.0:8000/
W chrome http://127.0.0.1:8000/

(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py makemigrations profiles_api
