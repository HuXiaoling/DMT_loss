clear,clc

edge_out = load('output/dimo_edge.txt');
vert_out = load('output/dimo_vert.txt');

mask = zeros(1024,1024,10);
for i=1:length(vert_out)
    mask(vert_out(i,1)+1, vert_out(i,2)+1, vert_out(i,3)+1) = 1;
end
% volumeViewer(mask)
% imshow(mask,[])
% imwrite(mask, 'mask_dmt.png');


% se = strel('sphere',1);
% mask = imdilate(mask,se);

% volumeViewer(temp)

outputFileName_data = 'mask.tiff';

for K=1:size(mask,3)
    slice = mask(:,:,K);
    imwrite(slice, outputFileName_data, 'WriteMode', 'append');
end
