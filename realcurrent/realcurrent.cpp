// realcurrent.cpp

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>
#include <vector>
#include <thread>

namespace py = pybind11;

std::vector<py::object> execute_concurrent(const std::vector<py::function>& funcs, const std::vector<py::tuple>& args) {
    std::vector<py::object> results;
    results.reserve(funcs.size());

    for (size_t i = 0; i < funcs.size(); ++i) {
        results.push_back(funcs[i](args[i][0].cast<int>(), args[i][1].cast<int>()));
    }

    return results;
}

PYBIND11_MODULE(realcurrent, m) {
    m.def("execute_concurrent", &execute_concurrent, "Execute Python functions concurrently");
}
