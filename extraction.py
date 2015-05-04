#coding: utf-8
#　'.*?'　で最短文字列の一致

# for process xml
from bs4 import BeautifulSoup
from xml.etree.ElementTree import *
import xml.etree.ElementTree as et
# import sys
import sys
# regular expression
import re


# pick out word between tag
def pickOutTag(soup, tag_name):
  # Tag of regular expression <'tag_name'**> 'word' </'tag_name'> 
  re_tag = re.compile('<' + tag_name + '("[^"]*\"|\'[^\']*\'|[^\'\">])*>(.*)</' + tag_name + '>')
  # convert to str
  words = soup.prettify().encode('utf-8')
  # turn off blank and line break
  words = words.replace(' ', '').replace('\n', '')
  # serch word
  match_word = re_tag.search(words)
  # process word
  if not match_word == None:
    word = re.sub(r'<("[^"]*\"|\'[^\']*\'|[^\'\">])*>', '', match_word.group(0) )
  else:
    word = 'error'
    
  return word

# pick out All interpretation between tag
def pickOutTagAll(soup, tag_name):
  # interpretation list
  interpretation_list = list()
  # Tag of regular expression 
  re_tag = re.compile('<' + tag_name + '[^<]*>.*?</'+ tag_name + '>')
  # convert to str
  words = soup.prettify().encode('utf-8')
  words = words.replace(' ', '').replace('\n', '')
  # find all interpretation
  match_words = re_tag.findall(words)
  
  # append interpretation to list
  if not match_words == []:
    for interpretation in match_words:
      interpretation_list.append(re.sub(r'<("[^"]*\"|\'[^\']*\'|[^\'\">])*>', '', interpretation) )      
  else:
    interpretation_list.append('error')
    
  return interpretation_list
  
if __name__ == '__main__':
  
  list_word = list()
  file =  open(sys.argv[1], 'r')

  soup = BeautifulSoup(file)

  # <hd> </hd> の中の見出し語の読みを抽出
  #hd = pickOutTag(soup , 'hd')
  #print hd
  # <orth> </orth> の中の見出し語を抽出
  orth = pickOutTag(soup, 'orth')
  print orth
  
  # <su> </su>  のなかの語釈文抽出
  su_list = pickOutTagAll(soup, 'su')
  for interpretation in su_list:
    print interpretation
    
  