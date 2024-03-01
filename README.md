# Project3 - Data Visualization Track
## Education Funding Analysis

### Team Members: 
- James Draper
- Kelsey Kraft
- Mariah McLelan
- Amarilli Novel
- Hisako Yamanaka

  
### Research Question to Answer:
How does the funding allocated to education impact the success of students and schools?

### Project Description:
The project aims to analyze the impact of education funding on the success of students and schools. 
Specifically, the study will focus on the relationship between state funding in Texas education, SAT/ACT scores, and dropout rates. 
Through statistical and visual analysis, we will determine whether higher funding leads to better outcomes or if there is a point where the impact of funding levels off.

### Data Sets Source:
https://tea.texas.gov/

> https://tea.texas.gov/reports-and-data/school-data/campus-and-district-type-data-search

> https://tea.texas.gov/reports-and-data/school-performance/accountability-research/c[…]-graduation-and-dropout/completion-graduation-and-dropout-data

> https://tea.texas.gov/reports-and-data/school-performance/accountability-research/ap/ib-and-sat/act

> https://tea.texas.gov/finance-and-grants/state-funding/state-funding-reports-and-data

> https://tea.texas.gov/finance-and-grants/state-funding/state-funding-reports-and-data/peims-financial-standard-reports

https://schools.texastribune.org/states/tx/

### Development
Began our study by searching for suitable datasets, focusing on the Texas Education system and referring to the TEA Texas Education Agency website.
We found six relevant Excel files, which we converted to .csv files. Also, we found Public Schools Explorer website, which we scraped data fpr all the districts

Our first challenge was to clean the data frames. 
We focused solely on total operating revenue, which Texas uses to support educational operations and facility construction in public school districts. 
This revenue comes from local, state, and federal funding sources, with the majority coming from state and local sources and only a relatively small amount from the federal government.  

State government aid is the primary funding source for elementary and secondary education, followed by local contributions (primarily property taxes). On average, 8% of revenues come from the federal government, 47% from the state, and 45% from local sources[^bignote2].
[^bignote2]:  McFarland, J., Hussar, B., Wang, X., Zhang, J., Wang, K., Rathbun, A., … Bullock Mann, F. (2018). The condition of education 2018. National Center for Education Statistics.

We selected "All Students" as the group for SAT and ACT scores, as other groups had inconsistent data. 
Then, we merged the SAT and ACT scores with the cleaned finance data frame and formatted and sorted the values. 
We then proceeded to conduct a **statistical analysis** of the data.

### Statistical Analysis:
#### Texas Total Operating Revenue Results:
*Mean* Total Operating Revenue: 85,389,382

*Median* Total Operating Revenue: 22,696,266

*Standard Deviation*: 190,478,406

*Standard Error of the Mean*: 7,049,922

*Shapiro-Wilk Normality Test*:

Test Statistic: 0.4248087406158447
P-value: 4.7223758247746335e-43
The data does not follow a normal distribution (reject the null hypothesis).

The interquartile range of the total operating revenue is: 57181077.0

The median of the total operating revenue is: 22696266.0 

Values below -74376596.75 could be outliers.

Values above 154347711.25 could be outliers.

#### Texas Student Count Distribution Results:
*Mean* Student Count: 6,908

*Median* Student Count: 1,687

*Standard Deviation*: 15,534

*Standard Error of the Mean*: 575

*Shapiro-Wilk Normality Test*:

Test Statistic: 0.4364619851112366

P-value: 9.388699710976274e-43

The data does not follow a normal distribution (reject the null hypothesis).

The interquartile range of the Student Count is: 4531.5

The median of the Student Count is: 1687.0 

Values below -6042.25 could be outliers.

Values above 12083.75 could be outliers.

**visual analysis**:

### Visualization:
Our first goal was to investigate if there is a correlation between total operating revenue and student count. 

>![tor vs students!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/all%20budget%20vs%20student.jpeg)

The scatter plot shows a positive correlation between total operating revenue and student count.
Then, we analyzed a possible correlation between spending ranges (per student) and average SAT and ACT scores.

![>insert fig Spending Ranges (per student) vs. average total SAT score/ACT!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/spendingvact.png)

![sat spending!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/spendingvsat.png)

The line plot suggests that the budget doesn't significantly affect scores, as some schools with smaller budgets scored the highest.
Moreover, smaller schools tend to have higher ACT and SAT scores. 
These findings indicate that other factors besides budget allocation may influence academic performance, and further research is needed to identify these factors.
We then decided to examine whether there is a correlation between school size and performance in standardized tests.

![>insert fig. School Size vs. Average Total SAT ACT score !](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/sizevact.png)

![sat!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/sizevsat.png)

