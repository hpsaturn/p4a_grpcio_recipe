# coding=utf-8

from pythonforandroid.recipe import CythonRecipe, Recipe
from os.path import join
from pythonforandroid.util import current_directory
import sh
from pythonforandroid.logger import shprint
import glob


class GRPCIORecipe(CythonRecipe):
    name = 'grpcio'
    version = 'v1.20.1'
    url = 'https://github.com/grpc/grpc/archive/{version}.zip'
    site_packages_name = 'grpcio'
    depends = ['grpc']
    cython_args = ['-Igrpc/src/python/grpcio']

recipe = GRPCIORecipe()
