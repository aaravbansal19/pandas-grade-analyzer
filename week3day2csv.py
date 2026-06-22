import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("grades.csv")

print(df)


print("Here are the core statistics for the data: ")
print()
average = df["Grade"].mean()
print("The average grade is a", average)
print("The median grade was a", df["Grade"].median())
print()
highest = df.loc[df["Grade"].idxmax()]
print("The highest grade was a", highest["Grade"])
lowest = df.loc[df["Grade"].idxmin()]
print("The lowest grade was a", lowest["Grade"])
print()
print("The standard deviation of the dataset is", df["Grade"].std())
print()
print("The student with the highest grade was", highest["Name"], "with a", highest["Grade"])
print("The student with the lowest grade was", lowest["Name"], "with a", lowest["Grade"])
print()
above_average = df[df["Grade"] > average]
print("The number students which performed above average are", len(above_average))
above_average = df[df["Grade"] < 80]
print("The number students which below an 80 are", len(above_average))
print()
print("Below is the students grade and age, with the grade in a decreasing order.")
print(df.sort_values("Grade", ascending=False))
print()
print("Below is the top 3 students.")
print(df.head(3))
print()
df_sorted = df.sort_values("Grade")
plt.bar(df_sorted["Name"], df_sorted["Grade"])
plt.xticks(rotation=45)
plt.show()



# print(df[df["Grade"] > 90])
# average = df["Grade"].mean()
# print(df[df["Grade"] > average])
# print(df.sort_values("Grade"))
# print(df.sort_values("Grade", ascending=False))
# print(df.sort_values("Grade", ascending=False).head(3))
# passed = df[df["Grade"] >= 70]
# print("There are", len(passed), "number of students who passed. ")





# df["Grade"].hist()
# plt.title("Grade Distribution")
# plt.xlabel("Grade Range")
# plt.ylabel("Number of students")
# plt.show()

# df_sorted = df.sort_values("Grade")
# plt.bar(df_sorted["Name"], df_sorted["Grade"])
# plt.xticks(rotation=45)
# plt.show()



# print(df)
# print(df.columns)
# print(df.index)
# print(df.shape)
# print(df["Grade"])
# print(df["Name"])
# print(df["Age"])
# print(df["Grade"].mean())
# print(df["Grade"].max())
# print(df["Grade"].min())
# highest = df.loc[df["Grade"].idxmax()]
# print("Highest:", highest["Name"], "with a score of", highest["Grade"])
# lowest = df.loc[df["Grade"].idxmin()]
# print("Lowest:", lowest["Name"], "with a score of", lowest["Grade"])
# print(df.head(1))
# print(df.tail(2))
# print(df["Grade"].mean())
# print(df["Grade"].median())
# print(df["Grade"].max())
# print(df["Grade"].min())
# print(df["Grade"].std())
#print(df["Grade"].describe())



