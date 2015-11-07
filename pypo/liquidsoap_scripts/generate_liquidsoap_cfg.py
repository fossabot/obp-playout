import logging
import sys
import time
sys.path.append("..")
from pypo.api_clients.api_client import AirtimeApiClient

def generate_liquidsoap_config(ss):
    data = ss['settings']

    print '**** DATA:'
    print data

    fh = open('/etc/playout/liquidsoap.cfg_', 'w')
    fh.write("################################################\n")
    fh.write("# THIS FILE IS AUTO GENERATED. DO NOT CHANGE!! #\n")
    fh.write("################################################\n")

    for d in data:
        key = d['keyname']

        str_buffer = d[u'keyname'] + " = "
        if d[u'type'] == 'string':
            val = '"%s"' % d['value']
        else:
            val = d[u'value']
            val = val.lower() if len(val) > 0 else "0"
        str_buffer = "%s = %s\n" % (key, val)
        fh.write(str_buffer.encode('utf-8'))

    fh.write('log_file = "/var/log/playout/ls/<script>.log"\n')
    fh.close()

logging.basicConfig(format='%(message)s')
ac = AirtimeApiClient(logging.getLogger())
attempts = 0
max_attempts = 2

while True:
    try:
        print 'pre api'
        ss = ac.get_stream_setting()
        print 'post api'
        print ss
        generate_liquidsoap_config(ss)
        break
    except Exception, e:
        if attempts == max_attempts:
            print "Unable to connect to the Airtime server."
            logging.error(str(e))
            sys.exit(1)
        else:
            time.sleep(3)
    attempts += 1