The data presented in the line graph indicates a substantial decline in academic scores when the school population increases.
At this point, we decided to narrow down our investigation:
We analyzed the five largest cities in Texas (by population): San Antonio, Austin, Fort Worth, Dallas, and Houston. 

![box plot kelsey!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/ACT-SAT-Boxplots.png)

Specifically, we focused on their respective Independent School Districts (ISD) and created a box plot that compares the total operating revenue of each ISD with their SAT and ACT Composite scores and demonstrates the variability of test scores within districts with some of the highest student counts and budgets. 

There is no better outcome in SAT and ACT tests as Total Operating Revenue increases. 
In fact, Austin ISD performs the best in both SAT and ACT while having a smaller budget than Fort Worth, Dallas, and Houston. 

We chose the five largest cities as these had plenty of schools reporting scores, allowing a coherent box plot graph (small districts with only one or two schools need to give more data to plot them in this manner). 

Using the same data, we created two scatterplots and two histograms:

![insert fig SAT Total and ACT Composite scatterplots!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/ACT-SAT-Oper-Rev-Scatter.png) 

![histograms !](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/ACT-SAT-Oper-Rev-Hist.png)

There is a negative correlation between Total Operating Revenue and ACT Composite and SAT Total scores, as indicated by the values of -0.03 and -0.09, respectively. 

At this juncture, we determined that comparing a larger urban center and a smaller municipality was necessary to confirm our hypothesis. 
To facilitate this assessment, we plan to implement `hvplot`, as data visualization tool.

![hisako act sat!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/5%20SAT%20vs%20ACT.jpeg)

We also created a treemap to visualize the differences between larger and smaller districts. The treemap is interactive and visible on the following website when the code is running:

> http://127.0.0.1:8050/

![non interactive!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/5%20trea%20map.png)

After collecting sufficient data on total operating revenue and SAT/ACT scores, we examined the potential correlation between funding and dropout rates.

![color-sorted histogram!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/DropoutRateByStudentCount.png)

The color-sorted histogram displays a relationship between the student counts of schools and the average dropout rates within those facets. 
Each vertical bar is an increasing measure of 20 students. 
At its lowest points, rates as low as 5 percent can be seen from the largest schools, while at its height, the schools with student populations between 60-80 and 300-320 peak at 48 and 56 percent.

![james fringe towns!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/DropoutRateBySchoolType.png)

The bar chart shows the average dropout rates by school type. The highest rate is in "Large Cities" at 2.59%, while the lowest is in "Rural Remote" towns at 0.39%.

![box plot James!](https://github.com/mariahmclelan/project1/blob/main/project_notebook/images/boxplot.png))

"Fringe Towns," shown in the second figure, have the second highest school type dropout rate at 1.75 percent overall, and in the first figure, it's noticeable that "Fringe Towns" are also the largest dropout rate in the four highest rates found in the first figure. Ockham's razor would suggest that Fringe towns are the most likely to produce dropouts, but we wanted slightly more than that. So, figure 3 contains a box and whisker plot to eliminate any possible outliers and show that "Large Cities" still have the highest rate without outliers, having an upper fence of 6.1 percent.


### Takeaways and conclusions:

- As expected, there is a positive correlation between total operating revenue and student count.
  That means the more students a school district has, the bigger the funding received.
  
- The budget doesn't significantly affect scores, as some schools with smaller budgets scored the highest.
  Moreover, smaller schools tend to have higher ACT and SAT scores.
  
- There is a substantial decline in academic scores when the school population increases.

- When analyzing the five largest cities in Texas by population, we discovered that Austin ISD performs the best in both SAT and ACT while having a smaller budget than Fort Worth, Dallas, and Houston.

- There is a negative correlation between Total Operating Revenue and ACT Composite and SAT Total scores, as indicated by the values of -0.03 and -0.09, respectively.

- Smaller schools, on average, do better than larger schools.

- Large Cities and large school districts have the highest dropout rates without outliers, having an upper fence of 6.1 percent.

In conclusion, education funding does not impact students' success in SAT and ACT scores. 
Also, the budget does not help with dropout rates since some schools with higher total operating revenue have the highest dropout rates.

After analyzing the data, a pertinent question arises: What is the key to success for smaller schools with higher ACT and SAT scores?

As per the American Federation of Teachers Texas, teachers must maintain an average of 20 students per class across the district, although no prescribed limit exists for individual secondary classrooms. The 22:1 ratio only applies to students in Kindergarten through fourth grade.

Further investigation may lead us to hypothesize that the optimal student-to-teacher ratio in smaller schools may be a factor that contributes to their superior academic performance when compared to larger schools with a lower percentage of teachers per student. 

To answer this question, we need to research more and this query could already be the draft of our project 2. 

