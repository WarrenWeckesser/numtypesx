
jinja = generator(py,
                  output : '@BASENAME@',
                  arguments : ['../tools/process_jinja.py', '@INPUT@', '@BUILD_DIR@'])

processed_jinja = jinja.process('logfloat_casts.c.jinja',
                                'logfloat_dtype.c.jinja',
                                'logfloat_scalar.c.jinja',
                                'logfloat_umath.c.jinja')

# headers = files('logfloat_casts.h', 'logfloat_dtype.h', 'logfloat_scalar.h', 'logfloat_umath.h')

py.extension_module(
    '_logfloat',
    ['logfloat_module.c', processed_jinja],
    include_directories : [inc_np],
    dependencies : [np_dep, npymath_lib],
    link_args : ['-lm'],
    install : true,
    subdir : 'numtypesx'
)
