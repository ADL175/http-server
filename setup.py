"""
setup for http-server package
"""
from setuptools import setup

DEPENDENCIES = ['pytest', 'pytest-cov', 'ipython']
EXTRA_PACKAGES = {
    'test': ['tox']
}

setup(
    name="http-server",
    description="""A module that implements an echo server.""",
    version='0.1',
    author='Miguel Pena and David Lim',
    author_email='miguelp1986@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    install_requires=DEPENDENCIES,
    extras_require=EXTRA_PACKAGES
)
