#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Test that we can add filesuffixes to $DSUFFIXES.
"""

import TestSCons

test = TestSCons.TestSCons()

test.write('SConstruct', """
env = Environment(DPATH=['.'])
env.Append(DSUFFIXES = ['.x'])
env.InstallAs('foo_d', 'foo.d')
env.InstallAs('foo_x', 'foo.x')
""")

test.write('foo.d', """\
import inc;
""")

test.write('foo.x', """\
import inc;
""")

test.write('inc.d', "inc.d 1\n")

test.run(arguments='.', stdout=test.wrap_stdout("""\
Install file: "foo.d" as "foo_d"
Install file: "foo.x" as "foo_x"
"""))

test.up_to_date(arguments='.')

test.write('inc.d', "inc 2\n")

test.run(arguments='.', stdout=test.wrap_stdout("""\
Install file: "foo.d" as "foo_d"
Install file: "foo.x" as "foo_x"
"""))

test.up_to_date(arguments='.')

test.pass_test()