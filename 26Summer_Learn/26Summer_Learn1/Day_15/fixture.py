import pytest
from survey import AnonymousSurvey

@pytest.fixture
def name_survey():
    return AnonymousSurvey("What is your name?")

def test_single_survey(name_survey):
    name_survey.store_response("Lily")
    assert "Lily" in name_survey.responses

def test_multiple_survey(name_survey):
    responses = ["Lily", "John"]
    for response in responses:
        name_survey.store_response(response)
    for response in responses:
        assert response in name_survey.responses