#include <pybind11/pybind11.h>
#include "ntl.h"  // Update this to the actual location of your ntl.h file
#include <iostream>

using namespace std;

namespace py = pybind11;

// Template instantiation for common types
template<typename T>
void bind_repeated_sqr_mod(py::module_& m, const std::string& typestr) {
    m.def(("RepeatedSqrMod_" + typestr).c_str(), &jpyo0803::RepeatedSqrMod<T>,
          py::arg("base"), py::arg("exp"), py::arg("mod") = 0,
          ("Compute base^exp % mod (if mod != 0) for type " + typestr).c_str());
}

template<typename T>
void bind_repeated_sqr(py::module_& m, const std::string& typestr) {
    m.def(("RepeatedSqr_" + typestr).c_str(), &jpyo0803::RepeatedSqr<T>,
          py::arg("base"), py::arg("exp"),
          ("Compute base^exp for type " + typestr).c_str());
}

template<typename T>
void bind_gcd(py::module_& m, const std::string& typestr) {
    m.def(("Gcd_" + typestr).c_str(), &jpyo0803::Gcd<T>,
          py::arg("x"), py::arg("y"),
          ("Gcd(x, y) for type " + typestr).c_str());
}

template<typename T>
void bind_is_prime(py::module_& m, const std::string& typestr) {
    m.def(("IsPrime_" + typestr).c_str(), &jpyo0803::IsPrime<T>,
          py::arg("x"),
          ("IsPrime(x) for type " + typestr).c_str());
}

PYBIND11_MODULE(ntl, m) {
    m.doc() = "Pybind11 wrapper for the number theory library";

    // Binding for integer types
    bind_repeated_sqr_mod<int32_t>(m, "int32");
    bind_repeated_sqr_mod<uint32_t>(m, "uint32");
    bind_repeated_sqr_mod<int64_t>(m, "int64");
    bind_repeated_sqr_mod<uint64_t>(m, "uint64");

    bind_repeated_sqr<int32_t>(m, "int32");
    bind_repeated_sqr<uint32_t>(m, "uint32");
    bind_repeated_sqr<int64_t>(m, "int64");
    bind_repeated_sqr<uint64_t>(m, "uint64");

    bind_gcd<uint32_t>(m, "uint32");
    bind_gcd<uint64_t>(m, "uint64");

    bind_is_prime<uint32_t>(m, "uint32");
    bind_is_prime<uint64_t>(m, "uint64");

    // If needed, add other types here such as float, double, etc.
}