"""Tornado Template Generator

This application uses the Tornado Template module to generate static HTML files
while still making available a subset of the Tornado template methods like
static_url.

"""
import argparse
import hashlib
import json
from os import path
import sys
from tornado import template

__version__ = '1.1.0'


class Generator(object):

    def __init__(self, file_name, static_path, static_prefix='/static/',
                 kwarg_file=None):
        self.file_name = file_name
        self.static_path = path.abspath(static_path)
        self.static_prefix = static_prefix
        self.kwarg_file = path.abspath(kwarg_file) if kwarg_file else None

    @property
    def static_abspath(self):
        return path.abspath(self.static_path).rstrip('/') + '/'

    def get_file_hash(self, file_path):
        with open(path.abspath(self.static_abspath + file_path), 'r') as handle:
            content = handle.read()
        hasher = hashlib.md5()
        hasher.update(content)
        return hasher.hexdigest()

    def make_static_url(self, file_path):
        try:
            return '%s?v=%s' % (self.static_prefix + file_path,
                                self.get_file_hash(file_path)[:4])
        except IOError as error:
            sys.stderr.write('ERROR: Could not make static url (%s)\n' % error)
            sys.exit(1)

    def generate(self):
        dirs = len(self.file_name.split('/'))
        file_path = '/'.join(path.abspath(self.file_name).split('/')[:-dirs])
        loader = template.Loader(file_path,
                                 namespace={'static_url': self.make_static_url})

        if self.kwarg_file:
            with open(self.kwarg_file) as handle:
                kwargs = json.load(handle)
        else:
            kwargs = {}

        return loader.load(self.file_name).generate(**kwargs)


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
    parser.add_argument('-k', '--kwarg_file',
                        action='store',
                        help='KWARG file in JSON format to use when generating')

    return parser.parse_args()


def main():
    args = parse_arguments()
    g = Generator(args.file, args.static_path, args.static_url_prefix,
                  args.kwarg_file)
    output = g.generate()
    if not args.output:
        print output
    else:
        with open(args.output, 'w') as handle:
            handle.write(output)


if __name__ == '__main__':
    main()
