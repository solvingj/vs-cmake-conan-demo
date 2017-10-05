## This project demonstrates Visual Studio's CMake integration with Conan


## Requirements
* Visual Studio 2017
* CMake Integration Enabled

## Suggested
* Visual Studio Python Language Support


## To Use
* In Visual Studio, choose "Open Folder" 
* Browse to the root of the project folder
* Select it to open it
* Visual Studio Automatically finds CMakeLists.txt
* Visual Studio Invokes Cmake to build the Cmake Cache 
* This line is thereby invoked: `include(conan_include.cmake)`
* This downloads the `conan.cmake` file if it doesn't exist
* The `conan.cmake` file is invoked
* `conan.cmake` detects your settings from visual studio
* `conan.cmake` invokes conan at the CLI with those settings
* The `conanbuildinfo.cmake` file is generated
* It can be found by clicking the following menu options: 

	`Cmake` -> `Cache` -> `Open Cache Folder` -> `CMakeLists.txt`

## Notes
During my last tests, this required one modification of the default values in CMakeSettings.json: 
* `"cmakeCommandArgs": "-DCMAKE_BUILD_TYPE=Debug"`

This is needed to help `conan.cmake` properly detect the build type, because it wasn't working when I tested.  Although, testing was done in the very first release of Visual Studio for Cmake's. 