#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import DINCAE
from sys import argv

# filename = "/path/to/file.nc"
# varname = "SST"
# outdir = "/path/to/output/dir"

if len(argv)!=4:
  print('infile,filename,varname,outdir')
  exit(1)

infile,filename,varname,outdir=argv

DINCAE.reconstruct_gridded_nc(filename,varname,outdir)
