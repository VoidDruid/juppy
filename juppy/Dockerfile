FROM juppy-base

# Install more kernels
RUN apt-get update

# Bash
RUN pip install bash_kernel && \
    python -m bash_kernel.install

# Javascript
# install nodejs/npm
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y build-essential nodejs npm
# install js kernel
RUN npm install --unsafe-perm -g ijavascript && \
    ijsinstall

# Forth
RUN apt-get install -y gforth && \
    cd /tmp && \
    git clone https://github.com/jdfreder/iforth && \
    cd iforth && \
    pip install . && \
    cd / && \
    rm -rf /tmp/iforth

# Erlang
# RUN git clone https://github.com/robbielynch/ierlang.git && \
#     cd ierlang && make demo3

# Clear
RUN apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/apt/lists/*
