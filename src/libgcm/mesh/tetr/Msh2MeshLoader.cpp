#include "libgcm/mesh/tetr/Msh2MeshLoader.hpp"

#include "libgcm/util/formats/MshTetrFileReader.hpp"

using namespace gcm;
using std::string;

Msh2MeshLoader::Msh2MeshLoader() {
    INIT_LOGGER("gcm.Msh2MeshLoader");
}

Msh2MeshLoader::~Msh2MeshLoader() {
}

string Msh2MeshLoader::getVtkFileName(string mshFile)
{
    return mshFile + ".tmp.vtu";
}

void Msh2MeshLoader::cleanUp() {
}

void Msh2MeshLoader::loadMesh(TetrMeshSecondOrder* mesh, GCMDispatcher* dispatcher, const string& fileName)
{
    auto body = mesh->getBody();
    auto& engine = Engine::getInstance();
    if( engine.getRank() == 0 )
    {
        LOG_DEBUG("Worker 0 started generating second order mesh");
        TetrMeshFirstOrder* foMesh = new TetrMeshFirstOrder();
        foMesh->setBody(body);

        TetrMeshSecondOrder* soMesh = new TetrMeshSecondOrder();
        soMesh->setBody(body);

        int sd, nn;
        AABB scene;
        GCMDispatcher* myDispatcher = new DummyDispatcher();
        preLoadMesh(&scene, sd, nn, fileName);
        myDispatcher->prepare(1, &scene);

        MshTetrFileReader* reader = new MshTetrFileReader();
        reader->readFile(fileName,
                            foMesh, myDispatcher, engine.getRank(), true);
        soMesh->copyMesh(foMesh);
        soMesh->preProcess();

        VTK2SnapshotWriter* sw = new VTK2SnapshotWriter();
        // FIXME are we really about to overwrite this file?
        sw->dump(soMesh, -1, fileName);

        delete sw;
        delete reader;
        delete foMesh;
        delete soMesh;
        LOG_DEBUG("Worker 0 completed generating second order mesh");
    }

    MPI::COMM_WORLD.Barrier();

    LOG_DEBUG("Starting reading mesh");
    Vtu2TetrFileReader* reader = new Vtu2TetrFileReader();
    reader->readFile(getVtkFileName(fileName), mesh, dispatcher, engine.getRank());
    delete reader;
    LOG_DEBUG("Deleting generated file: " << getVtkFileName(fileName));
    remove( getVtkFileName(fileName).c_str() );

    mesh->preProcess();
}

void Msh2MeshLoader::preLoadMesh(AABB* scene, int& sliceDirection, int& numberOfNodes, const string& fileName) {
    MshTetrFileReader* reader = new MshTetrFileReader();
    reader->preReadFile(fileName, scene, sliceDirection, numberOfNodes);
    delete reader;
}
