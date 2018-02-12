import urllib.request
from collections import Counter
import pickle
import re
import os

path = os.getcwd() + '/bigdata/'
text_file_list = os.listdir(path)

file_indexer = {}

# 텍스트파일 리스트
for file_name in text_file_list:
    with open(path+file_name) as f:
        text = f.read()
        # 정규 표현식을 사용해 단어 리스트(wordlist) 추출 'show me the money' -> ['show', 'me', 'the', 'money']
        wordlist = re.findall(r'\w+', text)
        print(wordlist)
        for word in wordlist:
            try:
                # 해당 단어의 value값이 존재한다면 value list에 단어를 추가
                file_indexer[word].append(file_name)
            except:
                # 만약 해당 단어의 key와 value값이 입력되지 않았다면 즉 첫번째 단어의 입력이라면
                # file_indexer[단어] = [파일이름] 형태로 key와 value값을 추가한다
                file_indexer[word] = [file_name]
"""
['show', 'me', 'the', 'money']
['me', 'the', 'black']
['to', 'the', 'home']
['want', 'to', 'the', 'sleep']
['my', 'life', 'for']
{'black': ['a2.txt'], 'to': ['b1.txt', 'b2.txt'], 'show': ['a1.txt'], 'home': ['b1.txt'], 'money': ['a1.txt'],
'me': ['a1.txt', 'a2.txt'], 'sleep': ['b2.txt'], 'want': ['b2.txt'], 'my': ['b3.dat'], 'for': ['b3.dat']
"""
print(file_indexer)

# 만든 딕셔너리를 저장
with open('./bigdata/file_indexer.pickle', 'wb') as oFile:
    pickle.dump(file_indexer, oFile)

# 확인
with open('file_indexer.pickle', 'rb') as ifile:
    object = pickle.load(ifile)

print(object)










































