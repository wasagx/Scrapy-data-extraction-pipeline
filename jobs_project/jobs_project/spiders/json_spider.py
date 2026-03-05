import json
import scrapy
from jobs_project.items import JobItem  

class JobSpider(scrapy.Spider):
    name = 'job_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'jobs_project.pipelines.DatabasePipeline': 300,
            'jobs_project.pipelines.CachePipeline': 400,
            'jobs_project.pipelines.MongoPipeline': 500,
        },
    }

    def start_requests(self):
        files = [
            'jobs_project/jobs_project/data/s01.json',
            'jobs_project/jobs_project/data/s02.json'
        ]
        for file_path in files:
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    # Directly call parse_page with data and file_path
                    yield from self.parse_page(data, file_path)
            except FileNotFoundError:
                self.logger.error(f"File not found: {file_path}")
            except json.JSONDecodeError as e:
                self.logger.error(f"Failed to parse JSON in {file_path}: {e}")

    def parse_page(self, data, file_path):
        jobs = data.get("jobs", [])

        for job in jobs:
            job_data = job.get("data", {})
            item = JobItem()
            try:
                # Populate fields with a default or `None` if missing
                item['slug'] = job_data.get("slug")
                item['language'] = job_data.get("language")
                item['languages'] = job_data.get("languages", [])
                item['req_id'] = job_data.get("req_id")
                item['title'] = job_data.get("title")
                item['description'] = job_data.get("description")
                item['street_address'] = job_data.get("street_address")
                item['city'] = job_data.get("city")
                item['state'] = job_data.get("state")
                item['country_code'] = job_data.get("country_code")
                item['postal_code'] = job_data.get("postal_code")
                item['location_type'] = job_data.get("location_type")
                item['latitude'] = job_data.get("latitude", 0.0)
                item['longitude'] = job_data.get("longitude", 0.0)

                # Handling categories as a list of objects
                item['categories'] = [
                    {"name": category.get("name", "")} for category in job_data.get("categories", [])
                ]

                # List fields
                item['tags'] = job_data.get("tags", [])
                item['tags5'] = job_data.get("tags5", [])
                item['tags6'] = job_data.get("tags6", [])
                item['benefits'] = job_data.get("benefits", [])
                item['category'] = job_data.get("category", [])
                item['tags1'] = job_data.get("tags1", [])
                item['tags2'] = job_data.get("tags2", [])
                item['tags8'] = job_data.get("tags8", [])


                # Other fields with fallback values
                item['brand'] = job_data.get("brand")
                item['promotion_value'] = job_data.get("promotion_value", 0.0)
                item['salary_currency'] = job_data.get("salary_currency")
                item['salary_value'] = job_data.get("salary_value", 0.0)
                item['salary_min_value'] = job_data.get("salary_min_value", 0.0)
                item['salary_max_value'] = job_data.get("salary_max_value", 0.0)
                item['employment_type'] = job_data.get("employment_type")
                item['hiring_organization'] = job_data.get("hiring_organization")
                item['source'] = job_data.get("source")
                item['apply_url'] = job_data.get("apply_url")
                item['internal'] = job_data.get("internal", False)
                item['searchable'] = job_data.get("searchable", False)
                item['applyable'] = job_data.get("applyable", False)
                item['li_easy_applyable'] = job_data.get("li_easy_applyable", False)
                item['ats_code'] = job_data.get("ats_code")

                # Handling meta_data as a nested dictionary
                item['meta_data'] = job_data.get("meta_data", {})

                # Dates and additional fields
                item['update_date'] = job_data.get("update_date")
                item['create_date'] = job_data.get("create_date")
                item['full_location'] = job_data.get("full_location")
                item['short_location'] = job_data.get("short_location")
                item['location_name'] = job_data.get("location_name")
                item['country'] = job_data.get("country")

                item['department'] = job_data.get("department")
                item['recruiter_id'] = job_data.get("recruiter_id")
                item['posted_date'] = job_data.get("posted_date")
                item['posting_expiry_date'] = job_data.get("posting_expiry_date")
                item['work_hours'] = job_data.get("work_hours")
                item['salary_frequency'] = job_data.get("salary_frequency")
                
                yield item
            except Exception as e:
                self.logger.error(f"Error processing job data from {file_path}: {e}")

    def handle_error(self, failure):
        self.logger.error(f"Request failed: {failure}")