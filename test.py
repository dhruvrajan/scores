from crawler.test_scraper import TestAPExamScraper
from unittest import TestSuite, makeSuite, TextTestRunner
import subprocess
import sys

def run_unit_tests():
    suite = TestSuite()
    suite.addTest(makeSuite(TestAPExamScraper))
    runner = TextTestRunner()
    runner.run(suite)

def run_flake8_linter():
    # TODO: this should probably recursively search through
    # the project and find .py files to test
    res = subprocess.call(['flake8', 'crawler'])
    if res is not None:
        sys.exit(1)

if __name__ == '__main__':
    run_unit_tests()
    run_flake8_linter()
