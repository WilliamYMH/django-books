from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    url(r'^$', views.index_redirect, name='index_redirect'),
    url(r'^books/', include('books.urls')),
]