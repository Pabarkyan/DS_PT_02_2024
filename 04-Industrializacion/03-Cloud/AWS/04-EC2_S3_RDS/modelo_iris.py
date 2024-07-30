import pymysql
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST_1')
username = os.getenv('USERNAME_1')
password = os.getenv('PASSWORD_1')
port = os.getenv('PORT_1')

db = pymysql.connect(host = host,
                     user = username,
                     password = password,
                     cursorclass = pymysql.cursors.DictCursor
)
# El objeto cursor es el que ejecutará las queries y devolverá los resultados

cursor = db.cursor()
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(user = username, pw = password, host = host, db = "iris"))

iris = pd.read_sql("SELECT * FROM iris.iris", con=engine)

X_iris = iris[["petal length (cm)", "petal width (cm)"]]
y_iris = iris['target']

tree_clf = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_clf.fit(X_iris, y_iris)

accuracy = accuracy_score(y_iris, tree_clf.predict(X_iris))
print(f"El accuracy es: {accuracy}")