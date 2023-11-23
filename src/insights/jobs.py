import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.jobs_list = list(reader)

    def get_unique_job_types(self) -> List[str]:
        job_types = []
        for jobs_list in self.jobs_list:
            if not jobs_list['job_type'] == '' and (
                not job_types.__contains__(jobs_list['job_type'])
            ):
                job_types.append(jobs_list['job_type'])

        return job_types

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


process = ProcessJobs()
