FROM continuumio/miniconda3

RUN apt-get update && \
    # install system packages
    apt-get install -y cmake build-essential gcc g++ git wget software-properties-common && \
    conda install -y numpy matplotlib seaborn scipy scikit-learn pandas pytorch jupyter nltk && \
    conda install -y -c conda-forge tensorflow keras opencv && \
    conda install -y -c anaconda tensorflow-gpu seaborn && \
    # clean
    apt-get autoremove -y && apt-get clean && \
    conda clean -i -l -t -y && \
    rm -rf /usr/local/src/*

RUN mkdir /juppy

COPY requirements.txt /juppy/
# install important stuff
RUN pip install -r /juppy/requirements.txt

# Prepare all
COPY prepare /juppy/
RUN chmod +x /juppy/prepare.sh
RUN "/juppy/prepare.sh"

RUN mkdir /opt/notebooks

COPY start.sh /juppy/
RUN chmod +x /juppy/start.sh

ENTRYPOINT [ "/juppy/start.sh" ]
EXPOSE 8888
