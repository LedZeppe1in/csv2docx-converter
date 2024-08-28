# csv2docx converter

**csv2docx-converter** is an application for converting source CSV tables to target DOCX documents.

## Version

0.1

## Installation

First, you need to clone the project into your directory:

```
git clone https://github.com/tabbydoc/csv2doc-converter.git
```

Next, you need to install all requirements for this project:

```
pip install -r requirements.txt
```

*I recommend you to use Python 3.10 or more.*

## Directory Structure

* `data` contains datasets of source tables in CSV format.
* `results` contains results in form of docx documents (*this directory is created by default*);
* `main.py` is main script for converting csv tables to docx documents.

## Usage

#### Console mode

In order to use **csv2docx-converter** in *console mode*, you may run the following command:

```
python main.py
```

Run this script to process source tables in CSV format. Tables must be located in `data` directory.

The processing result are presented as DOCX documents and will be saved to `result` directory.

## Author

* [Nikita O. Dorodnykh](mailto:dorodnyxnikita@gmail.com)