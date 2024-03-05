#!/usr/bin/env python
import time
from flyt_python import api
drone = api.navigation(timeout=120000) # instance of flyt droneigation class

#at least 3sec sleep time for the drone interface to initialize properly
time.sleep(3)

print 'taking off'
drone.take_off(10.0)

print 'Executing triangle formation'
drone.position_set(-5,8.66,0,relative=True)
drone.position_set(5,8.66,0,relative=True)
drone.position_set(0,-17.32,0,relative=True)

print 'Landing'
drone.land(async=False)

#shutdown the instance
drone.disconnect()
