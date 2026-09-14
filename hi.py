from sqlalchemy import create_engine,text

DATABASE_URL = "postgresql://neondb_owner:npg_xLM2sXzHu0vw@ep-delicate-art-b3tmxug6-pooler.c-4.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as conn:
        print("Connected!")

except Exception as e:
    print("ERROR:", e)
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            roll_no INTEGER
        )
    """))
    
    conn.commit()

print("Table created!")    
with engine.connect() as conn:
    conn.execute(
        text("""
            INSERT INTO students (name, roll_no)
            VALUES ('Ali', 101)
        """)
    )
    conn.commit()

print("Data inserted!")
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM students")
    )

    for row in result:
        print(row)