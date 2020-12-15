# this is Main urls.py


from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/',include('BasicApp.urls'))
]
