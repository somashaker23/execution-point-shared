from setuptools import setup, find_packages

setup(
    name="job-interface-shared",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    description="Shared library for JobInterface and related utilities.",
    author="Soma Sekhar",
    author_email="somashaker23@gmail.com",
    url="https://github.com/somashaker23/execution-point-shared",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="==3.10",
)
