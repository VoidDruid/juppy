requirements_file=""

function pip_install {
    echo "Trying to install requirements from '$requirements_file'"
    if [ -f "$requirements_file"]; then
        echo "Found requirements in '$requirements_file', installing"
        pip install -r $requirements_file
    else
        echo "File '$requirements_file' doesn't exist"
    fi
}

echo "Start installing requirements"

requirements_file="/opt/notebooks/requirements.txt"
$pip_install
requirements_file=$PIP_REQS
$pip_install

echo "Starting jupyter server"

/opt/conda/bin/jupyter notebook --allow-root --notebook-dir=/opt/notebooks --ip=0.0.0.0 --port=8888 --no-browser