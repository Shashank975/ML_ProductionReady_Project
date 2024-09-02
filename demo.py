# import os 
# mongo_db_url= os.getenv('MONGODB_URL')
# print(mongo_db_url)
from US_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()