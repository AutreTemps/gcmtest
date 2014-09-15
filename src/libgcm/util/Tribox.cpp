#include "libgcm/util/Tribox.hpp"
// FIXME this code has no license information
#include "libgcm/util/TriboxImpl.cpp"

#include <memory.h>

bool gcm::triangleIntersectsBox(const Node& boxCenter, const vector3r& boxHalfEdges, const Node& v1, const Node& v2, const Node& v3)
{
    float triverts[3][3];
    memcpy(triverts[0], v1.coords, sizeof(float)*3);
    memcpy(triverts[1], v2.coords, sizeof(float)*3);
    memcpy(triverts[2], v3.coords, sizeof(float)*3);

    return triBoxOverlap(boxCenter.coords, boxHalfEdges.coords, triverts);
}

bool gcm::triangleIntersectsCube(const Node& cubeCenter, real cubeHalfEdge, const Node& v1, const Node& v2, const Node& v3)
{
    return triangleIntersectsBox(cubeCenter, vector3r(cubeHalfEdge, cubeHalfEdge, cubeHalfEdge), v1, v2, v3);
}