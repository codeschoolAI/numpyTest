from setuptools import setup

setup(
   name='numpyTest',
   version='0.1.0',
   author='Javohir Jalilov',
   author_email='javohirjaliloff@gmail.com',
   packages=['basicNumpyTest'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/numpytest/',
   license='LICENSE.txt',
   description='This is numpy basic test',
   install_requires=[
       "pytest",
       "numpy"
   ],
)