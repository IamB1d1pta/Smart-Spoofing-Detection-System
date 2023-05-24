import socket
link="www.dghjdgf.com/paypal.co.uk/cycgi-bin/webscrcmd=_home-customer&nav=1/loading.php"
link1=link[:link.rfind('/')]
var=socket.gethostbyname(link1)
    print(var)
for j in range(len(link)):
    char=link[j]
    if link[j]=='/':
            break
        
print(char)
import pandas as pd
sv=pd.read_csv("phishing_site_urls.csv")
for i in range(549345):
    if link==sv.URL[i]:
            flag=1
            break
    else:
            flag=0
    
if flag==1:
    print("unsafe")
else:
    print("safe")
