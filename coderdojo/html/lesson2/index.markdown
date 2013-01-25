---

title: Gorey Coder Dojo HTML Lesson 2

---

<html>
<head>
<link href='http://fonts.googleapis.com/css?family=Cutive+Mono|Maven+Pro' rel='stylesheet' type='text/css'>

<style>
body { width:80%; margin:0 auto; font-family: 'Maven Pro', serif; font-size:1em; }

code { font-family: 'Cutive Mono', sans-serif; } 

h1 { border-bottom: 1px solid #ccc;}
</style>
</head>

<body>

# Lesson 2

## Introduction


In lesson 1 we looked at how to put together a webpage and looked at some basic html tags. This week well be looking at Cascading Style Sheets, or CSS for short. 

Using CSS allows us to add style to our HTML. There are a number of ways of applying CSS to HTML. But the basic format of css is property:value;

If you don't understand anything or something doesn't work the way you thing it should just shout for help!

## Startup

To start writing html you will need a text editor. One you can try is [Sublime Text](http://www.sublimetext.com/2) . Go there now and download and install it. You should never use Microsoft Word to write HTML. 

The next thing you need is a web browser. You can use your current web browser. Google Chrome is a good browser for using to check and debug (fix) your HTML code if there are errors in it. [Download Chrome Here](http://www.google.com/chrome).

A note on creating folders and html file names. It is best practice not to have spaces in the names of web folders or file names. So you can call your files anything like the following. 

+ MyWebPage.html
+ mywebpage.html
+ my-web-page.html

The following characters are valid urls ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=

## Applying CSS

On your desktop create a folder called coderdojo. In the coderdojo folder create another folder called lesson2.

When your ready open your text editor and type in the following code 
```
<!DOCTYPE html>
<html>
<head> 
  <title>CSS Page</title>
  <link type="text/css" rel="stylesheet" href="style.css">
</head>
<body>
  <h1>This is a h1 tag</h1>
   
  <p>This is a paragraph</p>
     
  <ul>
      <li>List item 1</li>
      <li>List item 2</li>
      <li>List item 3</li>
      <li>List item 4</li>
  </ul>
    <table>
      <tr>
        <td>cell 1</td>
        <td>cell 2</td>
      </tr>
      <tr>
        <td>cell 3</td>
        <td>cell 4</td>
      </tr>
    </table>
</body>
</html>
```

Save it as index.html in the lesson2 folder you created. Also create a new file called style.css in that same folder.


Now open your browser and press ctrl o (cmd o on a mac) file the index.html file and press open.


### Explanation 

In lesson 1 we covered the basic html tags. The new one we added here was in the ```<head>``` section. 

```<link type="text/css" rel="stylesheet" href="style.css">```

What we've done here is to add 

### Try It Yourself
Make a new page called page2.html on the page set the page title as My second page. Add a h1 tag and 2 paragraphs of text. Then add a h2 tag and another 2 paragraphs of text.

## Images

A web page looks pretty boring without images. 

Go to the web page (INSERT PAGE) , when the page opens right click on the image and select the Save Image As option and save the image to your lesson1 folder. 

Type out the following and save it in the lesson1 folder as page3.html

```
<!DOCTYPE html>
<html>
<head> 
  <title>Adding an image</title>
</head>
<body>
  <h1>Adding an image</h1>
  <p>
     <img src=”image1.jpg” alt=”My first image” text=”My First Image”>
    This is an image 
  </p>
</body>
</html>
   
### Explanation
   
The new tag we introduced is `<img>` this does not have a closing tag. In the image tag it has a number of attributes, these are src, alt, text. 
   
+ src (source) means the location of the file. The source can be absolute or relative to the page. Don't worry about this just now we'll talk about this later.
+ alt (alternate text) this is the text that will be shown if the image is not found.
+ title means the text that is shown when you hover over the image. 
   
### Try It Yourself

Save the image from this url (INSERT IMAGE2). Create a new page and add a title ‘My Second Image'. Add a h4 heading with the text of ‘My Second image'. And add the image. Save it in the lesson1 folder and call it page4.html 
    
## Links
    
The web would only be a series of pages without links!  So lets link all our pages together now. 
    
Open page1.html in your text editor.  Underneath the first paragraph add in the following text.

```html
<p><a href=”page2.html”>Page 2</a></p>
```

So it should read:

```
<!DOCTYPE html>
<html>
<head> 
  <title>First Page</title>
</head>
<body>
  <h1>Hello World!!</h1>
  <p>This is my first web page</p>
  <p><a href=”page2.html”>Page 2</a></p>
</body>
</html>
```

Save the file and open it in your web browser. Hover on the Page 2 link and click it.
    
### Explanation
    
The link tag is called an anchor tag. It is opened with `<a>` and closed with an `</a>`. All the text between the 2 tags will be the text that will be used in the link.
    
The `<a>` tag has one attribute ‘href' this is the page that it will link to. 
    
### Try It Yourself

On page 2 link to page 3. 
On page 3 link to page 4.
On page 4 link to page 1.
    
Now you can click on any of the links to open any of our pages. 
    
## Lists
    
Lists are used all the time on web pages. From showing bullet pointed lists of information or numbered lists. They are also used as the basic building blocks to create menus.
    
There are 3 types of lists 

+ Ordered Lists 
+ Unordered Lists
+ Definition Lists
    
Ordered lists appear as list with numbers 

1. Item 1
2.  Item 2
3.  Item 3
    
The above would be written in html as:

```
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>
```
          
Unordered lists appear as bullet points

+ Item 1
+ Item 2
+ Item 3
          
The above would be written in html as:

```
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```      
      
We'll leave definition lists out of it for the moment. 
      
So now lets add in links to all our pages to each page.
      
Open page1.html. Underneath your last paragraph add in the following:

```
<ul>
  <li><a href=”page1.html”>Page 1</a></li>
  <li><a href=”page2.html”>Page 2</a></li>
  <li><a href=”page3.html”>Page 3</a></li>
  <li><a href=”page4.html”>Page 4</a></li>
</ul>
```                    
                    
The page should look like the following:

```
<!DOCTYPE html>
<html>
<head> 
  <title>First Page</title>
</head>
<body>
  <h1>Hello World!!</h1>
  <p>This is my first web page</p>
  <p><a href=”page2.html”>Page 2</a></p>
  <ul>
    <li><a href=”page1.html”>Page 1</a></li>
    <li><a href=”page2.html”>Page 2</a></li>
    <li><a href=”page3.html”>Page 3</a></li>
    <li><a href=”page4.html”>Page 4</a></li>
  </ul>
</body>
</html>
```      
Save the file and open it in your browser.  Now click on any of the links you added.

### Explanation

We've added the unordered list and each item on the list is surrounded by a `<li></li>` , in between the `<li>` we have added a link (anchor) tag with a link to each page.

### Try It Yourself

Now add that to page2.html , page3.html and page4.html

## Tables


## Conclusion
What you have learned today are the basics in making a web page. All the tags you learned about today what you will use to create nearly all web pages. 

The next lesson is about learning Cascading Style Sheets or CSS for short. CSS adds colour to your page, changes the fonts, and lays items out on the page.  

</body>
</html>
