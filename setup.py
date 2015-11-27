from setuptools import setup

setup(
    name='eureka_template',
    version='0.0.1',
    description='Eureka Templating Library',
    author='Jorge Dias',
    author_email='jorge@mrdias.com',
    packages=['eureka_template'],
    install_requires=['python-eureka'],
    dependency_links=['https://github.com/diasjorge/python-eureka/tarball/registration#egg=python-eureka']
)
