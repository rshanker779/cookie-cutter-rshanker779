import pathlib

from setuptools import setup, find_packages

try:
    long_description = (pathlib.Path(__file__).parent / 'README.md').read_text()
except:
    long_description = None
setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description if long_description is not None else "{{cookiecutter.description}}",
    license="MIT",
    python_requires=">=3.7",
    install_requires=[
        "rshanker779_common",
    ],
    packages=find_packages(),
    entry_points={},
)