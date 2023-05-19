import dotenv, os
from pprint import pprint
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson import ObjectId

print('Last ran on utc time: ' + str(datetime.utcnow()))

# pymongo connection
mongo_client = MongoClient('mongodb://uxcamv3:9xJNhXR4cW4qtwtq@10.0.99.208:27017/uxcamv3')
mongo_db = mongo_client['uxcamv3']

print('connection compelete')

def get_all_appids():
    result = mongo_db['app'].find({
        'sdkIntegration.status': True
    },
        {'_id': 1}
    )
    return [str(i['_id']) for i in result]

def delete_app_data(app_id):
    # delete from session_<appid>
    result = mongo_db['session_' + app_id].drop()
    print('deleted from session')
    # delete from appUser<appid>
    result = mongo_db['appUser_' + app_id].drop()
    print('deleted from appuser')

def remove_unindexed_data():
    details = {}
    # get all the collections
    collection_names = mongo_db.list_collection_names()
    for col in collection_names:
        # if len(col) == 32:
        #     if col.startswith('session_') or col.startswith('appUser_'):
        #         print(col)
        #         mongo_db[col].drop()
        print(col)
        print(mongo_db[str(col)].stats(1024*1024*1024))

def main():
    appids = get_all_appids()
    l = len(appids)
    for n, appid in enumerate(appids):
        print(str(n+1) + '/' + str(l) + ': ' + appid)
        delete_app_data(appid)


if __name__ == '__main__':
    # print(get_all_appids())
    # main()
    remove_unindexed_data()




