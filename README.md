<p align="center">
  <img src="https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/211f229c-1df5-4496-b289-316b118656cf" />
</p>

[Link to the Application](https://corpse-corp.adaptable.app)
# Week 01
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
```python
...
ALLOWED_HOSTS = ["*"]
...
```


### 5)Create a .gitignore file:
Buatlah file `.gitignore` di direktori utama proyek Anda. Tambahkan detail yang diperlukan untuk mengabaikan file dan direktori yang tidak perlu dilacak oleh version control. Biasanya termasuk file seperti file database, file yang dihasilkan, dan informasi sensitif. `.gitignore` bisa dilihat di tutorial.


### 6)Link your project to a GitHub repository:
+ Buat repositori baru di GitHub. 
+ Inisialisasi repositori Git di direktori proyek Anda menggunakan perintah `git init`
+ Tambahkan file proyek Anda ke repositori Git menggunakan `git add .`
+ Commit perubahan menggunakan ` commit -m "Initial commit"`
+ Setel remote origin ke repositori GitHub Anda menggunakan `git remote add origin <repository-url>`
+ Push kode ke repositori remote menggunakan `git push -u origin master.in master`


### 7)Connect your app to an adaptable account:
Buka [Adaptable](https://adaptable.io) dan masuk dengan akun GitHub Anda. 
Pilih opsi membuat aplikasi baru, lalu pilih repositori proyek aplikasi Anda.
Pilih branch yang ingin dijadikan sebagai deployment branch.
Atur sesuai kebutuhan Anda, lalu deploy aplikasi Anda.

diatur sesuai kebutuhanmu lalu deploy aplikasimu. Contoh settingan yang bisa dipakai:

+ Pilihlah Python App Template sebagai template deployment, PostgreSQL sebagai tipe basis data yang akan digunakan, versi Python dengan spesifikasi aplikasimu.
+ Pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn appname.wsgi.
+ Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
+ Centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses deployment aplikasi.


## Start making the MVT
Gunakan perintah startapp untuk membuat aplikasi Django baru dalam proyek Anda: `python manage.py startapp main`.(main bisa diganti dengan nama yang anda ingin tetapi untuk sekarang akan dikatakan main). 
Ini akan membuat sebuah folder bernama `main`. 
Perbarui daftar `INSTALLED_APPS` di file `settings.py` untuk mencakup aplikasi yang baru saja dibuat. Contohnya:
```python
INSTALLED_APPS = [
    ...,
    'main',
    ...
]
```
Buat folder `templates` di dalam direktori aplikasi dan tambahkan template HTML untuk halaman web Anda. Sesuaikan template HTML agar sesuai dengan kebutuhan Anda. Anda dapat menggunakan Django template tags dan filters untuk merender data secara dinamis di template.Contoh: isi file htmlnya didalam `templates`:
```html
<h5>Name: </h5>
<p>Pak Bepe</p> <!-- Ubahlah sesuai dengan nama kamu -->
<h5>Class: </h5>
<p>PBP A</p> <!-- Ubahlah sesuai dengan kelas kamu -->
```


### Define models for the database:
Buka file `models.py` di dalam direktori aplikasi. 
Tentukan model-model yang diperlukan menggunakan field dan relasi model Django. 
Model mewakili tabel-tabel database dan relasinya. Contoh model sederhana:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
```
Jalankan perintah migrasi (`python manage.py makemigrations` dan `python manage.py migrate`) untuk membuat atau memperbarui skema database berdasarkan model-model Anda.


### Connect views and templates:
Buka file `urls.py` yang di  dalam folder `main`: lalu akan ditambahkan sebuat import dan fungsi yang akan bisa menampilkan secara dinamis:
```python
from django.shortcuts import render


def show_main(request):
    context = {
        'exampleVariableA': 'Dictionary',
        'exampleVariableB': 'Dictionary2'
    }

    return render(request, "main.html", context)
```
Lalu buka folder html anda dan bisa diubah isi bagian yang ingin ditampilkan secara dinamis. Contoh:
```html
...
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
...
```


### Configurating the URL Routing
Pertama buka file `urls.py` yang di dalam folder `main` lalu masukkan kode berikut:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Ini akan mengonfigurasi url ke applikasi `main`.

Lalu buka file `urls.py` yang di **luar** `main` dan masukkan kode berikut agar bisa mengonfigurasi url ke Proyekmu:
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
+ Untuk ngecheck apabila bekerja bisa jalankan proyek Django dengan perintah `python manage.py runserver`. Lalu buka link yang dibalikkan setelah dijalankan command didalam browsermu.


## Bagan Applikasi Web Berbasis Django
<p align="center">
  <img src="https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/ba0a6842-3bc7-4ecb-af16-cce9e9ef3b9c" />
</p>

HTTP Request:
+ Ketika seorang pengguna melakukan permintaan HTTP ke aplikasi Django, permintaan tersebut diterima oleh server web.Server web meneruskan permintaan ke Django framework.


URLs (`urls.py`):
+ Django menggunakan berkas urls.py untuk memetakan URL ke tampilan.
Dalam berkas urls.py, Anda mendefinisikan pola URL menggunakan fungsi path() dari modul django.urls.


Views (`views.py`):
+ Tampilan bertanggung jawab untuk memproses permintaan pengguna dan mengembalikan respons.
+ Dalam Django, tampilan dapat diimplementasikan sebagai fungsi atau tampilan berbasis kelas.
+ Tampilan berinteraksi dengan model untuk mengambil atau memperbarui data dari basis data.
+ Tampilan juga dapat menjalankan logika bisnis dan merender template untuk menghasilkan respons HTML.


Model (`models.py`):
+ Model mendefinisikan struktur dan perilaku data dalam aplikasi.
+ Setiap model dalam Django sesuai dengan tabel basis data dan mendefinisikan bidang dan hubungan.
+ Model menyediakan lapisan abstraksi untuk berinteraksi dengan basis data, memungkinkan Anda melakukan operasi CRUD (Create, Read, Update, Delete) pada data.


Template (HTML):
+ Template digunakan untuk menghasilkan respons HTML dinamis.
+ Template adalah berkas HTML yang dapat mencakup variabel, perulangan, kondisional, dan tag template lainnya.
+ Template dirender oleh tampilan, yang meneruskan data dari model ke template.
+ Django menyediakan mesin template yang memproses template dan menggantikan variabel dan tag dengan nilai aktual.
+ Template yang telah dirender dimasukkan dalam respons HTTP yang dikirimkan kembali kepada pengguna.

  
Respons HTTP:
+ Respons yang dihasilkan oleh tampilan, termasuk template yang telah dirender atau jenis respons lainnya, dikirimkan kembali kepada pengguna sebagai respons HTTP.
+ Server web menerima respons tersebut dan mengirimkannya ke browser pengguna.


## Virtual Enviroment 
Virtual environment akan memisahkan dependensi proyek Anda dari lingkungan Python sistem, memastikan konsistensi dan menghindari konflik dengan proyek lain. Langkah ini sangat penting karena setiap proyek mungkin membutuhkan versi library dan package yang berbeda. Meskipun memungkinkan untuk tidak menggunakan virtual environment, ini bukan pilihan ideal untuk pengembangan proyek Anda.


## MVC, MVT, MVVM
Model-View-Controller (MVC):
+ MVC adalah pola arsitektur yang memisahkan aplikasi menjadi tiga komponen utama: Model, View, dan Controller. 
+ Model menggambarkan data dan logika bisnis aplikasi.
+ View bertanggung jawab untuk menghadirkan antarmuka pengguna.
+ Controller menangani masukan pengguna, memperbarui Model, dan berkomunikasi dengan View.
+ Model tidak memahami View atau Controller, perubahan di View atau Controller dikomunikasikan melalui event notifications.


Model-View-Template (MVT):
+ Seperti MVC, MVT memisahkan aplikasi menjadi tiga komponen utama: Model, View, dan Template.
+ Model menggambarkan data dan logika bisnis, berinteraksi dengan basis data.
+ View menangani permintaan pengguna, memproses data dari Model, dan merender Template.
+ Template adalah berkas HTML yang mendefinisikan struktur dan tampilan antarmuka pengguna.
+ MVT mengikuti siklus permintaan-respons, pengguna membuat permintaan HTTP, View memproses permintaan, mengambil data dari Model, merender Template, dan mengirimkan respons HTTP kembali kepada pengguna.


Model-View-ViewModel (MVVM):
+ MVVM memisahkan aplikasi menjadi tiga komponen utama: Model, View, dan ViewModel.
+ Model menggambarkan data dan logika bisnis, mirip dengan MVC dan MVT.
+ View bertanggung jawab atas antarmuka pengguna, tetapi memiliki peran pasif dan tidak berinteraksi langsung dengan Model.
+ ViewModel bertindak sebagai perantara antara Model dan View. ViewModel mengekspos data dan logika Model ke View, memudahkan kerja.
MVVM juga mendukung pengikatan data dua arah, di mana perubahan di View secara otomatis disebarkan ke ViewModel dan sebaliknya. 


Perbedaan antara MVC, MVT, dan MVVM:
+ Dalam MVC, Controller berperan sebagai mediator antara Model dan View, sedangkan dalam MVT, View menangani permintaan pengguna dan berinteraksi dengan Model.
+ Dalam MVVM, ViewModel berfungsi sebagai perantara antara Model dan View. MVC dan MVT umumnya digunakan dalam aplikasi web, sementara MVVM sering digunakan dalam kerangka kerja UI modern.
+ MVC dan MVT mengikuti siklus permintaan-respons, sedangkan MVVM lebih berorientasi pada peristiwa dan mendukung pengikatan data dua arah.

# Week 02
* Unrelated Note: Untuk memudahkan akan mengubah path url yang di dalam `urls.py` di dalam applikasi menjadi sebagai berikut agar dapat langsung menampilkan main: 

     `path('', include('main.urls')),`

## Implementing Form dan Data Delivery

### 1)Make a Skeleton for Views and Connect them
Buat sebuah html file baru bernama `base.html` di dalam folder baru bernama `templates` terletak di dalam root folder yang berfungsi sebagai template dasar untuk halaman web lain dlm proyek serta dengan isi:
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
Buka `settings.py` dalam applikasi dan tambahkan `base.html` agar terdeteksi:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
```

Buka `main.html` didalam `main/templates` dan menggunakan template `base.html`. contohnya:
```html
{% extends 'base.html' %}

{% block content %}
    <h1>App list</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```
### 2)Make a form of input of items to the HTML
+ Buat file baru bernama `forms.py` dan isi sesuai dengan model databasemu. contoh:
```python
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name","species", "amount","causeOfDeath","spiritStatus","description"]
```

+ Buat sebuah fungsi di dalam `main/views.py` yang akan menambahkan hasil dari form, example:
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
serta ubah fungsi `show_main` sebagai berikut:  
```python
def show_main(request):
    items = Item.objects.all() //Grabs all the objects from the database

    context = {
        'name': 'Example1`', # Nama kamu
        'class': 'Example2', # Kelas PBP kamu
        'products': items,
    }

    return render(request, "main.html", context)
```

+ Buka `main/urls.py` lalu import  `create_product` dan menambah ke dalam `urlpatterns`
```
path('create-product', create_product, name='create_product'),
```
+ buat sebuah html file agar ada page khusus untuk input data, misalnya `create_product.html ` di dalam `main/templates` dengan isi sebagai berikut:
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

Untuk nanti menampilkan data (belum keliatan karena masih hanya input) bisa di edit `main/templates/main.html` agar ada tabel yang menampilkan input dari database, example:
tambahkan kode berikut pada bagian setelah `{% block content %}` :
```html
...

        {% comment %} Below is how to show the product data {% endcomment %}
    
        {% for item in products %} 
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.species}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.causeOfDeath}}</td>
                <td>{{item.spiritStatus}}</td>
                <td>{{item.description}}</td>
                <td>{{item.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    

{% endblock content %}
```

### 3)Returning Data with XML, XML+ ID, JSON and JSON+ID
+ XML<br>
Pertama ke `main/views.py` dan import beberapa hal dan juga menambahkan fungsi untuk menyimpan hasil query dari seluruh data dan fungsi satu lagi untuk return dalam bentuk xml: example:
```python
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Item.objects.all()
    
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
>Bisa di ubah data menjadi `data = Item.objects.filter(pk=id)` jika ingin mengembalikan data dengan ID pada fungsi show_xml dengan return

Lalu bisa diconnect ke path `url_patterns` untuk mengakses hasil dari fungsi, contoh:
```
from main.views import show_main, create_product, show_xml 

//tambahkan ke dalam url_patterns
...
path('xml/', show_xml, name='show_xml'),    
...

```
+ JSON<br>
Pertama ke `main/views.py` dan import beberapa hal dan juga menambahkan fungsi untuk menyimpan hasil query dari seluruh data dan fungsi satu lagi untuk return dalam bentuk JSON: example:
```python
def show_json(request):
    data = Item.objects.all()
    
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
```
>Bisa di ubah data menjadi `data = Item.objects.filter(pk=id)` jika ingin mengembalikan data dengan ID pada fungsi show_json dengan return

Lalu bisa diconnect ke path `url_patterns` untuk mengakses hasil dari fungsi, contoh:
```python
from main.views import show_main, create_product, show_xml, show_json

//tambahkan ke dalam url_patterns
...
path('json/', show_json, name='show_json'), 
...

```
## Perbedaan antara form POST dan form GET dalam Django
### Form GET:

+ Form GET mengirimkan data dalam bentuk string dan menggunakannya untuk membuat URL yang mengandung alamat tempat data harus dikirimkan, serta kunci dan nilai data. 
+ Form GET lebih umum digunakan untuk mengambil data dari server.
### Form POST:

+ Form POST digunakan untuk mengirimkan data yang dapat digunakan untuk mengubah status sistem, misalnya mengubah data dalam database.
+ Form POST mengirimkan data dalam bentuk yang lebih aman dibandingkan dengan Form GET, karena data yang dikirimkan tidak terlihat secara langsung dalam URL.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
Secara umum, XML, JSON, dan HTML memiliki peran mereka masing-masing dalam konteks pengiriman dan penyajian data. XML dan JSON biasanya digunakan untuk pertukaran data antara server dan klien, sementara HTML digunakan untuk struktur dan presentasi data di sisi klien.

### HTML:

+ HTML adalah bahasa markup standar untuk membuat halaman web dan aplikasi.
+ HTML digunakan untuk membangun struktur dan tampilan halaman web. Pada HTML tag telah ditentukan sebelumnya dan user tidak memiliki fleksibilitas untuk membuat tag mereka sendiri seperti pada XML dan JSON dalam hal menyimpan data.
+ HTML lebih cocok untuk menampilkan data secara visual kepada user.

### XML:
+ XML adalah bahasa markup yang mendefinisikan serangkaian aturan untuk pengkodean dokumen dalam format yang dapat dibaca oleh mesin dan manusia.
+ XML menggunakan struktur pohon dengan namespace untuk kategori data yang berbeda. Namespace digunakan untuk menghindari konflik antara elemen dan atribut dengan nama yang sama dalam dokumen XML.
+ XML mendukung berbagai jenis data seperti string, integer, boolean, date, image, namespace, dan custom types sesuai kebutuhan

### JSON:
+ JSON adalah format pertukaran data ringan yang mudah dibaca dan ditulis oleh manusia, serta mudah diurai dan dibuat oleh mesin.
+ JSON menggunakan struktur seperti dictionary pada python yaitu dengan pasangan key-value, sehingga JSON lebih sederhana dan memiliki sintaks yang lebih ringkas dibanding XML medium.com.
+ JSON lebih umum digunakan dalam pengembangan aplikasi web dan API karena dukungan yang kuat dari JavaScript.

## Penggunaan JSON dalam pertukaran data antara aplikasi web modern
JSON mudah dipelajari dan sederhana untuk dibaca dan dipahami. Selain itu, formatnya hanya berupa teks, sehingga dapat dengan mudah dikirim melalui server. Bahkan, aplikasi web lebih memilih JSON daripada XML karena lebih cepat dan lebih mudah untuk diurai. Beberapa hal yang membuat orang lebih memilih menggunakan JSON sebagai berikut:

**Cepat dan Efisien**<br>
Sintaks JSON cukup sederhana dan dapat menjelaskan dirinya sendiri secara bersamaan. Bahkan aplikasi yang tidak tahu jenis data apa yang diharapkan dapat menginterpretasikan JSON. Sintaksnya cukup mudah dipahami. Data berada dalam pasangan kunci-nilai, di mana titik dua memisahkan nama bidang dan nilainya.
Selain itu, JSON ringan dan kompak. Oleh karena itu, data yang sama dalam format JSON akan hampir dua pertiga dari XML. 

**Responsif**<br>
JSON adalah format data yang mudah diurai. Kelebihan dari penguraian JSON di sisi server adalah meningkatkan responsivitas. Dengan demikian, klien dapat mendapatkan respons lebih cepat terhadap pertanyaan mereka. Untuk alasan ini, JSON secara luas diadopsi sebagai format pertukaran data standar. 

***Key-Value Pair Approach***<br>
*Apporach* kunci/nilai yang digunakan oleh JSON membuatnya menjadi format data yang sederhana. Ini juga menyederhanakan operasi menulis dan membaca.

**Berbagi Data**<br>
Dari beberapa fungsi JSON, yang paling mencolok adalah berbagi data. Ini digunakan untuk menjalin koneksi antara bahasa front-end dan back-end untuk berbagi data. Pertama, bahasa front-end dikonversi menjadi teks JSON, yang dikenal sebagai serialisasi. Kemudian, teks JSON dikonversi menjadi data pemrograman, yang dikenal sebagai deserialisasi. Proses serialisasi dan deserialisasi cukup cepat dalam JSON, sehingga mempromosikan berbagi data terstruktur.

**Dukungan Browser yang Luas**<br>
 Beberapa browser yang mendukung JSON adalah Chrome 3 ke atas, Internet Explorer 8 ke atas, Safari 4 ke atas, Firefox 3.5 ke atas, dan Opera 10.5 ke atas.
 
## Postman Screenshot of the URL Access to the 5 Function (HTML, XML, XML ID, JSON, JSON ID)

**HTML**<br>
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/89521b0a-9b94-45a3-b54b-1c9b39db9a88)

**XML**<br>
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/822f8469-f2b7-4ecc-839e-f237d33b236b)

