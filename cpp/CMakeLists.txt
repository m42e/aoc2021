project(dcc CXX)
cmake_minimum_required(VERSION 3.16)


set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_BUILD_TYPE Debug)

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fconcepts")
if(PROF)
if(PROF_GEN)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-generate -O3  -flto")
else()
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-instr-use=default.profdata -O3")
endif()
else()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3  -flto")
endif()

file (GLOB sources CONFIGURE_DEPENDS *.cpp )

foreach(file ${sources})
  if (${file} MATCHES "challenge([0-2][0-9].).cpp" )
    string(REGEX REPLACE ".*/challenge([0-2][0-9].).cpp" "day\\1" execname ${file} )
    add_executable(${execname} challenge.cpp main.cpp ${file} )
  endif()
endforeach()

add_executable(dcc EXCLUDE_FROM_ALL ${sources})
