from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import time
import os

class APExamScraper(object):
    def __init__(self):
        self.url = 'http://bit.ly/29zOCEC'
        self.soup = self._initialize()

    def _initialize(self):
        try:
            html = urlopen(self.url)
        except HTTPError:
            time.sleep(5)
            self._initialize()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def _get_containers(self):
        tables = self.soup.find_all('tbody')
        exam_table_body = tables[0]
        containers = exam_table_body.children
        return containers

    def parse_exams(self):
        exams = []
        containers = self._get_containers()
        for container in containers:
            if not isinstance(container, NavigableString):
                text = container.td.a.get_text().strip()
                exams.append(text)
        return exams

    def parse_tables(self):
        raw_data = []
        formatted_data = []
        containers = self._get_containers()
        for container in containers:
            if not isinstance(container, NavigableString):
                table = container.find('table', {'id': 'tablefield-0'})
                indiv_exam = []
                for section in table.tbody.children:
                    row_info = ()
                    if not isinstance(section, NavigableString):
                        for row in section.children:
                            if not isinstance(row, NavigableString):
                                data = row.get_text()
                                row_info += (data,)
                        indiv_exam.append(row_info)
                raw_data.append(indiv_exam)
        for exam_data in raw_data:
            exam = {}
            for row in exam_data:
                course, score = row[0], row[1]
                try:
                    if '-' in score:
                        score_range = [int(x) for x in score.split('-')]
                        for x in range(score_range[0], score_range[1] + 1):
                            exam[x] = course
                    else:
                        exam[int(score)] = course
                except ValueError:
                    continue
            formatted_data.append(exam)
        return formatted_data

    def export_json(self):
        exam_names = self.parse_exams()
        exam_data = self.parse_tables()
        for name, table in zip(exam_names, exam_data):
            table['name'] = name
        os.chdir('data')
        with open('ap.json', 'w+') as f:
            json_data = json.dumps(exam_data)
            f.write(json_data)
            f.close()
        os.chdir('..')

if __name__ == '__main__':
    scraper = APExamScraper()
    scraper.export_json()
