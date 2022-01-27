# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="calc-py",
    version="2022.01.27-alpha",
    description="Calculadora de consola, permite multiplicar, dividir, sumar y restar",
    author="Juan Guillermo Hernandez Alacon",
    author_email="juanguillermoalarcon@gmail.com",
    url="NO",
    license="",
    scripts=["calcpy.py"],
    console=["calcpy.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)