l = 0;
h = 1;
wh = 5;
Point(1) = {-wh, -wh, l, 1};
Point(2) = {wh, -wh, l, 1};
Point(3) = {wh, wh, l, 1};
Point(4) = {-wh, wh, l, 1};
Point(5) = {-wh, wh, h, 1};
Point(6) = {wh, wh, h, 1};
Point(7) = {wh, -wh, h, 1};
Point(8) = {-wh, -wh, h, 1};
Line(1) = {4, 5};
Line(2) = {5, 6};
Line(3) = {6, 3};
Line(4) = {3, 4};
Line(5) = {4, 1};
Line(6) = {1, 8};
Line(7) = {8, 5};
Line(8) = {3, 2};
Line(9) = {2, 7};
Line(10) = {7, 6};
Line(11) = {7, 8};
Line(12) = {1, 2};
Line Loop(14) = {4, 1, 2, 3};
Plane Surface(14) = {14};
Line Loop(16) = {5, 6, 7, -1};
Plane Surface(16) = {16};
Line Loop(18) = {3, 8, 9, 10};
Plane Surface(18) = {18};
Line Loop(20) = {9, 11, -6, 12};
Plane Surface(20) = {20};
Line Loop(22) = {12, -8, 4, 5};
Plane Surface(22) = {22};
Line Loop(24) = {2, -10, 11, 7};
Plane Surface(24) = {24};
Surface Loop(26) = {24, 14, 22, 20, 18, 16};
Volume(26) = {26};
