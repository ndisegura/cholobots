# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:34:55 2024

@author: asegura
"""

import pyrosim.pyrosim as pyrosim

#tell pyrosim the name of the file where information about the world
# you're about to create should be stored. This world will currently be called box
pyrosim.Start_SDF("box.sdf")
#stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])

pyrosim.End()