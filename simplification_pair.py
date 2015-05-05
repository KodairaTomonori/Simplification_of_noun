#coding: utf-8
# 辞書データとJLPTのデータを使って平易化対の獲得
# python simplification_pair.py JLPT.txt

# import 
from extraction import *
from collections import OrderedDict

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
    
# remove sisused word
def removeDisusedWord(words):
  words = words.replace('。', '')
  words = words.replace('EOS', '')
  return words
  
# make simprification pair
def makeSimpPair():
  ''

# make cardinal sentence for interpretation  
def makeCardinalSentence(word):
  count = 0
  pos_dict = OrderedDict()
  mecab = MeCab.Tagger('-Ochasen')
  word = removeDisusedWord(word)
  word_list = mecab.parse(word).split('\n')
  for word in word_list:
    count += 1
    lists = word.split('\t')
    if len(lists) == 6:
      for i in lists:
        pos_dict[lists[0] ] = re.sub(r'-.*', '', lists[3]) 
  candidacy = extractCandidacy(pos_dict)
  return candidacy
  
  
# make dict reverse
def reverseDict(ordered_dict):
  num = len(ordered_dict)
  reverse_dict = OrderedDict()
  for i in range(0, num):
    word = ordered_dict.popitem()
    reverse_dict[word[0] ] = word[1]
  return reverse_dict
    
    
# extract candidacy for cardinal sentence
def extractCandidacy(dict_pos):
  num = len(dict_pos)
  candidacy = ''
  for i in range(0, num):
    word = dict_pos.popitem()
    if word[1] == '名詞':
      candidacy = word[0]
      break
  
  return candidacy

if __name__ == '__main__':

  # all file in directory
  #dict_names = glob.glob('../testdict/*')
  dict_names = glob.glob('../GSK/corpus/dict01/01/*')
  # difficulty 
  int_list = ['1', '2']
  # load JLPT to dictionaly
  jlpt_file = open(sys.argv[1], 'r')
  jlpt_dict = loadJLPT(jlpt_file)
  
  
  
  # all dict-file 
  for name in dict_names:
    #candidate word
    candidate_word = list()
    # open dict file
    dict_file = open(name, 'r')
    # make soup
    soup = BeautifulSoup(dict_file)

    # <orth> word </orth>: extract word
    orth = pickOutTag(soup, 'orth')
    if orth == 'error':
      orth = pickOutTag(soup, 'hd')
    print orth, name
'''
    # if exist orth in JLPT
    if orth in jlpt_dict:
    
      # if difficulty of word is '1' or '2'
      if jlpt_dict[orth] in int_list :
      
        # <su> interpretation </su>: extract interpretation
        su_list = pickOutTagAll(soup, 'su')
        
        #　extract simplification pair
        for su in su_list:
          candidate_word.append(makeCardinalSentence(su) )
        print 
    
      # append simplification pair
    # else next word
  
'''  