def read_envs(env_file):
    envs = {}
    for line in open(env_file, mode='r'):
        if not line:
            continue
        from_, to = line.strip(' \n').split(':')
        envs[from_] = to
    
    return envs
