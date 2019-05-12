from juppy-base

# Install more kernels

# Bash
RUN pip install bash_kernel && \
    python -m bash_kernel.install

# Javascript
RUN npm install --unsafe-perm -g ijavascript && \
    ijsinstall

# Erlang
# RUN git clone https://github.com/robbielynch/ierlang.git && \
#     cd ierlang && make demo3
