from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from details import getPhone, getTicketStatus


class GetResult(Action):
    def name(self):
       return 'get_result'

    def run(self, dispatcher, tracker, domain):
        p = str(tracker.get_slot('Priority'))
        if p == "p1":
            response = "P1 ticket is resolved"
        elif p == "p2":
            response = "P2 ticket is unresolved"
        elif p == "p3":
            response = "P3 ticket is being checked"
        else:
            response = "The ticket does not exist"
        dispatcher.utter_message(response)
        return [SlotSet('Priority', tracker.get_slot('Priority'))]


class GetCustomerPhone(Action):
    def name(self):
        return 'utter_phone'

    def run(self, dispatcher, tracker, domain):
        message = "No user found"
        user = str(tracker.get_slot('User'))
        response = getPhone(user)
        if response:
            message = response
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_message(message)
        return [SlotSet('User', tracker.get_slot('User'))]


class GetTicketDetails(Action):
    def name(self):
        return 'utter_ticket_details'

    def run(self, dispatcher, tracker, domain):
        ticketId = int(tracker.get_slot('tId'))
        message = getTicketStatus(ticketId)
        dispatcher.utter_message(message)
        return [SlotSet('tId', tracker.get_slot('tId'))]

