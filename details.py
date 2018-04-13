import json


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
                response = 'These are the ticket details <br> <b>Customer Name:</b> {}. <br><b>Customer ID:</b> {}. <br><b>Priority:</b> {}. <br><b> Assigned To:</b> {}. <br><b> Status:</b> {}.'.format(customerName, customerId, priorityName, assignedTo, status)
                break
            else:
                response = "None"
        return response


def getCustomerDetails(customerId):
    global response
    with open('customer.json') as json_data:
        data = json.load(json_data)
        for d in data:
            if customerId == d.get("_id"):
                name = d.get('name')
                phone = d.get('phone')
                email = d.get('email')
                address = d.get('address')
                response = "These are the customer details <br><b>Name</b>: {}. <br><b>Phone:</b> {}. <br><b>Email:</b> {}. <br><b>Address:</b> {}.".format(name, phone, email, address)
                break
            else:
                response = "None"
    return response


def getOrderDetails(orderId):
    with open('orders.json') as json_data:
        res = json.load(json_data)
        data = res.get('data')
        partner_order_details = data.get('partner_order_details')
        orderDetail = partner_order_details[0].get('orderDetail')
        if int(orderId) == partner_order_details[0].get('orderId'):
            response = "The customer has ordered the following"
            for od in orderDetail:
                response += " <br>\n <b>" + od.get('name') + ":</b> " + str(od.get('quantity'))
        else:
            response = "The order id does not exist."
        return response


if __name__ == '__main__':
    pass
