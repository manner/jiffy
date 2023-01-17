#!/bin/bash

sudo apt update
sudo apt install -y g++ libssl-dev cmake

mkdir -p build
cd build
cmake ..
make -j
