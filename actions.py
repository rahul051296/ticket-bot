from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from details import getTicketStatus, getCustomerDetails, getOrderDetails
from soup import translateGoogle


class GetCustomerDetails(Action):
    def name(self):
        return 'utter_customer_details'

    def run(self, dispatcher, tracker, domain):
        message = "No user found"
        user = str(tracker.get_slot('userId'))
        response = getCustomerDetails(user)
        if response:
            message = response
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_message(message)
        return [SlotSet('userId', tracker.get_slot('userId'))]


class GetTicketDetails(Action):
    def name(self):
        return 'utter_ticket_details'

    def run(self, dispatcher, tracker, domain):
        ticketId = str(tracker.get_slot('ticketId'))
        if ticketId == 'None':
            ticketId = str(tracker.get_slot('orderId'))
        message = getTicketStatus(ticketId)
        dispatcher.utter_message(message)
        return [SlotSet('ticketId', None)]


class GetOrderDetails(Action):
    def name(self):
        return 'utter_order_details'

    def run(self, dispatcher, tracker, domain):
        orderId = str(tracker.get_slot('orderId'))
        if orderId == 'None':
            orderId = str(tracker.get_slot('tId'))
        message = getOrderDetails(orderId)
        dispatcher.utter_message(message)
        return [SlotSet('orderId', None)]


class GetTranslation(Action):
    def name(self):
        return 'utter_translate_data'

    def run(self, dispatcher, tracker, domain):
        word = str(tracker.get_slot('word'))
        language = str(tracker.get_slot('language'))
        if (word == 'None') or (language == 'None'):
            dispatcher.utter_message("You have to provide the word and language in order for me to translate")
        else:
            message = translateGoogle(word, language)
            dispatcher.utter_message(message)
            return [SlotSet('language', tracker.get_slot('language'))]
