# Q-1 : write a Python program to generate a list of keys whose values are not None.

d = {'a':1,'b':None,'c':"ABC",'d':"123"}
# output: a, c, d
Output = [key for key, value in d.items() if value is not None]
print(Output)

# Q-2 : write a Python program to create a new list where each element is incremented by 1.

Input_lst = [1,2,3,4]
#Output = [2,3,4,5]

output_lst = [x + 1 for x in Input_lst]
print(output_lst)

# another way 

output_lst = []
for num in lst:
    output_lst.append(num + 1)
print(output_lst)

# Q-3 : You are given a DataFrame with two columns: student and age. Write a Python program using pandas to add a new column named is_adult. This column should contain "Yes" if the corresponding age is greater than 18, otherwise "No".

import pandas as pd

data = {
    'student': ['John', 'Alice', 'Bob', 'Emma'],
    'age': [20, 17, 22, 16]
}

df = pd.DataFrame(data)
print(df)

df['is_adult'] = df['age'].apply(lambda x: 'Yes' if x > 18 else 'No')
print(df)


# Q-4 : same for in PySpark 
from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# Create a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
data = [
    ("John", 20),
    ("Alice", 17),
    ("Bob", 22),
    ("Emma", 16)
]

# Create DataFrame
df = spark.createDataFrame(data, ["student", "age"])
df.show()


# Add the "is_adult" column
df = df.withColumn("is_adult", when(df["age"] > 18, "Yes").otherwise("No"))
df.show()


# Q-5 : Same quesry for in sql
'''
SELECT
    student,
    age,
    CASE
        WHEN age > 18 THEN 'Yes'
        ELSE 'No'
    END AS is_adult
FROM
    students;

'''











