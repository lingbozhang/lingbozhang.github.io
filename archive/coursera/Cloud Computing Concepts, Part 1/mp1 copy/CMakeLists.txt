cmake_minimum_required(VERSION 3.12)
project(mp1)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(mp1
        Application.cpp
        Application.h
        EmulNet.cpp
        EmulNet.h
        Grader.sh
        Log.cpp
        Log.h
        Makefile
        Member.cpp
        Member.h
        MP1Node.cpp
        MP1Node.h
        Params.cpp
        Params.h
        Queue.h
        stdincludes.h)
