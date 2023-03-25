clc
clear
tic

%% Parameters

inputPath = '**';

%% Get input

mfmFileList = dir([inputPath, '/*.mfm']);

for indFile = 1:size(mfmFileList, 1)
    
    mfmFileName = [mfmFileList(indFile).folder, '\', mfmFileList(indFile).name];
    mfmFile = fopen(mfmFileName, 'r');
    isAircraft = size(mfmFileList(indFile).folder,2)>6 && strcmp(mfmFileList(indFile).folder(end-7:end), 'aircraft');
    
    newContent = '';
    modified = 0;
    
    line = fgetl(mfmFile);
    
    while line~=-1

        if contains(line, 'shaders/std_effects/lightonly_alpha_flat.fx')
            
            if isAircraft
                newLine = replace(line, 'shaders/std_effects/lightonly_alpha_flat.fx', 'shaders/materials/pbs/propeller_material.fx');
            else
                newLine = replace(line, 'shaders/std_effects/lightonly_alpha_flat.fx', 'shaders/materials/pbs/glass_material.fx');
            end
            
            modified = 1;
            
        elseif contains(line, 'shaders/std_effects/lightonly_alpha_flat_skinned.fx')
            
            newLine = replace(line, 'shaders/std_effects/lightonly_alpha_flat.fx', 'shaders/materials/pbs/glass_material_skinned.fx');
            modified = 1;
            
        else
            
            newLine = line;
        
        end
        
        newContent = [newContent, newLine, '\r\n'];
        line = fgetl(mfmFile);
        
    end
    
    fclose(mfmFile);
    
    if modified
        mfmFile = fopen(mfmFileName, 'w');
        fprintf(mfmFile, newContent);
        disp([mfmFileName, ' is updated']);
        fclose(mfmFile);
    end
     
end

%% End

fclose all;
toc
disp('Finished');