**XML ID**<br>
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/58d0a0a0-dd2e-481c-a9ca-2ea3e0867479)

**JSON**<br>
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/2867bbad-0cae-47bb-a816-035afc8dd836)

**JSON ID**<br>
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/613636f5-04b6-406c-8509-f01d971fb32a)

# Tugas 04
## Implementing Registration, Loging and Logout for users
### 1)Creating a Form for User Registration
Pertama kita harus masuk ke dalam `main/views.py` lalu tambahkan import dan fungsi berikut yang akan membuat formulir pendaftaran secara otomatis. Jika data pendaftaran dikirimkan, akun user akan terbuat:
```python
#Imports
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

#Functions
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Lalu kita harus buat sebuah file html untuk `register.html` yang akan ditaro didalam `main/templates` folder. Seperti berikut:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Dan seperti biasa dengan membuat page baru kita harus connect ke dalam `main/urls.py`
```python
#Add the function as import
from main.views import register

#Inside urlpatterns add the following
path('login/', login_user, name='login'),
```

### 2)Making a login function
Untuk membuat fungsi kita perlu import beberapa fungsi dari django, dan membuat sebuah fungsi yang mengautentikasi sebuah user dan redirect ke dalam main web page. Contoh:
```python
#Nessecary imports
from django.contrib.auth import authenticate, login

