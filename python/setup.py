"""Use the same .yaml config files in every language

See: https://github.com/pbrandt1/everyconfig
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='everyconfig',
    version='1.0.3',
    description='use the same .yaml config files in every language',
    url='https://github.com/pbrandt1/everyconfig',
    author='Peter Brandt',
    author_email='peter.m.brandt@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
    keywords='configuration, configuration management, environment',
    packages=find_packages(),
    install_requires=['pyyaml', 'easydict']
)
    
