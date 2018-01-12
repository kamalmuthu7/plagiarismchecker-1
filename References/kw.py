from io import StringIO, BytesIO
import sys, re, string, logging
from collections import defaultdict
from datetime import datetime

# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter

from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import SnowballStemmer   
import nltk.data

# from network import download
# from ssk import SSK
words_cache = {}

def getwords(text, langs=["english", "russian"], debug = False):
    key = (text, tuple(langs))
    if (key in words_cache):
        if debug: print("found words in cache")
        return words_cache[key]
    punct = re.compile('[%s0-9\–]' % re.escape(string.punctuation))
    
    if debug: print("tokenize begin ({0})".format(timestr()))
    words = TreebankWordTokenizer().tokenize(str(text));
    if debug: print("tokenize ended ({0})".format(timestr()))

    if debug: print("del short words begin ({0})".format(timestr()))
    words[:] = [word for word in words if len(word)>2]
    if debug: print("del short words ended ({0})".format(timestr()))

    if debug: print("punctuation begin ({0})".format(timestr()))
    words[:] = [word for word in words if punct.sub("", word) == word]
    if debug: print("punctuation ended ({0})".format(timestr()))

    if debug: print("stopwords begin ({0})".format(timestr()))
    words[:] = [word.lower() for word in words]
    stops = [stopwords.words(lang) for lang in langs]
    for stop in stops:
        words[:] = [word for word in words if word not in stop]
    if debug: print("stopwords ended ({0})".format(timestr()))

    if debug: print("stemming begin ({0})".format(timestr()))
    stemmers = [SnowballStemmer(lang) for lang in langs]
    for stemmer in stemmers:
        words[:] = [stemmer.stem(word) for word in words]
    if debug: print("stemming ended ({0})".format(timestr()))

    words_cache[key] = words
    return words

text  = 'Peter Evans (born 1 August 1961) is a former breaststroke swimmer for Australia who won four Olympic medals in the 1980s. After training in the UK under David Haller, he returned to Australia in 1980. He rebuffed Australian government pressure to boycott the 1980 Moscow Olympics in response to the Soviet invasion of Afghanistan, and won gold in the 4×100 m medley relay as one of the Quietly Confident Quartet. He also won bronze in the 100 m breaststroke. After competing for the University of Arizona in the US, he returned to Australia for the 1982 Commonwealth Games in Brisbane, winning silver in the 100 m breaststroke and gold in the medley relay. He competed in his second Olympics in Los Angeles in 1984, winning bronze in the 100 m breaststroke and the medley relay. Evans retired from swimming after missing selection for the 1986 Commonwealth Games, and unsuccessfully attempted to follow his father Max into politics before pursuing a career in business. (Full article...) '


print(getwords(text,langs = "english",debug = False))
