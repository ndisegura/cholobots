# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:20:01 2024

@author: asegura
"""

import pybullet as p
import time

#Create physics object
physicsClient = p.connect(p.GUI)
#Disable sidebard
p.configureDebugVisualizer(p.COV_ENABLE_GUI,1)

for index in range(1000):
    time.sleep(1/60)
    p.stepSimulation()
    print(f'Index:{index}')
    
p.disconnect()