import streamlit as st
import sqlite3
from openai import OpenAI
from PIL import Image
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API
base_url = "https://api.aimlapi.com/v1"
api_key = os.getenv('OPENAI_API_KEY')  # Fetches api key from .env file
api = OpenAI(api_key=api_key, base_url=base_url)

# Function to establish a connection to the SQLite database
def get_database_connection(db_name="university.db"):
    conn = sqlite3.connect(db_name)
    return conn

# Function to convert English prompt to SQL query using OpenAI API
def convert_prompt_to_sql(prompt):
    # Define the system prompt for SQL conversion
    system_prompt = (
        '''
        Convert queries to SQL queries. Return the SQL query as plain text without any code formatting. 
        The database has the following tables: STUDENT, INSTRUCTOR, COURSE, ENROLLMENT.
        '''
    )

    try:
        # Create chat completion request
        chat_completion = api.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.5,
            max_tokens=512,
        )
        
        # Retrieve the generated SQL query
        response_text = chat_completion.choices[0].message.content
        return response_text.strip()
    
    except Exception as e:
        st.error(f"An error occurred while converting prompt to SQL: {e}")
        return None

# Function to explain the SQL query
def explain_sql_query(sql_query):
    explanation_prompt = (
        '''
        Explain the following SQL query in simple terms:
        {}
        '''.format(sql_query)
    )

    try:
        # Create chat completion request for explanation
        chat_completion = api.chat.completions.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "system", "content": "Explain SQL queries."},
                {"role": "user", "content": explanation_prompt},
            ],
            temperature=0.7,
            max_tokens=512,
        )
        
        # Retrieve the explanation
        explanation_text = chat_completion.choices[0].message.content
        return explanation_text.strip()
    
    except Exception as e:
        st.error(f"An error occurred while explaining the SQL query: {e}")
        return None

# Function to execute the SQL query and return results
def execute_sql_query(query):
    conn = get_database_connection()
    try:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        return results
    except sqlite3.Error as e:
        st.error(f"An error occurred while executing the SQL query: {e}")
        return None
    finally:
        conn.close()


# Streamlit app UI
st.set_page_config(page_title="SQL Query Generator", layout="centered")

st.markdown("<h5 style='text-align: center;'>------------------------------------------------------------------------------------------------------------</h5>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>SQL Query Generator &nbsp; &nbsp; 🔤 → 📊</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; margin-bottom: 20px;'>---------------------------------------------------------------------------------------------------------</h5>", unsafe_allow_html=True)

st.markdown(
    '<h5 style="text-align: justify;">This tool allows you to generate an SQL query from an English language prompt and execute it on <span style="color: red;">\'university.db\'</span> &nbsp;database, along with an explanation of the query.</h5>',
    unsafe_allow_html=True
)

st.write(" ")

st.info("""
**About the Database:**

The database contains the following tables:

- **STUDENT**: Stores information about students. It has _student_id_, _name_, _gender_, _age_ and _email_.
- **INSTRUCTOR**: Stores data about the instructors, has _instructor_id_, _name_, _department_ and _email_.
- **COURSE**: Details about the _course_id_, _course_name_, _credits_ and the _instructor_id_ of the instructor handling the course are present.
- **ENROLLMENT**: Records of which students are enrolled in what courses. It has _enrollment_id_, _course_id_, _student_id_ and _grade_ achieved by the students information.

You can enter your query in English below, related to the information in the tables of the database, and it will be converted into an SQL query to retrieve the desired information.

The Entity-Relationship (ER) diagram which visually represents the database is shown below:
""")

# Adding an image
image = Image.open('/home/rakshith/sql_llm_app/er_dig.png')  # Replace with the correct image path or URL
st.image(image, caption='ER diagram of the database', use_column_width=True)

st.write("")


# User input for English query
st.markdown("<h5>Enter your prompt:</h5>", unsafe_allow_html=True)
prompt = st.text_input("(Explain celarly what you want to retrieve from the database)")

# Button to generate and execute SQL query
if st.button("Submit"):
    if prompt:
        # Convert the English prompt to SQL
        sql_query = convert_prompt_to_sql(prompt)
        
        if sql_query:
            st.success("SQL query generated!")  # Success statement for query generation
            st.markdown("<h5>Generated SQL Query:</h5>", unsafe_allow_html=True)
            st.code(sql_query)  # Display the generated SQL query

            # Execute the generated SQL query
            results = execute_sql_query(sql_query)

            # Display the results in a structured format
            if results is not None:
                st.success("SQL query executed!")  # Success statement for query execution
                st.markdown("<h5>Query Results::</h5>", unsafe_allow_html=True)
                st.dataframe(results)  # Use dataframe for better readability

                # Get explanation for the SQL query
                explanation = explain_sql_query(sql_query)
                if explanation:
                    st.success("Explanation generated!")
                    st.markdown("<h5>Explanation of the SQL Query:</h5>", unsafe_allow_html=True)
                    st.write(explanation)  # Display the explanation
                else:
                    st.write("Failed to generate explanation!.")
            else:
                st.write("No results found.")
        else:
            st.error("Failed to generate SQL query!")
    else:
        st.error("Please enter a prompt.")



# Signature at the bottom
st.markdown("""
    <style>
    .signature {
        position: fixed;
        bottom: 0;
        right: 10px;  /* Adjust this value to control distance from the right */
        font-size: 14px;
        color: grey;
    }
    </style>
    <div class="signature">
        Rakshith Ram C.A.
    </div>
""", unsafe_allow_html=True)

