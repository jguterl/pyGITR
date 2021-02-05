#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:56:49 2021

@author: guterl
"""
# class InputGITR:
#     def init:
#         self.X
#         self.

#     def lines_to_gitr_geometry(filename, lines, Z, surface, inDir):

#     x1 = lines[:, 0]
#     z1 = lines[:, 1]
#     x2 = lines[:, 2]
#     z2 = lines[:, 3]
#     slope = lines[:, 4]
#     intercept = lines[:, 5]
#     line_length = lines[:, 6]
#     fileExists = os.path.exists(filename)

#     if not fileExists:
#         f = open(filename, "w")
#         f.close()

#     with io.open(filename) as f:
#         config = libconf.load(f)

#     config['geom'] = {}
#     config['geom']['x1'] = x1.tolist()
#     config['geom']['z1'] = z1.tolist()
#     config['geom']['x2'] = x2.tolist()
#     config['geom']['z2'] = z2.tolist()
#     config['geom']['slope'] = ['%.6f' % elem for elem in slope.tolist()]
#     config['geom']['intercept'] = ['%.6f' % elem for elem in intercept.tolist()]
#     config['geom']['length'] = line_length.tolist()
#     config['geom']['Z'] = Z.tolist()
#     config['geom']['surface'] = ['%i' % elem for elem in surface.tolist()]
#     config['geom']['inDir'] = ['%i' % elem for elem in inDir.tolist()]
#     config['geom']['y1'] = 0.0
#     config['geom']['y2'] = 0.0
#     config['geom']['periodic'] = 0

#     config['geom'] = InputGeo
#     with io.open(filename, 'w') as f:
#         libconf.dump(config, f)
# input.X=[]

# input.write(FileName)
#     def gmsh2Geom(gmsh:gmsh):
#         assert
