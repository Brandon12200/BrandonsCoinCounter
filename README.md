
# Brandon's Coin Counter

[www.brandonscoincounter.com](http://www.brandonscoincounter.com/)

#### Description:

##### Web Application Description

Brandon’s Coin Counter is a web application with tools to help users analyze their monthly spending habits and best develop future spending decisions. With a desire for data visualization in mind, Brandon’s Coin Counter clearly outlines how users are spending their money and the ways in which changes in their spending habits may affect their other areas of spending. It does this through three main features. With the main homepage feature, users are prompted to enter dollar values for every aspect of their monthly budget (income, housing, food, transportation, saving, debt payments, and other). From there, the program will make sure each value is a number and display information in regard to the monthly budget. This information is seen through a table that outlines the cost of each budget item and the percentage which that item takes up compared to the entire monthly income. Underneath the table, a pie chart that is made up of all these percentages is displayed, which helps users visualize exactly how their income is being divided each month. Finally, towards the bottom of the page, suggestions in regard to how the user can improve their spending habits are displayed. The suggestions that appear are dependent on the percentages of each budget item. So if the user already has what we believe to be a healthy budget, then no suggestions will appear. Alternatively, if there are ways in which we believe the imputed budget can be improved, then such suggested improvements will be displayed under the pie chart.

The second feature of the website is the Budget Builder, where users could choose a budget item from a dropdown menu and input a dollar value for the chosen item. Once the calculate button is pressed, the program will display a table with a hypothetical budget that we believe would be healthy for the user. This recommended budget will include the chosen item and its value but then will use such input to determine healthy values for each of the other budget values. The hope is that this feature will be useful for people considering changes to one of their budget items, as the recommended budget could inform whether they can afford such a change in their typical budget. For example, if a user is considering a transportation monthly payment of $250, the Budget Builder feature would tell them that for such a payment, it is recommended that they have a monthly income of at least $1,923.08 so they could still afford housing, food, appropriate saving, and other wants. Finally, beneath the displayed table, is a bar graph that displays the recommended percentages for each budget item. This, hopefully, enables users to visualize a recommended way in which they could be dividing their monthly income. In the code, the recommended percentages could be altered and the bar graph would respond appropriately.

The third featire is the Debt Planner, where users could input information about one debt item. This information include, its dollar amount, annual interest rate, and time frame for when the user would like to repay it. From there, the program displays the total amount of money the user is likely to pay after the desired time period, including interest, and a recommended monthly payment so that the debt balance reaches zero by the time goal of the user. Beneath such information is a table with rows that count be time (months or years). Each row contains the amount the user should have paid by that month or year and the balance that should remain. This gives the user a plan and milestones to reach over time. Finally is a line chart, which displays to the user the reccomended trajectory of time and remaining balance for the inputed debt item, so that thee user can get a sense of time and and a visualization of the rocommend process.

Finally, there is an About page, where users could read more about the web application and directions to use it. Taken all together, the features of Brandon’s Coin Counter serve to help users understand how they are spending their money and make good spending decisions in the future.

##### Application Inspiration

My decision to create this web application came out of need. As a recent college graduate beginning my financial journey, I have been trying to be smart in regard to how I spend my money. Therefore, I wanted something that would help me understand my spending and develop a plan for future financial decisions. Though the idea for this application came from my position as someone new to the financial world, I wanted to make something that is useful for everyone. If you are new to finances, like me, or someone just looking to improve their spending habits, you would certainly find use in my application.

##### Programming Description

This web application was built using a Flask framework. The front-end makes use of HTML, CSS, and JavaScript, and the back-end is built with Python. The heart of the backend lives in the “app.py” file but I was able to use functions that I created in “helpers.py” such as “calculate_budget” and “percent”. I spent a significant amount of my time working on front-end HTML files. This is because I made the main HTML file, “layout.html,” and then each feature, except the About page, had two HTML (ex. “builder.html” and “built.html”). Leveraging resources such as Bootstrap for the tables and navigation bar was very helpful and was significant in bettering the aesthetics of my web application.

The most challenging parts of building this application came while learning JavaScript to improve the usefulness of my pages, especially in terms of data visualization. The pie chart, bar graph, suggestions, and line chart were all dependent on other data on the page and used JavaScript to ensure their accuracy. For the pie chart and bar graph, I made use of the Chart.js library and implemented their templates. Despite using their library, it still took a significant amount of time to correctly display the tables and create the functions needed to call for the creation of such displays. While experiencing such challenges, I found myself determined to solve whatever was setting me back and get the graphics on the page. This was because I wanted data visualization to be a key aspect of my program. While using my program, I have found the visualization features to be especially useful, affirming my desire to have them included in the program. Through it all, I learned much about the JavaScript language and now understand the power of having a web application that can adapt to certain data points on the page.

##### Requirements

Flask==2.1.0; python_version > '3.6'
Flask==2.0.3; python_version < '3.7'
gunicorn==20.1.0

