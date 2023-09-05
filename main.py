import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
website_url = "https://infopark.in/companies/job-search"
keywords=["python","fresher"]
output_file=open("jobs.txt","w")
res = requests.get(website_url, verify=False)
soup = BeautifulSoup(res.text, 'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs :
    title_element=job.find("a")
    title=title_element.text
    link=title_element["href"]
    company_name=job.find("div",{"class":"jobs-comp-name"}).text
    last_date=job.find("div",{"class":"job-date"}).text
    if any( word.lower() in title.lower() for word in keywords):
         output_file.write(title + " " +company_name + " " + last_date + "\n" +link +"\n\n")
