clc
clear

% Get file list
pngList = dir('*.png');

% Create ouput folder
if ~exist('alphaRemoved', 'dir') 
    mkdir('alphaRemoved') 
end

% Traitement
for indPng = 1 : length(pngList)
    currentFileName = pngList(indPng).name;
    [im, map, alpha] = imread(currentFileName);
    imwrite(im, ['alphaRemoved/', currentFileName(1:end-4), '_ColorMap.png']);
    imWhite = ones([size(alpha), 3]);
    imwrite(imWhite, ['alphaRemoved/', currentFileName(1:end-4), '_AlphaMap.png'], 'Alpha', alpha);
end

% End
clear im map alpha imWhite
disp('finished');


