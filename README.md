# Issue_Counter


Issue Counter



Developed an flask application which contains two functions where one function renders the input page (login.html) which will accept the url on submit button it will redirect to the getIssues post method which is defines in app.py
getIssues-- will inturn call hit_url function which will accept input url as parameter
Based on input url open issues will be fetched and that response will be sent to other function (write_issuses) which will calculate the open issues 
1. count1- open issues less than 24 hrs
2. count2 – open issues more than 24 hrs and less than 7 days
3. count3 – open issues more than 7 days
4. count- total open issues
I will be sent as json object to hit_url function which will be rendered in result.html page 


Solution 
It can be extended get issue names based on filter 
No of commits can be counted 
Dates when issues where openend can be fetched 
Description for issues can be fetched

Example url:
hunspell/hunspell
Total issues=169
SrinithiParvathi/Test   My own repository with 3 issues
Total issues =3
 
 
