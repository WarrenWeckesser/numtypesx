#ifndef _LOGFLOAT_DTYPE_H
#define _LOGFLOAT_DTYPE_H


typedef struct {
    PyArray_Descr base;
} LogFloat32DTypeObject;

typedef struct {
    PyArray_Descr base;
} LogFloat64DTypeObject;

extern PyArray_DTypeMeta LogFloat32DType_Type;
extern PyArray_DTypeMeta LogFloat64DType_Type;

LogFloat32DTypeObject *
new_logfloat32dtype_instance(void);

LogFloat64DTypeObject *
new_logfloat64dtype_instance(void);

int
init_logfloat32_dtype(void);

int
init_logfloat64_dtype(void);

#endif  // _LOGFLOAT_DTYPE_H