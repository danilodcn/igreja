import os

from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), "README.md"))

setup(
    name="igreja",
    zip_safe=False,  # eggs are the devil.
    version="0.0.1",
    description="An site created for use in local church",
    long_description=readme.read(),
    author="Danilo Nascimento",
    author_email="daconnas.dcn@gmail.com",
    url="https://github.com/danilodcn/igreja/",
    python_requires=">=3.6",
    install_requires=[
        "Django>=2.2,!=3.0.*",
        "confusable_homoglyphs~=3.0",
    ],
)
