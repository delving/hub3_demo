#!/bin/bash

# This script is meant to be run from vagrant and from the user home directory

set -e

PROJECT_NAME="vagrant"
LOCALE="en_US.UTF-8"

export LC_ALL=${LOCALE}
sudo locale-gen ${LOCALE}
sudo update-locale ${LOCALE}
sudo dpkg-reconfigure locales

## install basic dependencies
sudo apt-get update -y -q
sudo apt-get -y install python-pip python3-pip python python3 python3-dev python-dev libxslt1-dev libxml2-dev \
    build-essential postgresql-9.3-postgis-2.1 postgresql-server-dev-9.3 zlib1g-dev libpq-dev libjpeg-dev \
    libffi-dev

# cp the deploy key
ssh-keyscan github.com >> ~/.ssh/known_hosts

# setup virtualenvwrapper
sudo pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

echo "export LC_ALL=${LOCALE}" >> .profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> .profile
echo "export DJANGO_SETTINGS_MODULE=\"projects.${PROJECT_NAME}.settings\"" >> .profile

# setting the settings module
export DJANGO_SETTINGS_MODULE="projects.${PROJECT_NAME}.settings"

# make virtual environments
set +e
rmvirtualenv ${PROJECT_NAME}_2
mkvirtualenv -p python ${PROJECT_NAME}_2
rmvirtualenv ${PROJECT_NAME}
mkvirtualenv -p python3 ${PROJECT_NAME}
set -e

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
fab local install

# after box

sudo find ~/${PROJECT_NAME}/project -type f -name "*.py[co]" -delete
sudo find ~/${PROJECT_NAME}/project -type d -name "__pycache__" -delete
sudo chown -R vagrant:vagrant ~/${PROJECT_NAME}
fab local create_dev
sudo chown -R vagrant:vagrant ~/NarthexFiles
fab local deploy_dev
fab local deploy_narthex
fab local reload_supervisor
