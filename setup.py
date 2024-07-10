from setuptools import setup
from build_web_ui import BuildFrontendCommand

setup(
    cmdclass={
        'build_ui': BuildFrontendCommand,
    }
)