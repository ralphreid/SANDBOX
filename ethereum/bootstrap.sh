#!/bin/bash

# from https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Ubuntu
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo add-apt-repository -y ppa:ethereum/ethereum-dev

# Update apt surpress output and auto yes
apt-get -qqy update

sudo apt-get install ethereum
