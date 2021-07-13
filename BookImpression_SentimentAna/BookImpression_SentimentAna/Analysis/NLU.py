from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import *
from ibm_watson import NaturalLanguageUnderstandingV1

from tqdm import tqdm

# NLUの資格情報
nlu_credentials = {
    "apikey": "fRFNSVJsMV8DBJ43ewqXFbqWcPG_Aby6vd-KUgapLX5H",
    "url": "https://api.jp-tok.natural-language-understanding.watson.cloud.ibm.com/instances/80615145-3719-4826-aea3-a604d7e42cef"
}


# API呼び出し用インスタンスの生成
authenticator = IAMAuthenticator(nlu_credentials["apikey"])
nlu = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)
nlu.set_service_url(nlu_credentials['url'])


class NLU():

# text: 対象テキスト 
# feature : 機能を意味するObject
# key: 分析結果 json を filterするためのキー 

    def call_nlu(self, text, features, key):

      response = nlu.analyze (text=text, features=features).get_result()

      return response [key]


    def get_document(self, bookimp):

      bar = tqdm(total=len(bookimp))
      bar.set_description('解析中...')

      features = Features(sentiment=SentimentOptions())
      bookimp_doc = []

      for element in bookimp:
    
        try:
          bookimp_doc.append(self.call_nlu(element, features, "sentiment"))
          bar.update(1)
        except:
          bar.update(1)
          pass
  
      return bookimp_doc

    def get_score(self, document):

      bookimp_score = []
      for element in document:
    
        bookimp_score.append('{}'.format(element['document']['score']))

      return bookimp_score