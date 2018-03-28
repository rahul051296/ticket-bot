from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from details import getTicketStatus, getCustomerDetails, getOrderDetails, getGoogleResult


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
        ticketId = int(tracker.get_slot('tId'))
        message = getTicketStatus(ticketId)
        dispatcher.utter_message(message)
        return [SlotSet('tId', None)]


class GetOrderDetails(Action):
    def name(self):
        return 'utter_order_details'

    def run(self, dispatcher, tracker, domain):
        orderId = int(tracker.get_slot('orderId'))
        message = getOrderDetails(orderId)
        dispatcher.utter_message(message)
        return [SlotSet('orderId', None)]


class GetRandomQuery(Action):
    def name(self):
        return 'utter_random_query'

    def run(self, dispatcher, tracker, domain):
        query = str(tracker.get_slot('query'))
        message = getGoogleResult(query)
        dispatcher.utter_message(message)
        return [SlotSet('query', tracker.get_slot('query'))]
