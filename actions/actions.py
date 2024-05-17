# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
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

from rasa.core.actions.action import Action
from rasa import core

class AddMedicationsAction(Action):
    
    def run(self, dispatcher, tracker):
        medication_name = tracker.get_slot("medication_name")
        response = f"API called to add medication: {medication_name}"
        dispatcher.utter_message(response)
        return core.ActionExecutionResult.success()
    
class ListMedicationsAction(Action):
    
    def run(self, dispatcher, tracker):
        response = f"API called to list the medications names"
        dispatcher.utter_message(response)
        return core.ActionExecutionResult.success()
    
class AboutDiseasesAction(Action):
    
    def run(self, dispatcher, tracker):

        disease_name = tracker.get_slot("disease_name")
        response = f"API called to retrieve information about {disease_name}"
        dispatcher.utter_message(response)
        return core.ActionExecutionResult.success()

class NotifyMedicationTakenAction(Action):
    
    def run(self, dispatcher, tracker):
        medication_name = tracker.get_slot("medication_name")
        response = f"API called to record that {medication_name} is taken."
        dispatcher.utter_message(response)
        return core.ActionExecutionResult.success()