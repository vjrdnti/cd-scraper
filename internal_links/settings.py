# settings.py

# Basic Scrapy Settings

# Identify the bot to websites (customize this)
BOT_NAME = 'internal_links'

# Direct the spider to your Scrapy modules
SPIDER_MODULES = ['internal_links.spiders']
NEWSPIDER_MODULE = 'internal_links.spiders'

# User agent to identify the spider (customize it)
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}


# Enable or disable robots.txt rules (set to False if you're scraping APIs)
ROBOTSTXT_OBEY = False

# Speed and Performance Settings

# Disable download delay to speed up scraping (default is 0.25)
DOWNLOAD_DELAY = 0.15

# The maximum number of concurrent requests that will be performed per domain
CONCURRENT_REQUESTS_PER_DOMAIN = 32

# Enable HTTP cache to speed up repeated requests
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Disable cookies if not required (enabled by default)
COOKIES_ENABLED = False

# Enable and configure AutoThrottle
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5    # Initial download delay in seconds
AUTOTHROTTLE_MAX_DELAY = 60     # Maximum delay in case of high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Target requests per remote server
DOWNLOAD_DELAY = 2   # Delay between each request

# Reduce number of concurrent requests


CONCURRENT_REQUESTS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 4  # Reduce requests per domain
CONCURRENT_REQUESTS_PER_IP = 4


RETRY_ENABLED = True
RETRY_TIMES = 5  # Number of retry attempts
RETRY_HTTP_CODES = [429, 403, 500, 502, 503, 504]
# Enable logging to monitor scraping activity
LOG_LEVEL = 'INFO'

# Output Settings
FEED_FORMAT = 'json'
FEED_URI = 'scraped_data.json'

# Disable the Telnet console (enabled by default)
TELNETCONSOLE_ENABLED = False

