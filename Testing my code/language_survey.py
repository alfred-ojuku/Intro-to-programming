from survey import AnonymousSurvey

#Define a question, and make a survey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#show the question and store the responses to the question
my_survey.show_question()
print("Enter q anytime to quit\n")
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

#show the survey results
print("\nThanks to those who participated in the event")
my_survey.show_response()
