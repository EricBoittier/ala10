#! /bin/sh
namd3 smd.namd > da_smd.log

vmd da.psf da_smd.dcd
