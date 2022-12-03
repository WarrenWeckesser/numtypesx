#include <Python.h>

#define PY_ARRAY_UNIQUE_SYMBOL numtypesx_ARRAY_API
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/arrayobject.h"
#include "numpy/experimental_dtype_api.h"

#include "logfloat_scalar.h"
#include "logfloat_dtype.h"
#include "logfloat_umath.h"


static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    .m_name = "numtypesx_module",
    .m_size = -1,
};

//
// Module initialization function
//
PyMODINIT_FUNC PyInit__numtypesx_module(void)
{
    if (_import_array() < 0) {
        return NULL;
    }
    if (import_experimental_dtype_api(5) < 0) {
        return NULL;
    }

    //
    // Create the extension module.
    //

    PyObject *m = PyModule_Create(&moduledef);
    if (m == NULL) {
        return NULL;
    }

    //
    // Create the Python scalars LogFloat32Scalar and LogFloat64Scalar.
    //
    if (PyType_Ready((PyTypeObject *) &LogFloat32Scalar_Type) < 0) {
        goto error;
    }

    if (PyModule_AddObject(m,
            "LogFloat32Scalar", (PyObject *) &LogFloat32Scalar_Type) < 0) {
        goto error;
    }

    if (PyType_Ready((PyTypeObject *) &LogFloat64Scalar_Type) < 0) {
        goto error;
    }

    if (PyModule_AddObject(m,
            "LogFloat64Scalar", (PyObject *) &LogFloat64Scalar_Type) < 0) {
        goto error;
    }

    //
    // Initialize the NumPy LogFloat32 and LogFloat64 DTypes.
    //

    if (init_logfloat32_dtype() < 0) {
        goto error;
    }

    if (PyModule_AddObject(m,
            "LogFloat32", (PyObject *) &LogFloat32DType_Type) < 0) {
        goto error;
    }

    if (init_logfloat64_dtype() < 0) {
        goto error;
    }

    if (PyModule_AddObject(m,
            "LogFloat64", (PyObject *) &LogFloat64DType_Type) < 0) {
        goto error;
    }

    if (init_logfloat_ufuncs() < 0) {
        goto error;
    }

    return m;

  error:
    Py_DECREF(m);
    return NULL;
}
