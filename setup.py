from setuptools import setup
import os
from setuptools import Command


class BuildFrontendCommand(Command):
    description = "Build the frontend using Vite"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system("cd experiment && npm ci && npm run build && cp -rf dist ../src")


setup(
    cmdclass={
        'build_web_ui': BuildFrontendCommand,
    }
)