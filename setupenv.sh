#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed."
    exit 1
fi
s
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt