cmake_minimum_required (VERSION 3.11)

if(TARGET say::say)
    set(say_FOUND TRUE)
elseif(TARGET CONAN_PKG::say)
    add_library(say::say INTERFACE IMPORTED)
    target_link_libraries(say::say INTERFACE CONAN_PKG::say)
    set(say_FOUND TRUE)
else()
    set(say_FOUND FALSE)
    if(say_FIND_REQUIRED)
        message(FATAL_ERROR "Unable to find CONAN_PKG::say, did you forget conan_basic_setup(TARGETS)?")
    endif()
endif()