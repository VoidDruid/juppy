# Juppy
## Универсальный образ для работы в jupyter

> **docker pull voidwalker/juppy**

Удобный alias для .bashrc, для запуска контейнера который собирается в этом репозитории:
note: замените в этой команде `~/Notebooks` на путь к директории где вы хотели бы хранить ноутбуки, и `8888` на порт, где бы вы хотели повесить jupyter

```bash
alias juppy='docker stop juppy; docker rm juppy; docker run --name=juppy -i -t -p 8888:8888 -v ~/Notebooks:/opt/notebooks juppy /bin/bash -c "/opt/conda/bin/jupyter notebook --allow-root --notebook-dir=/opt/notebooks --ip=0.0.0.0 --port=8888 --no-browser"'
```

**TODO**:
- Скрипт для запуска контейнера, с аргументами:
  - пересоздать контейнер, если он уже существует, или запустить имеющийся
  - порт для запуска
  - директория для /opt/notebooks
- Возможность монтировать локальный jupyter_notebook_config.py в контейнер
- Возможность устанавливать дополнительные системные пакеты (аналог requirements.txt, но для apt-get)
