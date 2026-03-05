# Use asyncio reactor compatible with Docker
from twisted.internet import asyncioreactor
asyncioreactor.install()


BOT_NAME = 'jobs_project'
SPIDER_MODULES = ['jobs_project.spiders']
NEWSPIDER_MODULE = 'jobs_project.spiders'

ROBOTSTXT_OBEY = False
LOG_LEVEL = 'DEBUG'

# Enable retries
RETRY_ENABLED = True
RETRY_TIMES = 3  # Retry a request 3 times before failing
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]

# Enable redirects
REDIRECT_ENABLED = True
REDIRECT_MAX_TIMES = 20  # Follow up to 20 redirects per request

# Built-in Scrapy middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
}

ITEM_PIPELINES = {
    'jobs_project.pipelines.DatabasePipeline': 300,
    'jobs_project.pipelines.CachePipeline': 400,
    'jobs_project.pipelines.MongoPipeline': 500,
}


