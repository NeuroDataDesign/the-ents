% Ganesh Arvapalli
% 2/26/19
clc;
clear all;

files = dir('*.nii.gz');
atlases = {};

fileID = fopen('region_vol_data.txt','w');

for i = 1:length(files)
% for i = 1:3
    fn = getfield(files, {i}, 'name');
    atlases{i} = double(niftiread(fn));
    if ~contains(fn, "DS")
        [r, v] = region_vols(atlases{i});
        fprintf(fileID, "%s (%d regions) average region volume: %.3f\n", fn, r, mean(v));
    end
end

fclose('all');


function [regions, vols]=region_vols(atlas)
    vols = [];
    % (Exclude 0 as a region since that's just background)
    range = min(min(min(atlas)))+1:max(max(max(atlas)));
    regions = length(range);
    
    for i=range
        vol = sum(sum(sum(atlas == i)));
        vols = [vols; vol];
    end
end



