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




# install liquidsoap from source

add "deb http://ftp.at.debian.org/debian-backports/ squeeze-backports main" to apt-sources
aptitude update

sudo apt-get -y --force-yes install git-core ocaml-findlib libao-ocaml-dev \
libportaudio-ocaml-dev libmad-ocaml-dev libtaglib-ocaml-dev libalsa-ocaml-dev \
libvorbis-ocaml-dev libladspa-ocaml-dev libxmlplaylist-ocaml-dev libflac-dev \
libxml-dom-perl libxml-dom-xpath-perl patch autoconf libmp3lame-dev \
libcamomile-ocaml-dev libcamlimages-ocaml-dev libtool libpulse-dev camlidl \
libfaad-dev libpcre-ocaml-dev 
 
#AAC encoder - only for Ubuntu versions 11.10 and up
sudo apt-get install libvo-aacenc-dev
 
rm -rf liquidsoap-full
git clone https://github.com/savonet/liquidsoap-full
cd liquidsoap-full
make init
make update
 
cp PACKAGES.minimal PACKAGES
 
sed -i "s/#ocaml-portaudio/ocaml-portaudio/g" PACKAGES
sed -i "s/#ocaml-alsa/ocaml-alsa/g" PACKAGES
sed -i "s/#ocaml-pulseaudio/ocaml-pulseaudio/g" PACKAGES
sed -i "s/#ocaml-faad/ocaml-faad/g" PACKAGES
 
#AAC+ support full instructions here: https://wiki.sourcefabric.org/x/NgPQ
#Remove the hash '#' symbol from the following line to enable AAC+ 
#sed -i "s/#ocaml-fdkaac/ocaml-fdkaac/g" PACKAGES
 

./bootstrap
./configure
make


