# Texas Education and Funding: a Visualization 

### Team Members: 
- James Draper
- Kelsey Kraft
- Mariah McLelan
- Amarilli Novel
- Hisako Yamanaka

  
### Project Overview:
Question to answer: How does the funding allocated to education impact the success of students and schools?

This is the second part of a team project about [Texas ISDs](https://github.com/mariahmclelan/TexasISDs).
The project aims to analyze the impact of education funding on the success of students and schools. 
Specifically, the study will focus on the relationship between state funding in Texas education, SAT/ACT scores, demographics, and dropout rates. 
Through a custom MongoDB database and visual analysis, we will determine whether higher funding leads to better outcomes or if there is a point where the impact of funding levels off.

### Data Sets Source:

[Texas Education Agency](https://tea.texas.gov/)

[Texas Education Agency Public Open Data Site: Current Districts ](https://schoolsdata2-tea-texas.opendata.arcgis.com/)

[Texas Education Agency Public Open Data Site: Currents Schools ](https://schoolsdata2-tea-texas.opendata.arcgis.com/)

[Texas schools geocoding project](https://github.com/utdata/texas-schools)

[The Texas Tribune](https://schools.texastribune.org/states/tx/)

We also used the cleaned dataset we created during the first part of our project [Score&Finance](https://github.com/mariahmclelan/Project3/blob/main/resources/scores_finances.json) 

### Break Down of Task:

    Mariah: Cleaning, merging, and transform datasets, Flask App Home Page, Maps and visualizations.
    James: Web Scraping.
    Kelsey: MongoDB and Flask App.
    Amarilli: GeoJSON datasets, Flask App Home Page, Maps, Visualizations, README. 
    Hisako: Presentation.

### Ethical data considerations

Part of this project is about web scraping. Before downloading or scraping the data, we reviewed the regulations and documents about the data usage. All the data we used for this project is ethically sourced.

### Development

The goal of this project was to create maps about Education and Funding in Texas, so we began our research looking for GeoJSON datasets to include with [our previous dataset](https://github.com/mariahmclelan/Project3/blob/main/resources/scores_finances.json)
One of our first tasks was to transform our cvs files into JSON format. Then we stored them in our MongoDB dataset that we named [texasSchoolsDB](https://github.com/mariahmclelan/Project3/blob/main/DB.ipynb) we created a collection for every dataset we had and later we imported the data and stored in our database. 
At this point we created a Flask App with X available routes X dataset and two Maps. 

Both maps are interactive and can be reached at [LINK]

The first map displays all the Texas districts for the 2022/2023 year. With a layer control, the boundaries can be turned off and on. Also, on this map, we displayed the Financial Data we got from our previous project, in particular:

- The student count for each district,
- The Total operation revenue for each district

The markers are differentiated according to the schools' ranking, and their size mirrors the size of the student population.  

The second map is a heat map of the SAT scores of every district in Texas, and the markers display the demographic of each district. 

Regarding the demographics, we also created radar charts displaying the population of each district.

![IMAGE]



### Takeaways and conclusions:

- The maps visually confirm the positive correlation between total operating revenue and student count.
  That means the more students a school district has, the bigger the funding received.
  
- The budget doesn't significantly affect SAT scores, as some schools with smaller budgets scored the highest.
  Moreover, smaller schools tend to have higher SAT scores.
  
- There is a substantial decline in academic scores when the school population increases.

- Smaller schools, on average, do better than larger schools.

In conclusion, education funding does not impact students' success. 


After analyzing the data, a pertinent question arises: What is the key to success for smaller schools with higher scores?

As per the American Federation of Teachers Texas, teachers must maintain an average of 20 students per class across the district, although no prescribed limit exists for individual secondary classrooms. The 22:1 ratio only applies to students in Kindergarten through fourth grade.

Further investigation may lead us to hypothesize that the optimal student-to-teacher ratio in smaller schools may be a factor that contributes to their superior academic performance when compared to larger schools with a lower percentage of teachers per student. 

Our web scraping project is still in progress. We still have thousands of rows of data to clean and analyze and this query could already be the draft of our next project. 

