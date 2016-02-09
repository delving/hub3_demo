#!/bin/bash

# This script is meant to be run from vagrant and from the user home directory

set -e

PROJECT_NAME="vagrant"
PASSWORD="#9@?[ZMh26VcF3jKw§ucy3!!@rmt"
LOCALE="en_US.UTF-8"


echo "export LC_ALL=${LOCALE}" >> .profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> .profile
echo "export DJANGO_SETTINGS_MODULE=\"projects.${PROJECT_NAME}.settings\"" >> .profile

export LC_ALL=${LOCALE}
sudo locale-gen ${LOCALE}
sudo update-locale ${LOCALE}
sudo dpkg-reconfigure locales

# add user
sudo adduser --quiet --disabled-password ${PROJECT_NAME}
sudo echo "${PROJECT_NAME}:${PASSWORD}" | chpasswd

# setting the settings module
export DJANGO_SETTINGS_MODULE="projects.${PROJECT_NAME}.settings"

## install basic dependencies
sudo apt-get update -y -q
sudo apt-get -y install python-pip python3-pip python python3 python3-dev python-dev libxslt1-dev libxml2-dev \
    build-essential postgresql-9.3-postgis-2.1 postgresql-server-dev-9.3 zlib1g-dev libpq-dev libjpeg-dev \
    libffi-dev

# cp the deploy key
ssh-keyscan github.com >> ~/.ssh/known_hosts
#mkdir -p ~/.ssh
#chmod 0700 ~/.ssh
#cp ~/${PROJECT_NAME}/project/deploy/id_rsa ~/.ssh/id_rsa
#chmod 0600 ~/.ssh/id_rsa

# setup virtualenvwrapper
sudo pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

# make virtual environments
deactivate
rmvirtualenv ${PROJECT_NAME}_2
mkvirtualenv -p python ${PROJECT_NAME}_2
rmvirtualenv ${PROJECT_NAME}
mkvirtualenv -p python3 ${PROJECT_NAME}

## go to mounted directory
cd  ${PROJECT_NAME}/project

## install python 3 dependencies
workon ${PROJECT_NAME}
pip install -r requirements/base.txt

# install on python 2 for fabric installation
workon ${PROJECT_NAME}_2
pip install --upgrade ndg-httpsclient
pip install -r requirements/base.txt
pip install fabric

# go to django dir
cd nave

# fabric installation steps
fab install
sudo chown -R vagrant:vagrant ~/${PROJECT_NAME}
fab create_dev
sudo chown -R vagrant:vagrant ~/NarthexFiles
fab deploy_dev
fab deploy_narthex
fab reload_supervisor
