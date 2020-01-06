#!/usr/bin/env bash

function pip_install {
    requirements_file=${PIP_REQS:-"/opt/notebooks/requirements.txt"}
    echo "Trying to install requirements from '$requirements_file'"
    if [ -f "$requirements_file"]; then
        echo "Found requirements in '$requirements_file', installing"
        pip install -r $requirements_file
    else
        echo "File '$requirements_file' doesn't exist"
    fi
}

echo "Start installing requirements"
$pip_install

echo "Starting jupyter server"
# TODO: user config at /juppy/jupyter_notebook_config.py
/opt/conda/bin/jupyter notebook --allow-root --notebook-dir=/opt/notebooks --ip=0.0.0.0 --port=8888 --no-browser
