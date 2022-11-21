%
% this script generates a sequenced of horizontal and vertical
% graycode images of size (1024 x 768) and writes them out to
% the subdirectory "gray"
%

% first build a table of the gray code sequence for each of
% integers 0..1023
X = dec2gray(0:1280,11);

%X = [zeros(128,10); X; zeros(128,10)]; %pad with zeros to avoid 11th bit

% write out the horizontal code
for i = 1:11
  % the image
  I = repmat(X(:,i),1,800);
  % and its inverse
  I2 = 1-I;
  imwrite(I',sprintf('gray/%2.2d.png',i),'png');
  imwrite(I2',sprintf('gray/%2.2d_i.png',i),'png');
end

%now write out the vertical code
X = dec2gray(0:799,10);
for i = 1:10
  I = repmat(X(:,i),1,1280);
  I2 = 1-I;
  imwrite(I,sprintf('gray/%2.2d.png',i+11),'png');
  imwrite(I2,sprintf('gray/%2.2d_i.png',i+11),'png');
end

