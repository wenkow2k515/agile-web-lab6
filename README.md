# agile-web-lab6  
this is the flask of the web page</br>
use __flask run__ to run the program<br>   
the web page got 5 routes __/ /hello /helloname /hellonamen /looping /jinja__<br>  
on localhost:5000 you can add zhe routes to url to get the page<br>  
__/helloname__ use get which need use the fromat like _http://127.0.0.1:5000/helloname?name=bruh_ to go to the page with the name as bruh<br>  
__/hellonamen__ use /<> to return the name like _http://127.0.0.1:5000/helloname?name=bruh_ which pass the value by parameter<br>  
__/jinja__ use jinja and block extend to combine two pages content<br>  
__/form__ is use form to pass the value to the other pages like in __/form__ page when you pass the value and click the submit, you will pass it to __/post__<br> 