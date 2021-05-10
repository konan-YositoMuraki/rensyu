import gzip
import xml.etree.ElementTree as ET

filename = '/Users/murakiyoshito/project/recommend/pubmed18n0360.xml.gz'  #'pubmed18n0360.xml.gz'

def open_by_suffix(filename):
    if filename.endswith('.gz'):
        return gzip.open(filename, 'rt',
                         encoding='utf-8')
    else:
        return open(filename, 'r',
                    encoding='utf-8')
with open_by_suffix(filename) as f:

    tree = ET.parse(f)
    #xmlファイルを一行ずつ読み込む
    for line in tree.iter():#tag = 'LastName''Title''ArticleTitle''Year''Affiliation''AbstractText'
        print(line.tag,line.attrib,line.text)