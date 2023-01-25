if (NOT APPLE AND UNIX)
  set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--no-as-needed -ldl")
endif ()

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../libjiffy/src
        ${CMAKE_CURRENT_SOURCE_DIR}/../thirdparty/libcuckoo
        ${Boost_INCLUDE_DIRS})
add_executable(storaged ${CMAKE_CURRENT_SOURCE_DIR}/src/storage_server.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/server_storage_tracker.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/src/server_storage_tracker.h)

add_dependencies(storaged boost_ep ${HEAP_MANAGER_EP} thrift_ep)

target_link_libraries(storaged jiffy ${HEAP_MANAGER_LIBRARY} ${Boost_PROGRAM_OPTIONS_LIBRARY})

install(TARGETS storaged
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib)