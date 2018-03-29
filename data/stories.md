## story 01
* greet
    - utter_greet
    - utter_wish

## story 02
* goodbye
    - utter_goodbye
    
## story 03
* greet
    - utter_greet
    - utter_wish
* goodbye
    - utter_goodbye
    
## story 04
*inform
    - utter_inform
*ticket[tId=234]
    - slot{"tId":"234"}
    - utter_ticket_details
*order_details[orderId=14]
    - slot{"orderId":"14"}
    - utter_order_details
*customer_details[userId=ae1246feb23]
    - slot{"userId":"ae1246feb23"}
    - utter_customer_details
    
## story 05    
*order_details
    -  utter_ask_orderId
*order_details[orderId=14]
    - slot{"orderId":"14"}
    - utter_order_details
*customer_details
    - utter_ask_userId
*customer_details[userId=ae1246feb23]
    - slot{"userId":"ae1246feb23"}
    - utter_customer_details
*ticket
    - utter_ask_tid
*ticket[tId=234]
    - slot{"tId":"234"}
    - utter_ticket_details

## Generated Story -140704532190416742
* greet
    - utter_greet
    - utter_wish
* alright
    - utter_alright
    - utter_help
* what_can_do
    - utter_what_can_do
* personal
    - utter_personal
* what_doing
    - utter_what_doing
* goodbye
    - utter_goodbye
    - export    

## full story 06
* greet
    - utter_greet
    - utter_wish
*formality
    - utter_formality
    - utter_help
*alright
    - utter_alright
    - utter_help
*personal
    - utter_personal
*what_doing
    - utter_what_doing
*what_can_do
    - utter_what_can_do
*inform
    - utter_inform
*ticket
    - utter_ask_tid
*ticket[tId=234]
    - slot{"tId":"234"}
    - utter_ticket_details
*order_details
    -  utter_ask_orderId
*order_details[orderId=14]
    - slot{"orderId":"14"}
    - utter_order_details
*customer_details
    - utter_ask_userId
*customer_details[userId=ae1246feb23]
    - slot{"userId":"ae1246feb23"}
    - utter_customer_details
*alright
    - utter_alright
* goodbye
    - utter_goodbye
    
## Generated Story -4232465529050964925
* greet
    - utter_greet
    - utter_wish
* formality
    - utter_formality
    - utter_help
* personal
    - utter_personal
* what_can_do
    - utter_what_can_do
* what_doing
    - utter_what_doing
* inform
    - utter_inform
* ticket
    - utter_ask_tid
* ticket{"tId": "234"}
    - slot{"tId": "234"}
    - utter_ticket_details
    - slot{"tId": null}
* order_details
    - utter_ask_orderId
* order_details{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
* customer_details
    - utter_ask_userId
* greet{"userId": "ae1246feb23"}
    - slot{"userId": "ae1246feb23"}
    - utter_customer_details
    - slot{"userId": "ae1246feb23"}
* alright
    - utter_alright
* goodbye
    - utter_goodbye
    - export


## Generated Story -6387244784396528377
* greet
    - utter_greet
    - utter_wish
* formality
    - utter_formality
    - utter_help
* inform
    - utter_inform
* customer_details
    - utter_ask_userId
* greet{"userId": "ae1246feb23"}
    - slot{"userId": "ae1246feb23"}
    - utter_customer_details
    - slot{"userId": "ae1246feb23"}
* ticket
    - utter_ask_tid
* ticket{"tId": "66"}
    - slot{"tId": "66"}
    - utter_ticket_details
    - slot{"tId": null}
* order_details
    - utter_ask_orderId
* order_details{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
* alright
    - utter_alright
* goodbye
    - utter_goodbye
    - export

## Generated Story -4187621466367840145
* personal
    - utter_personal
* what_can_do
    - utter_what_can_do
* inform
    - utter_inform
* order_details
    - utter_ask_orderId
* order_details{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
* ticket
    - utter_ask_tid
* ticket{"tId": "234"}
    - slot{"tId": "234"}
    - utter_ticket_details
    - slot{"tId": null}
* google_search{"query": "time right now?"}
    - slot{"query": "time right now?"}
    - utter_google_search
    - slot{"query": null}
* customer_details{"userId": "ae1246feb23"}
    - slot{"userId": "ae1246feb23"}
    - utter_customer_details
    - slot{"userId": "ae1246feb23"}
* goodbye
    - utter_goodbye
    - export
## Generated Story 6518969113481579838
* greet
    - utter_greet
    - utter_wish
* ticket{"query": "know my ticket status"}
    - slot{"query": "know my ticket status"}
    - utter_ask_tid
* ticket{"orderId": "234"}
    - slot{"orderId": "234"}
    - utter_ticket_details
    - slot{"tId": null}
* order_details
    - utter_ask_orderId
* order_details{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
    - slot{"orderId": null}
* goodbye
    - utter_goodbye
    - export
## Generated Story -6310372898247009718
* greet
    - utter_greet
    - utter_wish
* alright
    - utter_alright
    - utter_help
* ticket{"tId": "234"}
    - slot{"tId": "234"}
    - utter_ticket_details
    - slot{"tId": null}
* ticket{"tId": "66"}
    - slot{"tId": "66"}
    - utter_ticket_details
    - slot{"tId": null}
* order_details{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
    - slot{"orderId": null}
* ticket{"tId": "66"}
    - slot{"tId": "66"}
    - utter_ticket_details
    - slot{"tId": null}
* customer_details{"userId": "ae1246feb23"}
    - slot{"userId": "ae1246feb23"}
    - utter_customer_details
    - slot{"userId": "ae1246feb23"}
* alright
    - utter_alright
* goodbye
    - utter_goodbye
    - export
## Generated Story -2992657373646789301
* greet
    - utter_greet
    - utter_wish
* formality
    - utter_formality
    - utter_help
* ticket
    - utter_ask_tid
* ticket{"orderId": "234"}
    - slot{"orderId": "234"}
    - utter_ticket_details
    - slot{"tId": null}
    - export
## Generated Story 2865882562750618852
* order_details{"query": "know a order detail"}
    - slot{"query": "know a order detail"}
    - utter_ask_orderId
* goodbye{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
    - slot{"orderId": null}
    - export
## Generated Story 8090788600899997824
* greet
    - utter_greet
    - utter_wish
* order_details{"orderId": "14"}
    - slot{"orderId": "14"}
    - utter_order_details
    - slot{"orderId": null}
* alright
    - utter_alright
* goodbye
    - utter_goodbye
    - export
## Generated Story 3852445592793712920
* ticket
    - utter_ask_tid
* ticket{"orderId": "234"}
    - slot{"orderId": "234"}
    - utter_ticket_details
    - slot{"tId": null}
* ticket{"orderId": "66"}
    - slot{"orderId": "66"}
    - utter_ticket_details
    - slot{"tId": null}
    - export
