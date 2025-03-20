import time
from bs4 import BeautifulSoup
import requests
import re

print('Put some skill that you are not familiar with')
unfamiliar_skill = input(">").split()
print('Filtering out...')

def find_jobs():
    html_text = requests.get("https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=").text
    #print(html_text)
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("div", class_ = "srp-listing clearfix")
    #print(jobs)
    for index, job in enumerate(jobs):
        company_name = job.find("span", class_ = "srp-comp-name").text
        skills = job.find("div", class_ = "srp-keyskills").text.strip().replace(" ", ",")
        #skills_formated = re.sub(r' (?=\w)', '|', skills)
        #skills_formated = "|".join(skills.split())
        job_posting_date = job.find("span", class_ = "posting-time").text
        more_info = job.a['href']
        if unfamiliar_skill[0] not in skills and unfamiliar_skill[1] not in skills:
            with open(f"posts/{index}.txt", "w") as file:
                file.write(f"Company Name: {company_name}\n")
                file.write(f"Required Skills: {skills}\n")
                file.write(f"Job Posting Date: {job_posting_date}\n")
                file.write(f"More Info: {more_info}")
            print(f"File Saved: {index}")
        print("")

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60) #delay call by 10 min