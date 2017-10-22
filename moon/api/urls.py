from django.conf.urls import url

from rest_framework.authtoken import views
from server.views import ServerAPI,\
						 ServerCreateAPI,\
						 ServerStatsAPI


urlpatterns = [

    # url(r'^token/$', views.obtain_auth_token),

	url(r'^server/$', ServerAPI.as_view(), name='api_server'),
	url(r'^server/create/$', ServerCreateAPI.as_view(),
													 name='api_server_create'),
	url(r'^server/stats/$', ServerStatsAPI.as_view(),
											   name='api_server_stats_create'),

]
