FROM juppy-base

# Install more kernels

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

# Erlang
# RUN git clone https://github.com/robbielynch/ierlang.git && \
#     cd ierlang && make demo3
