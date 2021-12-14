# Term 3 design thinking project
**NOTE: Readme of web app is in web app folder**
Watch the video describing our work [here](https://youtu.be/EXGVJrGnt-k) 

# Task 1
Task 1 description:

Build a **Multiple Linear Regression model** that predicts the number of deaths in various countries due to COVID-19. You are free to select and choose the dataset you would like to use while building the model and are allowed to use the Pandas Library in your code and can use Excel.

The following technical/tool constraint applies: you are NOT allowed to use any existing machine learning packages, such as scikit-learn.

As a general guide, you may need to undertake the following actions:
- Find data sets for the **number of deaths** in various countries **(a minimum of 20 countries)** due to COVID-19.
- Research for appropriate predictor variables to predict deaths due to COVID-19.
- You may use time as one of the predictors (in which case you could attempt to predict death rates in the future), or you may choose to leave it out (in which case, you would be looking at the deaths at a fixed chosen point in time).
- Find data sets on the chosen predictors for the various countries in the model.
- Use **plots** to visualize and understand your data.
- Build a **model** and **test the accuracy of your model**, using an appropriately chosen metric(hint: r2 is not a good metric for this task).
- If needed, improve your model by incorporating other predictors, and/or removing existing ones.
- Discuss your data sets, model, accuracy, and what metrics you used to judge the accuracy.

# Overview of task 1 implementation:

Our team built a **Multiple Linear Regression model** that predicts the number of deaths in various countries due to COVID-19. 

We used the COVID-19 dataset by Our World in Data as it contain data on many suitable variables from many countries. 

We have filtered the countries and have chosen to look at the data of the European Union, United Kingdom and United States as these countries have many similarities across economic indicators, COVID management strategies and COVID-19 progression. These similarities will help reduce the variance in our model and help us gather a better prediction. 

Target: `total_deaths`
Predictor variables: (selected according to research done) 

`icu_patients`, `icu_patients_per_million`, `hosp_patients`, `hosp_patients_per_million`, `hospital_beds_per_thousand`, `reproduction_rate`, `stringency_index`, `total_tests`, `total_vaccinations`, `population_density`,`gdp_per_capita`, `location`, `date`

Note: we did NOT use any existing machine learning packages, such as scikit-learn as it was the constraint of the project

# Task 2

Task 2 description: 
You are free to find and define a problem (apply the discovery and define phases first, from the UK Design Council Double Diamond, 3.007 Design Thinking and Innovation) of your interest related to COVID-19. The problem can be modelled either using Linear Regression (or Multiple Linear Regression) or Logistic Regression, which means you can work with either continuous numerical data or classification.

The following technical/tool constraint applies: you are NOT allowed to use Neural Networks or other Machine Learning models. You must use Python and Jupyter Notebook.

In general, you may want to consider performing the following steps:
- Find an interesting problem which you want to solve either using **Linear Regression or Classification** (please check with your instructors first on whether the problem makes sense).
- Find a **dataset** to build your model. For example, you can use Kaggle (https://www.kaggle.com/datasets) to find suitable datasets.
- Use **plots** to visualize and understand your data.
- Create **training and test** data sets.
- Build your model.
- Choose an **appropriate metric** to evaluate your model (you may use the same metric as the one used in Task 1).
- Improve your model.

# Overview of task 2 implementation:

### Design question: How did COVID-19 impact the economy?

Since macro economy indicators is usually published only once during each financial quarter, there will only be 4 data points if we look at the 2021/2021 period. Hence, we did not use macro economy indicators as the target as there is insfficient data for the time period we are looking at.

Thus, we decided to use price of gold ETFs ([SPDR Gold Shares (GLD)](https://finance.yahoo.com/quote/GLD/history?p=GLD)) as a proxy of economic health. This is because [gold usually rises alongside investors' uncertainty in the economy](https://www.npr.org/sections/coronavirus-live-updates/2020/07/27/895975866/economic-uncertainty-drives-gold-price-to-a-record-high). In uncertain economic times, investors tend to put their money in gold.

On the yahoo finance, they provide open, high, low, close, and volume of price of gold ETF. We chose to focus on close gold price because [it is a stock’s closing price that determines how a share performed during the day](https://analyzingalpha.com/open-high-low-close-stocks). 

### Goal: predict close gold prices given COVID's impact

#### We are going to predict gold close price using **multi linear regression**
