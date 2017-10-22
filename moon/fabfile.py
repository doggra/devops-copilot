import re

from fabric.api import *

env.use_ssh_config = True
env.hosts = ['sin', 'decyzje']
usload = r'(?P<users>\d+)\suser'


@task
def clear_mem_cache():
	sudo('echo 3 > /proc/sys/vm/drop_caches')


@task
def check_stats():
	usercpu = run('uptime')
	mem = run('free | grep Mem | awk \'{print $3/$2 * 100.0}\'')
	load = run('cat /proc/loadavg')
	m = re.search(usload, usercpu)
	if m:
		users = m.group('users')

		results = {"users": users, 
				   "load": load.split(" ")[2],
				   "mem": mem}

		print(results)
		return results