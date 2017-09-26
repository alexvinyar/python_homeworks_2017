from pattern.web import Wikipedia, plaintext
import string

class WikiParser:
    def __init__(self):
        pass
    
    def get_articles(self, start, depth, max_count):
        start_article = Wikipedia().article(start)
        links = start_article.links
        list_of_strings = []
        for l in links:
            raw = Wikipedia().article(l)
            text = plaintext(raw.source)
            text = text.lower().split()
            text = ' '.join([x.strip(string.punctuation) for x in text])
            list_of_strings.append(text)
        return list_of_strings
