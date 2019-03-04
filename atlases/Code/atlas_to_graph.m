% Ganesh Arvapalli
% 2/12/19

function [G] = atlas_to_graph(filename)
    G = graph();
    img = double(niftiread(filename));
    values = unique(img);
    vector = img(:);
    for i = 1:length(vector)
        G = addnode(G, vector(i));
    end

    for i = 1:length(values)
        indices = find(vector == values(i));
        combos = combnk(indices, 2);
        for j = 1:length(combos)
            G = addedge(combos(j, 1), combos(j, 2));
        end
    end
    plot(G);
end

% files = dir('*.nii.gz');
% atlases = {};
% 
% %for i = 1:length(files)
% for i = 1:5
%     atlases{i} = double(niftiread(getfield(files, {i}, 'name')));
% end
