
import csv
import random
from faker import Faker

fake = Faker()

#Header for the CSV file
header = ["name", "country", "IELTS", "TOEFL", "Duolingo","GRE", "Bachelors Degree", "Aggregate", "Backlogs", "Work experience in years", "LOR"]

# Options for the "Bachelors Degree" column
bachelors_degrees = ["Computer Science", "Electrical Engineering", "Civil Engineering", 
                     "Electronics and Communication", "Mechanical Engineering", "Information Technology"]

#Function to generate random data for each column
def generate_random_data():
    name = fake.name()
    country = fake.country()
    Ielts = round(random.uniform(5.0, 8.5) * 2) / 2  # IELTS scores are multiples of 5
    TOEFL = random.randint(80, 120)
    Duolingo = random.randint(80, 140)
    gre = random.ranInt(290,340)
    bachelors_degree = random.choice(bachelors_degrees)
    aggregate = round(random.uniform(6.0, 10)* 2)/2
    backlogs = random.randint(0, 5)
    work_experience = random.randint(0, 5)
    lor = random.randint(2,4)
    
    return [name, country, Ielts, TOEFL, Duolingo, gre, bachelors_degree, aggregate, backlogs, work_experience, lor]

# Generating and writing data to the CSV file
file_path = "dataval.csv"

with open(file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Writing the header
    writer.writerow(header)

    # Writing 1000 records
    for _ in range(1000):
        writer.writerow(generate_random_data())

print(f"CSV file generated successfully: {file_path}")
