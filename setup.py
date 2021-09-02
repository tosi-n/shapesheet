from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open('requirements.txt') as f:
  requirements = f.readlines()

VERSION = '0.1.0'
DESCRIPTION = 'Extraction of title section'
LONG_DESCRIPTION = 'A package that allows for the extraction of title section from styled pdf documents'
REQUIREMENTS = requirements



# Setting up
setup(
    name="shapesheet",
    version=VERSION,
    author="tosi-n (Tosin Dairo)",
    author_email="tosin94.td@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://bitbucket.org/logicallydevs/shapesheet",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    keywords=['python', 'document', 'pdf', 'parser', 'extraction', 'title'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='==3.9',
)

    