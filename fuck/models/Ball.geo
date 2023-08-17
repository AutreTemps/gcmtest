SetFactory("OpenCASCADE");

Sphere(1) = {0, 0, 0, 0.076 / 2};

Physical Volume ("Ball", 1) = {1};

Mesh.CharacteristicLengthMax = 0.0035;
Mesh 3;
