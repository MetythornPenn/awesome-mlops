from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/db")
def db_check():
    conn = psycopg2.connect("dbname=mydb user=myuser password=mypassword host=postgres")
    cur = conn.cursor()
    cur.execute("SELECT 1")
    return {"db": cur.fetchone()}
