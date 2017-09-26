from pattern.en import ngrams
from collections import Counter
import re


class TextStatistics:
    def __init__(self, articles):
        self.articles = articles
    
    def get_top_3grams(self, n):
        super_article = ' '.join(self.articles)
        super_article = re.sub('[0-9]+ ','',super_article)
        tg = ngrams(super_article)
        count = Counter(tg)
        top = count.most_common(n)
        list_of_3grams_in_descending_order_by_freq = []
        list_of_their_corresponding_freq = []
        for i in top:
            list_of_3grams_in_descending_order_by_freq.append(i[0])
            list_of_their_corresponding_freq.append(i[1])
        return (list_of_3grams_in_descending_order_by_freq, list_of_their_corresponding_freq)
    
    def get_top_words(self, n):
        stop = ['aboard','about','above','across','after','against','along','alongside','amid','among','amongst','around',
                'as','aside','astride','at','atop','barring','before','behind','below','beneath','beside','besides','between',
                'beyond','but','by','circa','concerning','considering','despite','down','during','except','excepting','excluding',
                'failing','following','for','from','in','including','inside','into','like','minus','near','nearby','next',
                'notwithstanding','of','off','on','onto','opposite','outside','over','past','per','plus','regarding','round',
                'save','since','than','through','throughout','till','times','to','toward','towards','under','underneath','unlike',
                'until','unto','up','upon','versus','via','with','within','without','worth','a','an','the']
        
        super_article = ' '.join(self.articles)
        super_article = re.sub('[0-9]+ ','',super_article)
        words = super_article.split()
        words = [x for x in words if x not in stop]
        count = Counter(words)
        top = count.most_common(n)
        list_of_words_in_descending_order_by_freq = []
        list_of_their_corresponding_freq = []
        for i in top:
            list_of_words_in_descending_order_by_freq.append(i[0])
            list_of_their_corresponding_freq.append(i[1])
        return (list_of_words_in_descending_order_by_freq, list_of_their_corresponding_freq)
