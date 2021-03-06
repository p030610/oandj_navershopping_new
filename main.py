import requests
from openpyxl import load_workbook
import pandas as pd
import time
from sqlalchemy import false
import xlrd
import threading
import json
from selenium import webdriver

mall_name_list = []

total_crawl = 0


result_df = pd.DataFrame(columns=["업체명", "쇼핑몰명","주소", "사업자번호", "대표자", "고객센터", "이메일", "상품리뷰수", "카테고리"])
result_df.to_excel("업체_1.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_2.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_3.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_4.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_5.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_6.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_7.xlsx", encoding="utf-8-sig")
result_df.to_excel("업체_8.xlsx", encoding="utf-8-sig")


class core_1(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_1.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_1.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_1", options=self.options)

    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 1 : 

                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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


                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]), params=params)
                
                    if response.status_code == 200 :

                        itemlist = response.json()

                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                            
                    else : 
                        print("too many requests error")

class core_2(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_2.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_2.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_2", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 2 : 

                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]), params=params)

                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                            
                    else : 
                        print("too many requests error")

class core_3(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_3.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_3.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_3", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 3 : 
                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]), params=params)
                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                            
                    else : 
                        print("too many requests error")

class core_4(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_4.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_4.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_4", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 4 : 
                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]),  params=params)

                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                    else : 
                        print("too many requests error")


class core_5(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_5.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_5.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_5", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 5 : 
                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]),  params=params)

                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                    else : 
                        print("too many requests error")

class core_6(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_6.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_6.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_6", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 6 : 
                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]),  params=params)

                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                    else : 
                        print("too many requests error")

class core_7(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_7.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_7.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_7", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 7 : 
                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]),  params=params)

                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                    else : 
                        print("too many requests error")

class core_8(threading.Thread):
    def __init__(self,mall_name_list):
        threading.Thread.__init__(self) 

        self.workbook_name = '업체_8.xlsx'
        self.wb = load_workbook(self.workbook_name)
        self.page = self.wb.active
        self.mall_name_list = mall_name_list
        
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36")
        self.options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.options.add_argument('--disable-blink-features=AutomationControlled')

        # self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_8.exe", options=self.options)
        self.driver = webdriver.Chrome(executable_path = "./chromedrivers/chromedriver_8", options=self.options)
    def run(self):

        for name, row in category_num.iterrows() : 
            for pagingindex in range(1,100) : 
                if pagingindex % 8 == 0 : 
                    params = {
                        'sort': str(sort),
                        'pagingIndex': str(pagingindex),
                        'pagingSize': '80',
                        'viewType': 'list',
                        'productSet': str(productset),
                        'catId': str(row["카테고리번호"]),
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

                    response = requests.get('https://search.shopping.naver.com/api/search/category/' + str(row["카테고리번호"]),  params=params)

                
                    if response.status_code == 200 :

                        itemlist = response.json()
                        for i in itemlist['shoppingResult']['products']:
                            try : 
                                malladdress = i["mallInfoCache"]["bizplBaseAddr"]
                                businessno = i["mallInfoCache"]["businessNo"]
                                malllink = i["mallPcUrl"]
                                shoppingmallname = i["mallInfoCache"]["name"]
                                print(shoppingmallname)
                                reviews = i["reviewCountSum"]
                                if "smartstore" in malllink: 

                                    self.driver.get(malllink)    

                                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[0].click()
                                    time.sleep(1)
                                    try : 
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    except : 
                                        self.driver.find_elements_by_class_name("_3oMcQ3LMwm")[1].click()
                                        time.sleep(1)
                                        texts = self.driver.find_elements_by_class_name("_10PxysFyMd")
                                        mallname = texts[0].text
                                        representative = texts[1].text
                                        gogek = texts[5].text
                                        email = texts[6].text
                                    
                                    self.page.append(["",shoppingmallname, mallname,malladdress,businessno,representative,gogek,email, reviews,row["세분류"]])
                                    self.wb.save(filename=self.workbook_name)
                                    print("correct")
                                    mall_name_list.append(mallname)
                        
                            except : 
                                print("pass")
                    else : 
                        print("too many requests error")


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
category_num = pd.read_excel("./20220407.xlsx")
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

one_core = core_1(mall_name_list)
two_core = core_2(mall_name_list)
three_core = core_3(mall_name_list)
four_core = core_4(mall_name_list)
five_core = core_5(mall_name_list)
six_core = core_6(mall_name_list)
seven_core = core_7(mall_name_list)
eight_core = core_8(mall_name_list)
one_core.start()
two_core.start()
three_core.start()
four_core.start()
five_core.start()
six_core.start()
seven_core.start()
eight_core.start()

one_core.join()
two_core.join()
three_core.join()
four_core.join()
five_core.join()
six_core.join()
seven_core.join()
eight_core.join()

#파일취합

df_1 = pd.read_excel("./업체_1.xlsx")
df_2 = pd.read_excel("./업체_2.xlsx")
df_3 = pd.read_excel("./업체_3.xlsx")
df_4 = pd.read_excel("./업체_4.xlsx")
df_5 = pd.read_excel("./업체_5.xlsx")
df_6 = pd.read_excel("./업체_6.xlsx")
df_7 = pd.read_excel("./업체_7.xlsx")
df_8 = pd.read_excel("./업체_8.xlsx")

df_total = pd.concat([df_1,df_2,df_3,df_4,df_5,df_6,df_7,df_8], ignore_index=True)

df_total = df_total.sort_values("상품리뷰수", ascending=False)

df_total.to_excel("./업체_통합본.xlsx")