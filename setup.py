import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fizzbuzz-cleonard",
    version="0.0.1",
    author="Chris Leonard",
    author_email="chris.leonard@terminallabs.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cleonard/ccl_fizzbuzz",
    project_urls={
        "Bug Tracker": "https://github.com/cleonard/ccl_fizzbuzz/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
