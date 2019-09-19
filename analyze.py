'''
Natural Language Sentiment Analysis
    using Google Cloud Natural Language API

Accepted file types:
    - .xls/.xlsx (! without a header)
        for multi-analysis where each cell is analyzed individually
    - .txt for a single analysis on the whole file

Accepted languages(detected automatically) for Sentiment Analysis:
    Language                            ISO-639-1 Code
    Chinese (Simplified)	                zh
    Chinese (Traditional)	                zh-Hant
    English	                                en
    French	                                fr
    German	                                de
    Italian	                                it
    Japanese	                            ja
    Korean	                                ko
    Portuguese (Brazilian & Continental)	pt
    Spanish	                                es
https://cloud.google.com/natural-language/docs/languages

SCORE of the sentiment ranges between -10 (negative) and 10 (positive)
    and corresponds to the overall emotional leaning of the text.

MAGNITUDE indicates the overall strength of emotion
    (both positive and negative) within the given text, between 0.0 and +inf.

Example usage:
    python3 analyze.py test.xls
'''

import sys

# To show progress bar
from tqdm import tqdm

# My files
import check as ck
import excel as xl
import google_nl as g
import print_results

if __name__ == '__main__':
    TYPE = ck.check(sys.argv)
    FILE = sys.argv[1]

#    class Sent:
#        score = 0.568784152
#        magnitude = 0.498455648
#    SEN = Sent()
    
    if TYPE == '.txt':
        TXT = open(FILE, "r")
        SEN = g.analyze_sentiment(TXT.read())
        TXT.close()
        print_results.text(SEN)
    elif TYPE == 'excel':
        DATA, ROWS_NB = xl.get_xl(FILE)
        for LINE in tqdm(range(1, ROWS_NB)):
            SEN = g.analyze_sentiment(DATA.iloc[LINE, 0])
            xl.store_results("s_" + FILE, LINE, SEN.score, SEN.magnitude)
        print_results.excel(FILE)
