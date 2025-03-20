# 🏢 RealWorld Web Scraper 🕷️ (Python, BeautifulSoup, Requests)

## 📌 Overview  
This Python web scraper **extracts job postings** from TimesJobs.  
It **filters out jobs** based on **unfamiliar skills** and saves each job post as a `.txt` file.  

## 🛠️ Tech Stack  
- **Python**
- **BeautifulSoup4** (For HTML parsing)
- **Requests** (For HTTP requests)
- **Lxml** (For efficient parsing)
- **File Handling (`.txt` format)**

## 🔧 How It Works  
1️⃣ **Fetches job postings from TimesJobs** using HTTP requests.  
2️⃣ **Parses job details** (company, skills, date, job link).  
3️⃣ **Filters out jobs** that require unfamiliar skills.  
4️⃣ **Saves job details into `.txt` files** inside the `posts/` folder.  
5️⃣ **Automatically scrapes new jobs every 10 minutes.**  

## 📂 Sample Output (`posts/0.txt`)  
Company Name: ABC Tech Solutions
Required Skills: Python,Django,REST,SQL 
Job Posting Date: 1 day ago 
More Info: https://m.timesjobs.com/job-detail/abc-tech


