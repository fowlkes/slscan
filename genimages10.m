%
% this script generates a sequenced of horizontal and vertical
% graycode images of size (1024 x 768) and writes them out to
% the subdirectory "gray"
%

% first build a table of the gray code sequence for each of
% integers 0..1023
X = dec2gray(0:1023,10);

% write out the horizontal code
for i = 1:10
  % the image
  I = repmat([zeros(128,1); X(:,i); zeros(128,1)],1,800);
  I2 = repmat([zeros(128,1); 1-X(:,i); zeros(128,1)],1,800);
  imwrite(I',sprintf('gray/%2.2d.png',i),'png');
  imwrite(I2',sprintf('gray/%2.2d_i.png',i),'png');
end

%now write out the vertical code
X = dec2gray(0:799,10);
for i = 1:10
  I = [zeros(800,128) repmat(X(:,i),1,1024) zeros(800,128)];
  I2 = [zeros(800,128) repmat(1-X(:,i),1,1024) zeros(800,128)];
  imwrite(I,sprintf('gray/%2.2d.png',i+10),'png');
  imwrite(I2,sprintf('gray/%2.2d_i.png',i+10),'png');
end

