from setuptools import setup, find_packages

setup(
    name="pybingx",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="A Python client for the BingX API",
    author="Ryan Hayabusa",
    author_email="ryu8777@gmail.com",
    url="https://github.com/ryu878/pybingx",
)
