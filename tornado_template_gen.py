"""Tornado Template Generator

This application uses the Tornado Template module to generate static HTML files
while still making available a subset of the Tornado template methods like
static_url.

"""
import argparse
import hashlib
from os import path
import sys
from tornado import template

__version__ = '1.0.0'


class Generator(object):

    def __init__(self):
        self.static_prefix = '/static/'
        self.static_path = None

    @property
    def static_abspath(self):
        return path.abspath(self.static_path).rstrip('/') + '/'

    def get_file_hash(self, file_path):
        with open(path.abspath(self.static_abspath + file_path), 'r') as handle:
            content = handle.read()
        hasher = hashlib.md5()
        hasher.update(content)
        return hasher.hexdigest()

    def make_static_url(self, file_path, static_url_prefix='/static/'):
        try:
            return '%s?v=%s' % (static_url_prefix + file_path,
                                self.get_file_hash(file_path)[:4])
        except IOError as error:
            sys.stderr.write('ERROR: Could not make static url (%s)\n' % error)
            sys.exit(1)

    def generate(self, file_name, static_path, static_url_prefix=None):
        if static_url_prefix:
            self.static_prefix = static_url_prefix
        dirs = len(file_name.split('/'))
        file_path = '/'.join(path.abspath(file_name).split('/')[:-dirs])
        self.static_path = path.abspath(static_path)
        loader = template.Loader(file_path,
                                 namespace={'static_url': self.make_static_url})
        return loader.load(file_name).generate()


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate static HTML from '
                                                 'tornado templates.')
    parser.add_argument('-f', '--file',
                        action='store',
                        required=True,
                        help='The template file to render')
    parser.add_argument('-s', '--static_path',
                        action='store', default='static',
                        help='Path to the static file directory')
    parser.add_argument('-p', '--static_url_prefix',
                        action='store',
                        help='Path to the static file directory')
    parser.add_argument('-o', '--output',
                        action='store',
                        help='Write the output to the specified file instead '
                             'of STDOUT')
    return parser.parse_args()


def main():
    args = parse_arguments()
    g = Generator()
    output = g.generate(args.file, args.static_path, args.static_url_prefix)
    if not args.output:
        print output
    else:
        with open(args.output, 'w') as handle:
            handle.write(output)


if __name__ == '__main__':
    main()
