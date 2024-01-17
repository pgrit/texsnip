import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="texsnip",
    version="1.1.0",
    author="Pascal Grittmann",
    author_email="grittmann@cg.uni-saarland.de",
    description="Tiny package to quickly add LaTeX text to your favorite vector graphics package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgrit/texsnip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)