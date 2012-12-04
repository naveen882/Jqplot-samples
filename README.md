Jqplot-samples
==============

Jqplot samples

1.Install cdr model in setting.py

2.Add the following entry in main urls.py
	url(r'^cdr/', include('cdr.urls')),
	
3.python manage.py syncdb to create the tables

4.cd cdr/ && python generate_data.py #To generate the data

5.http://127.0.0.1/cdr/get_data/    ## To generate line chart

6.http://127.0.0.1/cdr/get_pie_data/ ## To generate pie chart
