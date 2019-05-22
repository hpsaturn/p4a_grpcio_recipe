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

        # ...so we manually run cython from the user's system
        shprint(sh.find, self.get_build_dir('armeabi'), '-iname', '*.pyx', '-exec',
                self.ctx.cython, '{}', ';', _env=env)

        # now cython has already been run so the build works
        shprint(hostpython, 'setup.py', 'build_ext', '-v', _env=env)

        # stripping debug symbols lowers the file size a lot
        build_lib = glob.glob('./build/lib*')
        shprint(sh.find, build_lib[0], '-name', '*.o', '-exec',
                env['STRIP'], '{}', ';', _env=env)

recipe = PYGRPCIORecipe()
