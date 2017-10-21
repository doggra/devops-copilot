from django.conf.urls import url

from .views import ServerList

urlpatterns = [
	url(r'^list/', ServerList.as_view(), name='server_list'),
]
