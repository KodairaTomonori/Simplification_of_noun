#coding: utf-8
# 辞書データとJLPTのデータを使って平易化対の獲得
# python simplification_pair.py *.dict  JLPT

# import 
from extraction import *

# load JLPT[(word, difficulty)]
def loadJLPT(file):
  'a'

# make simprification pair
def makeSimpPair():
  'a'

# make cardinal sentence for interpretation  
def makeCardinalSentence():
  'a'

# extract candidacy for cardinal sentence
def extractCandidacy():
  'a'
  
if __name__ == '__main__':
  
  dict_file = open(sys.argv[1], 'r')
  #JLPT_file = open(sys.argv[2], 'r')
  
  
  soup = BeautifulSoup(dict_file)

  orth = pickOutTag(soup, 'orth')
  print orth
  
  # <su> </su>  のなかの語釈文抽出
  su_list = pickOutTagAll(soup, 'su')
  for interpretation in su_list:
    print interpretation
    
  
  # if difficulty of word is '1' or '2'
    
    #　extract simplification pair
    
    # append simplification pair
  # else next word
  
  