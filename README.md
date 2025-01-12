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

python manage.py createsuperuser
superuser email = bzdybel.sem03@gmail.com
passwd= Bozena1234

from profiles_api.models import UserProfile
user = UserProfile.objects.get(email='bzdybel.sem03@gmail.com')  # Replace with the email of the user you are testing
print(user.check_password('Bozena1234'))

(env) vagrant@ubuntu-bionic:/vagrant$ python manage.py shell
P
>>> user.check_password('Bozena1234')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'user' is not defined
>>> from profiles_api.models import UserProfile
>>> user = UserProfile.objects.get(email='bzdybel.sem03@gmail.com')  # Replace with the email of the user you are testing
>>> print(user.check_password('Bozena1234'))
True
>>> print("Is Staff:", user.is_staff)
Is Staff: False
>>> print("Is Active:", user.is_active)
Is Active: True

from profiles_api.models import UserProfile
# Find the superuser by email (or another unique identifier)
superuser = UserProfile.objects.get(email='bzdybel.sem03@gmail.com')
superuser.delete()
print("Superuser deleted successfully.")


django chrome nie chcial wstac python manage.py runserver 0.0.0.0:8000 --verbosity 3 ->ruszylo

python manage.py changepassword bzdybel.sem03@gmail.com ->
