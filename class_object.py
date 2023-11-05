#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:30:54 2023

@author: umidjon
"""

class Kompyuter:
    def __init__(self,ram, hdd, gpu, cpu):
        self.ram=ram
        self.hdd=hdd
        self.gpu=gpu
        self.cpu=cpu
        
macbook = Kompyuter('16gb','1tb','m2','m2')
macbuk = Kompyuter('8gb','1tb','m2','m2')