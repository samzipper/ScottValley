## SVIHM_OpenAndRun.py
# Simple test script to see if I can open SVIHM with FloPy.
# SVIHM was manually copied from UCDavisHydro folder into this repository.

import os
import numpy as np
import flopy
import pandas as pd
import flopy.utils.binaryfile as bf
import platform

# set up your model
modelname = 'SVIHM'
modflow_v = 'mfnwt'

# where is your model? (path relative to root of repository)
os.chdir('modflow')

# where is your MODFLOW-2005 executable?
if (modflow_v=='mf2005'):
    if platform.system() == 'Windows':
        path2mf = 'C:/Users/Sam/Dropbox/Work/Models/MODFLOW/MF2005.1_12/bin/mf2005.exe'
    else: 
        path2mf = modflow_v
elif (modflow_v=='mfnwt'):
    if platform.system() == 'Windows':
        path2mf = 'C:/Users/Sam/Dropbox/Work/Models/MODFLOW/MODFLOW-NWT_1.1.4/bin/MODFLOW-NWT.exe'
    else:
        path2mf = modflow_v

## Load SVIHM
mf = flopy.modflow.Modflow.load(modelname+'.nam', 
        exe_name=path2mf, version=modflow_v)

# inspect
mf.get_package_list()

mf.dis.plot()
mf.bas6.plot()
mf.drn.plot()
mf.upw.plot()

## where are the WEL and SFR packages?