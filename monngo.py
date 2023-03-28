if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")

    db = client['CodeDB']
    collection = db['codecollection']
    print("data base creation successful")

    document1 = [{'_id': 1,
                  'title': 'sleep',
                  'import': 'from rails.dsl.components.power.PowerSleepStateComponent import PowerSleepStateComponent',
                  'component': 'PowerSleepStateComponent',
                  'code': ['def verifysleep():',
                           '    if self._powerSleepStateComponent.isS3Enabled()']
                  },
                 {'_id': 2,
                  'title': 'wake',
                  'import': 'from rails.dsl.components.power.PowerWakeStateComponent import PowerWakeStateComponent',
                  'component': 'PowerWakeStateComponent',
                  'code': ['def verifywake():',
                           '    if self._powerWakeStateComponent.isS3Enabled()']},
                 {'_id': 3,
                  'title': 'shutdown',
                  'import': 'from rails.dsl.components.power.PowerStateComponent import PowerStateComponent',
                  'component': 'shutdownComponent',
                  'code': ['def putshutdown():',
                           '    if self._PowerStateComponent.shutdown']},
                 ]
    #var = input("enter the component ")
    #collection.insert_many(document1)
    var = "wake"
    impdocu = collection.find({'title': 'wake'}, {'code': 0, 'component': 0, '_id': 0, 'title': 0})

    compdocu = collection.find({'title': 'wake'}, {'code': 0, 'import': 0, '_id': 0, 'title': 0})
    codedocu = collection.find({'title': 'wake'}, {'component': 0, 'import': 0, '_id': 0, 'title': 0})
    #{Name: {$ in:["Chris", "Bob"]}}, {Age: 0, _id: 0})

    for item in impdocu:
        print("import", item)
    for item in compdocu:
        print("component", item)
    for item in codedocu:
        print("code", item)
