# Master makefile for rDock
#
# Compilation build targets
#
# make linux-g++        g++, 32-bit 
# make linux-g++-64     g++, 64-bit 
# make linux-pathCC-64  Pathscale 64-bit (AMD Opteron x86_64)
#
# The above targets are also available with a -dt suffix to build the
# Daylight toolkit dependent exes as well (rbtether, smart_rms)
# e.g. make linux-g++-dt
# 
# The above targets are also available with a -debug suffix to build
# the rDock library and exes in debug mode.
# e.g. make linux-g++-debug
#
# Testing build targets
#
# make test             Runs rDock unit tests
#
# Distribution build targets
#
# make dist             Creates binary distribution
# make src_dist         Creates source distribution
#                       (including binaries if built)
# make clean            Removes intermediate build files
# make distclean        Also removes installed exes and libs
#
# Note: use 'make distclean' before 'make src_dist' to create
# the most compact source-only distribution
################################################################
#
#PRODUCT		:= $(shell ./p4utils.pl PRODUCT)
#CODELINE	:= $(shell ./p4utils.pl CODELINE)
PRODUCT		:= ..
CODELINE	:= 
VERSION		:= $(shell ./p4utils.pl VERSION)
TAR     	= tar -cvzf

# File lists for rDock distribution
# We make use of the symbolic link in the build directory
# rdock -> ../../../rdock
# so that we can preserve full pathnames in the tar file
#
DIST_BIN =	$(PRODUCT)/$(CODELINE)/bin/ \
		$(PRODUCT)/$(CODELINE)/lib/ \
		$(PRODUCT)/$(CODELINE)/fw/lib/

DIST_DATA =	$(PRODUCT)/$(CODELINE)/data/ \
		$(PRODUCT)/$(CODELINE)/docs/

DIST_SRC =	$(PRODUCT)/$(CODELINE)/include/ \
		$(PRODUCT)/$(CODELINE)/src/ \
                $(PRODUCT)/$(CODELINE)/build/ \
                $(PRODUCT)/$(CODELINE)/import/simplex/ \
                $(PRODUCT)/$(CODELINE)/import/tnt/




# Environment for running rDock unit tests
export RBT_ROOT	= ../
export RBT_HOME	= ./test/RBT_HOME
export LD_LIBRARY_PATH = ../lib

##################################################
# Main rDock build targets
.PHONY: linux-g++ linux-g++-64 linux-pathCC-64
linux-g++:
	$(MAKE) "PLATFORM=linux-g++" "CONFIG=release" "VERSION=$(VERSION)" -f Makefile rdock

linux-g++-64:
	$(MAKE) "PLATFORM=linux-g++-64" "CONFIG=release" "VERSION=$(VERSION)" -f Makefile rdock

linux-pathCC-64:
	$(MAKE) "PLATFORM=linux-pathCC-64" "CONFIG=release" "VERSION=$(VERSION)" -f Makefile rdock

# Debug versions of the above
.PHONY:	linux-g++-debug linux-g++-64-debug linux-pathCC-64-debug
linux-g++-debug:
	$(MAKE) "PLATFORM=linux-g++" "CONFIG=debug" "VERSION=$(VERSION)" -f Makefile rdock

linux-g++-64-debug:
	$(MAKE) "PLATFORM=linux-g++-64" "CONFIG=debug" "VERSION=$(VERSION)" -f Makefile rdock

linux-pathCC-64-debug:
	$(MAKE) "PLATFORM=linux-pathCC-64" "CONFIG=debug" "VERSION=$(VERSION)" -f Makefile rdock

# Release versions including the Daylight-dependent executables
.PHONY:	linux-g++-dt linux-g++-64-dt linux-pathCC-64-dt
linux-g++-dt:
	$(MAKE) "PLATFORM=linux-g++" "CONFIG=release" "VERSION=$(VERSION)" -f Makefile rdock-dt

linux-g++-64-dt:
	$(MAKE) "PLATFORM=linux-g++-64" "CONFIG=release" "VERSION=$(VERSION)" -f Makefile rdock-dt

linux-pathCC-64-dt:
	$(MAKE) "PLATFORM=linux-pathCC-64" "CONFIG=release" "VERSION=$(VERSION)" -f Makefile rdock-dt

