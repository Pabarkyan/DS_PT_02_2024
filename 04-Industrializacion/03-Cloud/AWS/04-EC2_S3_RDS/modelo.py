# Utilizando sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
from sklearn.ensemble import RandomForestClassifier



port = 3306

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(user = username, 
                                                                        pw = password, 
                                                                        host = host, 
                                                                        db = "iris"))

dt = pd.read_sql("SELECT * FROM iris.iris", con=engine)

rf = RandomForestClassifier(random_state=43)
X = dt.drop("target", axis=1)
y = dt["target"]

rf.fit(X,y)
dt["prediction"] = rf.predict(X)

import boto3
from io import StringIO
session = boto3.Session()
s3 = session.client('s3')

csv_buffer = StringIO()
dt.to_csv(csv_buffer, index=False)
s3.put_object(Bucket="clase2007jgs", Key="iris.csv", Body=csv_buffer.getvalue())