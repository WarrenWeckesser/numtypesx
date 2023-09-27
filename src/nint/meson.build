
common_jinja = fs.copyfile('common.jinja')
jinja = generator(py,
                  output : '@BASENAME@',
                  arguments : ['process_jinja.py', '@INPUT@', '@BUILD_DIR@'],
                  depends : [process_jinja_py, common_jinja])

nint_python_scalars_c = jinja.process('nint_python_scalars.c.jinja')

py.extension_module(
    '_nint',
    [nint_python_scalars_c],
    include_directories : [inc_np],
    dependencies : [np_dep, npymath_lib],
    link_args : ['-lm'],
    install : true,
    subdir : 'numtypesx'
)
