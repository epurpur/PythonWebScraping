## **About Me**

Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    Brown Science & Engineering Library room I046


I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various engineering departments
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Random other things as they come up

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)

~R workshops
  * Data Wrangling in R                                       Tuesday, 1/28  10:00 - 12:00 Brown 133
  * Data Visualization in R                                   Tuesday, 2/4   10:00 - 12:00 Brown 133
  
~Python Workshops
  * Data Visualization with MatPlotLib                        Tuesday, 2/4   2:00 - 4:00 Brown 133
  * Web Scraping in Python                                    Tuesday, 2/11  2:00 - 4:00 Brown 133


We are partnering with Research Computing to offer all workshops in one series this semester!
[Research Computing](https://www.rc.virginia.edu/)

## ** Python Web Scraping ** 
This is an introductory workshop to web scraping in Python. It is assumed you have at least a little bit of experience using Python, but not required. 

## ** What is web scraping? **
Let's start with the basics. Basically, web scraping is extracting or retrieving data from a website. If you have ever copy and pasted a piece of information from a web page, you have manually done web scraping. Web scraping via a programming language like python automates the process to do it programmatically. We can use the structure of websites to drill down to the information we want, then extract it for our own purposes. 

Web pages are built using text-based markup langauges (like HTML!) and have a structure. You don't need to be that familiar with HTML to web scrape, but basically an HTML website is structured in a way that all information is inside various tags, very similar to XML.  

## **HTML Tags**
HTML stands for HyperText Markup Language and is the most basic building block of the web. It defines the meaning and structure of a website while other technologies define the site's appearance (CSS) and functionality (Javascript).

HTML uses "markup" to annotate text, images, and other content for display in a web browser. An HTML tag defines one part of a webpage and the element inside the tag describes what content will be in that element. Tags have an opening and closing tag.

example: 
<!DOCTYPE html>
<html>
<title> Page Title </title>
</html>    

## **Page Source**
To view the underlying html (or other) code of a website, choose any website, right click on the screen and 'View Page Source'. 

    -At least, for Google Chrome and Firefox. Safari (and other) web browsers are slightly different
    
-You will see a bunch of jumbled html code. Sometimes it is prettier than others. But, there it is! The code that powers the web page you are looking at. You'll see all kinds of tags. Some of the information is human readable and other parts are not. 

A more effective way (for our purposes) to view the page source is to right click and "Inspect". This is the same page source information, but structured better. Also, notice that you can move through the tags and see which control various parts of the web page. This will come in handy later!

## **Beautiful Soup**
Today we will be using the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) python library to scrape web pages! The most recent version of Beautiful Soup is Beautiful Soup 4.8. Here is a link to [Beautiful Soup 4 Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Here is a description from the Beautiful Soup Homepage:
You didn't write that awful page. You're just trying to get some data out of it. Beautiful Soup is here to help. Since 2004, it's been saving programmers hours or days of work on quick-turnaround screen scraping projects.

Beautiful Soup is a Python library designed for quick turnaround projects like screen-scraping. Three features make it powerful:

1. Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application.

2. Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.

3. Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.



