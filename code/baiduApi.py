# encoding:utf-8

import requests
import base64
import os
import time
import pandas as pd
'''
网络图片文字识别
'''

def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
 
list_name=[]
path='C:/Users/Cheung/Downloads/'   #文件夹路径
listdir(path,list_name)
basepath = ''
chineseWomen = []
cosmoWomen = []
forhimMagazineWomen = []

def getandsaveText(filepaths):
    # 获取每一个图片的text
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
        # 二进制方式打开图片文件
    for filepath in filepaths:
        if '.jp' in filepath:           
            try:
                f = open(filepath, 'rb')
                print("open", filepath)
                img = base64.b64encode(f.read())
                params = {"image":img}
                access_token = '24.a155b276480ff9462d0597f43658056a.2592000.1622115233.282335-24078709'
                request_url = request_url + "?access_token=" + access_token
                headers = {'content-type': 'application/x-www-form-urlencoded'}
                # 图像识别过返回的text
                response = requests.post(request_url, data=params, headers=headers)
                results = response.json()
                #wordsNum = results['words_result_num']
                words = [i['words'] for i in results['words_result']]
                #words.append(wordsNum)
                # 保存至csv文件
                mistake_count = 0
                filepath = filepath.split('.',-1)
                if len(filepath) == 3:
                    filepath = filepath[0]+filepath[1]
                elif len(filepath) == 2:
                    filepath = filepath[0]
                else:
                    mistake_count = mistake_count + 1
                resultsText = pd.DataFrame(words)
                resultsText.to_csv(filepath +'.csv',encoding = "utf-8")
                print(filepath," saved")
                time.sleep(1)
            except BaseException:
                raise("something wrong")
                pass
          
        else:
            pass
        
    print("可能有这么多遗漏",mistake_count)
        
forhimMagazinepath='C:/Users/Cheung/Downloads/男人装杂志数据/' 
chinesepath='C:/Users/Cheung/Downloads/chineseWomen/'        
cosmopath='C:/Users/Cheung/Downloads/cosmo/'
#listdir(forhimMagazinepath,forhimMagazineWomen)
listdir(chinesepath,chineseWomen)
#listdir(cosmopath,cosmoWomen)
#getandsaveText(cosmoWomen)
getandsaveText(chineseWomen)
# getandsaveText(forhimMagazineWomen)