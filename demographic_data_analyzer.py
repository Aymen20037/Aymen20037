import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. How many people of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    total = df.shape[0]
    bachelors_count = df[df["education"] == "Bachelors"].shape[0]
    percentage_bachelors = round((bachelors_count / total) * 100, 1)

    # 4 & 5. Advanced education vs non-advanced education salaries
    advanced_education = ["Bachelors", "Masters", "Doctorate"]
    higher_edu = df[df["education"].isin(advanced_education)]
    lower_edu = df[~df["education"].isin(advanced_education)]

    higher_edu_rich = round((higher_edu[higher_edu["salary"] == ">50K"].shape[0] / higher_edu.shape[0]) * 100, 1)
    lower_edu_rich = round((lower_edu[lower_edu["salary"] == ">50K"].shape[0] / lower_edu.shape[0]) * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people working min hours per week and earning >50K
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_min_workers = min_workers[min_workers["salary"] == ">50K"]
    rich_percentage = round((rich_min_workers.shape[0] / min_workers.shape[0]) * 100, 1)

    # 8. Country with highest percentage of people earning >50K
    country_counts = df["native-country"].value_counts()
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts()
    rich_country_percent = (rich_by_country / country_counts * 100).dropna()
    highest_earning_country = rich_country_percent.idxmax()
    highest_earning_country_percentage = round(rich_country_percent.max(), 1)

    # 9. Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_edu_rich)
        print("Percentage without higher education that earn >50K:", lower_edu_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India for those earning >50K:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_edu_rich,
        "lower_education_rich": lower_edu_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }