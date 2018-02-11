import urllib.request
from collections import Counter
import pickle
import re
import os

path = os.getcwd() + '/bigdata/'
text_file_list = os.listdir(path)

file_indexer = {}

# �ؽ�Ʈ���� ����Ʈ
for file_name in text_file_list:
    with open(path+file_name) as f:
        text = f.read()
        # ���� ǥ������ ����� �ܾ� ����Ʈ(wordlist) ���� 'show me the money' -> ['show', 'me', 'the', 'money']
        wordlist = re.findall(r'\w+', text)
        print(wordlist)
        for word in wordlist:
            try:
                # �ش� �ܾ��� value���� �����Ѵٸ� value list�� �ܾ �߰�
                file_indexer[word].append(file_name)
            except:
                # ���� �ش� �ܾ��� key�� value���� �Էµ��� �ʾҴٸ� �� ù��° �ܾ��� �Է��̶��
                # file_indexer[�ܾ�] = [�����̸�] ���·� key�� value���� �߰��Ѵ�
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

# ���� ��ųʸ��� ����
with open('./bigdata/file_indexer.pickle', 'wb') as oFile:
    pickle.dump(file_indexer, oFile)

# Ȯ��
with open('file_indexer.pickle', 'rb') as ifile:
    object = pickle.load(ifile)

print(object)










































