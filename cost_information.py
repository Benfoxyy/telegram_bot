import re
from bs4 import BeautifulSoup


def design(lst):
    return (f'''
💰Gold :
                    
18% : {((lst[0][0])//10):,}
24% : {((lst[1][0])//10):,}

🪙Coin :

Bahar coin : {((lst[2][0])//10):,}
Imami coin : {((lst[3][0])//10):,}
Half coin : {((lst[4][0])//10):,}
Quarter coin : {((lst[5][0])//10):,}

💵Currency :

USD : {((lst[6][0])//10):,}
EUR : {((lst[7][0])//10):,}
GBP : {((lst[8][0])//10):,}
''')

def cost(request):
    f_list=[]
    soup=BeautifulSoup(request.text,'html.parser')
    price=soup.find(class_="value")
    sub=re.sub(',','',str(price))
    res=re.findall(r'\d+',sub)
    f_res=int(res[0])
    f_list.append(f_res)
    return f_list