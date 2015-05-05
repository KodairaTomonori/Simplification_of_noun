#!/usr/bin/python
#coding: UTF-8
#日本語能力試験の基準語彙表を整頓
#置換作業（手作業）元ファイルのタブの連続に何か一文字を追加
#　　　　　　　　　、と・を//に変換
#               「と//が重複してあるところの調整
#                。の削除
#                -の削除
#                」の削除
#



import MeCab

def getPos(word):
  mecab = MeCab.Tagger()
  pos = mecab.parseToNode(word.encode('utf-8'))
  pos = pos.next
  pos = pos.feature
  pos = pos.split(',')
  return pos[0].decode('utf-8')

if __name__ == "__main__":
  import sys
  import codecs

  #file = open(sys.argv[1], "r")
  fin  = codecs.open('noryoku.txt', 'r', 'utf-16')
  fout = codecs.open('JLP.txt', 'w', 'utf-16')
  fout.write(u'表記\t読み\t級\t品詞\n')
  mecab = MeCab.Tagger()
  for line in fin:
    sentense = line.strip()
    words = sentense.split('\t')
    #表記
    word1 = words[3]
    #読み
    word0 = words[0]
    # 級
    word2 = words[1]
    #もし日本語じゃなかったら表記を読みに
    if ord(word1[0]) < 255:
      word1 = words[0]
          #print type(word1)
    
    #表記の品詞分類
    # 表記が２個、同じ読みである場合
    if "//" in word1:
      word3 = word1.split("//")
      for (w3, w0) in zip(word3, word0.split("//") ):
        pos = getPos(w3)
        
        fout.write(u'{0}\t{1}\t{2}\t{3}\n'.format(w3, w0, word2, pos ) )
        word1 = word3[0]
    # （　は表記につけてもつけなくてもいいやつ ex.　自立（する
    elif "(" in word1:
      word3 = word1.split("(")
      word0 = word0.split("(")
      pos = getPos(word3[0])
      fout.write(u'{0}\t{1}\t{2}\t{3}\n'.format(word3[0], word0[0], word2, pos) )
      pos = getPos("".join(word3))
      fout.write(u'{0}\t{1}\t{2}\t{3}\n'.format("".join(word3), "".join(word0), word2, pos) )
    elif u"「" in word1:
      word3 = word1.split(u"「")
      word0 = word0.split(u"「")
      fout.write(u'{0}\t{1}\t{2}\t{3}\n'.format(word3[0], word0[0], word2, pos) )
    else:
      wor = u'{0}\t{1}\t{2}\t{3}\n'.format(word1, word0, word2, pos)
      fout.write(wor)

