# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.3'


setup(
    name='django-json-render',
    version=version,
    keywords='Django JSON Render',
    description='Django JSON Render',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-json-render',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['json_render'],
    py_modules=[],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
