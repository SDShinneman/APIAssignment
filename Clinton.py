# Question 1
# data = urllib2.urlopen(https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446475214687&searchText=*&beginDate=&endDate=&collectionMatch=false&postedBeginDate=&postedEndDate=&caseNumber=F-2014-20439&page=1&start=1&limit=500000).read()

# Question 2
# data = urllib2.urlopen(https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446475214687&searchText=Benghazi&beginDate=&endDate=&collectionMatch=false&postedBeginDate=&postedEndDate=&caseNumber=F-2014-20439&page=1&start=1&limit=500000).read

# Question 3
import re, urllib2, json
from urllib2 import urlopen

data = urllib2.urlopen(https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446475214687&searchText=*&beginDate=&endDate=&collectionMatch=false&postedBeginDate=&postedEndDate=&caseNumber=F-2014-20439&page=1&start=1&limit=500000).read()
result = json.loads(data)

def clean_json(json):
    dirty_json = urllib2.urlopen(https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446475214687&searchText=*&beginDate=&endDate=&collectionMatch=false&postedBeginDate=&postedEndDate=&caseNumber=F-2014-20439&page=1&start=1&limit=500000).read()
    valid_json = clean_json(dirty_json)
    return re.sub(r'new Date\(.*?\)', '""', json)

for row in data.find_all('pdfLink')
    print data.get('pdfLink')
