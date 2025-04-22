## CS453 Assignment 2: Coverage Profiler for Python

With this assignment, we will try implementing a basic coverage profiler for Python that can measure statement and branch in a similar way to the widely used [coverage.py](https://coverage.readthedocs.io/en/7.4.0/). Write a program that accepts another Python script file, as well as its arguments (if any required), and generates a JSON file `pcov.json` containing coverage information. The skeleton code, called `pcov.py`, contains a specific format. Consider the following target code, `example2.py`, which you can find under the directry `examples`:

```python
import sys 

x = int(sys.argv[1])
y = int(sys.argv[2])

if x == 10 and y == 5:
    print("Hello")
elif y == 1:
    print("Welcome")
else:
    print("Bye")
```

When you invoke `pcov.py` as follows:

```bash
$ python3 pcov.py -t examples/example2.py 5 5
```

it should generate the following (note that `5 5` at the end is consumed as command line arguments for the target script, `example2.py`).

```json
{
    "target_file": "examples/example2.py",
    "covered_lines": 6,
    "num_statements": 8,
    "statement_coverage": "75.00",
    "covered_branches": 2,
    "num_branches": 4,
    "branch_coverage": "50.00"
}
```

The profiler should also support the verbose mode (specified by option `-v`):

```bash
$ python3 pcov.py -v -t examples/example2.py 5 5
```

it should generate the following (the missing statements and branches should be recorded). A branch from line number `a` to `b` can be represented `a->b`.

```json
{
    "target_file": "examples/example2.py",
    "covered_lines": 6,
    "num_statements": 8,
    "statement_coverage": "75.00",
    "missing_lines": [
        "7",
        "9"
    ],
    "covered_branches": 2,
    "num_branches": 4,
    "branch_coverage": "50.00",
    "missing_branches": [
        "6->7",
        "8->9"
    ]
}
```

The output format is already specified in the skeleton code. You need to provide covered and total statements/branches, as well as two lists that contain string representations for missing statements/branches.

### Scopes

Here are clarifications about the scope of the coverage.

- We will consider the behaviour of `coverage.py` as the reference. You can check the reference behaviour by running `coverage.py` and looking at the json report. Please see the documentation for the details.

- Note that `coverage.json` uses the line number -1 to denote the end of the program.
- You have to instrument the code yourself. Specifically, **do not rely on trace functions provided by Python**. The aim of this assignment is to learn the general approach towards code instrumentation, not just to measure Python coverage.

### Skeleton and Test Code

This repository includes a skeleton code named `pcov.py` for your profiler. Please keep the existing code and the command line interface provided, so that GitHub Classroom can run the automated grading scripts. The usage is:

```bash
$ usage: pcov.py [-h] [-v] -t TARGET [remaining ...]

Measures coverage.

positional arguments:
  remaining

options:
  -h, --help            show this help message and exit
  -v, --verbose
  -t TARGET, --target TARGET
```

The repository also includes public test cases: please refer to them for more detail.

### Libraries and Python Version

- The template repository is configured with Python 3.10. 
- We will use coverage.py version 7.2.3 as the gold standard.

### Report

In addition to the implementation, submit a brief report as part of the repository. Name the file `report.pdf` in the root directory of the assignment repository. The report should contain the following:

- A brief description of the problem in your own understanding
- How you designed your solution
- Any unique idea/technique that you think you contributed to the implementation
- A brief summary of what you've learnt