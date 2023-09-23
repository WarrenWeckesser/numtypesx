project(
  'numtypesx',
  'c',
  meson_version: '>= 1.1.0',
  default_options: [
    'c_std=c11',
  ]
)

py_mod = import('python')
py = py_mod.find_installation(pure: false)

message('Python is at ' + py.full_path())

cc = meson.get_compiler('c')

# Generate _version.py by reading the version from pyproject.toml.
custom_target(input : 'pyproject.toml',
              output : '_version.py',
              command : [
                py, '../tools/make_version_file.py',
                '@INPUT@', '@OUTPUT@'
              ],
              install : true,
              install_dir : py.get_install_dir() / 'numtypesx')

#----------------------------------------------------------------------
# Get the numpy include directory, and find the npymath library.
#----------------------------------------------------------------------

incdir_numpy = run_command(py,
  [
    '-c',
    'import numpy; print(numpy.get_include())'
  ],
  check: true
).stdout().strip()

message('NumPy include directory is ' + incdir_numpy)

includes = include_directories(
  [
    incdir_numpy,
  ],
)

inc_np = include_directories(incdir_numpy)
np_dep = declare_dependency(include_directories: inc_np)

npymath_path = incdir_numpy / '..' / 'lib'
npymath_lib = cc.find_library('npymath', dirs: npymath_path)


#----------------------------------------------------------------------
# Python source code to be installed.
#----------------------------------------------------------------------

py.install_sources(
  [
    'numtypesx/__init__.py',
  ],
  subdir : 'numtypesx',
)

py.install_sources(
  [
    'numtypesx/tests/__init__.py',
    'numtypesx/tests/test_logfloat_scalars.py',
    'numtypesx/tests/test_logfloat_ufuncs.py',
    'numtypesx/tests/test_copy.py',
    'numtypesx/tests/test_comparison.py',
  ],
  subdir : 'numtypesx/tests',
)

subdir('src')
