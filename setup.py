from setuptools import setup
import sys

install_requires = ['tornado']
if sys.version_info < (2, 7, 0):
    install_requires.append('argparse')

console_scripts = ['tornado-template-gen=tornado_template_gen:main']


setup(name='tornado_template_gen',
      version='1.1.0',
      description='Generate static HTML files using the Tornado template '
                  'module',
      url='https://github.meetmecorp.com/Rejected/transformer',
      author='Gavin M. Roy',
      author_email='gmr@meetme.com',
      entry_points={'console_scripts': console_scripts},
      license='BSD',
      py_modules=['tornado_template_gen'],
      install_requires=install_requires,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 2 :: Only',
          'Topic :: Software Development :: Build Tools'])
