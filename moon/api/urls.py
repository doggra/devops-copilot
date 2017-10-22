from django.conf.urls import url

from server.views import ServerAPI,\
						 ServerStatsAPI


urlpatterns = [
	url(r'^server/$', ServerAPI.as_view(), name='api_server'),
	url(r'^server/stats/$', ServerStatsAPI.as_view(),
											   name='api_server_stats_create'),

]
