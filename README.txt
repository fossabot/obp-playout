# installation

aptitude install python-setuptools supervisor sudo
easy_install PIP
pip install virtualenv

# installing pypo
su pypo
cd ~/src/
git clone git@lab.hazelfire.com:hazelfire/obp/pypo.git
cd pypo/pypo/

virtualenv env
source env/bin/activate
pip install -r requirements.txt


# run the scripts



cd /home/pypo/src/pypo/pypo/liquidsoap_scripts
sudo -u pypo /usr/local/bin/liquidsoap --verbose -f ls_script.liq

cd /home/pypo/pypo
sudo -u pypo env/bin/python pypo.py





