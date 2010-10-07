# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Extension
import sys, os

setup(
    name				= 'pylibconfig',
    description			= "libconfig bindings for Python",
    version				= "0.0.1",
    author				= "Sergey S. Gogin",
    author_email		= "d-x@bk.ru",
	maintainer			="cnangel",
	maintainer_email	= "cnangel@gmail.com",
    keywords			= "libconfig libconfig++ boost python config configuration",
    test_suite			= "tests",
	license				= "bsd",
	url					= "",
    ext_modules			= [
        Extension(
            "pylibconfig",
            ["src/pylibconfig.cc"],
            libraries=["boost_python-vc90-mt-1_44", "libconfig++"],
            library_dirs=['../libconfig-1.4.5/Release', 'C:/Program Files (x86)/boost/boost_1_44/lib'],
            include_dirs=['../libconfig-1.4.5/lib', 'C:/Program Files (x86)/boost/boost_1_44']
            #language='c++',
            #extra_compile_args=["/EHsc"]
                 )
                ]
     )
