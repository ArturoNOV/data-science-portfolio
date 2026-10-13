# Sprint 7 — Python Development Tools and Applications

**TripleTen Data Science Bootcamp — Sprint 7 Exercises**

## Overview

This folder contains the exercises completed during Sprint 7 of the TripleTen
Data Science Bootcamp.

The exercises cover several Python development concepts beyond basic data
analysis, including object-oriented programming, file handling, JSON, web
APIs, automated testing, command-line interfaces, image manipulation,
Jupyter Notebook fundamentals, and a small Streamlit application.

Some exercises have been lightly adapted for the portfolio to improve
portability, error handling, and code readability while preserving the
original learning objectives.

## Contents

### Python scripts

- `bank_account_oop.py` — object-oriented programming using classes,
  instance methods, static methods, and class methods.
- `file_and_json_operations.py` — reading and writing text and JSON files,
  including data retrieved from an external API.
- `api_requests.py` — HTTP requests, API endpoints, query parameters, and
  JSON responses.
- `accuweather_api.py` — location and weather forecast requests using the
  AccuWeather API.
- `age_group.py` — conditional logic, functions, interactive execution, and
  automated tests.
- `sign.py` — simple function logic, interactive execution, and automated
  tests.
- `prime.py` — prime-number validation and use of a `main()` entry point.

### Image manipulation

The `image-manipulation/` directory contains a progression of command-line
image-processing exercises using Pillow and `argparse`.

The sequence demonstrates progressively more advanced functionality:

- `image_rotator_01.py` — rotates a predefined image.
- `image_rotator_02.py` — accepts input file, output file, and rotation angle
  as command-line arguments.
- `image_rotator_03.py` — introduces an optional rotation angle with a
  default value.
- `image_rotator_04.py` — adds an optional information flag.
- `image_rotator_05.py` — adds file-not-found error handling.
- `image_resizer.py` — resizes an image using user-supplied width and height.
- `tripleten_logo.jpeg` — source image used by the first rotation exercise.

Generated image files are intentionally excluded from version control.

### Jupyter Notebook basics

The `notebook-basics/` directory contains:

- `my_notebook.ipynb` — introductory use of code cells, Markdown, embedded
  images, and execution of an external Python script.
- `cpus.py` — auxiliary script executed from the notebook.

### Streamlit coin-toss application

The `streamlit-coin-toss/` directory contains a small interactive Streamlit
application that simulates repeated coin tosses using a Bernoulli
distribution.

The application demonstrates:

- Streamlit widgets
- `st.session_state`
- dynamically updated charts
- SciPy probability distributions
- pandas DataFrames
- retention of results across repeated executions

It has its own `requirements.txt` because it functions as an independent
mini-application.

## Installation

Install the dependencies for the general Sprint 7 exercises with:

```bash
pip install -r requirements.txt
```

For the Streamlit application, install its dependencies separately:

```bash
pip install -r streamlit-coin-toss/requirements.txt
```

## Automated Tests

`age_group.py` and `sign.py` include automated tests that can be executed
with pytest.

Run both with:

```bash
python -m pytest age_group.py sign.py -q
```

The scripts can also be executed directly to use their interactive examples:

```bash
python age_group.py
python sign.py
```

## AccuWeather API

`accuweather_api.py` requires an AccuWeather API key.

The key is intentionally not stored in the repository. Before running the
script, define the `ACCUWEATHER_API_KEY` environment variable.

In PowerShell:

```powershell
$env:ACCUWEATHER_API_KEY="YOUR_API_KEY"
python accuweather_api.py
```

## Image Manipulation Examples

The image manipulation scripts are command-line programs.

For example:

```bash
python image-manipulation/image_rotator_02.py INPUT_FILE OUTPUT_FILE 45
```

Using an optional angle:

```bash
python image-manipulation/image_rotator_03.py INPUT_FILE OUTPUT_FILE --angle 45
```

Displaying image information:

```bash
python image-manipulation/image_rotator_04.py INPUT_FILE OUTPUT_FILE --angle 45 --info
```

Resizing an image:

```bash
python image-manipulation/image_resizer.py INPUT_FILE OUTPUT_FILE 300 200
```

## Streamlit Application

Run the coin-toss application from the `sprint-07` directory with:

```bash
streamlit run streamlit-coin-toss/app.py
```

The application keeps a history of experiments during the Streamlit session.

## Generated Files

Some exercises intentionally create files as part of their learning
objective.

For example:

- `file_and_json_operations.py` generates `lines.txt` and
  `samsung_items.json`.
- the image-manipulation scripts generate rotated or resized image files.

These generated outputs are excluded from version control because they can
be reproduced by running the corresponding scripts.
