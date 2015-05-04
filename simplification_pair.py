#coding: utf-8
# 辞書データとJLPTのデータを使って平易化対の獲得
# python simplification_pair.py *.dict  JLPT.txt

# import 
from extraction import *
from collections import defaultdict

# glob make file-list in directory
import glob

import MeCab

# load JLPT[(word, difficulty)]
def loadJLPT(file):
  jlpt_dict = {}
  
  for line in file:
    line = line.strip()
    pair = line.split('\t')
    jlpt_dict[pair[0]] = pair[2]
    
  return jlpt_dict
    
# make simprification pair
def makeSimpPair():
  'a'

# make cardinal sentence for interpretation  
def makeCardinalSentence(word):
  mecab = MeCab.Tagger('-Ochasen')
  print mecab.parse(word)

# extract candidacy for cardinal sentence
def extractCandidacy():
  'a'


if __name__ == '__main__':

  # all file in directory
  dict_names = glob.glob('../testdict/*')
  # difficulty 
  int_list = ['1', '2']
  # load JLPT to dictionaly
  jlpt_file = open(sys.argv[1], 'r')
  jlpt_dict = loadJLPT(jlpt_file)
  
  # all dict-file 
  for name in dict_names:
  
    # open dict file
    dict_file = open(name, 'r')
    # make soup
    soup = BeautifulSoup(dict_file)

    # <orth> word </orth>: extract word
    orth = pickOutTag(soup, 'orth')
    
    # if exist orth in JLPT
    if orth in jlpt_dict:
    
      # if difficulty of word is '1' or '2'
      if jlpt_dict[orth] in int_list :
      
        # <su> interpretation </su>: extract interpretation
        su_list = pickOutTagAll(soup, 'su')
        
        #　extract simplification pair
        for su in su_list:
          makeCardinalSentence(su)
          
    
      # append simplification pair
    # else next word
  
  