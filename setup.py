from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "ntl_cpp",                               # Name of the module
        ["ntl_cpp/ntl_pybind.cpp", "ntl_cpp/ntl.cpp"], # Correctly list source files
        include_dirs=["ntl_cpp"],                      # Update include directory if needed
        extra_compile_args=['-std=c++17'],              # Additional flags (like C++ standard)
    )
]


# Setup function
setup(
    name="ntl",
    version="0.0",
    author="Jinwon Pyo",
    description="Number theory tools library",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    install_requires=[
        "pybind11>=2.12",    # Ensure pybind11 is installed
        "sympy>=1.12"        # Specify the version of sympy you need
    ],
    zip_safe=False,
)