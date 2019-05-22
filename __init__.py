# coding=utf-8

from pythonforandroid.recipe import CythonRecipe, Recipe
from os.path import join
from pythonforandroid.util import current_directory
import sh
from pythonforandroid.logger import shprint
import glob


class GRPCIORecipe(CythonRecipe):
    name = 'pygrpcio'
    version = 'v1.20.1'
    url = 'https://github.com/grpc/grpc/archive/{version}.zip'
    depends = ['grpc']

    def build_cython_components(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            hostpython = sh.Command(self.ctx.hostpython)

            # This first attempt *will* fail, because cython isn't
            # installed in the hostpython
            try:
                shprint(hostpython, 'setup.py', 'build_ext', _env=env)
            except sh.ErrorReturnCode_1:
                pass


recipe = GRPCIORecipe()
