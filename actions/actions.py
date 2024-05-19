# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions




from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# from rasa import core
# from rasa.core.actions.action import Action
#import openai


class actionaddmedication(Action):
    def name(self) -> Text: 
        return "action_add_medication"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        medication = tracker.get_slot("add_medication")
        
        if not medication:
            response = "sorry! i did not get medication name"
        else:
            response = f"API called to add medication: {medication}"

        dispatcher.utter_message(text = response)
        
        return []
    
class actionmedicationname(Action):
    
    def name(self) -> Text:
        return "action_medication_name"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = "API called to list medication name"

        dispatcher.utter_message(text = response)
        
        return []
    
class actiondiseasedetails(Action):
    
    def name(self) -> Text:
        return "action_disease_details"
    
    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        disease = tracker.get_slot("about_diseases")
        
        response = f"API called to get {disease} details"

        dispatcher.utter_message(text = response)
        
        return []


# class OpenAIRequestAction(Action):

#     def __init__(self):
#         API_KEY = "sk-proj-bpuOX2JgxmLeYuZ1vMPrT3BlbkFJZZT8sUEApTIBsCHmGdN6"
#         openai.api_key = "API_KEY"

#     def run(self, dispatcher, tracker):

#         user_query = tracker.get_slot("user_query")
        
#         prompt = f"Here is a medical query from a user: {user_query}"
        
#         response = openai.Completion.create(
#             model = "gpt-4-turbo"
#             engine="text-davinci-003",
#             prompt=prompt,
#             max_tokens=1024,
#             n=1,
#             stop=None,
#             temperature=0.7,
#         )
        
#         openai_response = response.choices[0].text.strip()
       
#         dispatcher.utter_message(openai_response)
        
#         return core.ActionExecutionResult.success()
