#!/bin/sh

./env/bin/python liquidsoap_scripts/generate_liquidsoap_cfg.py
sleep 2
cd liquidsoap_scripts
sudo -u pypo /usr/local/bin/liquidsoap --verbose -f ls_script.liq

