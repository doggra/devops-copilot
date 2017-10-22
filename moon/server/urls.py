from django.conf.urls import url

from .views import ServerList, ServerDetails

urlpatterns = [
	url(r'^list/', ServerList.as_view(), name='server_list'),
	url(r'^details/(?P<pk>[\w\d-]+)/$', ServerDetails.as_view(), 
														name='server_details'),
]
