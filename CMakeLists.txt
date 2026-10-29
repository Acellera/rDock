# Build used for the pip wheel (pyproject.toml). The conda package still uses build/makefile.
cmake_minimum_required(VERSION 3.18)
project(rDock CXX)

# Same flags as build/tmakelib/linux-g++-64/tmake.conf. No -DNDEBUG, so asserts stay on like in the make build.
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -ffast-math")
add_compile_options(-std=c++14 -fpermissive -w)
add_compile_definitions(_NDEBUG)
set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")

file(GLOB LIB_SOURCES src/lib/*.cxx src/GP/Rbt*.cxx import/simplex/src/*.cxx)
add_library(Rbt SHARED ${LIB_SOURCES})
target_include_directories(Rbt PUBLIC include include/GP import/simplex/include import/tnt/include)

find_library(POPT popt REQUIRED)
set(EXES rbdock rbcavity rbmoegrid rblist rbcalcgrid)
foreach(exe ${EXES})
  add_executable(${exe} src/exe/${exe}.cxx)
  target_link_libraries(${exe} Rbt ${POPT})
endforeach()

# Laid out as RBT_ROOT inside the python package, see python/rdock/__init__.py
install(TARGETS Rbt LIBRARY DESTINATION rdock/lib)
install(TARGETS ${EXES} RUNTIME DESTINATION rdock/bin)
install(FILES lib/SDRecord.pm lib/run_rbfuncs.pl DESTINATION rdock/lib)
install(PROGRAMS
  bin/make_grid.csh bin/rbhtfinder bin/run_rbdock.pl bin/run_rbscreen.pl
  bin/sdfield bin/sdfilter bin/sdmodify bin/sdreport bin/sdrmsd bin/sdsort bin/sdsplit bin/sdtether
  DESTINATION rdock/bin)
install(DIRECTORY data DESTINATION rdock)
