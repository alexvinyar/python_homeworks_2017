import unittest


def poly_hash(s, x=31, p=997):
    h = 0
    for j in range(len(s)-1, -1, -1):
        h = (h * x + ord(s[j]) + p) % p
    return h


def search_rabin_multi(text, patterns):
    p = 997
    x = 31
    all_indices = []  
    for pattern in patterns:
        indices = []
        
        if len(pattern) == 0:
            all_indices.append([])
            continue
        
        if len(text) < len(pattern):
            all_indices.append([])
            continue
        
        # precompute hashes
        precomputed = [0] * (len(text) - len(pattern) + 1)
        precomputed[-1] = poly_hash(text[-len(pattern):], x, p)
        
        factor = 1
        for i in range(len(pattern)):
            factor = (factor*x + p) % p
            
        for i in range(len(text) - len(pattern)-1, -1, -1):
            precomputed[i] = (precomputed[i+1] * x + ord(text[i]) - factor * ord(text[i+len(pattern)]) + p) % p
        
        pattern_hash = poly_hash(pattern, x, p)
        for i in range(len(precomputed)):
            if precomputed[i] == pattern_hash:
                if text[i: i + len(pattern)] == pattern:
                    indices.append(i)
        
        all_indices.append(indices)
        
    return all_indices


class SearchRabinMultiTest(unittest.TestCase):
    def setUp(self):
        self.search = search_rabin_multi

    def test_empty(self):
        text = ''
        patterns = ['dust','inc']
        self.assertEqual(self.search(text,patterns),[[],[]])

    def test_var(self):
        text = 'dust'
        patterns = ['du','dustdust','']
        self.assertEqual(self.search(text,patterns),[[0],[],[]])

    def test_count(self):
        text = 'Betty Botter bought some butter'
        patterns = ['tt','ter']
        indices = [[2, 8, 27],[9,28]]
        self.assertEqual(self.search(text,patterns),indices)
    
        
unittest.main()
