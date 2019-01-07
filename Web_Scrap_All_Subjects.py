# The Scraper with subject name!!
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://results.smu.edu.in/smit/results_grade_view.php?exam=41&subject=10314')
soup = BeautifulSoup(html.read(),'html.parser')
# print(soup)
filter1 = soup.findAll('div',{'class':"content",'style':"font-family:courier"})
# print(filter1)
filter2 = soup.findAll('p',{'class':"sub-heading2"})
filter3 = filter2[0].getText()
print(filter3)
print(filter3[8:])

########################################################################################################################
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://results.smu.edu.in/smit/results_grade_selection.php?exam=41')
soup = BeautifulSoup(html.read(),'html.parser')
# print(soup)
count = 0
link_list = []
for link in soup.findAll('a', attrs={'href': re.compile("results")}):
     if 'BACK' not in link.string:
        print(link.get('href'))
        print(link.string)
        link_list.append(link.get('href'))
        count +=1
print("The Count of Total Subjects in SMIT is "+str(count)+"!!!!!")

########################################################################################################################
# extracting the number of reg_no. redesign of code!
import re
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
new_count = 0
for i in range(count):
    html = urlopen('https://results.smu.edu.in/smit/{}'.format(link_list[i]))
    soup = BeautifulSoup(html.read(),'html.parser')
    # Subject name
    filter2 = soup.findAll('p',{'class':"sub-heading2"})
    filter3 = filter2[0].getText()
    subject = filter3
    subject1 = subject
    if "/" in subject:
        subject1 = subject1.replace("/"," ")
    if ":" in subject:
        subject1 = subject1.replace(":","")
    file = open("C:\\Users\\Yasser Arafat\\Desktop\\all_subject_dump\\{}.json".format(subject1),"w")
    # Extracting data
    data = soup.findAll('div',{'class':"content",'style':"font-family:courier"})
    filter_data = re.findall(r'\d{6,9}\d+.+\d+?\s+\w+',str(data))
    filter_credit = re.findall(r'Subject\s?Credit?\s?:?\s?[\d.]?[\d.]?[\d.]?',str(data))
    credit_filter_list = filter_credit[0].split()
    credit = credit_filter_list[3]
    lenght = len(filter_data)
    dict_large = {}
    for i in range(lenght):
        list_data = filter_data[i].split()
        list_data.append(subject1)
        dict_small = {"{}".format(list_data[0]):{"{}".format(list_data[5]):[list_data[1],list_data[2],list_data[3],list_data[4],credit]}}
        dict_large.update(dict_small)
    json.dump(dict_large,file)
    file.close()
    new_count +=1
    print("Successful! and count is {} and subject is {}".format(new_count,subject1))
