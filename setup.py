from setuptools import setup, find_packages

setup(
    name="fancyprint",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Lebimle",
    description="A package for cool printing effects",
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    include_package_data=True,
)