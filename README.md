# Useful scripts for WoWS skin modding

![GitHub last commit](https://img.shields.io/github/last-commit/SEA-group/Scripts-storage)
![GitHub issues](https://img.shields.io/github/issues-raw/SEA-group/Scripts-storage)
![GitHub downloads](https://img.shields.io/github/downloads/SEA-group/Scripts-storage)

By AstreTunes @ SEA group

A bunch of unnecessary but useful scripts for World of Warships skin modding; "necessary" scripts are [here](https://github.com/SEA-group/ContentSDK-0.9.7-fix-tools)

## Content
. **SEA_camo_remover_py3.py** disables camouflages by editing material tag in *.visual* files
. **SEA_camo_reverser_py3.py** restores the camouflages disabled by the *SEA_camo_remover_py3.py*
. **SEA_comma2point_py3.py** replaces commas with points in ascii *.obj* files, because the chinese WoT Model Editor cannot recognize comma as decimal mark
. **SEA_fx_update_py3.py** parses *.mfm* files and changes `shaders/std_effects/PBS_*.fx` to newer `shaders/materials/pbs/*_material.fx`
. **MatrixCal.m** calculates transformation matrices