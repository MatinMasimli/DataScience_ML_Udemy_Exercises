This is the first capstone project on Data Science and Machine Learning Udemy Course. The project covers all the materials
such as Numpy, Pandas, Data Visualization tools like Matplotlib, Seaborn that are taught for Data Science part of the course. 
The attached images are the outputs of some of the questions. The following are the questions of the project:

1. Check the info() of the df.
2. Check the head of df.
3. What are the top 5 zipcodes for 911 calls?
4. What are the top 5 townships (twp) for 911 calls?
5. Take a look at the 'title' column, how many unique title codes are there?
6. In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use
   .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value. 
   For example, if the title column value is EMS: BACK PAINS/INJURY, the Reason column value would be EMS.
7. What is the most common Reason for a 911 call based off of this new column?
8. Now use seaborn to create a countplot of 911 calls by Reason.
9. Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
10. Use pd.to_datetime to convert the column from strings to DateTime objects.
11. You can now grab specific attributes from a Datetime object by calling them. Use .apply() to create 3 new columns called      Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column.
12. Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the      day of the week:
13. Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
14. Same as question 13 for Month:
15. Create a groupby object called byMonth, where you group the DataFrame by the month column and use the count() method for 
   aggregation. Use the head() method on this returned DataFrame.
16. Create a simple plot off of the dataframe indicating the count of calls per month.
