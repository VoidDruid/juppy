#!/usr/bin/env bash
set -e

make build
python3 install.py out

exit 0
