from pymongo import MongoClient

MONGO_DB_URL = "mongodb://Guru99:password@localhost:27017/?authSource=shortener&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
#"mongodb://fmtest:fmADC12#Test@localhost:27020/test?authSource=admin"
#"mongodb://Guru99:password@localhost:27017/?authSource=shortener&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"


class Mongo_connection:
    def __init__(self):
        self.__mongo_client = MongoClient(MONGO_DB_URL)

    def get_database_collection(self,db_name="test", collection="People_v2"):
        self.db = self.__mongo_client[db_name]
        self.collection = self.db[collection]
        return self.collection

    """
    def update_ids(self,item_type,process_ids):
    # def update_ids(*args):
        # print(*args)
        item_collection={
        "movie":IVA_MOVIES_COLLECTION,
        "show":IVA_SHOWS_V1_COLLECTION,
        "person":IVA_PEOPLE_COLLECTION,
        "season":IVA_SEASON_COLLECTION,
        "episode":IVA_EPISODE_V1_COLLECTION
        }
    
        collection=Mongo_connection().get_database_collection(db_name="iva",collection=item_collection[item_type])
        collection.update_many(filter={"Source.Id":{"$in":process_ids}},update= {"$set": {"is_schema_processed": True}})
    """