#Example of function
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Sebelum selesai dengan login kita harus buat sebuah html untuk menampilkan halaman login dengan membuat `login.html` yang berada didalam folder `main/templates`. Contoh:
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
Lalu seperti biasa connect ke dalam `main/urls.py`:
```python
#Import
from main.views import login_user
```
```python
#Add in urlpatterns:
path('login/', login_user, name='login'),
```

### 3)Making a logout function
Untuk membuat fungsi logout kita butuh import dari django lagi dan membuat sebuah fungsi untuk logout didalam `main/view.py` sebagai berikut:
```python
#Import
from django.contrib.auth import logout

#Add ogout function
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Pemanggilan logout function terjadi ketika logged in user memencet tombol logout didalam `main/templates/main.html`, maka tambahkan kode berikut:
```html
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

Lalu connect ke dalam `main/urls.py` dan tambahkan berikut:
```python
#Add Import
from main.views import logout_user

#Add to urlpatterns
path('logout/', logout_user, name='logout'),
```

## Restricting Access to only logged in user
Didalam `main/views.py` import berikut dan pastikan ditaruh sebelum kode yang akan menampilkan halaman yang hanya bisa diakses oleh logged in user contoh:
```python
#Necessary Import
from django.contrib.auth.decorators import login_required

#Add this before the thing you want to show to logged in user
@login_required(login_url='/login')
def somerandomfunction(request):
...

```

