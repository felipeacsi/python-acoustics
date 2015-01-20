import os
from setuptools import setup, find_packages
from setuptools import Extension
import numpy as np

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = "A Python library aimed at acousticians."

setup(
      name='acoustics',
      version='0.0',
      description="Acoustics module for Python.",
      long_description=long_description,
      author='Python Acoustics',
      author_email='fridh@fridh.nl',
      license='LICENSE',
      packages=find_packages(exclude=["tests"]),
      #py_modules=['turbulence'],
      scripts=[],
      zip_safe=False,
      install_requires=[
          'numpy >=1.8',
          'scipy >= 0.14',
          'matplotlib',
          'six >= 1.4.1',
          'numexpr',
          ],
      extras_require={
          'jit': 'numba',
          'fast_fft': 'pyFFTW',
          'io': 'pandas',
          },
      ext_modules=[Extension("acoustics._signal", ["acoustics/_signal.c"])],
      include_dirs=[np.get_include()]
      )
