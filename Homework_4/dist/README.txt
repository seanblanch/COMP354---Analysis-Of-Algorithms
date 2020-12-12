==================
Dependencies
==================

You'll need a Python module called Pillow (a fork of PIL,
the Python Imaging Library) which is used to generate the
output images in this problem set. There are a number of
easy ways to get Pillow. If you've installed PyPy and PIP:

$ pypy3 -m pip install --upgrade Pillow


If you've installed PIP but are using python3 (not PyPy):

$ python3 -m pip install --upgrade Pillow
or
$ python -m pip install --upgrade Pillow

Depending on what alias you've set for Python 3 (which may vary
if you have multiple versions of Python installed).


See Pillow's installation page if you have any trouble:

https://pillow.readthedocs.io/en/stable/installation.html


==================
Running the tests
==================

A few simple sanity tests are provided; you can run them by typing

$ pypy3 test_dnaseq.py

To run the full comparison program, run

$ pypy3 dnaseq.py data/inputa0.fa data/inputb0.fa output.png

Replace "inputa0.fa" and "inputb0.fa" with filenames in the data
directory.

(Replace pypy3 with your python3 alias if you haven't installed PyPy)