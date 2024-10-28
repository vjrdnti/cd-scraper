# cd-scraper
[Strictly for educational purposes only]
College dunia or similar large sites may not allow many concurrent requests for large scraping.
here I use the locally imported sitemap with each entry manipulated as an api link
then i use a basic spider to scrape the data and save it in a structured format
the main learning outcome was use of middlewares and the settings.py
in which i handle:
1) delay in initial downloads
2) concurrent_requests (per domain/ per IP)
3) retry times, and status codes to trigger
4) middleware to generate random users
5) user agent header

note: the feed_uri json is not required as my spider already dumps the data in a csv.
the final outputs were included in .gitignore as they are huge in size

