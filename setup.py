import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="screener", 
    version="0.0.1",
    author="x14119641",
    author_email="",
    description="Stock Screener",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/x14119641/screener",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)