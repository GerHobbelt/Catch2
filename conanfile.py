from conans import ConanFile, CMake, tools

class Catch2Conan(ConanFile):
    description = "A modern, C++-native, framework for unit-tests, TDD and BDD"
    exports = "LICENSE.txt"
    exports_sources = "CMakeLists.txt", "CMake/*", "extras/*", "src/*"
    generators = "cmake"
    license = "BSL-1.0"
    name = "catch2"
    settings = "os", "compiler", "build_type", "arch"
    topics = ("conan", "catch2", "unit-test", "tdd", "bdd")
    url = "https://github.com/tnt-coders/Catch2.git"

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["CATCH_INSTALL_DOCS"] = "OFF"
        cmake.definitions["CATCH_INSTALL_HELPERS"] = "ON"
        cmake.configure(build_folder="build")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
