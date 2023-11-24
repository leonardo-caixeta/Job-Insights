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

    def filter_by_multiple_criteria(
            self, jobs: List[dict], filter_criteria: dict) -> List[dict]:
        filtered_jobs = list()
        for job in jobs:
            if all(job[key] == value
                   for key, value in filter_criteria.items()):
                filtered_jobs.append(job)

        return filtered_jobs


process = ProcessJobs()
jobs = [
    {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
    {"id": 3, "industry": "Finance", "job_type": "FULL_TIME"},
    {"id": 4, "industry": "IT", "job_type": "CONTRACTOR"},
    {"id": 5, "industry": "Healthcare", "job_type": "FULL_TIME"},
]
result = process.filter_by_multiple_criteria(
            jobs, {"industry": "IT", "job_type": "FULL_TIME"}
        )

print(result)
