---

title: Gorey Coder Dojo HTML Lesson 2

---


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

What we've done here is to add the style sheet to the page. As we have not added any styles yet we won't see anything.

There are 2 other ways to add styles to a page, we won't cover them just yet. But you can look up some of the website resources at the end of the page to learnmore.


## CSS

You apply CSS to selectors. There are 3 different types of selectors. For the moment we'll concentrate on the html tag selectors e.g. body or p

To apply CSS you use property:value.


In you style.css file add the following.

```
body{
  font-size:16px;
}

h1{
  font-size:23px;
  color:navy;
}

p{
  font-size:10px;
  color:red;
}

```
   
### Explanation
   
We have added 2 styles to 3 selectors. We have changed the font-size for the everything in the body section to 16px, this is applied to the whole document.

We then override the font-size on the h1 and p tags. We also change the color for the fonts with the color style.

When using sizes in CSS, in this case px, there are a number of different units we can use:

+ em - e.g. font-size: 3em
+ px - e.g. font-size: 14px 
+ pt - e.g. as font-size: 14pt
+ % - e.g. as font-size: 50%

Usually when writing pages for a website you would use em or %, but for the purposes of learning css using px as unit of measurement is easier. 

When using colors (note the American way of spelling, it's not the European way, colour).

There are several ways to state a color with CSS. Several ways to state the color red are:

+ red
+ rgb(255,0,0)  (rgb values between 0 and 255)
+ rgb(100%,0%,0%)  (rgb values percentage)
+ #ff0000 (hexadecimal)
+ #f00 (hexadecimal shorthand)

You would usually use rgb or hexadecimal when building a webpage but for now we'll use the following:

aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, orange, purple, red, silver, teal, white, and yellow



### Try It Yourself

Add the color purple to the body tag, change the color on the li element to lime.

Let's introduce a new property called background-color. Set you body background color to green. and your h1 tag background color to white.

By now you should have a very interesting looking page!


## Fonts

Before we start into fonts, in your style sheet add the following  ``` /* ``` before your text and after all the text add ``` */ ```
These are comments and anything between them are ignored. They are good for leaving little notes to yourself about the blocks of css you write.

So we've commented out the css you've already written.

Now we'll add the following:

```
body{

}

font-family
This is the font itself, such as Times New Roman, Arial, or Verdana.

The font you specify must be on the user's computer, so there is little point in using obscure fonts. There are a select few 'safe' fonts (the most commonly used are arial, verdana and times new roman), but you can specify more than one font, separated by commas. The purpose of this is that if the user does not have the first font you specify, the browser will go through the list until it finds one it does have. This is useful because different computers sometimes have different fonts installed. So font-family: arial, helvetica, for example, is used so that similar fonts are used on PC (which traditionally has arial, but not helvetica) and Apple Mac (which, traditionally, does not have arial and so helvetica, which it does normally have, will be used).

Note: if the name of a font is more than one word, it should be put in quotation marks, such as font-family: "Times New Roman".

font-size
The size of the font. Be careful with this - text such as headings should not just be a paragraph in a large font; you should still use headings (h1, h2 etc.) even though, in practice, you could make the font-size of a paragraph larger than that of a heading (not recommended for sensible people).

font-weight
This states whether the text is bold or not. In practice this usually only works as font-weight: bold or font-weight: normal. In theory it can also be bolder, lighter, 100, 200, 300, 400, 500, 600, 700, 800 or 900, but seeing as many browsers shake their heads and say "I don't think so", it's safer to stick with bold and normal.

font-style
This states whether the text is italic or not. It can be font-style: italic or font-style: normal.

text-decoration
This states whether the text is underlined or not. This can be:

text-decoration: overline, which places a line above the text.
text-decoration: line-through, strike-through, which puts a line through the text.
text-decoration: underline should only be used for links because users generally expect underlined text to be links.
This property is usually used to decorate links, such as specifying no underline with text-decoration: none.

text-transform
This will change the case of the text.

text-transform: capitalize turns the first letter of every word into uppercase.
text-transform: uppercase turns everything into uppercase.
text-transform: lowercase turns everything into lowercase.
text-transform: none I'll leave for you to work out.


    
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


