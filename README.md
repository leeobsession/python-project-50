### Hexlet tests and linter status:
[![Actions Status](https://github.com/leeobsession/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/leeobsession/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/46c511b3a6792f75844c/maintainability)](https://codeclimate.com/github/leeobsession/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/46c511b3a6792f75844c/test_coverage)](https://codeclimate.com/github/leeobsession/python-project-50/test_coverage)


# Difference Calculator

The Difference Calculator is a Python 3 program that allows you to compare JSON and YAML files, highlighting the differences between them. This tool is useful for understanding changes between configurations, data files, or any text-based hierarchical structures in JSON and YAML formats.

## Features

- Compare both JSON and YAML files.
- Identify and display differences in a human-readable format.
- Visualize hierarchical differences to understand the changes better.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Demonstration](#demonstration)

# Installation

Install using pip:

    pip install brain-games

or clone the repository and install manually:

    $ git clone https://github.com/leeobsession/python-project-50

# Usage

Run the script and provide the paths to the two files you want to compare:

    gendiff file_path1 file_path2

By default, the "stylish" formatter will work, to select the "plain" or "json" formatter, enter **-f/--format (prefered format)** at the end of command.

# Options

-h, --help: Show the help message and exit.
-f, --format: Specify the format in which you want to see the difference between the files.

# Demonstration

***Instructions output:***
[![asciicast](https://asciinema.org/a/605335.svg)](https://asciinema.org/a/605335)


***Default format (stylish):***
[![asciicast](https://asciinema.org/a/605336.svg)](https://asciinema.org/a/605336)

***Plain format:***
[![asciicast](https://asciinema.org/a/605340.svg)](https://asciinema.org/a/605340)

***Json format***
[![asciicast](https://asciinema.org/a/605341.svg)](https://asciinema.org/a/605341)