from rest_framework import serializers
from .models import Server, ServerStats


class ServerSerializer(serializers.ModelSerializer):

	stats = serializers.DictField(source='last_stats', read_only=True)

	class Meta:
		model = Server
		exclude = ('owner',)


class ServerStatsSerializer(serializers.ModelSerializer):
	cpu = serializers.DictField(source='get_cpu_load')
	mem = serializers.CharField(source='get_mem_usage')

	class Meta:
		model = ServerStats
		fields = ['cpu', 'mem', 'users']


class ServerStatsCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = ServerStats
		fields = '__all__'