##################################################
# Run unit tests
# Requires unit_test executable (should be built by the above) and active site (.as) files
# for 1koc and 1YET, generated by rbcavity (cavity mapping)
.PHONY:	test
test:	./test/RBT_HOME/1koc.as ./test/RBT_HOME/1YET.as ./test/RBT_HOME/1YET_test.as
	@echo ""
	@echo "Running rDock unit tests..."
	@echo ""
	@$(RBT_ROOT)/bin/rbdock -r1YETmine.prm -i ./test/RBT_HOME/1YET_c.sd -p dock.prm -n 20 -s 48151623 -o 1YET_test_out > 1YET_test_out.log
	@mv 1YET_test_out.log 1YET_test_out.sd ./test/RBT_HOME/
	@python ./test/RBT_HOME/check_test.py ./test/RBT_HOME/1YET_reference_out.sd ./test/RBT_HOME/1YET_test_out.sd

./test/unit_test:
	$(warning $@ executable not found)
	$(warning Use 'make <PLATFORM>' first)
	$(warning e.g. 'make linux-g++')
	$(error Unit tests failed)

# Generate the .as file for 1koc
./test/RBT_HOME/1koc.as:	./test/RBT_HOME/1koc.prm
	@echo ""
	@echo "Cavity mapping of 1koc.prm"
	@echo ""
	@$(RBT_ROOT)/bin/rbcavity -r1koc.prm -was
	@mv 1koc.as ./test/RBT_HOME/

# Generate the .as file for 1YET
./test/RBT_HOME/1YET.as:	./test/RBT_HOME/1YET.prm
	@echo ""
	@echo "Cavity mapping of 1YET.prm"
	@echo ""
	@$(RBT_ROOT)/bin/rbcavity -r1YETmine.prm -was
	@mv 1YETmine.as ./test/RBT_HOME/

# Generate the .as file for 1koc
./test/RBT_HOME/1YET_test.as:	./test/RBT_HOME/1YET_test.prm
	@echo ""
	@echo "Cavity mapping of 1YET_test.prm"
	@echo ""
	@$(RBT_ROOT)/bin/rbcavity -r1YET_test.prm -was
	@mv 1YET_test.as ./test/RBT_HOME/

##################################################
# Create distributions (.tgz files)
#
# Without source code
.PHONY:	dist src_dist clean distclean
dist:
	$(TAR) $(PRODUCT)_$(CODELINE).tgz \
		--exclude=*~ \
		$(DIST_BIN) $(DIST_DATA)

# With source code
src_dist:
	$(TAR) $(PRODUCT)_$(CODELINE)_src.tgz \
		--exclude=*~ \
		--exclude=$(PRODUCT)/$(CODELINE)/build/*.tgz \
		--exclude=$(PRODUCT)/$(CODELINE)/build/Makefile.* \
		--exclude=$(PRODUCT)/$(CODELINE)/build/linux* \
		--exclude=$(PRODUCT)/$(CODELINE)/build/test/*.o \
		--exclude=$(PRODUCT)/$(CODELINE)/build/test/unit_test \
		--exclude=$(PRODUCT)/$(CODELINE)/build/test/RBT_HOME/*.as \
		--exclude=$(PRODUCT)/$(CODELINE)/build/restart.sd \
		$(DIST_BIN) $(DIST_DATA) $(DIST_SRC)

# Removes all intermediate build files under ./build
# but does not remove the installed libraries and exes in ../lib and ../bin
clean:
	-rm -rf ./linux-g++ ./linux-g++-64 ./linux-pathCC-64
	-rm -f ./Makefile.*
	-rm -f ./test/*.o
	-rm -f ./test/RBT_HOME/*.as
	-rm -f ./test/unit_test
	-rm -f ./test/RBT_HOME/1YET_test_out*
	-rm -f ./restart.sd

# Also removes the installed libraries and exes
# Use 'make distclean' before 'make src_dist' to create the most
# compact source distribution
distclean:	clean
	-rm -f ../lib/libRbt*
	-rm -f ../bin/rb*
	-rm -f ../bin/smart_rms
