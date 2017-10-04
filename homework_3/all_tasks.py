from pattern.web import Wikipedia, plaintext
from nltk.util import ngrams
from collections import Counter
import string
import re
import numpy as np

class WikiParser:
    def __init__(self):
        pass
    
    def get_articles(self, start):
        start_article = Wikipedia().article(start)
        links = start_article.links
        list_of_strings = []
        for l in links:
            raw = Wikipedia().article(l)
            text = plaintext(raw.source)
            text = text.lower().split()
            text = ' '.join([x.strip('"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~') for x in text])
            list_of_strings.append(text)
        return list_of_strings


class TextStatistics:
    def __init__(self, articles):
        self.articles = articles
    
    def get_top_3grams(self, n, use_idf):
        in_sentences = {}
        tg = []
        super_article = '. '.join(self.articles)
        super_article = super_article.lower().split()
        super_article = ' '.join([x.strip('"#$%&\'()*+,-/:;<=>@[\\]^_`{|}~') for x in super_article])
        sentences = filter(None,re.split('[.!?]',super_article))
        for sentence in sentences:
            stg = [''.join(x) for x in ngrams(sentence,3)]
            tg += stg
            for i in set(stg):
                if i in in_sentences:
                    in_sentences[i] += 1
                else:
                    in_sentences[i] = 1
        count = Counter(tg)
        if use_idf:
            count = [(ngram, freq * np.log(float(len(sentences)) / in_sentences[ngram]))
                     for ngram,freq in count.items()]
        else:
            count = count.items()
        top = sorted(count,key=lambda x: x[1],reverse=True)[:n]
        list_of_3grams_in_descending_order_by_freq = []
        list_of_their_corresponding_freq = []
        for i in top:
            list_of_3grams_in_descending_order_by_freq.append(i[0])
            list_of_their_corresponding_freq.append(i[1])
        return (list_of_3grams_in_descending_order_by_freq, list_of_their_corresponding_freq)
    
    def get_top_words(self, n, use_idf):
        stop = ['aboard','about','above','across','after','against','along','alongside','amid','among','amongst','around',
                'as','aside','astride','at','atop','barring','before','behind','below','beneath','beside','besides','between',
                'beyond','but','by','circa','concerning','considering','despite','down','during','except','excepting','excluding',
                'failing','following','for','from','in','including','inside','into','like','minus','near','nearby','next',
                'notwithstanding','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round',
                'save','since','than','through','throughout','till','times','to','toward','towards','under','underneath','unlike',
                'until','unto','up','upon','versus','via','with','within','without','worth','a','an','the']

        in_articles = {}
        all_words = []
        for article in self.articles:
            article = re.sub('[0-9]+ ','',article)
            words = article.lower().split()
            words = [x.strip(string.punctuation) for x in words if x not in stop]
            all_words += words
            for word in set(words):
                if word in in_articles:
                    in_articles[word] += 1
                else:
                    in_articles[word] = 1
        count = Counter(all_words)
        if use_idf:
            count = [(word, freq * np.log(float(len(self.articles)) / in_articles[word]))
                     for word,freq in count.items()]
        else:
            count = count.items()
        top = sorted(count,key=lambda x: x[1],reverse=True)[:n]
        list_of_words_in_descending_order_by_freq = []
        list_of_their_corresponding_freq = []
        for i in top:
            list_of_words_in_descending_order_by_freq.append(i[0])
            list_of_their_corresponding_freq.append(i[1])
        return (list_of_words_in_descending_order_by_freq, list_of_their_corresponding_freq)
    

class Experiment:
    def show_results(self):
        p = WikiParser()
        articles = p.get_articles('Natural language processing')
        ts = TextStatistics(articles)
        ngr = ts.get_top_3grams(20,True)
        nw = ts.get_top_words(20,True)
        for g,freq in zip(ngr[0],ngr[1]):
            print(''.join(g)+': '+str(freq))
        print('\n')
        for word,freq in zip(nw[0],nw[1]):
            print(word+': '+str(freq))   
        

## th: 49756.5389305
##the: 46323.7340107
##he : 40711.3938865
##ion: 37665.2329342
##tio: 35442.7981008
##ing: 34591.92297
## in: 34510.8592322
##on : 33593.4842788
##ati: 32348.2453289
## of: 32113.9048147
##ng : 32100.5164577
##of : 31294.0387485
## an: 31112.6643377
##ed : 31061.058146
##al : 30635.1173816
## co: 30489.4033129
##es : 29457.9769901
##and: 29107.4160881
##nd : 29004.3348625
##ent: 27980.6500252
##
##
##displaystyle: 2310.10666486
##turing: 1675.6819155
##arabic: 1088.58984025
##x: 849.586594457
##eu: 815.361355212
##tone: 811.861393169
##learning: 800.008421613
##chomsky: 799.302357237
##german: 797.592521573
##european: 778.368830252
##languages: 776.191835293
##english: 748.83102793
##turkish: 734.268297915
##retrieved: 720.344457971
##union: 708.95976536
##spanish: 682.142723497
##verbs: 673.23420318
##speech: 664.372230413
##dialects: 656.71754684
##i: 650.243980334
