import requests as r
x=input("ENTER BOOK NAME : ")
x.replace('','+')
x.lower()
a=r.get(f"http://openlibrary.org/search.json?title={x}")
b=a.json()
n=b['docs'][0]['author_name'][0]
p=b['docs'][0]['first_publish_year']
e=b['docs'][0]['edition_count']
s=b['docs'][0]['subject'][0]
print("AUTHOR NAME : ",n)
print("FIRST PUBLISHER YEAR : ",p)
print("EDITION COUNT : ",e)
print("SUBJECT OF THE BOOK : ",s)