## Making use of Cookies
Kita bisa mengguankan data dari cookies untuk misalnya membuat sebuah data yang menampilkan fitur last login.
Pertama kita masukan `import datetime` kedalam `main/views.py` dan pada fungsi `login_user` kita akan ubah menjadi sebagai berikut:
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        #Bagian yang diganti
        if user is not None:   
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Lalu pada fungsi `show_main` tambahkan `'last_login': request.COOKIES['last_login'],` di dalam context.Serta edit fungsi `logout_user` menjadai sebagai berikut:
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Terakhir untuk menampilkan datanya kita bisa edit `main/templates/main.html` dan tambahkan `{{ last_login }}`. Contoh:
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

## Making each User have have their own product
Untuk melakukan ini kita harus masuk ke dalam `main/models.py` dan edit `models.py` dengan menambahkan sebuah import dan tambah data user. Contoh:
```python
#Add this Import
from django.contrib.auth.models import User

#Add inside Item
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ...
```
Selanjutnya, kita harus edit fungsi  `show_main` dan `create_product` agar sebagai berikut:
```python
#Display main web page
def show_main(request):
    #Change this
    items = Item.objects.filter(user=request.user)
    ...
    
    context = {
        #Change this
        'name': request.user.username,
        ...
    }
    
#Modify create prodcut to save data into respective user
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        userItem = form.save(commit=False)
        userItem.user = request.user
        userItem.save()
        return HttpResponseRedirect(reverse('main:show_main'))'
        ...
```

