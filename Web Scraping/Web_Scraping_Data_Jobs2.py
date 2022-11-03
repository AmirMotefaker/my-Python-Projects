ef make_indeed_url(search_job, search_location, job_age):
    job = search_job.replace(' ', '%20')
    location = search_location.replace(',', '%2C').replace(' ', '%20')
    indeed_job_url = f'https://www.indeed.com/jobs?q={job}&l={location}&fromage={job_age}'
    return indeed_job_url

def scrape_job_page_meta(job_page_html):
    page_soup = BeautifulSoup(job_page_html.text, 'lxml')
    df_columns = ['job_title', 'company_name', 'company_location', 'est_salary', 'job_href','job_desc']
    jobs_df = pd.DataFrame(columns = df_columns)
    for job in page_soup.find_all('div',{"id":"mosaic-provider-jobcards"}):
        for href_post in job.find_all('a', href=True):
            if href_post.find('a', href=True):
                job_desc_href = 'https://www.indeed.com'+str(href_post['href'])
                job_desc = scrape_job_description(job_desc_href)
                for job_meta in href_post.find_all('div',{"class":"job_seen_beacon"}):
                    job_title, company_name, company_location, estimated_salary = scrape_job_card(job_meta)
                    print(f'{job_title}, {job_desc_href}')        
                    job_dict = {'job_title': job_title,
                                'company_name': [company_name],
                                'company_location': [company_location],
                                'est_salary': [estimated_salary],
                                'job_href': [job_desc_href],
                                'job_desc': [job_desc]}
                    j_df = pd.DataFrame.from_dict(job_dict)
                    jobs_df= jobs_df.append(j_df, ignore_index=True)
    return jobs_df
  
def scrape_job_card(job_meta):
    try:
        job_title = job_meta.find('h2', {'class':'jobTitle'}).get_text().lstrip('new\n')
    except:
        job_title = 'No job title found'
    try:
        company_name = job_meta.find('span',{'class':'companyName'}).get_text()
    except:
        company_name = 'No Company Name'
    try:
        company_location = job_meta.find('div', {'class':'companyLocation'}).get_text()
    except:
        company_location = 'No Location'
    try:
        estimated_salary = job_meta.find('div', {'class':'metadata salary-snippet-container'}).get_text()
    except:
        estimated_salary = 'No Estimated Salary'
    return job_title, company_name, company_location, estimated_salary

def scrape_job_description(job_desc_href):
    try:
        page = web_scrape_api_call(job_desc_href)
        soup = BeautifulSoup(page.content, 'html.parser')
        job_desc = soup.find(id='jobDescriptionText')
        job_desc = job_desc.text.replace('\n', ' ').replace('\r', '')
    except:
        job_desc = 'No Job Description'
    return job_desc

def job_loc_scrape_loop(job_list,loc_list,job_age):
    date = dt.datetime.today().strftime('%Y-%m-%d')
    for job in job_list:
        for loc in loc_list:
            print(f'Scraping: {job} {loc}')
            indeed_url = make_indeed_url(job, loc, job_age)
            indeed_response = web_scrape_api_call(indeed_url)
            result_df = scrape_job_page_meta(indeed_response)
            result_df['retrieve_date'] = date
            print('dumping to sql')
            sql_dump(result_df, 'data/jobs', 'indeed_jobs')
    return None

def sql_dump(df, db, table):
    con = sqlite3.connect(db) 
    df.to_sql(table, con, if_exists='append')
    con.close()

job_list = ["Data Scientist", "Data Analyst", "Data Engineer",
                "Machine Learning Engineer", "Business Intelligence Analyst"]
primary_city_state_list = ["Atlanta, GA", "Austin, TX", "Boston, MA", "Chicago, IL",
                    "Denver, CO", "Dallas-Ft. Worth, TX", "Los Angeles, CA",
                    "New York City, NY", "San Francisco, CA", "Seattle, WA"]
job_loc_scrape_loop(job_list, primary_city_state_list, '7')

def web_scrape_api_call(url_to_scrape):
    url = "https://api.webscrapingapi.com/v1"
    params = {
    "api_key":WebScrapingAPIkey,
    "url":url_to_scrape
    }
    response = requests.request("GET", url, params=params)
    return response

