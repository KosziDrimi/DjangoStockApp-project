# DjangoStockApp

Program offering the possibility to generate the table with closing prices for particular stocks during chosen periods. 

It consists of two connected apps:
- **app_1** - allows user's login (_/app_1/accounts/login/_), logout (_/app_1/accounts/logout/_) and registration (_/app_1/register/_);
- **app_2** - (_/app_2/show/_) provides the form to choose the stock code and dates of interest followed by the table with the result (dates & closing prices) generated from the database. 
This part of the application is accessible only for the logged users. There is a possibility to log out on both its sites.

There are two sqlite databases provided - each for every app. 
The one related to stocks' prices was build by `database.py` python script using data from [link](https://stooq.pl/).

Technologies: Python 3.8.3, Django, HTML5, Bootstrap 5.0, pandas.

In order to see this project you should run `python manage.py runserver` on your command line and open the browser at local host specified. 


