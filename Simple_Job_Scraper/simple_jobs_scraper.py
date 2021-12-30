from jobs_scraper import JobsScraper

# Let's create a new JobsScraper object and perform the scraping for a given query.
position_var = "Python"

scraper = JobsScraper(country="ca", position=position_var, location="Toronto", pages=3)
df = scraper.scrape()

df.to_csv(rf'{position_var} jobs.csv', index = False)