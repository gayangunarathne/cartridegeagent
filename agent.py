#!/usr/bin/env python
import stomp
import time
import logging
import sys
import random
import os
import threading

fo = open("/home/gayan/Resources/Stratos/payload/launch-params", "r+")
str = fo.read(1000);

print "Read String is : ", str

sd = dict(u.split("=") for u in str.split(","))

print [i for i in sd.keys()]

print "HOST_NAME   ", sd['HOST_NAME']





def runningSuspendScript():
    print "inside thread"
    os.system('./script.sh')
def MyThread2():
    pass

def listeningTopology():
    class MyListener(stomp.ConnectionListener):
        def on_error(self, headers, message):
            print('received an error %s' % message)
        def on_message(self, headers, message):
            for k,v in headers.iteritems():
                print('header: key %s , value %s' %(k,v))
            print('received message\n %s'% message)


    dest='/topic/topology'
    conn=stomp.Connection([('localhost',61613)])
    print('set up Connection')
    conn.set_listener('somename',MyListener())
    print('Set up listener')

    conn.start()
    print('started connection')

    conn.connect(wait=True)
    print('connected')
    conn.subscribe(destination=dest, ack='auto')
    print('subscribed')


def listeningInstanceNotifier():
    class MyListener(stomp.ConnectionListener):
        def on_error(self, headers, message):
            print('received an error %s' % message)
        def on_message(self, headers, message):
            for k,v in headers.iteritems():
                print('header: key %s , value %s' %(k,v))
            print('received message\n %s'% message)


    dest='/topic/instance-notifier'
    conn=stomp.Connection([('localhost',61613)])
    print('set up Connection')
    conn.set_listener('somename',MyListener())
    print('Set up listener')

    conn.start()
    print('started connection')

    conn.connect(wait=True)
    print('connected')
    conn.subscribe(destination=dest, ack='auto')
    print('subscribed')

def onInstanceStartedEvent():
    print('on instance start up event')



t1 = threading.Thread(target=runningSuspendScript, args=[])

t1.start()

t2 = threading.Thread(target=listeningInstanceNotifier, args=[])

t2.start()

t3 = threading.Thread(target=listeningTopology, args=[])

t3.start()

onInstanceStartedEvent()

