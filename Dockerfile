FROM python:3.9-slim

# Set working directory to `jobs_project`
WORKDIR /app/jobs_project

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install -r /app/requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"

# Start the Scrapy spider
CMD ["python", "-m", "scrapy", "crawl", "job_spider", "--nolog"]

