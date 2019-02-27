function [atlas1_flat, atlas2_flat, ConcordanceValues1] = ConcordanceCalculator(atlas1File,atlas2File)
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

ConcordanceValues1 = zeros(length(values1),length(values2));
for i = 1:length(atlas1_flat)
   x = atlas1_flat(i)+1;
   y = atlas2_flat(i)+1;
   ConcordanceValues1(x,y) = ConcordanceValues1(x,y)+1;
end

for j = 1:length(values1)
    rowCount = sum(ConcordanceValues1(j,:));
    ConcordanceValues1(j,:) = ConcordanceValues1(j,:)/rowCount;
end

end

