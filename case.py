#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:15:15 2019

@author: charliegarcia
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def circ_area(diameter):
    return math.pi*(diameter/2)**2

def torroid_volume(nominal_diameter, o_cs):
    r = o_cs/2
    R = nominal_diameter/2
    return (2*(math.pi**2))*R*(r**2)

def max_pressure(sigma_max, diameter, thickness):
    return (sigma_max*2*thickness) / diameter

def num_bolts(max_shear, max_bearing, pressure, diameter, bolt_diameter):
    load_on_end = pressure * np.pi * (diameter / 2 ) ** 2
    limit = max(max_shear, max_bearing)
    
def o_compression(gland_depth, o_cs):
    return (o_cs-gland_depth)/o_cs #Should be about 18%

def o_strech(ID, o_ID):
    return (ID-o_ID)/o_ID #Should be ~5%

def gland_volume(gland_depth, OD, height):
    return (circ_area(OD) - circ_area(OD - (2*gland_depth))) * height

def tensile_stress(ID, OD, load):
    area = circ_area(OD) - circ_area(ID)
    stress = load/area
    return stress
    
    
fourforty_dia = .1120
fourforty_alloy_shear = 946 #lbs, fastener torqued to 8in-lbs

num_32_o_ring_ID = 1.864 #in
num_32_o_ring_OD = 2.004 #in
num_32_o_ring_CS = (num_32_o_ring_OD - num_32_o_ring_ID)/2
num_32_R = num_32_o_ring_OD - num_32_o_ring_CS


OD = 2.0
ID = .943*2
gland_depth = (OD-ID)/2

print(o_strech(ID,num_32_o_ring_ID))
print(o_compression(gland_depth, num_32_o_ring_CS))
print(torroid_volume(num_32_R,num_32_o_ring_CS)/gland_volume(gland_depth,OD,.09))
print(tensile_stress(ID, OD, 4712))