#!/bin/sh

echo "######################"
echo "# restarting playout #"
echo "######################"
echo
supervisorctl restart liquidsoap.pypo
supervisorctl restart pypo
supervisorctl status