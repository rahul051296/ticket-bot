from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from details import getTicketStatus, getCustomerDetails, getOrderDetails, getGoogleResult
from soup import  searchWeatherDetails, searchWordMeaning

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
        ticketId = str(tracker.get_slot('tId'))
        if ticketId == 'None':
            ticketId = str(tracker.get_slot('orderId'))
        message = getTicketStatus(ticketId)
        dispatcher.utter_message(message)
        return [SlotSet('tId', None)]


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




class searchWeather(Action):
    def name(self):
        return 'utter_weather_details'

    def run(self,dispatcher, tracker, domain):
        location_var = str(tracker.get_slot('location'))
        if location_var == 'None':
           dispatcher.utter_message('You will have to provide the location for me to get you the weather details  ')
        else:
            message = searchWeatherDetails(location_var)
            dispatcher.utter_message(message)
        return [SlotSet('location', tracker.get_slot('location'))]

class searchMeaning(Action):
    def name(self):
        return 'utter_word_meaning'

    def run(self,dispatcher, tracker, domain):
        word_var= str(tracker.get_slot('word'))
        if word_var == 'None':
            word_var = str(tracker.get_slot('word'))
        message = searchWordMeaning(Word_var)
        dispatcher.utter_message(message)
        return [SlotSet('word', tracker.get_slot('word'))]
