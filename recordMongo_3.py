import cnfOperations as cnf
import pymongo
import listDict_3 as ld_3


class RecordMongo():
    @staticmethod
    def record_mongo():
        lst = ld_3.ListDict()
        myclient = pymongo.MongoClient(cnf.cnfOperation.readMongoDb())
        mydb = myclient[cnf.cnfOperation.readMy_Db()]

        mycol = mydb[cnf.cnfOperation.readMy_Col_3()]

        mycol.insert_many(lst.list_to_dict())

        documents = list(mycol.find({}, {'_id': 0}))
        res = [list(idx.values()) for idx in documents]

        for index1, row in enumerate(res):
            for index2, item in enumerate(row):
                try:
                    res[index1][index2] = (float(item))
                except ValueError:
                    pass
        return res
