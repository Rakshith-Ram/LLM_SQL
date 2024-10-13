import sqlite3
import random
import os

# Function to create the database and insert sample data
def create_complex_database(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Create STUDENT table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS STUDENT (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            email TEXT UNIQUE
        )
    """)

    # Create INSTRUCTOR table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS INSTRUCTOR (
            instructor_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            email TEXT UNIQUE
        )
    """)

    # Create COURSE table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COURSE (
            course_id TEXT PRIMARY KEY,
            course_name TEXT NOT NULL,
            credits INTEGER,
            instructor_id TEXT,
            FOREIGN KEY (instructor_id) REFERENCES INSTRUCTOR(instructor_id)
        )
    """)

    # Create ENROLLMENT table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ENROLLMENT (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            course_id TEXT,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES STUDENT(student_id),
            FOREIGN KEY (course_id) REFERENCES COURSE(course_id)
        )
    """)

    # Insert sample data into STUDENT
    students = [
        ('S001', 'Aarav Patel', 20, 'Male', 'aarav.patel@university.edu.in'),
        ('S002', 'Meera Sharma', 21, 'Female', 'meera.sharma@university.edu.in'),
        ('S003', 'Ravi Kumar', 22, 'Male', 'ravi.kumar@university.edu.in'),
        ('S004', 'Ananya Iyer', 19, 'Female', 'ananya.iyer@university.edu.in'),
        ('S005', 'Karan Singh', 22, 'Male', 'karan.singh@university.edu.in'),
        ('S006', 'Neha Reddy', 21, 'Female', 'neha.reddy@university.edu.in'),
        ('S007', 'Vikram Desai', 23, 'Male', 'vikram.desai@university.edu.in'),
        ('S008', 'Pooja Menon', 20, 'Female', 'pooja.menon@university.edu.in'),
        ('S009', 'Aditi Barua', 22, 'Female', 'aditi.barua@university.edu.in'),
        ('S010', 'Devang Ghosh', 21, 'Male', 'devang.ghosh@university.edu.in'),
        ('S011', 'Rohan Banerjee', 20, 'Male', 'rohan.banerjee@university.edu.in'),
        ('S012', 'Priya Nair', 22, 'Female', 'priya.nair@university.edu.in'),
        ('S013', 'Kunal Bhatt', 23, 'Male', 'kunal.bhatt@university.edu.in'),
        ('S014', 'Sanya Kapoor', 19, 'Female', 'sanya.kapoor@university.edu.in'),
        ('S015', 'Harshad Shetty', 22, 'Male', 'harshad.shetty@university.edu.in'),
        ('S016', 'Reena Gupta', 20, 'Female', 'reena.gupta@university.edu.in'),
        ('S017', 'Farhan Ahmed', 21, 'Male', 'farhan.ahmed@university.edu.in'),
        ('S018', 'Tanvi Deshmukh', 22, 'Female', 'tanvi.deshmukh@university.edu.in'),
        ('S019', 'Yashwant Mahato', 23, 'Male', 'yashwant.mahato@university.edu.in'),
        ('S020', 'Shruti Rai', 21, 'Female', 'shruti.rai@university.edu.in'),
        ('S021', 'Akash Thakur', 20, 'Male', 'akash.thakur@university.edu.in'),
        ('S022', 'Lakshmi Viswanathan', 21, 'Female', 'lakshmi.viswanathan@university.edu.in'),
        ('S023', 'Gurpreet Kaur', 22, 'Female', 'gurpreet.kaur@university.edu.in'),
        ('S024', 'Aditya Joshi', 23, 'Male', 'aditya.joshi@university.edu.in'),
        ('S025', 'Nandita Dey', 20, 'Female', 'nandita.dey@university.edu.in'),
        ('S026', 'Shubham Shinde', 22, 'Male', 'shubham.shinde@university.edu.in'),
        ('S027', 'Pallavi Mishra', 21, 'Female', 'pallavi.mishra@university.edu.in'),
        ('S028', 'Ramesh Gowda', 23, 'Male', 'ramesh.gowda@university.edu.in'),
        ('S029', 'Isha Sinha', 22, 'Female', 'isha.sinha@university.edu.in'),
        ('S030', 'Nikhil Rao', 20, 'Male', 'nikhil.rao@university.edu.in'),
        ('S031', 'Salman Sheikh', 21, 'Male', 'salman.sheikh@university.edu.in'),
        ('S032', 'Sneha Khanna', 20, 'Female', 'sneha.khanna@university.edu.in'),
        ('S033', 'Aniket Mehta', 22, 'Male', 'aniket.mehta@university.edu.in'),
        ('S034', 'Kavita Yadav', 21, 'Female', 'kavita.yadav@university.edu.in'),
        ('S035', 'Rajeshwari Pillai', 23, 'Female', 'rajeshwari.pillai@university.edu.in'),
        ('S036', 'Manoj Tripathi', 21, 'Male', 'manoj.tripathi@university.edu.in'),
        ('S037', 'Vijay Kannan', 22, 'Male', 'vijay.kannan@university.edu.in'),
        ('S038', 'Sonali Choudhury', 20, 'Female', 'sonali.choudhury@university.edu.in'),
        ('S039', 'Deepak Jain', 23, 'Male', 'deepak.jain@university.edu.in'),
        ('S040', 'Bhavya Agarwal', 22, 'Female', 'bhavya.agarwal@university.edu.in'),
        ('S041', 'Alok Sharma', 20, 'Male', 'alok.sharma@university.edu.in'),
        ('S042', 'Divya Prasad', 21, 'Female', 'divya.prasad@university.edu.in'),
        ('S043', 'Rahul Srivastava', 22, 'Male', 'rahul.srivastava@university.edu.in'),
        ('S044', 'Srishti Khatri', 23, 'Female', 'srishti.khatri@university.edu.in'),
        ('S045', 'Mohit Verma', 21, 'Male', 'mohit.verma@university.edu.in'),
        ('S046', 'Anusha Kulkarni', 22, 'Female', 'anusha.kulkarni@university.edu.in'),
        ('S047', 'Tushar Roy', 23, 'Male', 'tushar.roy@university.edu.in'),
        ('S048', 'Nisha Pawar', 21, 'Female', 'nisha.pawar@university.edu.in'),
        ('S049', 'Vishal Dixit', 22, 'Male', 'vishal.dixit@university.edu.in'),
        ('S050', 'Chaitra Hegde', 20, 'Female', 'chaitra.hegde@university.edu.in')]


    cur.executemany("INSERT INTO STUDENT (student_id, name, age, gender, email) VALUES (?, ?, ?, ?, ?)", students)

    # Insert sample data into INSTRUCTOR
    instructors = [
        ('I01', 'Dr. Anjali Joshi', 'Computer Science', 'anjali.joshi@university.edu.in'),
        ('I02', 'Prof. Ramesh Kumar', 'Mathematics', 'ramesh.kumar@university.edu.in'),
        ('I03', 'Dr. Kavita Mehta', 'Electronics', 'kavita.mehta@university.edu.in'),
        ('I04', 'Prof. Arjun Rao', 'Mechanical Engineering', 'arjun.rao@university.edu.in'),
        ('I05', 'Dr. Neha Shetty', 'Physics', 'neha.shetty@university.edu.in')
    ]
    cur.executemany("INSERT INTO INSTRUCTOR (instructor_id, name, department, email) VALUES (?, ?, ?, ?)", instructors)

    # Insert sample data into COURSE
    courses = [
        ('C01', 'Data Structures', 3, 'I01'),
        ('C02', 'Control Systems', 3, 'I03'),
        ('C03', 'Calculus', 4, 'I02'),
        ('C04', 'Digital Circuits', 4, 'I03'),
        ('C05', 'Fluid Mechanics', 3, 'I04'),
        ('C06', 'Operating Systems', 3, 'I01'),
        ('C07', 'Machine Design', 4, 'I04'),
        ('C08', 'Quantum Physics', 4, 'I05'),
        ('C09', 'Linear Algebra', 3, 'I02'),
        ('C10', 'Machine Learning', 4, 'I01')
    ]
    cur.executemany("INSERT INTO COURSE (course_id, course_name, credits, instructor_id) VALUES (?, ?, ?, ?)", courses)

    # Insert sample data into ENROLLMENT
    grades = ['A', 'B', 'C', 'D', 'E', 'F']
    enrollments = [
        ('S' + str(random.randint(1, 50)).zfill(3), 'C' + str(random.randint(1, 10)).zfill(2), random.choice(grades))
        for _ in range(200)
    ]
    cur.executemany("INSERT INTO ENROLLMENT (student_id, course_id, grade) VALUES (?, ?, ?)", enrollments)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Create the complex database

    db_name = "university.db"

    if os.path.exists(db_name):
        print(f"Warning: The database '{db_name}' already exists.")
        exit()
    else:
        create_complex_database(db_name)
        print("Database created with sample data.")
