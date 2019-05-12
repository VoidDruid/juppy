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
# install nodejs/npm
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y build-essential nodejs npm
# AWS
RUN pip install boto3
# install pymars (it's cool)
RUN pip install pymars
# install important stuff
RUN pip install requests Flask Pillow SQLAlchemy beautifulsoup4 psycopg2-binary

# Prepare all
COPY prepare /
RUN chmod +x prepare.sh
CMD ["./prepare.sh"]

RUN mkdir /opt/notebooks

EXPOSE 8888
