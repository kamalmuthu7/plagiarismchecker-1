from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^plagiarism/',views.check,name = 'check'),
    url(r'^plagchecker',views.geturls,name='geturls'),
    ]
