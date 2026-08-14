from survey import AnonymousSurvey

question = "What is your name?"
name_survey = AnonymousSurvey(question)
name_survey.show_question()
print("input 'q' to quit\n")
while True:
    new_question = input()
    if new_question == "q":
        break
    else:
        name_survey.store_response(new_question)
print("Survey finished")
name_survey.show_results()
