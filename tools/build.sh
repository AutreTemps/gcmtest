#!/bin/bash
export LD_LIBRARY_PATH=./build/:/usr/lib64/openmpi/lib/
rm -R bin/ lib/ include/ share/
waf distclean
waf configure --prefix=. --cxxflags=-O3 --without-headers --without-resources
waf install