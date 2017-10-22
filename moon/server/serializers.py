from rest_framework import serializers
from .models import Server, ServerStats


class ServerSerializer(serializers.ModelSerializer):

	stats = serializers.JSONField(source='last_stats', read_only=True)

	class Meta:
		model = Server
		exclude = ('owner',)


class ServerStatsSerializer(serializers.ModelSerializer):

	class Meta:
		model = ServerStats
		fields = '__all__'
