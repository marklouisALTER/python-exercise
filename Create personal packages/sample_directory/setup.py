# this is you were setup the your packages 
from setuptools import setup  # to setup the packages

setup(name='my_package',  # name of the package you want to be
    version='0.0.1',  # version number
    description='An example personal packages',  # description
    author='Mark Louis A. Bernardo',  # author
    author_email='marlouismark@gmail.com',  # email address
    packages=['my_packages'],  # where the packages is located
    install_requires=['matplotlib', 'numpy==1.15.4', 'pycodestyle>=2.14.0']  # the packages needed to when using this packages
    )