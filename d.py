import pymongo


mongodb = pymongo.MongoClient("mongodb+srv://huitzoo:halo1603@ttarritmiasf-5bevl.mongodb.net/TTarritmiasF?retryWrites=true&w=majority")
collection = mongodb.arrhytmias.comments


content = {
    "ok":"false",
    "comment":"d"
}

collection.insert_one(content)