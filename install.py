import os
import shutil
import sys
import subprocess

from read_envs import read_envs

out_dir = sys.argv[1]

print('\nINSTALLING JUPPY\n')

def read_var(prompt, default, expand=True):
    var = input(f'{prompt} (default: {default}): ') or default
    if expand:
        var = os.path.expanduser(var)
    return var


notebooks_dir = read_var('Directory for notebooks', '~/Notebooks')
envs_dir = read_var('Directory for cache - python packages, etc.', '~/.juppy')
juppy_port = read_var('Port for jupyter', '8888', expand=False)

os.makedirs(envs_dir, exist_ok=True)
os.makedirs(notebooks_dir, exist_ok=True)

envs = {**read_envs('juppy-base/envs.txt'), **read_envs('juppy/envs.txt')}

volumes = {}
for mount_to, source in envs.items():
    volumes[f'{envs_dir}/{source}'] = mount_to

for source in envs.values():
    print(f'Unpacking {source}.tar to {envs_dir}')
    # python's "tarfile" throws errors unpacking conda
    subprocess.check_call(['tar', '-xf', f'{out_dir}/{source}.tar', '-C', envs_dir])

shutil.rmtree(out_dir)

volumes_string = ' '.join(map(lambda source: f'-v {source}:{volumes[source]}', volumes.keys()))

alias_str=f"alias juppy='\
docker stop juppy; docker rm juppy; \
docker run --name=juppy -i -t -p {juppy_port}:8888 -v {notebooks_dir}:/opt/notebooks {volumes_string} juppy /bin/bash -c \
\"/opt/conda/bin/jupyter notebook --ip=0.0.0.0 --port=8888\"\
'"

print('\n----------------\n\n' + alias_str)
