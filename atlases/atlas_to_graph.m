% Ganesh Arvapalli
% 2/12/19

files = dir('*.nii.gz');
atlases = {};

%for i = 1:length(files)
for i = 1:5
    atlases{i} = double(niftiread(getfield(files, {i}, 'name')));
end
