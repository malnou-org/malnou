import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions

def watsonNLU(versionID, apiKey, apiURL, model_id, Text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version = versionID,
        iam_apikey = apiKey,
        url = apiURL)

    response = natural_language_understanding.analyze(
        text = Text,
        features=Features(
            concepts=ConceptsOptions(limit=50),
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=50, model=model_id),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                    limit=50))).get_result()

    return response