[Link to the Application](https://corpse-corp.adaptable.app)

## Setup Django
### 1)Set up a directory and use a virtual environment:
Buatlah direktori baru untuk proyek Anda. Gunakan virtual environment menggunakan tools seperti venv atau virtualenv. Virtual environment akan memisahkan dependensi proyek Anda dari lingkungan Python sistem, memastikan konsistensi dan menghindari konflik dengan proyek lain. Langkah ini penting karena setiap proyek mungkin membutuhkan versi library dan package yang berbeda.

### 2)Install necessary tools and libraries:
Buatlah file `requirements.txt` yang berisi daftar library dan package yang dibutuhkan untuk proyek Django Anda dan masukkan yang berikut:
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Anda dapat menginstal dependensi ini menggunakan package manager pip dengan menjalankan perintah `pip install -r requirements.txt`. Pastikan untuk secara teratur memperbarui file ini saat proyek Anda berkembang dan dependensi baru ditambahkan.

### 3)Run the django-admin command to create a new Django app:
Buka terminal atau command prompt dan navigasikan ke direktori proyek Anda. 
Jalankan perintah berikut untuk membuat aplikasi Django baru: `django-admin startapp appname `
Gantilah appname dengan nama yang diinginkan untuk aplikasi Anda.

### 4)Set the allowed hosts in the settings.py file:
Buka file `settings.py` yang terletak di folder proyek Anda. 
Temukan variabel `ALLOWED_HOSTS` dan tambahkan nama host atau alamat IP yang diizinkan untuk mengakses aplikasi Django Anda. 
Langkah ini penting untuk alasan keamanan, karena membantu mencegah akses yang tidak sah. 
Anda dapat mengaturnya hingga semua orang bisa dengan melakukan hal berikut:
```
...
ALLOWED_HOSTS = ["*"]
...
```

### 5)Create a .gitignore file:
Buatlah file `.gitignore` di direktori utama proyek Anda. Tambahkan detail yang diperlukan untuk mengabaikan file dan direktori yang tidak perlu dilacak oleh version control. Biasanya termasuk file seperti file database, file yang dihasilkan, dan informasi sensitif. Contoh file `.gitignore`
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```


### 6)Link your project to a GitHub repository:
Buat repositori baru di GitHub. 
Inisialisasi repositori Git di direktori proyek Anda menggunakan perintah `git init`
Tambahkan file proyek Anda ke repositori Git menggunakan `git add .`
Commit perubahan menggunakan ` commit -m "Initial commit"`
Setel remote origin ke repositori GitHub Anda menggunakan `git remote add origin <repository-url>`
Push kode ke repositori remote menggunakan `git push -u origin master.in master`

### 7)Connect your app to an adaptable account:
Buka [Adaptable](https://adaptable.io) dan masuk dengan akun GitHub Anda. 
Pilih opsi membuat aplikasi baru, lalu pilih repositori proyek aplikasi Anda.
Pilih branch yang ingin dijadikan sebagai deployment branch.
Atur sesuai kebutuhan Anda, lalu deploy aplikasi Anda.

diatur sesuai kebutuhanmu lalu deploy aplikasimu. Contoh settingan yang bisa dipakai:
```
Pilihlah Python App Template sebagai template deployment, PostgreSQL sebagai tipe basis data yang akan digunakan, versi Python dengan spesifikasi aplikasimu.
Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn shopping_list.wsgi.
Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.
```

### Start making the MVT
Use the startapp command to create a new Django app within your project: `python manage.py startapp main`
Update the INSTALLED_APPS list in the `settings.py` file to include the newly created app. Like the following:
```
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
Create a `templates` folder inside the app directory and add HTML templates for your web pages.
Customize the HTML templates to suit your needs. You can use Django template tags and filters to dynamically render data in the templates.

### Define models for the database:
Open the `models.py` file inside your app directory.
Define the necessary models using Django's model fields and relationships. Models represent database tables and their relationships.Example of one:
```
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
```
Run the migration command (`python manage.py makemigrations` and `python manage.py migrate`) to create or update the database schema based on your models.

### Connect views and templates:
Open the `views.py` file inside your app directory.
Define view functions or classes that handle HTTP requests and render templates.
Use the Django template system to connect the views with the corresponding HTML templates.
Create URL patterns in the urls.py file inside your app directory to map URLs to the appropriate view functions or classes.
