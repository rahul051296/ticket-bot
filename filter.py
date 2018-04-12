def addData(nlu_dir, value):
        text = value.get('text')
        entities = value.get('entities')
        textSplit = text.split()
        for entity in entities:
            textSplit = [txt.replace(entity.get('entityValue'), "[{}]({})".format(entity.get('entityValue'), entity.get('entity'))) for txt in textSplit]
        value = " ".join(textSplit)
        with open(nlu_dir, "a+") as data:
            if data.write("\n- {}".format(value)):
                print("Successfully added {} into {}".format(value, data.name))
            else:
                print("Failed to add {} into {}".format(value, data.name))


def intentStatus(message, intent):
    addData(("./data/nlu/" + intent + ".md"), message)


if __name__ == '__main__':
    intentStatus({'text': 'what about coimbatore', 'entities': [{'entity': 'location', 'entityValue': 'coimbatore'}]}, "weather_details")
