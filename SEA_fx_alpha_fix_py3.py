#! /usr/bin/env python3
# coding:utf-8

import os

def file_extension(path): 
  return os.path.splitext(path)[1]

def main(fileDir):
    for root, dirs, files in os.walk(fileDir):
        for file in files:
            if file.endswith('mfm'):
                mfm_file_path = os.path.join(root, file)
                with open(mfm_file_path, 'r+') as file_obj:
                    print(file)
                    all_the_lines=file_obj.readlines()
                    file_obj.seek(0)
                    file_obj.truncate()
                    if root.endswith('aircraft'):
                        for line in all_the_lines:
                            file_obj.write(line.replace('shaders/std_effects/lightonly_alpha_flat.fx', 'shaders/materials/pbs/propeller_material.fx')\
                                .replace('shaders/std_effects/lightonly_alpha_flat_skinned.fx', 'shaders/materials/pbs/glass_material_skinned.fx'))
                    else:
                        for line in all_the_lines:
                            file_obj.write(line.replace('shaders/std_effects/lightonly_alpha_flat.fx', 'shaders/materials/pbs/glass_material.fx')\
                                .replace('shaders/std_effects/lightonly_alpha_flat_skinned.fx', 'shaders/materials/pbs/glass_material_skinned.fx'))
                    file_obj.close()

main("./")