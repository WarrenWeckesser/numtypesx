from os import path


def get_version():
    """
    Find the value assigned to __version__ in numtypesx/__init__.py.

    This function assumes that there is a line of the form

        __version__ = "version-string"

    in __init__.py.  It returns the string version-string, or None if such a
    line is not found.
    """
    with open(path.join("numtypesx", "__init__.py"), "r") as f:
        for line in f:
            s = [w.strip() for w in line.split("=", 1)]
            if len(s) == 2 and s[0] == "__version__":
                return s[1][1:-1]


def configuration(parent_package='', top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)

    cfiles = [
        "numtypesx_module.c",
        "logfloat_dtype.c.src",
        "logfloat_casts.c.src",
        "logfloat_scalar.c.src",
        "logfloat_umath.c.src",
    ]
    cfiles = [path.join('src', f) for f in cfiles]

    config.add_subpackage('numtypesx')
    config.add_subpackage('numtypesx/tests')

    config.add_extension(
        'numtypesx._numtypesx_module',
        sources=cfiles,
        include_dirs=[numpy.get_include(), "src"],)
    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(
        name="numtypesx",
        version=get_version(),
        configuration=configuration,
    )
