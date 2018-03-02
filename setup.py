from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="baidutts",
    version="1.0.0",
    author="X-mile",
    author_email="15622388695@163.com",
    description="A Python library for changing text to speech through baidu.",
    long_description=open("README.md").read(),
    license="MIT",
    url="https://github.com/xiaomile/baidutts",
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Multimedia :: Video',
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=True,
    install_requires=[
        'wave',
        'pydub',
        'pyaudio',
        'requests'
    ]
)
