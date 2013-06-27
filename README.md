Tornado Template Generator
==========================
Generates static HTML files using Tornado templates with a subset of the
available methods available when writing dynamic web apps. It properly handles
includes and extended templates as well as all the base escaping methods. It
does not include any of the request related variables.

Motivation
----------
I use this to build static HTML files that use the template {{static_path()}} method
for cache busting static files.

Python Version
--------------
Python 2.6 or 2.7

Installation
------------
Install via pip:

    pip install tornado_template_gen

Use
---
tornado_template_gen -f path/to/template.html -s path/to/static/files [-p /url_prefix/] [-o OUTPUT FILE] [-k KWARG_FILE]

If you do not specify an output file, it will spit the rendered content to STDOUT.

Keyword Arguments File
----------------------
If you include a Keyword Arguments file (KWARGS) the values in the file will be
passed into the generate method making the values available during template
rendering. The file should be in JSON format.

Example:

    {"my_key": "my_value",
     "version": "99.99.99"}

License
-------
Copyright (c) 2013, MeetMe
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
 * Neither the name of the MeetMe nor the names of its contributors may be used
   to endorse or promote products derived from this software without specific
   prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
