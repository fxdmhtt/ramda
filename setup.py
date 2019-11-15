import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ramda",
    version="0.26.1.0905",
    author="Junkang Yuan",
    author_email="yuanjunkang@gmail.com",
    description="A practical functional library for JavaScript programmers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.babiggy.com:10080/root/ramda.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
