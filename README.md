# Python Document Header Library

The Python Document Header Library is a versatile Python tool for adding headers to documents in various formats, including DOCX, PDF, and images. This library simplifies the process of customizing and adding headers to your documents programmatically.

## Features

- Add custom headers to DOCX documents.
- Insert headers into PDF files with ease.
- Overlay headers onto image files.
- Highly customizable header content, including text, images, and formatting options.
- Cross-platform support (Windows, macOS, and Linux).

## Installation

You can install the library using pip:

```bash
pip install document-header-library
```


## Usage

Here's a basic example of how to use the library to add a header to a DOCX document:

```python
from document_header_library import DOCXHeader

# Create a DOCXHeader instance with your document
header = DOCXHeader('example.docx')

# Customize the header content and formatting
header.set_text('My Document Header', font_size=14, bold=True)
header.set_alignment('center')

# Save the document with the new header
header.save('output.docx')
```


