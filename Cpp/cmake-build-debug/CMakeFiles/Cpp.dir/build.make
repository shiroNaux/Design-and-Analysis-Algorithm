# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "D:\Application\Clion\CLion 2020.1\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "D:\Application\Clion\CLion 2020.1\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\Shiro\Documents\PTTKTT\Cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\Shiro\Documents\PTTKTT\Cpp\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Cpp.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Cpp.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Cpp.dir/flags.make

CMakeFiles/Cpp.dir/travelingSaleman.cpp.obj: CMakeFiles/Cpp.dir/flags.make
CMakeFiles/Cpp.dir/travelingSaleman.cpp.obj: ../travelingSaleman.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\Shiro\Documents\PTTKTT\Cpp\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Cpp.dir/travelingSaleman.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\Cpp.dir\travelingSaleman.cpp.obj -c C:\Users\Shiro\Documents\PTTKTT\Cpp\travelingSaleman.cpp

CMakeFiles/Cpp.dir/travelingSaleman.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Cpp.dir/travelingSaleman.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\Shiro\Documents\PTTKTT\Cpp\travelingSaleman.cpp > CMakeFiles\Cpp.dir\travelingSaleman.cpp.i

CMakeFiles/Cpp.dir/travelingSaleman.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Cpp.dir/travelingSaleman.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\Shiro\Documents\PTTKTT\Cpp\travelingSaleman.cpp -o CMakeFiles\Cpp.dir\travelingSaleman.cpp.s

# Object files for target Cpp
Cpp_OBJECTS = \
"CMakeFiles/Cpp.dir/travelingSaleman.cpp.obj"

# External object files for target Cpp
Cpp_EXTERNAL_OBJECTS =

Cpp.exe: CMakeFiles/Cpp.dir/travelingSaleman.cpp.obj
Cpp.exe: CMakeFiles/Cpp.dir/build.make
Cpp.exe: CMakeFiles/Cpp.dir/linklibs.rsp
Cpp.exe: CMakeFiles/Cpp.dir/objects1.rsp
Cpp.exe: CMakeFiles/Cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\Shiro\Documents\PTTKTT\Cpp\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Cpp.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Cpp.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Cpp.dir/build: Cpp.exe

.PHONY : CMakeFiles/Cpp.dir/build

CMakeFiles/Cpp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Cpp.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Cpp.dir/clean

CMakeFiles/Cpp.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\Shiro\Documents\PTTKTT\Cpp C:\Users\Shiro\Documents\PTTKTT\Cpp C:\Users\Shiro\Documents\PTTKTT\Cpp\cmake-build-debug C:\Users\Shiro\Documents\PTTKTT\Cpp\cmake-build-debug C:\Users\Shiro\Documents\PTTKTT\Cpp\cmake-build-debug\CMakeFiles\Cpp.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Cpp.dir/depend
