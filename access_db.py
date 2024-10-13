import sqlite3

def get_database_connection(db_file):
    """Connect to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_tables_and_columns(conn):
    """Retrieve and display all tables and their columns."""
    try:
        cursor = conn.cursor()

        # Get the list of tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("Tables and their columns:\n")
            for table in tables:
                table_name = table[0]
                print(f"Table: {table_name}")

                # Retrieve the columns for each table
                cursor.execute(f"PRAGMA table_info({table_name});")
                columns = cursor.fetchall()

                if columns:
                    print("Columns:")
                    for column in columns:
                        print(f"- {column[1]} ({column[2]})")
                else:
                    print("No columns found.")
                print("\n" + "-"*30 + "\n")
        else:
            print("No tables found in the database.")

    except sqlite3.Error as e:
        print(f"Error retrieving tables/columns: {e}")

    finally:
        cursor.close()

def main(db_file):
    """Main function to display tables and columns."""
    conn = get_database_connection(db_file)
    if conn:
        get_tables_and_columns(conn)
        conn.close()

# Example usage
if __name__ == "__main__":
    db_file = "university.db"  # Replace with your .sql file path
    main(db_file)
