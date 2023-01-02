import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3 (
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)

MODEL_ID1 = 'en-fr'

def englishtofrench(englishtext):
    if englishtext is None:
        return "Please enter text to be translated."

    temp = language_translator.translate(
        text=englishtext,
        model_id=MODEL_ID1).get_result()
    translation = temp['translations'][0]['translation']
    frenchtext = translation
    return frenchtext

MODEL_ID2 = 'fr-en'

def frenchtoenglish(frenchtext):
    if frenchtext is None:
        return "Please enter text to be translated."

    temp = language_translator.translate(
        text=frenchtext,
        model_id=MODEL_ID2).get_result()
    translation = temp['translations'][0]['translation']
    englishtext = translation
    return englishtext