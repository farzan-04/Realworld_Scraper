import time
import os
import requests
from bs4 import BeautifulSoup

print("Put some skills that you are NOT familiar with (separated by space):")
unfamiliar_skills = input(">").split()
print("Filtering out jobs with skills:", unfamiliar_skills)


def find_jobs():
    URL = "https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation="
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print("⚠ Error: Unable to fetch data. Retrying later...")
        return

    soup = BeautifulSoup(response.text, "lxml")
    jobs = soup.find_all("div", class_="srp-listing clearfix")

    # Ensure the 'posts' directory exists
    os.makedirs("posts", exist_ok=True)

    for index, job in enumerate(jobs):
        try:
            company_name = job.find("span", class_="srp-comp-name").text.strip()
            skills = job.find("div", class_="srp-keyskills").text.strip().replace(" ", ",")
            job_posting_date = job.find("span", class_="posting-time").text.strip()
            more_info = job.a["href"]

            # Check if job contains unfamiliar skills
            if not any(skill.lower() in skills.lower() for skill in unfamiliar_skills):
                with open(f"posts/{index}.txt", "w", encoding="utf-8") as file:
                    file.write(f"Company Name: {company_name}\n")
                    file.write(f"Required Skills: {skills}\n")
                    file.write(f"Job Posting Date: {job_posting_date}\n")
                    file.write(f"More Info: {more_info}")
                print(f"✅ Job saved: posts/{index}.txt")
        except AttributeError:
            print(f"⚠ Skipping a job listing due to missing data.")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"⏳ Waiting {time_wait} minutes before scraping again...")
        time.sleep(time_wait * 60)  # Delay before next run
