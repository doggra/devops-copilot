# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from rest_framework import generics

from .models import Server, ServerStats

from .serializers import ServerSerializer,\
						 ServerStatsSerializer,\
						 ServerStatsCreateSerializer


class ServerList(ListView):
	model = Server


class ServerAPI(generics.RetrieveUpdateAPIView):
	""" Endpoint for retrieving and updateing server info.
	"""
	queryset = Server.objects.all()
	serializer_class = ServerSerializer


class ServerStatsAPI(generics.ListAPIView):
	""" Endpoint for fetching server statistics.
	"""
	queryset = ServerStats.objects.all()
	serializer_class = ServerStatsSerializer


class ServerStatsCreateAPI(generics.CreateAPIView):
	""" Endpoint for fetching server statistics.
	"""
	queryset = ServerStats.objects.all()
	serializer_class = ServerStatsCreateSerializer