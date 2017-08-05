
# coding: utf-8

# In[58]:

import nltk
from nltk import word_tokenize
import urllib.request
from bs4 import BeautifulSoup

nltk.download('stopwords')
nltk.download('punkt')


# In[59]:

from nltk.tokenize import sent_tokenize


# In[60]:

from nltk.tokenize import word_tokenize


# In[61]:

from nltk.corpus import stopwords


# In[62]:

from collections import defaultdict


# In[63]:

from string import punctuation


# In[64]:

from heapq import nlargest



# In[65]:

#FrequencySummariser class 
##eliminates stopwords
##finding out frequency of the words from the text 
##assigning score of imp for each words in text 
##ranking sentences 

class FrequencySummarizer:
#### defining the constructor
    def __init__(self,min_cut=0.1 , max_cut = 0.9):
        self._min_cut = min_cut 
        self._max_cut = max_cut 
        self._stopwords = set(stopwords.words('english')+list(punctuation))
        
#### takes the list of sentences and return the frequency of the words 
        
    def _compute_frequencies(self,word_sent):
        freq = defaultdict(int)
        for sentence in word_sent:
            for word in sentence:
                if word not in self._stopwords:
                    freq[word]+= 1
                    
        max_freq = float(max(freq.values()))
        for word in freq.keys():
            freq[word] = freq[word]/max_freq
            if freq[word] >= self._max_cut or freq[word]<= self._min_cut:
                del freq[word]
    
         
        return freq

    
####this function takes the raw text and no of sentences we want as summary and returns the summary 

    def summarize(self,text,n):
        sents = sent_tokenize(text)
        assert n <= len(sents)
        
        for s in sents:
            word_sent = word_tokenize(s.lower())
        #word_sent = [word_tokenize(s.lower()) for s in sents]
        self._freq = self._compute_frequencies(word_sent)
        ranking = default(int)
        for i,sent in enumerate(word_sent):
            for word in sent:
                if word in self._freq:
                    rankings[i] += self._freq[w]
            
    
        sent_idx = nlargest(n,rankings,key =rankings.get)
            
        return [sents[j] for j in sent_idx]
    
    
####this function will take the url from the washington post and returns the titele and text removing all the crud 

    def get_only_text_washingtonpost_url(url):
        page = urllib.urlopen(url).read().decode('utf8')
        soup = BeautifulSoup(page)
        text = ''.join(map(lambda p: p.text,soup.find_all('article')))
        soup2 = BeautifulSoup(text)
        text = ''.join(map(lambda p: p.text,soup.find_all('p')))
        
        return soup.title.text,text
    
    


    

    
    
    
            
    
                    


# In[46]:

someUrl = 'https://www.washingtonpost.com/news/business/wp/2017/08/04/martin-shkreli-jury-enters-fifth-day-of-deliberations/?hpid=hp_hp-top-table-main_shkreli-301pm-b%3Ahomepage%2Fstory&utm_term=.7474791cd544'
textSummary = get_only_text_washingtonpost_url(someUrl)


# In[47]:

def get_only_text_washingtonpost_url(url):
        page = urllib.request.urlopen(url)
        
        soup = BeautifulSoup(page)
        text = ''.join(map(lambda p: p.text,soup.find_all('article')))
        soup2 = BeautifulSoup(text)
        text = ''.join(map(lambda p: p.text,soup.find_all('p')))
        
        return soup.title.text,text


# In[48]:

someUrl = 'https://www.washingtonpost.com/news/business/wp/2017/08/04/martin-shkreli-jury-enters-fifth-day-of-deliberations/?hpid=hp_hp-top-table-main_shkreli-301pm-b%3Ahomepage%2Fstory&utm_term=.7474791cd544'
textSummary = get_only_text_washingtonpost_url(someUrl)
textSummary


# In[50]:

fs = FrequencySummarizer()


# In[69]:

summary = fs.summarize(textSummary[1],3)


# 

# In[ ]:



