# Rainfall-Prediction-Website

## Workflow chart
![1](https://github.com/rajiv8/Rainfall-Prediction/blob/master/static/workFlow.png)

## STEPS TAKEN IN THE PROCESS:->
#### CONNECTION TO HTML:
1.	 A user issues a request for a domain's root URL / to go to its index page
2.	main.py maps the URL / to a Python function
3.	The Python function finds a web template living in the templates/ folder.
4.	A web template will look in the static/ folder for any images, CSSfiles it needs as it renders to HTML
5.	Rendered HTML is sent back to main.py
6.	main.py sends the HTML back to the browser

#### URL IN THE BROWSER AND BACKEND CONNECTION:
1.	First. we imported the Flask class and a function render template.
2.	Next, we created a new instance of the Flask class.
3.	We then mapped the URL / to the function index(). Now, when someone visits this URL, the function index() will execute.
4.	The function index() uses the Flask function render template() to render the index.html template we just created from the templates/ folder to the browser.
5.	Finally, we use run() to run our app on a local server.
6.	We'll set the debug flag to true, so we can view any applicable error messages if something goes wrong, and so that the local server automatically reloads after we've made changes to the code.
7.	 When we visited http://127.0.0.1:5000/, main.py had code in it, which mapped the URL / to the Python function index().
8.	index() found the web template index.html in the templates/ folder, rendered it to HTML, and sent it back to the browser.
