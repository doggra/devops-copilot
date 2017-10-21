# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
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


class Server(models.Model):
	owner = models.ForeignKey(User)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
							editable=False, unique=True)
	os = models.IntegerField(default=0, choices=OS_DISTRO)
	hostname = models.CharField(max_length=255)
	status = models.IntegerField(default=0, choices=STATUS)
	stats = models.ManyToManyField('ServerStats', blank=True)

	def __unicode__(self):
		return str(self.uuid)

	@cached_property
	def last_stats(self):
		stats = self.stats.latest('datetime')
		return {"cpu_1": stats.cpu_load_5,
				"cpu_5": stats.cpu_load_5,
				"cpu_15": stats.cpu_load_15,
				"mem": stats.mem_usage,
				"net_dl": stats.net_dl,
				"net_up": stats.net_ul,
				"users": stats.users}



class ServerStats(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	cpu_load_1 = models.DecimalField(max_digits=5, decimal_places=2)
	cpu_load_5 = models.DecimalField(max_digits=5, decimal_places=2)
	cpu_load_15 = models.DecimalField(max_digits=5, decimal_places=2)
	mem_usage = models.IntegerField()
	net_dl = models.IntegerField()
	net_ul = models.IntegerField()
	users = models.IntegerField()

	def __unicode__(self):
		return self.datetime.strftime("%Y/%m/%d %H:%M")

	@cached_property
	def get_cpu_load(self):
		return {"1": self.cpu_load_1,
				"5": self.cpu_load_5,
				"15": self.cpu_load_15}

	def get_mem_usage(self):
		return "{}%".format(self.mem_usage)