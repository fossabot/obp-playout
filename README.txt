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



mkdir -p /var/log/pypo/ls/
chown -R pypo:pypo /var/log/pypo


# run the scripts
su pypo
cd /home/pypo/src/pypo/pypo/liquidsoap_scripts
/usr/local/bin/liquidsoap --verbose -f ls_script.liq

su pypo
cd /home/pypo/src/pypo/pypo
env/bin/python pypo.py


# add to supervisor
ln -s /home/pypo/src/pypo/conf/* /etc/supervisor/conf.d/


streams.scheduled_play_start
s0.push annotate:media_id="bc975011-4155-11e3-9643-b8f6b11a3aed",liq_start_next="6.0",liq_fade_in="2.0",liq_fade_out="2.0",liq_cue_in="0.0",liq_cue_out="10.0",schedule_table_id="bc975011-4155-11e3-9643-b8f6b11a3aed",replay_gain="0 dB":/home/pypo/test.mp3
s0.push annotate:media_id="8a3f6ab5-4612-11e3-88d2-b8f6b11a3aed",liq_start_next="10.0",liq_fade_in="10.0",liq_fade_out="10.0",liq_cue_in="0.0",liq_cue_out="40.0",schedule_table_id="8a3f6ab5-4612-11e3-88d2-b8f6b11a3aed",replay_gain="0 dB":/home/pypo/track_01.mp3

streams.scheduled_play_start
s0.push annotate:media_id="t0",liq_start_next="10.0",liq_fade_in="15.0",liq_fade_out="15.0",liq_cue_in="0.0",liq_cue_out="30.0",schedule_table_id="s0",replay_gain="0 dB":/home/pypo/track_01.mp3
s1.push annotate:media_id="t0",liq_start_next="10.0",liq_fade_in="15.0",liq_fade_out="15.0",liq_cue_in="0.0",liq_cue_out="30.0",schedule_table_id="s0",replay_gain="0 dB":/home/pypo/test.mp3





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


# to use audio processing

include "ocaml-ladspa" in PACKAGES
also install ladspa-sdk libladspa-ocaml
and the plugins:
caps mcp-plugins cmt blop tap-plugins ladspa-sdk csladspa tap-plugins swh-plugins



# run in dev-mode

## liquidsoap
supervisorctl stop liquidsoap.pypo
cd /home/pypo/src/pypo/pypo/liquidsoap_scripts
sudo -u pypo /usr/local/bin/liquidsoap --verbose -f ls_script.liq

# pypo
supervisorctl stop pypo
cd /home/pypo/src/pypo/pypo
sudo -u pypo env/bin/python pypo.py




