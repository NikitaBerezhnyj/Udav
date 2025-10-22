cmake_minimum_required(VERSION 3.15)
project(udav)

set(CMAKE_CXX_STANDARD 17)

include_directories(src/includes)

add_executable(udav
    src/main.cpp
    src/compiler.cpp
    src/cli.cpp
)
