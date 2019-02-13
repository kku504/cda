#!/usr/bin/env python

import glob
import re
import os
import shutil
import datetime
import subprocess

#backup lftp.conf
shutil.copyfile('/etc/lftp.conf','/etc/lftp_' + datetime.datetime.now().strftime
("%Y%m%d") + '.conf')
#get the latest key pem
list_of_pem_files = glob.glob("/etc/pki/entitlement/*key.pem")
latest_file = max(list_of_pem_files,key=os.path.getctime)

new = re.sub('[^0-9]', '',latest_file)

#get the current key pem
def get_oldkey():
    lftp = open("/etc/lftp.conf","r")
    p = re.compile('.*-key.pem')
    for line in lftp:
        if p.match(line):
            return line

oldkey = get_oldkey()
old = oldkey.split('/')[-1].split('.')[0].split('-')[0]

#replace if new key pem is pulled from RHN
if old != new:
    cmd = "sed -i -e 's/" + old + "/" + new + '/g\' ' +"/etc/lftp.conf"
    #print(cmd)

os.system(cmd)

