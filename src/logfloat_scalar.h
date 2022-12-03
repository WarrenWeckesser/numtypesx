#ifndef _LOGFLOAT_SCALAR_H
#define _LOGFLOAT_SCALAR_H

typedef struct {
    PyObject_HEAD
    float log;  // The natural log of the value.
} LogFloat32Scalar;

typedef struct {
    PyObject_HEAD
    double log;  // The natural log of the value.
} LogFloat64Scalar;

extern PyTypeObject LogFloat32Scalar_Type;
extern PyTypeObject LogFloat64Scalar_Type;

#endif  // _LOGFLOAT_SCALAR_H
