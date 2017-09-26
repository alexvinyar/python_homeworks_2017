from pattern.web import Wikipedia, plaintext
from task_1 import WikiParser
from task_2 import TextStatistics
import string


class Experiment:
    def show_results(self):
        p = WikiParser()
        articles = p.get_articles('Natural language processing',None,None)
        ts = TextStatistics(articles)
        ngr = ts.get_top_3grams(20)
        nw = ts.get_top_words(20)
        for g,freq in zip(ngr[0],ngr[1]):
            print(' '.join(g)+': '+str(freq)+' occurrences')
        print('\n')
        for word,freq in zip(nw[0],nw[1]):
            print(word+': '+str(freq)+' occurrences')   
        print('\n\n')
        
        raw = Wikipedia().article('Natural language processing')
        text = plaintext(raw.source)
        text = text.lower().split()
        text = ' '.join([x.strip(string.punctuation) for x in text])
        ts = TextStatistics([text])
        ngr = ts.get_top_3grams(5)
        nw = ts.get_top_words(5)
        for g,freq in zip(ngr[0],ngr[1]):
            print(' '.join(g)+': '+str(freq)+' occurrences')
        print('\n') 
        for word,freq in zip(nw[0],nw[1]):
            print(word+': '+str(freq)+' occurrences')

            
##natural language processing: 327 occurrences
##from the original: 306 occurrences
##v t e: 276 occurrences
##archived from the: 265 occurrences
##the original on: 238 occurrences
##the use of: 226 occurrences
##as well as: 215 occurrences
##one of the: 200 occurrences
##a b c: 185 occurrences
##proceedings of the: 180 occurrences
##the european union: 157 occurrences
##of the european: 154 occurrences
##such as the: 152 occurrences
##cambridge university press: 152 occurrences
##the number of: 141 occurrences
##university press isbn: 140 occurrences
##a number of: 140 occurrences
##a set of: 131 occurrences
##for example the: 131 occurrences
##based on the: 130 occurrences
##
##
##and: 16530 occurrences
##is: 8622 occurrences
##that: 4793 occurrences
##are: 4272 occurrences
##language: 3972 occurrences
##or: 3790 occurrences
##be: 3397 occurrences
##it: 2615 occurrences
##this: 2404 occurrences
##which: 2163 occurrences
##can: 1955 occurrences
##not: 1935 occurrences
##was: 1784 occurrences
##english: 1737 occurrences
##speech: 1707 occurrences
##such: 1682 occurrences
##have: 1644 occurrences
##also: 1638 occurrences
##languages: 1636 occurrences
##words: 1598 occurrences
##
##
##
##natural language processing: 14 occurrences
##a chunk of: 6 occurrences
##chunk of text: 6 occurrences
##of natural language: 5 occurrences
##systems based on: 4 occurrences
##
##
##and: 70 occurrences
##language: 59 occurrences
##is: 48 occurrences
##natural: 37 occurrences
##such: 30 occurrences
