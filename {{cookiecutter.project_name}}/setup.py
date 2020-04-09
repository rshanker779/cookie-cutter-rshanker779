from setuptools import setup, find_packages
import os
try:
    with open(os.path.join(os.path.dirname(__file__)), 'README.md') as f:
        long_description = f.read()
except:
    long_description = None
setup(
    name="{{cookiecutter.project_name}}",
    version="1.0.0",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description if long_description is not None else "{{cookiecutter.description}}",
    license="MIT",
    python_requires=">=3.7",
    install_requires=[
        "rshanker779_common",
        "coverage",
    ],
    packages=find_packages(),
    entry_points={},
    test_suite="{{cookiecutter.project_name}}/tests",
)
