# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import User


OS_DISTRO = (
	(0, "Debian"),
	(1, "CentOS"),
)

STATUS = (
	(0, "Install"),
	(1, "Ready"),
	(2, "Updating"),
	(3, "Alert"),
)


class Server(models.Model):
	owner = models.ForeignKey(User)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
							editable=False, unique=True)
	os = models.IntegerField(null=True, choices=OS_DISTRO)
	hostname = models.CharField(max_length=255)
	status = models.IntegerField(default=0, choices=STATUS)

	def __unicode__(self):
		return self.hostname


class ServerStats(models.Model):
	server = models.ForeignKey(Server)
	datetime = models.DateTimeField(auto_now_add=True)
	cpu_load_1 = models.DecimalField(max_digits=5, decimal_places=2)
	cpu_load_5 = models.DecimalField(max_digits=5, decimal_places=2)
	cpu_load_15 = models.DecimalField(max_digits=5, decimal_places=2)
	mem_usage = models.IntegerField()
	net_dl = models.IntegerField()
	net_ul = models.IntegerField()
	users = models.IntegerField()

	def __unicode__(self):
		return "{} {}".format(self.datetime.strftime("%Y%m%d%H%M"), self.server)
