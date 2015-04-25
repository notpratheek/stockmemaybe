# stockmemaybe
Scraping and predictive analytics of stock data

Stock Me Maybe is a web application that lets you peek into the future of stock prices!
It uses sentiment and predictive analytics.
Stock Me Maybe is written in Python using the web application framework named Django. 
MySQL is used for database management.

<h3>Requirements:</h3>
<ol>
  <li>Virtualenv (https://pypi.python.org/pypi/virtualenv)</li>
  <li>MySQL (https://www.mysql.com/)</li>
</ol>

<h3>Running the project:</h3>
<ol>
  <li>Create a virtual environment: 'virtualenv env -ppython3.4'.</li>
  <li>Activate the virtualenv: 'source env/bin/activate'.</li>
  <li>run 'pip install -r path/to/requirements.txt'.</li>
  <li>Create a new database in MySQL called stockmemaybe.</li>
  <li>In stockmemaybe/settings.py, enter the username and password in the DATABASES section.</li>
  <li>If you haven't created an app for twitter access yet, create one.</li>
  <li>Enter consumer key, consumer secret, oauth token oauth token secret from your twitter app into the respective fields in ugc/views.py tweets_get() method.</li>
  <li>Run the application on the local host using the command : “python manage.py runserver”</li>
  <li>Open the web browser and enter the url “localhost:8000/main”.</li>
  <li>Enter the company ticker in the textbox.</li>
  <li>Press the “Analyse” button.</li>
  <li>The project computes and displays the predicted stock price for the entered company.</li>
</ol>
