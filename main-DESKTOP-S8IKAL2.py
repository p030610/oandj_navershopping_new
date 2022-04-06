import requests
from openpyxl import load_workbook
import pandas as pd
import time
import xlrd
from bs4 import BeautifulSoup
import threading
import json


class core_1(threading.Thread):
    def __init__(self, page, wb, mall_name_list,malllink):
        threading.Thread.__init__(self) 
        self.page = page
        self.wb = wb
        self.mall_name_list = mall_name_list
        self.malllink = malllink
 
    def run(self):
        print("first core running")

        # print(self.malllink)

        req = requests.get(self.malllink)

        if req.status_code == 200 :
            soup = BeautifulSoup(req.text, 'html.parser')

            s = soup.find('script', type='application/ld+json')

            # JUST THIS
            core_1_result = json.loads(s.text)

            print(core_1_result)





            
            # if mallname in self.mall_name_list : 
            #     continue
            # self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
            # self.wb.save(filename=workbook_name)
            # print("correct")
            # self.mall_name_list.append(mallname)
        else : 
            pass

        
        


result_df = pd.DataFrame(columns=["업체명", "쇼핑몰명","주소", "사업자번호", "대표자", "고객센터", "이메일", "상품리뷰수", "카테고리"])
result_df.to_excel("업체.xlsx", encoding="utf-8-sig")
workbook_name = '업체.xlsx'
wb = load_workbook(workbook_name)
page = wb.active

print('1:네이버페이')
print('2:쇼핑윈도')
menunum = input("옵션을 선택해주세요.")
print('1:네이버 랭킹순')
print('2:낮은 가격순')
print('3:높은 가격순')
print('4:등록일순')
print('5:리뷰 많은순')
print('6:리뷰 좋은순')
sortnum = input("정렬옵션 선택해주세요.")
category_num = pd.read_excel("20220125.xlsx")
if int(menunum) == 1 :
    productset = "checkout"
elif int(menunum) == 2 :
    productset = "window"

if int(sortnum) == 1 :
    sort = "rel"
elif int(sortnum) == 2 :
    sort = "price_asc"
elif int(sortnum) == 3 :
    sort = "price_desc"
elif int(sortnum) == 4 :
    sort = "date"
elif int(sortnum) == 5 :
    sort = "review"
elif int(sortnum) == 6 :
    sort = "review_rel"

for name, row in category_num.iterrows() : 
    for pagingindex in range(1,100) : 

        headers = {
            'authority': 'search.shopping.naver.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'NNB=SGEE6N223FDGE; nx_ssl=2; autocomplete=use; AD_SHP_BID=3; nid_inf=2033597324; NID_AUT=tPQ918slnie7DGW2Id2zMd7qpolug1biL4Rb0Fcp3aVHtv2Avspxj8dyqjRnprGL; NID_JKL=rgjVaA5SGX/YtPCA2kxyBrwXbiGjfeewZHF/matt3Sw=; ncpa=3925768|l1hdblxs|ac8d56e9367839acee6c336ee8ce85d32af00602|s_502ee152aed5|6729f4c72f37ef1201ccf63c0b4b2f5407888ca6:1195318|l1heo7xs|54bb3ec1ca718de06c618d5c57ef841c47b6bca4|s_12503b6a62b1d|8d23234fd4fb6a33921229feb0cf9ba1f0b3c475:569556|l1km84vs|70b6a616d851f9f175493a53ac0cefe1b1645739|s_15c012d8b4517|09cf181168e9c15556dbd18024dad9770ad480ca:556323|l1km8foo|516ba5dbc58b9b7d8bf9f06c305964583cadea37|s_145de4a3a744|9962b1340998fa018f8d4dd69be7399706bab29d; NID_SES=AAABoXZXdaJH6I30U3evN7zhrbTkTv0q/27X3XdQwKJh5W2r5nD/qM8CqMvYklTMndxGxuZZkqU+wzBmTi0j7xafQhyhk95Bp6unoCAg42jp0ZgBSRRbhwf65pLmI35vwADzfGOJGTr3ZJMeU8KJ26IHbQBIaLiQ4N2tFrbmd0ikB5mxwJ2tYonJAVxmMwypkFYm3uKU03VP03yJZcoDVOvZoc7bnZuwrodJIW0DQ6g4syHEH9rjvs1gt7sr034M0Cu25eO7n+JZKBdvYIZwQ48WmUYI41K/vml050kAhLhgFmBbuBrUOWTqDmYuBbXLQMobbNDXbYpXMF7n26iHX45ssa4/aVYEvXsfceDVtTmkWIhuN6wlVlUQryYMeBW4psY0/lhZuQBupA875kgYif7jyUOq3+O6e/iDUJCcaifqmlf1aofk7j66FXkf2CdBqW5i4WadmkirAYuz3aLSafsB9/AUIqPc1d4bjsbWD/vdj4xqaifwL9LLhSHs6R5PfDW2SRViEkVEYlqONgHY6gXjja6nyPrNS3vHlE+bS5iTOH/xJm7qL64gopT0IfD3LNp/IQ==; sus_val=MTmJYAm84K5GEFEnLi9alVSk; spage_uid=',
            'logic': 'PART',
            'referer': 'https://search.shopping.naver.com/search/category/100007657?catId=50000807&iq=%EB%B4%84%EC%9B%90%ED%94%BC%EC%8A%A4&origQuery&pagingIndex=2&pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        }

        params = {
            'sort': 'rel',
            'pagingIndex': '1',
            'pagingSize': '80',
            'viewType': 'list',
            'productSet': str(productset),
            'catId': '50000807',
            'brand': '',
            'maker': '',
            'spec': '',
            'mall': '',
            'deliveryFee': '',
            'deliveryTypeValue': '',
            'iq': '',
            'eq': '',
            'xq': '',
            'frm': 'NVSHCHK',
            'window': '',
        }

        params = (
            ('catId', '50000192'),
            ('frm', 'NVSHCHK'),
            ('iq', ''),
            ('origQuery', ''),
            ('pagingIndex', str(pagingindex)),
            ('pagingSize', '80'),
            ('productSet', str(productset)),
            ('query', ''),
            ('sort', str(sort)),
            ('timestamp', ''),
            ('viewType', 'list'),
        )

        response = requests.get('https://search.shopping.naver.com/api/search/category/100007657', headers=headers, params=params)

        mall_name_list = []
       
        if response.status_code == 200 :

            itemlist = response.json()
            index_product = 0
            for i in itemlist['shoppingResult']['products']:
                index_product += 1
                try : 
                    malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                    businessno = i["mallInfoCache"]["businessNo"]
                    malllink = i["mallPcUrl"]
                    shoppingmallname = i["mallInfoCache"]["name"]
                    reviews = i["reviewCountSum"]
                    if "smartstore" in malllink: 
                        first_core = core_1(page,wb,mall_name_list,"https://brand.naver.com/woolly")
                        first_core.run()
                        
                except : 
                    print("pass")
        else : 
            print("too many requests error")

