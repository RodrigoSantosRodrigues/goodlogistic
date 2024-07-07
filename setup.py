from setuptools import find_packages, setup

setup(
    name="goodlogistic",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Rodrigo J. R Santos",
    author_email="contato@goodtruck.org.br",
    description="Toolkit for logistic problem, designed for real challenges Nonprofit organization.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/daftar/goodlogistic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