> Make sure to always run `python manage.py makemigrations` and `python manage.py migrate` to save changes to the model

### Example:
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/98a9527f-77f2-4513-848f-751dbd1ed985)
![image](https://github.com/Hilmy224/shopping-list-TaskVersion/assets/108089955/cb2d8fa4-7174-4110-8c0a-7df36159a692)


##  Django UserCreationForm Pros and Cons
Django `UserCreationForm` adalah sebuah _class_ form yang termasuk kedalam sistem autentikasi Django yang digunakan untuk mebuat sebuah user account baru.<br>
**Pros:**
+ UserCreationForm Django dibangun ke dalam sistem otentikasi Django, yang berarti Anda tidak perlu menulis formulir dan kode validasi Anda sendiri untuk membuat pengguna baru. Ini dapat menghemat banyak waktu dan upaya.
+ UserCreationForm Django menyertakan fitur keamanan bawaan. Sebagai contoh, secara otomatis meng-hash kata sandi pengguna, yang melindunginya agar tidak disimpan dalam teks biasa. Ini juga menyediakan validasi untuk bidang nama pengguna dan kata sandi, membantu mencegah kesalahan keamanan yang umum terjadi pada data-flair.training.
+ UserCreationForm Django mudah digunakan, baik untuk pengembang maupun pengguna. Bagi para pengembang, ini menyediakan API yang sederhana dan mudah. Bagi pengguna, ini menyediakan formulir yang jelas dan mudah digunakan untuk membuat akun baru dzone.com.

**Cons**
+ UserCreationForm Django didesain untuk menangani kasus penggunaan yang paling umum untuk membuat akun pengguna baru. Jika Anda perlu mengumpulkan informasi tambahan dari pengguna (seperti alamat email, nama lengkap, dan lain-lain), Anda perlu memperluas UserCreationForm atau membuat formulir sendiri. Hal ini dapat menambah kerumitan pada kode Anda.
+ UserCreationForm Django merupakan bagian dari sistem autentikasi Django, yang berarti bergantung pada bagian lain dari sistem tersebut. Jika Anda ingin menggunakan sistem autentikasi yang berbeda, atau jika Anda ingin menyesuaikan sistem autentikasi Django dengan cara yang tidak didukung oleh UserCreationForm, Anda mungkin akan mengalami kesulitan.

## Diffrence between authentication and authorization in Django
+  Authentication di Django adalah proses verifikasi identitas `user`. Ini mengonfirmasi bahwa `user` adalah orang yang mereka klaim. Hal ini biasanya dilakukan melalui nama pengguna dan kata sandi, tetapi sistem otentikasi Django fleksibel dan memungkinkan metode lain juga
+ Authorization di Django, menentukan apa yang boleh dilakukan oleh `authenticated user`.Ini melibatkan izin yang mengindikasikan operasi apa (seperti melihat, menambah, mengubah, atau menghapus) yang dapat dilakukan pengguna pada objek tertentu

## Web Cookies and How Django uses them
**Cookies** dalam sebuah aplikasi web merupakan data kecil yang disimpan oleh browser anda dan dikirim dengan setiap `HTTP Request`. **Cookies** digunakan untuk mengingat informasi tentang user seperti preferences, authentication status, dan session-related data

Django menggunakan cookie untuk mengelola sesi data pengguna. *Session framework* memungkinkan Anda untuk menyimpan dan mengambil data sewenang-wenang pada basis per-pengunjung situs. Secara default, Django menggunakan **session cookies** untuk menyimpan data sesi, yang berarti bahwa data aktual disimpan di sisi server, sedangkan cookie sisi klien berisi ID sesi untuk identifikasi.
>To set and get cookies in Django, you can use the set_cookie and get methods on the request and response objects

## Cookies Safe?
Cookie pada umumnya aman digunakan dalam pengembangan web, namun memiliki potensi risiko keamanan dan privasi. Berikut ini beberapa hal yang perlu diperhatikan saat menggunakan cookie resources:

+ Sensitive Information: Cookie tidak boleh digunakan untuk menyimpan informasi sensitif, seperti kata sandi atau nomor kartu kredit. Jika penyerang berhasil mencuri cookie, mereka dapat memperoleh akses ke informasi sensitif yang ada di dalamnya resources.
+ Secure Flag: Jika situs web Anda menggunakan HTTPS (which it should), pastikan cookie memiliki Secure Flag yang ditetapkan. Hal ini memastikan bahwa cookie hanya akan dikirim melalui koneksi terenkripsi, sehingga mengurangi risiko penyadapan oleh *third party*.
+ HttpOnly Flag: Menetapkan bendera HttpOnly pada cookie akan mencegah skrip sisi klien mengakses cookie. Hal ini dapat membantu mencegah serangan seperti Cross-Site Scripting (XSS), di mana penyerang dapat mencoba mengakses cookie melalui JavaScript.
+ SameSite Attribute: Atribut ini dapat membantu melindungi dari serangan **Cross-Site Request Forgery (CSRF)**. Atribut ini memungkinkan Anda untuk menyatakan bahwa cookie tidak boleh dikirim bersama dengan cross-site requests. Hal ini membantu mencegah penyerang mengelabui peramban pengguna untuk membuat permintaan ke situs web.
+ Expiration: Perhatikan waktu expiration cookie Anda. Memiliki waktu expiration yang lebih pendek dapat mengurangi risiko penyerang menggunakan cookie lama untuk mendapatkan akses pengembang.


# Tugas 04
## Styling the App
>In the app, I use a mixture of inline and external stylesheet
### 1)Adding External Styling Sheet
[Source](https://www.erprealm.com/codebase/getdata/add-external-css-file-to-django-template/)
<br>Intinya buat sebuah static folder dan sebuah file bernama `style.css` dalam folder applikasimu dan pastikan ada `{% load static %}` didalam file html serta sebuah link contohnya:
```html
    <!-- Link for boostrapCSS and script of javascript -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tulpen+One&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'style.css' %}">
```

Di dalam `style.css` bisa buat selector untuk styling.

### 2)Default Body Styling
Inside `base.html` that is the templates for other pages:
```html
<body class="please">
        {% block content %}
        {% endblock content %}
    </body>
```
Inside `style.css`:
```css
.please {
    background: #333;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: #c4c4c4;
  }
```

### 3)Specific Styling(Ex: Login)


The css selectors used to style `login.html`:
```css
 .form-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
  }

.login-font {
    font-family: 'Tulpen One',cursive;
    font-size: 120px;
    color:crimson;
    text-align: center;
}

.login-input{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 100%;
    color: #c4c4c4;
    justify-content: center;
    width: 100%;
}
.fill-button {
    background-color: #333;
    color: #c4c4c4;
    border: none;
    border-radius: 5px;
    display: block;
    width: 100%;
    height: 40px;
    transition: background-color 0.3s;
    margin-top: 10px;
  }
  
  .fill-button:hover {
    background-color:crimson;
  }
  
```

Putting those selectors in the HTML:
```html
{% block content %}

<div class="form-center">
    <div>
    <h1 class="login-font">COVENANT</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table class="login-input">
            <tr>
                <td>Username: </td>
            </tr>
            <tr>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
            <tr>
                <td>Password: </td>
            </tr>     
            <tr>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>
        </table>
        <input class="fill-button" type="submit" value="Enter Covenant">
    </form>

    {% if messages %}
        <ul style="font-size: 10px;">
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>   
    {% endif %}     
    <div style="margin-top: 30px; text-align: center;">
    Want exlusive gems when trading bodies?<br>
     <a href="{% url 'main:register' %}">Start a bloodpact now!!!</a>
    </div>
    </div>
</div>

{% endblock content %}
```

### 4) Decorating Main
I attempted to make a card system by making use of the `{% for item in products %}` by having a container for it we can make a item amount of cards inside the container example:
```html
<div class="card-deck">
        {% for item in products %}
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">{{ item.name }}</h5>
              <p class="card-text">Species: {{ item.species }}</p>
              <p class="card-text">Amount: {{ item.amount }}</p>
              <p class="card-text">Cause of Death: {{item.causeOfDeath}}</p>
              <p class="card-text">spiritStatus: {{item.spiritStatus}}</p>
              <p class="card-text">Description: {{item.description}}</p>
              <p class="card-text">Last Seen: {{item.date_added}}</p>
            </div>
          </div>
```

You can then stylize the class as you wish

### 5)Making an Edit Button
Open `main/views.py` and make a function that edit the values of the items:
```python
def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

Then make a page for editing said item by making a html file for it:
```html
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

As always connect  it to your `main/urls.py` by putting `from main.views import edit_product` and adding the path url `path('edit-product/<int:id>', edit_product, name='edit_product'),` into the urlpatterns.

Lastly make a button of sorts in `main.html`, for example:
```html
<a style="text-decoration: none;" href="{% url 'main:edit_product' item.pk %}">
    <button class="card-buttons">
    Button
    </button>
</a>
```

### 6)Delete Item Button
First make a `delete_product` function like so:
```python
def delete_product(request,id):
    if request.method == "POST":
        tempItem=Item.objects.get(pk=id)
        tempItem.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
And of course connect it in `urls.py` by putting:
```python
#Add this import 
from main.views import delete_product

#Add this path into urls pattern
path('deleteProduct/<int:id>/',delete_product,name='delete_product'),
```
Lastly put a button in the `main.html`, ex:
```html
<form method="post" action="{% url 'main:delete_product' item.id %}">
    {% csrf_token %}
    <button class="card-buttons" type="submit">⨻</button>
</form>
```

##  Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
## Jelaskan HTML5 Tag yang kamu ketahui.
## Jelaskan perbedaan antara margin dan padding.
## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
