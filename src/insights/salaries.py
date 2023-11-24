from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = 0
        for job in self.jobs_list:
            job_max_salary = job["max_salary"]
            if job_max_salary.isdigit() and (int(job_max_salary) > max_salary):
                max_salary = int(job_max_salary)

        return max_salary

    def get_min_salary(self) -> int:
        min_salary = None
        for job in self.jobs_list:
            job_min_salary = job["min_salary"]
            if job_min_salary.isdigit() and (
                (min_salary is None) or int(job_min_salary) < min_salary
            ):
                min_salary = int(job_min_salary)

        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        def salary_is_valid(salary_value):
            match salary_value:
                case int():
                    return True
                case str():
                    if salary_value.isdigit():
                        return True
                    return False
                case _:
                    return False

        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError()

        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        if (
            not salary_is_valid(min_salary)
            or not salary_is_valid(max_salary)
            or not salary_is_valid(salary)
            or int(max_salary) < int(min_salary)
        ):
            raise ValueError()

        return int(min_salary) <= int(salary) and int(salary) <= int(
            max_salary
        )

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass


process = ProcessSalaries()
process = process.get_max_salary()
