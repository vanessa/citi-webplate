#!/bin/bash

sudo -u ${2} python setup.py --PROJECT_DIR ${1} --USER_NAME ${2} --IP_ADDRESS ${3}
sudo -u ${2} rm gunicorn-config root-name root-name.conf

sudo -u ${2} mv -v gunicorn_start /home/${2}/bin/
sudo -u ${2} chmod u+x /home/${2}/bin/gunicorn_start

sudo -u ${2} mkdir /home/${2}/run

sudo -u ${2} mkdir /home/${2}/logs
sudo -u ${2} touch /home/${2}/logs/gunicorn-error.log

mv -v ${1}.conf /etc/supervisor/conf.d/

supervisorctl reread
supervisorctl update

supervisorctl restart

mv -v ${1} /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/${1} /etc/nginx/sites-enabled/${1}
rm /etc/nginx/sites-enabled/default

service nginx restart
reboot
