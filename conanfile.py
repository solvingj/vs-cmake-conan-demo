from conans import ConanFile

class VsCmakeConanDemo(ConanFile):
  name = "VsCmakeConanDemo"
  version = "0.1.0"
  description = "A demo of using Visual Studio's Cmake integration with Conan.io"
  author = "SolvingJ/Bincrafters"
  generators = "cmake"
  url = "https://github.com/solvingj/vs-cmake-conan-demo"
  requires = "jsonformoderncpp/2.1.1@vthiery/stable", \
        "OpenSSL/1.0.2l@conan/stable", \
		"Boost.Asio/1.64.0@bincrafters/stable"

