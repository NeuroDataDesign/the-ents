function [atlas1_cell, atlas2_cell, DiceValues1] = DiceCalculator(atlas1File,atlas2File)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Description: Calculates the Dice coefficient between two input atlases. 
%              Currently outputs the Dice coefficient per ROI for atlas1 to
%              atlas2
%
% Inputs:      atlas1File - The filepath of the .nii file for the first
%                           atlas
%              atlas2File - The filepath of the .nii file for the second
%                           atlas
%
% Outputs:     atlas1_cell - A cell array representation of the first atlas
%                            where each cell corresponds to an ROI and
%                            contains the indices of the points in that ROI
%              atlas2_cell - A cell array representation of the second 
%                            atlas where each cell corresponds to an ROI 
%                            and contains the indices of the points in that 
%                            ROI
%              DiceValues1 - A MxN matrix where M is the number of ROIs in
%                            the first atlas and N is the number of ROIs in
%                            the second atlas. Each value Aij is the Dice
%                            coefficient between the ith ROI in the first
%                            atlas and the jth ROI in the second atlas


% Read in atlas nifti files
atlas1 = double(niftiread(atlas1File));
atlas2 = double(niftiread(atlas2File));

% Calculate total elements in each atlas image
size1 = prod(size(atlas1));
size2  = prod(size(atlas2));

% Flatten each of the atlas images into 1D
atlas1_flat = reshape(atlas1, [size1,1]);
atlas2_flat = reshape(atlas2, [size2, 1]);

% Calculate number of ROIs for each atlas
values1 = unique(atlas1);
values2 = unique(atlas2);

% Set up cell arrays for new atlas representation
atlas1_cell = cell(length(values1),1);
atlas2_cell = cell(length(values2),1);

% Add a second column to the flattened atlases which contains the indexes
% of each of the current points. This column allows for the location of
% the ROI to be preserved when the array is sorted by ROI number
atlas1_flat = [atlas1_flat, (1:length(atlas1_flat))'];
atlas2_flat = [atlas2_flat, (1:length(atlas2_flat))'];
atlas1_flat = sort(atlas1_flat,1);
atlas2_flat = sort(atlas2_flat,1);

% For each of the ROIs, add the locations of the points in that ROI into
% the corresponding cell in the cell representation
startInd1 = 1;
for i = 1:length(values1)
   key = find(atlas1_flat(:,1) ==i,1);
   endInd1 = atlas1_flat(key,2);
   atlas1_cell{i} =  startInd1:endInd1;
   startInd1 = endInd1+1;    
end
atlas1_cell{end} = startInd1:length(atlas1_flat);

startInd2 = 1;
for i = 1:length(values2)
   key = find(atlas2_flat(:,1) ==i,1);
   endInd2 = atlas2_flat(key,2);
   atlas2_cell{i} =  startInd2:endInd2;
   startInd2 = endInd2+1;    
end
atlas2_cell{end} = startInd2:length(atlas2_flat);


% Calculate the Dice coefficient between every pair of ROIs in the two
% atlases. Atlas1 (A) is always the reference here, so the equation for Dij
% is the number of times Ai contains the same locations as Bj divided by
% the total number of locations in Ai
DiceValues1 = zeros(length(values1),length(values2));
for i = 1:length(values1)
    for j = 1:length(values2)
        diffnum = length(setdiff(atlas1_cell{i}, atlas2_cell{j}));
        concurrances = length(atlas1_cell{i})-diffnum;
        DiceValues1(i,j) = concurrances/length(atlas1_cell{i});
    end
end

end

