#!/bin/bash

apt-get update
apt-get -y upgrade
apt-get -y install build-essential libpq-dev python3-pip python3-dev
apt-get -y install postgresql postgresql-contrib
apt-get -y install nginx
apt-get -y install supervisor

systemctl enable supervisor
systemctl start supervisor

pip3 install --upgrade pip
pip3 install virtualenv
