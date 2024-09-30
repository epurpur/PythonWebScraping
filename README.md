```
Last updated 09/30/2024
```


## **About Me**


Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    Brown Science & Engineering Library room I054


I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various engineering departments
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Random other things as they come up

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)


We are partnering with Research Computing to offer all workshops in one series this semester!
[Research Computing](https://www.rc.virginia.edu/)

## Other Upcoming Workshops

| Workshop | Date | Time |
| ---- | ---- | ---- |
| Intro to Python pt 1                                                |       Wednesday 9/4   |  10:00 - 11:30am
| Intro to Python pt 2                                                |       Wednesday 9/11  |  10:00 - 11:30am
| Intro to Version Control w/ Git + Github                            |       Wednesday 9/11  |  1:00 - 2:30pm
| Python Data Analysis + Visualization                                |       Wednesday 9/18  |  10:00 - 11:30am
| Local Large Language Models                                         |       Wednesday 9/25  |  10:00 - 11:30am
| Python Web Scraping                                                 |       Wednesday 10/2  |  10:00 - 11:30am


## ** Python Web Scraping ** 
This is an introductory workshop to web scraping in Python. It is assumed you have at least a little bit of experience using Python, but not required. 

## ** What is web scraping? **
Let's start with the basics. Basically, web scraping is extracting or retrieving data from a website. If you have ever copy and pasted a piece of information from a web page, you have manually done web scraping. Web scraping via a programming language like python automates the process to do it programmatically. We can use the structure of websites to find to the information we want, then extract it for our own purposes. 

Web pages are built using text-based markup languages (like HTML!) and have a structure. You don't need to be that familiar with HTML to web scrape, but basically an HTML website is structured in a way that all information is inside various tags.

## Quick Introduction to HTML
HTML stands for HyperText Markup Language and is the basic structural element that is used to create web pages. It defines the structure of a website while other technologies define the site's appearance (CSS) and functionality (Javascript). When an HTML document is loaded by a web browser, the browser uses HTML tags to render the page content.

HTML uses "markup" to annotate text, images, and other content for display in a web browser. An HTML tag defines one part of a webpage and the element inside the tag describes what content will be in that element. Tags have an opening and closing tag.

## **HTML Tags**
There are many, just know that they each define one element of the webpage. Each tag has a closing and ending tag. 

    <!DOCTYPE html>
    <html>
        <head>
            <title>Page Title</title>
        </head>
        <body>
            <h1>Homepage Headline</h1>
            <p>This is a paragraph.</p>
        </body>
    </html>  

## **Page Source**
To view the underlying html (or other) code of a website, choose any website, right click on the screen and 'View Page Source'. 
    
-You will see a bunch of jumbled html code. Sometimes it is prettier than others. But, there it is! The code that defines the web page you are looking at. You'll see all kinds of tags. Some of the information is human readable and other parts are not. 

A more effective way (for our purposes) to view the page source is to right click and "Inspect". This is the same page source information, but structured better. Also, notice that you can move through the tags and see which control various parts of the web page. This will come in handy later!

## **Beautiful Soup**
Today we will be using the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) python library to scrape web pages! The most recent version of Beautiful Soup is Beautiful Soup 4.12. Here is a link to [Beautiful Soup 4 Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Beautiful Soup 4 is a python library for pulling data out of HTML and XML files. Note, this is not all web pages!

Here is a description from the Beautiful Soup Homepage:
You didn't write that awful page. You're just trying to get some data out of it. Beautiful Soup is here to help. Since 2004, it's been saving programmers hours or days of work on quick-turnaround screen scraping projects.

Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping. Three features make it powerful:

1. Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application.

2. Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.

3. Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.


## **Selenium**

Selenium automates your web browser. Link to the documentation: [https://www.selenium.dev/](https://www.selenium.dev/)
There are a lot of reasons why you might use this. It is commonly used for testing web applications but can also be used for purposed like web scraping, which we will do today!

The first thing we need to use to use selenium is install a **web driver** which allows you to drive a browser natively with your code, just as if you were a human doing it. 




