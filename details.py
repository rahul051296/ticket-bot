import json


def getTicketStatus(ticketId):
    global response
    with open('tickets.json') as json_data:
        data = json.load(json_data)
        res = data.get('data')
        tickets = res.get('tickets')
        for t in tickets:
            if t.get('id') == ticketId:
                priorityName = t.get('priorityName')
                customerName = t.get('customerName')
                assignedTo = t.get('assignedTo')
                status = t.get('status')
                response = 'These are the ticket details \n Customer Name: {} \n Priority: {}\n Assigned To: {}\n ' \
                           'Status: {}'.format(customerName, priorityName, assignedTo, status)
                break
            else:
                response = 'Not Found'
        return response


def getPhone(name):
    global response
    with open('customer.json') as json_data:
        data = json.load(json_data)
        for d in data:
            if name.lower() in d.get("name").lower():
                response = d.get('phone')
                break
    return response
