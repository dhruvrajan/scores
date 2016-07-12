# Scores

[![](https://travis-ci.org/utexasdev/scores.svg?branch=master)](https://travis-ci.org/utexasdev/scores)
[![codecov.io](http://codecov.io/github/utexasdev/scores/coverage.svg?branch=master)](http://codecov.io/github/utexasdev/scores?branch=master)

Determine which college courses at [The University of Texas at Austin](https://utexas.edu) you can receive credit for based on your standardized test performance.

We currently support:
- [Advanced Placement](https://apstudent.collegeboard.org/home)

# Set up

[Python 3.5](https://www.python.org/downloads/release/python-350/) is the only major prerequisite for the project. The rest of the dependencies can be installed via `setup.sh`.

Because we're working with a [virtual environment](https://pypi.python.org/pypi/virtualenv), make sure to perform `source venv/bin/activate` before running any of the Python files.

`public` contains the static website that is deployed to the `gh-pages` branch to be hosted on [https://utexasdev.github.io/scores](https://utexasdev.github.io/scores).

# Contributing

Contributions to this repository are always welcome – from those that have a lot to no experience at all!
- Non-programmers: Take a look at the current website at [https://utexasdev.github.io/scores](https://utexasdev.github.io/scores). If there are problems with the website or features that should be implemented, file an issue on the [issues page](https://github.com/utexasdev/scores/issues).
- Programmers: Get started by sifting through the issues on the [issues page](https://github.com/utexasdev/scores/issues).
  - Issues with the tag `bugs` are problems with the application; these can probably be fixed in under 25 lines of code.
  - Issues with the tag `enhancements` will require a more in-depth analysis of the project and a lot of coding/testing.
  - Pull requests should be submitted to the `develop` branch. PRs must pass the Travis CI and Codecov test in order to be merged. The `develop` branch will be merged with the `master` branch every week.
