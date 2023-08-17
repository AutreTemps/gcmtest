SetFactory("OpenCASCADE");

Circle(1) = {0, 0, 0, 0.286 / 2};

Curve Loop(1) = {1};

Plane Surface(1) = {1};

Physical Curve(1) = {1};
Physical Surface("Round") = {1};

Extrude {0, 0, 0.06} { Surface{1}; }

Physical Volume ("Disc", 1) = {1};

Mesh.CharacteristicLengthMax = 0.0035;
Mesh 3;
