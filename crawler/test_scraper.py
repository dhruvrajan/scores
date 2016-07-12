from unittest import TestCase, main
from .scraper import APExamScraper
from bs4 import NavigableString
import json
import os

class TestAPExamScraper(TestCase):
    def setUp(self):
        self.scraper = APExamScraper()

    def test_initialize(self):
        soup = self.scraper._initialize()
        self.assertIsNot(soup, None)

    def test_get_containers(self):
        containers = self.scraper._get_containers()
        container_items = 0
        self.assertIsNot(containers, None)
        for item in containers:
            if not isinstance(item, NavigableString):
                container_items += 1
        self.assertEqual(container_items, 34)

    def test_parse_exams(self):
        exams = self.scraper.parse_exams()
        self.assertIsNot(exams, None)
        self.assertEqual(len(exams), 34)
        for exam in exams:
            self.assertNotEqual(exam[0], ' ')
            self.assertNotEqual(exam[-1], ' ')
            self.assertIn('AP Exam', exam)

    def test_parse_tables(self):
        data = self.scraper.parse_tables()
        self.assertIsNot(data, None)
        self.assertEqual(len(data), 34)

    def test_export_json(self):
        self.scraper.export_json()
        os.chdir('data')
        self.assertIn('ap.json', os.listdir())
        with open('ap.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 34)
        os.remove('ap.json')
        os.chdir('..')

if __name__ == '__main__':
    main()
