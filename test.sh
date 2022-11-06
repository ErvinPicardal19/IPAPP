#!/bin/bash

if python3 -m unittest -v test.py | grep "OK"; then
    exit 0
else
    exit 1
fi