# Problem Statement

Create a scraper to scrape product reviews from a Walmart product link using Python and Selenium.

Link to scrape: 
https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365

The tasks that need to be done by scraper:
- Open the above url in Google chrome
- Scroll down to the review section
- Click See All Reviews
- Sort reviews by most recent first
- Get all review blocks and then extract certain infomation
- Click the next page and do the same till you see reviews from December 2020
- Close the browser and save the file

The values that should be saved in CSV file are:
- Review date
- Reviewer name
- Review title
- Review body or description
- Rating given by the user

The whole process should be automated.
