# to connect this file with Main urls.py and views.py

from django.urls import path
from . import views

urlpatterns = [
      path('sql',views.dispsqldata)
    , path('APImain',views.API_mainpage)
    , path('GETsql/displaymytable',views.GET_sql,name="GET_sqltable")
    , path('POSTsql/insertintable',views.post_Insertsql,name="post_Insertsql")
    , path('POSTsql/updateintable',views.post_Updatesql, name="post_Updatesql")
    , path('POSTsql/deleteintable',views.post_Deletesql,name="post_Deletesql")
]



