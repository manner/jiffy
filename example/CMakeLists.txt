# Almost all CMake files should start with this
# You should always specify a range with the newest
# and oldest tested versions of CMake. This will ensure
# you pick up the best policies.
cmake_minimum_required(VERSION 3.12)

# This is your project statement. You should always list languages;
# Listing the version is nice here since it sets lots of useful variables
project(
        JiffyExample
        VERSION 1.0
        LANGUAGES CXX)

# If you set any CMAKE_ variables, that can go here.
# (But usually don't do this, except maybe for C++ standard)

# Find packages go here.

# You should usually split this into folders, but this is a simple example

# This is a "default" library, and will match the *** variable setting.
# Other common choices are STATIC, SHARED, and MODULE
# Including header files here helps IDEs but is not required.
# Output libname matches target name, with the usual extensions on your system
#add_library(Jiffy simple_lib.cpp simple_lib.hpp)
#add_subdirectory(../libjiffy ../libjiffy)
#target_include_directories(JiffyExample PUBLIC ../libjiffy)
#include_directories(${PROJECT_SOURCE_DIR}/libjiffy/src/jiffy/client)


#target_include_directories(JiffyExample PRIVATE ${PROJECT_SOURCE_DIR}/libjiffy/src/jiffy)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../libjiffy/src)

add_executable(JiffyExample example.cpp)
add_executable(JiffyReader reader.cpp)
target_link_libraries(JiffyExample jiffy)
target_link_libraries(JiffyReader jiffy)

# Link each target with other targets or add options, etc.
#SET(TARGET_H
#        ../libjiffy/src/jiffy/client/jiffy_client.h)

#SET(TARGET_SRC
#        example.cpp
#        ../libjiffy/src/jiffy/client/jiffy_client.cpp)
# Adding something we can run - Output name matches target name

# Make sure you link your targets with this command. It can also link libraries and
# even flags, so linking a target that does not exist will not give a configure-time error.
#target_link_libraries(JiffyExample Jiffy)