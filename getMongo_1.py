import cnfOperations as cnf
import pymongo
import pandas as pd
import numpy as np


class GetMongo():
    @staticmethod
    def get_value_mongo():
        myclient = pymongo.MongoClient(cnf.cnfOperation.readMongoDb())
        mydb = myclient[cnf.cnfOperation.readMy_Db()]
        mycol = mydb[cnf.cnfOperation.readMy_Col_1()]
        mydoc_all = mycol.find()
        df = pd.DataFrame(list(mydoc_all))
        df['Temp'] = df['Temp'].astype(np.float64)
        return df
