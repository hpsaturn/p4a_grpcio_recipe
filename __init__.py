# coding=utf-8

from pythonforandroid.recipe import CythonRecipe, Recipe
from os.path import join
from pythonforandroid.util import current_directory
import sh
from pythonforandroid.logger import shprint
import glob


class PYGRPCIORecipe(CythonRecipe):
    name = 'pygrpcio'
    version = 'v1.20.1'
    url = 'https://github.com/grpc/grpc/archive/{version}.zip'
    depends = ['grpc']
    cython_args = ['-Igrpc/src/python/grpcio/grpc/_cython']

recipe = PYGRPCIORecipe()
