# Juppy
## Универсальный образ для работы в jupyter
Удобный alias для .bashrc, для запуска контейнера который собирается в этом репозитории:

```bash
alias juppy='docker stop juppy; docker rm juppy; docker run --name=juppy -i -t -p 8888:8888 -v /home/$USER/Documents/Notebooks/:/opt/notebooks juppy /bin/bash -c "/opt/conda/bin/jupyter notebook --allow-root --notebook-dir=/opt/notebooks --ip=0.0.0.0 --port=8888 --no-browser"'
```