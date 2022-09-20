# CyVerse Coding Exercise

This coding exercise has two parts. The first part of the exercise is intended to demonstrate knowledge of RESTful web
services. The second part is intended to demonstrate the ability to create a simple user interface. You can feel free to
use any programming languages and frameworks that you want.

Note: the sample data set is large and there's no requirement to use all of the data in the exercise. Feel free to use a
subset of the data or to use another data set entirely.

## Part 1: RESTful Web Service Endpoint

The purpose of this portion of the exercise is to take the data from a CSV file and create a RESTful web service that
will return the same data in JSON format. The simplest version of this would be to create an endpoint that accepts a GET
request without any parameters and returns the contents of the CSV file as a JSON document. If time permits and you'd
like to get fancy, you could add query parameters to filter the results or change the sort order.

The means of ingesting the CSV file is up to you. For a simple implementation, you can read the contents directly from
the CSV file. If you'd like to make the implementation of the service a little bit easier, you might choose to write a
script to ingest the contents of the file into a relational database such as SQLite, or a NoSQL database such as
MongoDB.

## Part 2: User Interface

The purpose of this portion of the exercise is to build a user interface to display the data from the CSV file. The user
interface will make a call to the REST endpoint to obtain the data and display the results in a simple HTML
table. CyVerse uses NextJS and React for its user interface, but the framework that you use in this exercise is up to
you. As with the previous portion of the exercise, you can choose to add additional features such as sorting and
filtering if you like.
