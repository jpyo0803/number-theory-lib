cmake_minimum_required(VERSION 3.10)
project(ntl VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)

find_package(pybind11 REQUIRED)

pybind11_add_module(ntl ntl_cpp/ntl_pybind.cpp ntl_cpp/ntl.cpp)
