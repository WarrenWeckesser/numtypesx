

gen = generator(py,
                output : '@BASENAME@',
                arguments : ['../tools/conv_template.py', '@INPUT@', '@BUILD_DIR@'])

processed_src = gen.process('logfloat_dtype.c.src', 'logfloat_casts.c.src',
                            'logfloat_scalar.c.src', 'logfloat_umath.c.src')

# headers = files('logfloat_casts.h', 'logfloat_dtype.h', 'logfloat_scalar.h', 'logfloat_umath.h')

py.extension_module(
    '_logfloat',
    ['logfloat_module.c', processed_src],
    include_directories : [inc_np],
    dependencies : [np_dep, npymath_lib],
    link_args : ['-lm'],
    install : true,
    subdir : 'numtypesx'
)
