import json

from soup import searchBingMeaning


def getTicketStatus(ticketId):
    global response
    with open('tickets.json') as json_data:
        data = json.load(json_data)
        res = data.get('data')
        tickets = res.get('tickets')
        for t in tickets:
            if t.get('id') == int(ticketId):
                priorityName = t.get('priorityName')
                customerName = t.get('customerName')
                customerId = t.get('customerId')
                assignedTo = t.get('assignedTo')
                status = t.get('status')
                response = 'These are the ticket details <br> <b>Customer Name:</b> {} <br><b>Customer Id:</b> {} <br><b>Priority:</b> {}<br><b> Assigned To:</b> {}<br><b> Status:</b> {}'.format(customerName, customerId, priorityName, assignedTo, status)
                break
            else:
                response = 'Not Found'
        return response


def getCustomerDetails(userId):
    global response
    with open('customer.json') as json_data:
        data = json.load(json_data)
        for d in data:
            if userId == d.get("_id"):
                name = d.get('name')
                phone = d.get('phone')
                email = d.get('email')
                address = d.get('address')
                response = "These are the customer details <br><b>Name</b>: {}<br><b>Phone:</b> {}<br><b>Email:</b> {}<br><b>Address:</b> {}".format(name, phone, email, address)
                break
    return response


def getOrderDetails(orderId):
    with open('orders.json') as json_data:
        res = json.load(json_data)
        data = res.get('data')
        partner_order_details = data.get('partner_order_details')
        orderDetail = partner_order_details[0].get('orderDetail')
        if int(orderId) == partner_order_details[0].get('orderId'):
            result = "The customer has ordered the following"
            for od in orderDetail:
                result += " <br>\n <b>" + od.get('name') + ":</b> " + str(od.get('quantity'))
        else:
            result = "The order id does not exist."
        return result


def getGoogleResult(query):
    result = "I was not able to understand your question.. <br>This is what I found on the web for <i>'{}'</i> <br> <a href='https://www.google.co.in/search?q={}' target='_blank'>Click Here</a>".format(query,query)
    return result


def getMeaning(query):
    meaning = searchBingMeaning(query)
    return meaning


if __name__ == '__main__':
    print(getMeaning("wire"))
