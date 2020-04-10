from conans import ConanFile, CMake

class Pkg(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt", "!src/build*/*", "Find*.cmake"
    requires = "say/0.1@user/testing"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("Find*.cmake", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]