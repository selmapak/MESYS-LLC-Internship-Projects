import os
import random
import pandas as pd


random.seed(42)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# COUNTRIES

countries = {
    "Germany": {
        "Bavaria": ["Munich", "Augsburg", "Regensburg"],
        "North Rhine-Westphalia": ["Cologne", "Dusseldorf", "Bonn"],
        "Berlin-Brandenburg": ["Berlin", "Potsdam", "Cottbus"]
    },
    "France": {
        "Ile-de-France": ["Paris", "Versailles", "Nanterre"],
        "Auvergne-Rhone-Alpes": ["Lyon", "Grenoble", "Annecy"],
        "Provence-Alpes-Cote dAzur": ["Marseille", "Nice", "Toulon"]
    },
    "Spain": {
        "Catalonia": ["Barcelona", "Girona", "Tarragona"],
        "Madrid Region": ["Madrid", "Alcala", "Getafe"],
        "Andalusia": ["Seville", "Malaga", "Granada"]
    }
}

# SCHOOLS

schools = []
row_no = 1

for country, regions in countries.items():
    for region, cities in regions.items():
        for city in cities:
            for _ in range(3):
                schools.append([
                    country,
                    region,
                    city,
                    f"School_{row_no}",
                    random.choice([1, 5, 9]),
                    random.choice([4, 8, 12]),
                    random.randint(2, 4),
                    random.randint(15, 20),
                    random.randint(25, 35)
                ])
                row_no += 1

schools_df = pd.DataFrame(
    schools,
    columns=[
        "Country", "Region", "City", "School",
        "Start_Class", "Class_Count",
        "Max_Section", "Min_Students", "Max_Students"
    ]
)

schools_df.to_csv(
    os.path.join(OUTPUT_DIR, "Schools.csv"),
    index=False,
    encoding="utf-8",
    lineterminator="\n"
)

# STUDENTS & REGISTRATION

students = []
registrations = []
student_id = 1

for year in range(2015, 2024):
    for school in schools_df.itertuples(index=False):

        capacity = int(school.Class_Count * school.Max_Section * school.Max_Students)
        year_capacity = int(capacity * random.uniform(0.7, 1.3))

        total_slots = int(school.Class_Count * school.Max_Section)
        slots = [year_capacity // total_slots] * total_slots
        for i in range(year_capacity % total_slots):
            slots[i] += 1

        slot_index = 0

        for grade in range(
            int(school.Start_Class),
            int(school.Start_Class + school.Class_Count)
        ):
            for sec_no in range(1, int(school.Max_Section) + 1):
                section = chr(64 + sec_no)
                count = slots[slot_index]
                slot_index += 1

                for _ in range(count):
                    gender = random.choice(["M", "F"])

                    students.append([
                        student_id,
                        gender,
                        f"Name_{student_id}",
                        f"Surname_{student_id}"
                    ])

                    registrations.append([
                        school.School,
                        grade,
                        section,
                        student_id,
                        year,
                        1
                    ])
                    registrations.append([
                        school.School,
                        grade,
                        section,
                        student_id,
                        year,
                        2
                    ])

                    student_id += 1

students_df = pd.DataFrame(
    students,
    columns=["Student", "Gender", "Name", "LastName"]
)

registration_df = pd.DataFrame(
    registrations,
    columns=["School", "Class", "Section", "Student", "Year", "Semester"]
)

students_df.to_csv(
    os.path.join(OUTPUT_DIR, "Students.csv"),
    index=False,
    encoding="utf-8",
    lineterminator="\n"
)

registration_df.to_csv(
    os.path.join(OUTPUT_DIR, "SchoolRegistration.csv"),
    index=False,
    encoding="utf-8",
    lineterminator="\n"
)

# WITHDRAWALS

reasons = {
    "DroppedSchool": ["failed classes", "financial problems", "another reason"],
    "GoneToAnotherSchool": ["address change", "dislike the system", "have problems"]
}

withdrawals = []
withdraw_students_by_year = {year: set() for year in range(2015, 2024)}

for year in range(2015, 2024):
    students_year = registration_df[
        registration_df["Year"] == year
    ]["Student"].unique().tolist()

    withdraw_count = int(len(students_year) * random.uniform(0.03, 0.06))
    withdraw_students = random.sample(students_year, withdraw_count)

    for sid in withdraw_students:
        row = registration_df[
            (registration_df["Student"] == sid) &
            (registration_df["Year"] == year)
        ].iloc[0]

        main_reason = random.choice(list(reasons.keys()))
        detail = random.choice(reasons[main_reason])

        withdrawals.append([
            row["School"],
            int(row["Class"]),
            sid,
            year,
            "No School" if main_reason == "DroppedSchool" else "Another School",
            detail
        ])

        if year < 2023:
            withdraw_students_by_year[year + 1].add(sid)

withdrawals_df = pd.DataFrame(
    withdrawals,
    columns=["School", "Class", "Student", "Year", "toWhere", "Reason"]
)

withdrawals_df.to_csv(
    os.path.join(OUTPUT_DIR, "Withdrawals.csv"),
    index=False,
    encoding="utf-8",
    lineterminator="\n"
)

# REJECTED

rejected = []
rejected_student_id = student_id

for year in range(2015, 2024):
    for school in schools_df.itertuples(index=False):
        capacity = int(school.Class_Count * school.Max_Section * school.Max_Students)
        applications = int(capacity * random.uniform(1.05, 1.25))
        rejected_count = applications - capacity
        applied_class = int(school.Start_Class + school.Class_Count - 1)

        for _ in range(rejected_count):
            rejected.append([
                school.School,
                applied_class,
                rejected_student_id,
                year
            ])
            rejected_student_id += 1

rejected_df = pd.DataFrame(
    rejected,
    columns=["School", "Class", "Student Id", "Year"]
)

rejected_df.to_csv(
    os.path.join(OUTPUT_DIR, "Rejected.csv"),
    index=False,
    encoding="utf-8",
    lineterminator="\n"
)

# GRADUATES

graduates = []

for year in range(2015, 2024):
    withdrawn = withdraw_students_by_year[year]

    for school in schools_df.itertuples(index=False):
        last_class = int(school.Start_Class + school.Class_Count - 1)

        last_students = registration_df[
            (registration_df["School"] == school.School) &
            (registration_df["Class"] == last_class) &
            (registration_df["Year"] == year)
        ]["Student"].unique().tolist()

        for sid in last_students:
            if sid not in withdrawn:
                graduates.append([school.School, sid, year])

graduates_df = pd.DataFrame(
    graduates,
    columns=["School", "Student", "Year"]
)

graduates_df.to_csv(
    os.path.join(OUTPUT_DIR, "Graduates.csv"),
    index=False,
    encoding="utf-8",
    lineterminator="\n"
)
