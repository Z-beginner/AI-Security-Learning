from survey import AnonymousSurvey

def test_store_single_response():
    question = "What is your name?"
    name_survey = AnonymousSurvey(question)
    name_survey.store_response('Lily')
    assert "Lily" in name_survey.responses

def test_store_multiple_responses():
    question = "What is your name?"
    name_survey = AnonymousSurvey(question)
    responses = ["Lily", "John", "Doe"]
    for response in responses:
        name_survey.store_response(response)
    for response in responses:
        assert response in name_survey.responses