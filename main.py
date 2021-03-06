#!/usr/bin/env python
import sys
import time
import os
import re
from daemon import daemon
from dsocket import dsockets

# define all paths required
currentPath = os.path.dirname(os.path.realpath(__file__))
pidFilePath = currentPath + "/tmp/process.pid"
logfilePath = currentPath + "/tmp/logs"
errfilePath = currentPath + "/tmp/err"
domainName = None

class vagrantpyd(daemon):

    def run(self):
        # TODO: Load the domain name of the system from config.inc.php
        # And store that as env variable

        # Define event listener for named pipe here
        # Currently writing to temp code to test daemon for now
        try:
            mysock = dsockets()
            mysock.create()
        except Exception as inst:
            # TODO print correct exception message
            print ("[%s] Unable to listen to sockets required to communicate with daemon.\nException: %s ") % (time.time(), inst)
            sys.exit(1)

    def _stop(self):
        print ("attempting to stop listening to socket.")
        # TODO: Code to stop listening to socket, created by
        # another instance of same program

# Create a tmp directory if not exists
# if required by the files needed
os.chdir(currentPath)
if not os.path.exists("./tmp/"):
    os.makedirs("./tmp/")

# Create log files if not exists
if not os.path.exists(logfilePath):
    file = open(logfilePath, 'a+')
    file.close()

# Create err files if not exists
if not os.path.exists(errfilePath):
    file = open(errfilePath, 'a+')
    file.close()


if __name__ == "__main__":
    daemon = vagrantpyd(pidFilePath, logfilePath, errfilePath)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            # Code to check if config file exists
            print("Vagrant Cluster Manager Daemon starting ...")
            daemon.start()
        elif 'stop' == sys.argv[1]:
            print ("Vagrant Cluster Manager Daemon stopping ...")
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            print ("Vagrant Cluster Manager Daemon restarting ...")
            daemon.restart()
        else:
            print ("Unknown command!")
            print ("usage: %s start|stop|restart") % sys.argv[0]
            sys.exit(2)

        sys.exit(0)
    else:
        print ("usage: %s start|stop|restart") % sys.argv[0]
        sys.exit(2)
