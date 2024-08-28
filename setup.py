from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("VERSION", "r", encoding="utf-8") as f:
    version = f.read()

setup(
    name="csv2docx",
    version=version,
    description="An application for converting source CSV tables to target DOCX documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nikita O. Dorodnykh",
    author_email="dorodnyxnikita@gmail.com",
    maintainer="Nikita O. Dorodnykh",
    maintainer_email="dorodnyxnikita@gmail.com",
    packages=find_packages(),
    data_files=[("", ["VERSION"])],
    python_requires=">=3.10",
    license="Apache Software License",
    classifiers=[
        "Development Status :: Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers, System Analytics",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License"
    ]
)
