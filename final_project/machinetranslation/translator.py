import json 
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
url = 'REhiCUdRa-pQuK-TjDRzIAptPu-fAQzsr6b-ZmAjxm7L'
apikey = 'https://api.jp-tok.language-translator.watson.cloud.ibm.com/instances/fe588435-d34e-4e98-93f4-3f9e2eaa01fe'



authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    # print(translation)
    return translation['translations'][0]['translation']


def frenchToEnglish(frenchText):
    #write the code here
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    # print(translation)
    return translation['translations'][0]['translation']

