import sys
import os

import docker as dk

from read_envs import read_envs

docker = dk.from_env()

juppy_v, target = sys.argv[1:]
env_file = juppy_v + '/envs.txt'

print('Env file:', env_file)
print('Target dir:', target)

envs = read_envs(env_file)

print('\nSources:')
for key, value in envs.items():
    print(f'\t{key}:', value)

try:
    if not os.path.exists(target):
        os.makedirs(target)
    
    container = docker.containers.run(juppy_v, 'sh', detach=True)

    for from_, to in envs.items():
        path = f'{target}/{to}.tar'
        if os.path.exists(path):
            os.remove(path)

        with open(path, 'wb+') as destination:
            bits, stats = container.get_archive(from_)
            print('Copying', stats['name'])
            for chunk in bits:
                destination.write(chunk)
except Exception as e:
    print(e)
finally:
    container.stop()
    container.remove()
