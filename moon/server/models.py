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
