import psycopg

print("Testing PostgreSQL connection...")

try:
    connection = psycopg.connect(
        host="127.0.0.1",
        port=5433,
        dbname="pulse_db",
        user="pulse_user",
        password="pulse_local_test_2026"
    )

    print("CONNECTED SUCCESSFULLY!")
    connection.close()

except Exception as error:
    print("CONNECTION FAILED:")
    print(error)