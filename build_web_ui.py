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
        os.system("cd experiment && npm ci && npm run build && cp -rf build ../server")
