from os import path
from jinja2 import Environment, FileSystemLoader


def main(src, destdir):
    basename = path.basename(src)
    fsl = FileSystemLoader(path.dirname(src))
    env = Environment(loader=fsl,
                      variable_start_string='{=',
                      variable_end_string='=}')
    tmpl = env.get_template(basename)
    out = tmpl.render()
    out_filename, ext = path.splitext(basename)
    out_fullpath = path.join(destdir, out_filename)
    with open(out_fullpath, 'w') as f:
        f.write(out)


if __name__ == "__main__":
    import argparse
    import pathlib

    descr = ('CLI for simple jinja template processing. '
             'Convert "<input>.jinja" to "<input>".')
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('src', type=pathlib.Path,
                        help='Source file')
    parser.add_argument('destdir', type=pathlib.Path,
                        help='Destination directory')
    args = parser.parse_args()

    src = path.join(args.src.resolve())
    destdir = path.join(args.destdir.resolve())
    main(src, destdir)
