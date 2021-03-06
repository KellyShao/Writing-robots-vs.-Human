
import csv
import math
import random
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text 
from sklearn import metrics
from sklearn.metrics import roc_curve,auc,f1_score
import matplotlib.pyplot as plt
from gensim.models import word2vec
from gensim import corpora
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import remove_stopwords
from gensim.parsing.preprocessing import strip_short
from gensim.parsing.preprocessing import strip_non_alphanum


stop_words = text.ENGLISH_STOP_WORDS.union([u'apr',u'archetypr',u'aug',u'configuration',u'conference',u'continuing'])#estimate
sci_file = "cs_papers/sci_after_filter.csv"
scigen_file = "cs_papers/scigen_after_filter - Copy.csv"

def import_data(file,row_content,x):
    content = []
    label = []
    content_1 = open(file, 'r')
    csv_reader = csv.reader(content_1)
    for row in csv_reader:
        row = unicode(row[row_content], errors='ignore')
        row_new = remove_stopwords(row)
        row_new = strip_numeric(row_new)
        #row_new = strip_non_alphanum(row_new)   
        row_new = strip_short(row_new,minsize = 3)
        content.append(row_new)
    length = len(content)
    for i in range(0,length):
        label.append(x)
    
    return content,label

sci_content, sci_label = import_data(sci_file,1,1)
scigen_content, scigen_label = import_data(scigen_file,1,0)
len1=len(sci_content)
len2=len(scigen_content)
data = sci_content+scigen_content
label = sci_label+scigen_label

#def extract_sentence(content,percent):
#    new_content = []
#    for line in content:
#        sum = len(line)+1
#        sum = math.ceil(sum*percent)
#        new_filter = []
#        cnt = 0
#        new_line = []
#        for word in line:
#           cnt =cnt+1
#           if(cnt<=sum):
#                new_line.append(word)
#        new_content.append(new_line)
#    return new_content

def extract_sentence(content,percent):
    new_content = []
    for line in content:
        sum = len(line)+1
        sum = math.ceil(sum*percent)
        if sum>len(line):
            sum -=1
        new_line = random.sample(line,int(sum))
        new = []
        for i in new_line:
            new.append(i)
        new_content.append(new)
    return new_content


def build_dict(data,stop_words):
    texts = [[word for word in document.lower().split() if word not in stop_words]
             for document in data]
    dictionary = corpora.Dictionary(texts)
    return texts,dictionary

content, dict = build_dict(data,stop_words)
model = word2vec.Word2Vec(content, min_count=1)#,iter=50)
model.save("auto_human_sentence.model")

def f1(content, label, cross_fold):
    f1_mean = np.zeros(20)
    for i in range(0,cross_fold):
        print i
        content_auto = content[0:928]
        content_human = content[928:1836]
        label_auto = label[0:928]
        label_human = label[928:1836]
        random_num = np.random.randint(low=0, high=100)
        #print 'random_num_auto:' +str(random_num)
        content_train_auto,content_test_auto,label_train_auto,label_test_auto = train_test_split(content_auto, label_auto, test_size=0.2,random_state=random_num)
        random_num = np.random.randint(low=0, high=100)
        #print 'random_num_human:' +str(random_num)
        content_train_human,content_test_human,label_train_human,label_test_human = train_test_split(content_human, label_human, test_size=0.2,random_state=random_num)

        content_train = content_train_auto+content_train_human
        content_test = content_test_auto+content_test_human
        label_train = label_train_auto+label_train_human
        label_test = label_test_auto+label_test_human
        #print 'len(content_train):'+str(len(content_train))
        #print 'len(content_test):'+str(len(content_test))

        #build matrics
        train = []
        w2v_model =word2vec.Word2Vec.load("auto_human_sentence.model")
        print "model load successed"
        for each_train in content_train:
            word_num = 0
            vector = np.zeros(100)
            for word in each_train:
                if unicode(word) in w2v_model:
                    vector += w2v_model[unicode(word)]
                    word_num += 1
            vector=vector/word_num
            train.append(vector)
        #print "train builed"

        #build clf
        clf = svm.SVC(kernel='linear',cache_size=20000)#, probability=True)
        clf_res = clf.fit(train, label_train)

        for percent in range(1,101,5):
            test = []
            new_content_test = extract_sentence(content_test,percent*0.001)
            for each_test in new_content_test:
                word_num = 0
                vector = np.zeros(100)
                for word in each_test:
                    if unicode(word) in w2v_model:
                        vector += w2v_model[unicode(word)]
                        word_num += 1
                vector=vector/word_num
                test.append(vector)
            print percent
            
            pred =  clf_res.predict(test)
            score_micro = f1_score(label_test, pred, average='micro')
            score_macro = f1_score(label_test, pred, average='macro')
            f1=(score_macro+score_micro)/2
            print 'f1: %0.20f'%f1
            f1_mean[(percent-1)/5]+=f1
    f1_mean = f1_mean/cross_fold
    x_axis = range(1,21)
    x=np.array(x_axis)
    plt.plot(x,f1_mean)
    plt.show()
    print f1_mean
    f1_mean = list(f1_mean)
    f1_mean_csv=pd.DataFrame(f1_mean)
    f1_mean_csv.to_csv('f1/f1_array_small.csv',mode='a',header=False)#encoding="utf-8")




f1(content,label,10)

