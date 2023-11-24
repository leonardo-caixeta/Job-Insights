from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        industry_types = []
        for i in self.jobs_list:
            if not i['industry'] == '' and (
                    not industry_types.__contains__(i['industry'])):
                industry_types.append(i['industry'])

        return industry_types
