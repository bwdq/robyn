NO_DB = """
    from robyn import Robyn

    app = Robyn(__file__)

    @app.get("/")
    def index():
        return "Hello World!"

    if __name__ == "__main__":
        app.start()
        """
POSTGRES = """
from robyn import Robyn
import psycopg2

app = Robyn(__file__)

@app.get("/")
def index():

    conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")

    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TEST (ID INT PRIMARY KEY NOT NULL);")
    conn.commit()
    conn.close()
    return "Hello World!"


if __name__ == "__main__":
    app.start()
"""
MONGO = """
from robyn import Robyn
from pymongo import MongoClient

app = Robyn(__file__)

# https://www.mongodb.com/languages/python

@app.get("/")
def index():
    dbname = get_database()
    collection_name = dbname["user_1_items"]
    item_1 = {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance"
    }

    item_2 = {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    }
    collection_name.insert_many([item_1, item_2])
    return "Hello World!"


if __name__ == "__main__":
    app.start()

def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']
"""
SQLITE = """
from robyn import Robyn
import sqlite3

app = Robyn(__file__)

@app.get("/")
def index():
    # your db name
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("CREATE TABLE test(column_1, column_2)")
    res = cur.execute("SELECT name FROM sqlite_master")
    th = res.fetchone()
    print(th)
    return "Hello World!"


if __name__ == "__main__":
    app.start()
"""
PRISMA = """
from robyn import Robyn
from prisma import Prisma
from prisma.models import User

app = Robyn(__file__)
prisma = Prisma(auto_register=True)


@app.startup_handler
async def startup_handler() -> None:
    await prisma.connect()


@app.shutdown_handler
async def shutdown_handler() -> None:
    if prisma.is_connected():
        await prisma.disconnect()


@app.get("/")
async def h():
    user = await User.prisma().create(
        data={
            "name": "Robert",
        },
    )
    return user.json(indent=2)

app.start(port=8080)
"""
SQLALCHEMY = """
from robyn import Robyn
"""
