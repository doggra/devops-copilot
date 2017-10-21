from django.conf.urls import url

from server.views import ServerAPI,\
						 ServerStatsAPI,\
						 ServerStatsCreateAPI

urlpatterns = [
	url(r'^server/(?P<pk>[\w\d-]+)/$', ServerAPI.as_view(), name='api_server'),
	url(r'^server/(?P<pk>[\w\d-]+)/stats/$', ServerStatsAPI.as_view(), name='api_server_stats'),
	url(r'^server/(?P<pk>[\w\d-]+)/stats/create/$', ServerStatsCreateAPI.as_view(), name='api_server_stats_create'),
]
