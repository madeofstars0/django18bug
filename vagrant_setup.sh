#!/bin/bash

echo "Fixing tty issue with root"
sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile

echo "Updating package lists..."
apt-get -y update
aptitude -y upgrade --safe 2> /dev/null

apt-get -y install \
  build-essential \
  libssl-dev \
  openssl \
  python3-pip \
  python3-dev \
  libgeos-c1 \
  gdal-bin \
  git \
  proj-bin \
  libhiredis-dev \
  postgresql \
  postgresql-contrib \
  postgis \
  postgresql-9.3-postgis-2.1 \
  libpq-dev \
  libxml2-dev \
  libxslt1-dev \
  redis-server \
  curl

# Install the python3 versions of virtualenv and wrapper
pip3 install virtualenv 
pip3 install virtualenvwrapper

#service postgresql restart

sudo -u postgres /usr/bin/createuser -s vagrant
sudo -u postgres /usr/bin/createdb -E utf-8 -O vagrant bug_dev
sudo -u postgres /usr/bin/psql -d bug_dev -c "CREATE EXTENSION postgis;"

cat >> /home/vagrant/.bashrc << EOF
export PATH=/usr/local/bin:$PATH
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
workon sherman_api

cd /vagrant

echo "Installing requirements.txt"
pip install -r /vagrant/requirements.txt

echo "Running Migrations"
./manage.py migrate

echo "--"
echo "To run the test suite: ./manage.py test"
echo ""

EOF

su vagrant -c "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 && source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv --python=/usr/bin/python3 sherman_api" 

echo ""
echo "Finished setting up the development server."
echo ""
echo "Login to the vagrant box with:"
echo "vagrant ssh"
echo ""
