# Number Frequency Analyzer

A simple Python project that reads numbers from a text file, converts them into integers, and calculates how often each number appears.

## Features

- reads data from a text file
- converts comma-separated values into integers
- skips empty values
- calculates frequency of each number
- uses both standard dictionaries and `defaultdict`

## Project files

- `word_counter.py` — main Python script
- `counter.txt` — sample input file

## Example input

```text
1,2,5,7,2,4,9,6,3
3,2,1,4,2
Output:
{1: 2, 2: 3, 3: 1, 4: 2, 5: 1, 6: 1, 7: 1, 9: 1}

Technologies used
Python 3
collections.defaultdict
Purpose

This project was created while learning Python fundamentals, especially:

file handling
string processing
loops
dictionaries
data parsing
