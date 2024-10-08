# rDOCK BUILD INSTRUCTIONS

```
In this file you have the basic commands for installing rDock in 32- or 64-bits linux computers.
 For a more detailed explanation, please open the Getting Started guide or full documentation 
 in our webpage or in docs folder.
```

## BACKGROUND

rDock is written in C++ and makes heavy use of the C++ Standard Template Library (STL).
All source code is compiled into a single shared library (libRbt.so).
The executables are light-weight command-line applications linked with libRbt.so.

rDock should compile on the majority of Unix/Linux platforms with little or no
modification. However, only the following combinations have been thoroughly
tested:

openSUSE 32 and 64 bits.
Ubuntu 32 and 64 bits.
*  Both with compiler versions higher than 3.3.


### PREREQUISITES:

Make sure you have the following packages installed:

*  gcc		GNU C compiler (or your preferred C compiler)
*  g++		GNU C++ compiler (or your preferred C++ compiler)
*  make
*  popt		Command-line argument processing (run-time)
*  popt-devel	Command-line argument processing (compile-time)
*  cppunit		C++ unit testing framework (port of JUnit)
*  cppunit-devel		C++ unit testing framework (port of JUnit)

After installing these dependencies, please follow the following steps:

## BASIC BUILD INSTRUCTIONS:

### Step 1) BUILD

* Change current directory to build folder:
```
$ cd rDock_2021.1_src/build
```
And run, either:

```
$ make linux-g++           #for 32-bit build with g++ compiler
$ make linux-g++-64        #for 64-bit build with g++ compiler
```

If wish to use a different compiler/architecture combination, or if you wish to
change the compiler flags, see below.

The built libraries and executables are copied to their run-time locations
(../lib and ../bin) as part of Step 1.

### Step 2) TEST

```
$ make test                #Runs rDock unit tests
```

If the test has succeed, you are done, enjoy using rDock!
Otherwise, please check your dependencies and all the previous commands or go to 
Support Section in the webpage (http://rdock.sourceforge.net) to ask for help.

### Step 3) INSTALL

You can either run rDock directly from the build location initial testing), or 
install the binaries and data files to a new location.

Set the necessary environmental variables for running rDock in the command line.
(for example, in a bash shell):

```
$ export RBT_ROOT=/path/to/rDock/installation/
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$RBT_ROOT/lib
$ export PATH=$PATH:$RBT_ROOT/bin
```

### OTHER MAKE TARGETS

`make src_dist` 		Creates source distribution

`make clean`              Removes all intermediate build files

`make distclean`         Also removes installed libs and exes in ../lib and ../bin

