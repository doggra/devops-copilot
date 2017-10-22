# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import uuid
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property


OS_DISTRO = (
	(0, "Unknown"),
	(1, "Debian"),
	(2, "CentOS"),
)

STATUS = (
	(0, "Install"),
	(1, "Ready"),
	(2, "Updating"),
	(3, "Alert"),
)


class ServerStats(models.Model):
	uuid = models.ForeignKey('Server')
	datetime = models.DateTimeField(auto_now_add=True)
	cpu_load_15 = models.DecimalField(max_digits=5, decimal_places=2)
	mem_usage = models.IntegerField()
	net_dl = models.IntegerField()
	net_ul = models.IntegerField()

	def __unicode__(self):
		return self.datetime.strftime("%Y/%m/%d %H:%M")


class Server(models.Model):
	owner = models.ForeignKey(User)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
							editable=False, unique=True)
	os = models.IntegerField(default=0, choices=OS_DISTRO)
	hostname = models.CharField(max_length=255)
	status = models.IntegerField(default=0, choices=STATUS)

	def __unicode__(self):
		return str(self.uuid)

	@cached_property
	def last_stats(self):
		last_24h = datetime.datetime.now()-datetime.timedelta(days=1)
		ss = ServerStats.objects.filter(uuid__uuid=self.uuid, 
										datetime__gt=last_24h)
		return [{"cpu_15": float(stats.cpu_load_15),
							"mem": stats.mem_usage,
							"net_dl": stats.net_dl,
							"net_ul": stats.net_ul} for stats in ss]
