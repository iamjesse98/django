from django.conf.urls import url
from . import views

# r'^s' default homepage
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
]
