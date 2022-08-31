# Stack Overflow Jobs Scraper
### A simple scraper for the jobs section on Stack Overflow.

This program allows you to paste a Stack Overflow Jobs URL into the command line to generate a CSV file of all results containing company name, position name and the URL to the job post.

--------
## Sample output:

|ID|Company Name|Job Title|Job Post URL|
|:-|:-|:-|:-|
|1|Acme Corp.|Full Stack Developer|https://stackoverflow.com/jobs/123456/some-url|
---------


### Instructions to run program:
1. Clone the repo to your local system.

2. Install requirements using the following command:  
```
pip install -r requirements.txt
```
3. Run the following command:  
```
python3 scraper.py
```
4. The program will generate a CSV file in the same directory as itself.
