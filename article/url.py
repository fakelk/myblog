from django.conf.urls import url, include
from article import views

url patterns = [
    url(r'^myview/$',views.myview),
    url(r'^hello world/$',views.hello_world),
    url(r'^nama/p<nama>[\w-]+)/(?p<umur>[0-9]+)$',nama_saya, umur),
]
