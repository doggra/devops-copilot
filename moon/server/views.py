# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied

from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from rest_framework import exceptions
from .models import Server, ServerStats
from .serializers import ServerSerializer,\
						 ServerStatsSerializer


class ServerCreateAPI(generics.CreateAPIView):
	serializer_class = ServerSerializer

	def perform_create(self, serializer):
		# Only for logged in users.
		try:
			serializer.save(owner=self.request.user)
		except:
			raise PermissionDenied


class ServerList(ListView):
	model = Server


class ServerDetails(DetailView):
	model = Server


class ServerAPI(views.APIView):
	""" Endpoint for updating server info.
	"""

	# Update server information.
	def post(self, request, format=None):
		server = get_object_or_404(Server, pk=request.data['uuid'])
		ss = ServerSerializer(server, data=request.data)
		if ss.is_valid():
			ss.save()
			return Response(ss.data)
		else:
			return Response(ss.errors)


class ServerStatsAPI(views.APIView):
	""" Endpoint for fetching and updating server statistics.
	"""

	def get(self, request, format=None):
		servers = Server.objects.all()
		serializer = ServerSerializer(servers, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):

		# Get server's last stats by UUID.
		if 'uuid' in request.data:
			server = get_object_or_404(Server,pk=request.data['uuid'])
			return Response(server.last_stats)

		# Update server stats.
		else:
			ss = ServerStatsSerializer(data=request.data, many=True)
			if ss.is_valid():
				ss.save()
				return Response("OK")
			else:
				return Response(ss.errors)

			return Response(server.last_stats)
