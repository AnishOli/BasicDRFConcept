# Django REST Framework Basic API (GET) with Serializer

A simple **Django REST Framework project** demonstrating how to create a **GET API using a Class-Based View (APIView)** and a **Serializer**.

The serializer converts **complex data types (like dictionaries or models)** into **Python native datatypes**, which Django REST Framework then renders into **JSON responses**.

---

# Table of Contents

- Project Setup
- Create Virtual Environment
- Install Dependencies
- Create Django Project
- Create Django App
- Register Applications
- Create Serializer
- Create API View
- Configure URLs
- Run the Server
- Test the API
- Project Structure
- Technologies Used

---

# 1. Create Virtual Environment

```bash
python -m venv myenv
```

Activate the environment.

### Windows

```bash
myenv\Scripts\activate
```

### Mac / Linux

```bash
source myenv/bin/activate
```

---

# 2. Install Required Packages

```bash
pip install django
pip install djangorestframework
```

---

# 3. Create Django Project

```bash
django-admin startproject DrfProject
cd DrfProject
```

---

# 4. Create Django App

```bash
python manage.py startapp drfApp
```

---

# 5. Register Applications

Open:

```
DrfProject/settings.py
```

Add the following to **INSTALLED_APPS**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'drfApp',
]
```

---

# 6. Create Serializer

Create a file:

```
drfApp/serializers.py
```

```python
from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    name= serializers.CharField()
    age= serializers.IntegerField()
    email=serializers.EmailField()
```

### What the Serializer Does

The serializer converts **complex data types** into **Python native datatypes** so that Django REST Framework can render them into **JSON**.

---

# 7. Create Class-Based API View

Open:

```
drfApp/views.py
```

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher
from .serailizer import TeacherSerializer


class TestApiView(APIView):
    def get(self,request):
        modelterm=Teacher.objects.all()
        serailizerterm= TeacherSerializer(modelterm,many=True)    
        return Response({"message":serailizerterm.data})
        

```

---

# 8. Create App URLs

Create:

```
drfApp/urls.py
```

```python
from django.urls import path
from .views import TestApiView
urlpatterns = [
    path('test',TestApiView.as_view())
]
```

---

# 9. Connect URLs to Project

Open:

```
DrfProject/urls.py
```

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drfApp.urls')),
]
```

---

# 10. Run the Server

```bash
python manage.py runserver
```

---

# 11. Test the API

Open the following URL in your browser:

```
http://127.0.0.1:8000/test
```

Example Response:

```json
{
  "name": "Anish",
  "age": 24,
  "email": "anish@gmail.com"
}
```

---

# Project Structure

```
DrfProject
│
├── DrfProject
│   ├── settings.py
│   ├── urls.py
│
├── drfApp
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
└── manage.py
```

---

# Technologies Used

- Python
- Django
- Django REST Framework
