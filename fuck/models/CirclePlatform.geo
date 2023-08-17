SetFactory("OpenCASCADE");

Circle(1) = {0, 0, 0, 0.2};
Circle(2) = {0, 0, 0, 0.02};

Curve Loop(1) = {1};
Curve Loop(2) = {2};

Plane Surface(1) = {1, 2};

Physical Curve(1) = {1};
Physical Surface("Round") = {1};

Extrude {0, 0, 0.03} { Surface{1}; }

Physical Volume ("Platform", 1) = {1};

Mesh.CharacteristicLengthMax = 0.00347;
Mesh 3;
