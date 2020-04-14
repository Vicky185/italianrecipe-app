# Italian Gluttony 

## A Recipe Manager Application for Italian Cuisine Lovers.

### An application manager which uses Python to relate to a MongoDB database.
In this app, users will be able to view, add/create/upload, share, edit and delete all family, famous and favourite italian recipes.  

_[Visit the website here](http://italia-recipes-app.herokuapp.com/index "Visit the website here")_



## The User Experience (UX)
***

#### Project purpose

To provide an application which makes you immediately think of Italy. This is a website for Italians, fans of Italian food and cuisine, and those who love to cook. They will be able to share recipes with others but also view what others have uploaded and continue to inspire their cooking. 

Italian food has developed over time and still remains to be one of the most popular dishes in the world - helped significantly by 'pizzas'! The brief of this project was to target those who love italian food, love to cook and need a place to store their recipes which is a site that is user friends and tailored to their wants/needs. <enter>

The following requirements were set at the beginning of the project:
* primary target audience are italians, lovers of italian food, and amateur cooks who want/need a place to store recipes
* the look needs to speak and feel italian
* needs to have an option to create, edit and update, as well as delete recipes
* needs to have a page where you can see all the recipes
* needs to be able to search for recipes.

#### User stories

As a general user, 
* I want the page to be simple and easy to use

As an existing chef/amateur cook, I want 
* to immediately think of Italy
* the page to feel and look like a cooking website
* to share and upload recipes option
* to be able to edit any recipes if I make a mistake
* to have an app to store my recipes and make it easy to find them

As a potential user and fan of Italian food, I want 
* to find and view new recipes to try
* to be able to add recipes if i want to



## Features
***

For this site, a range of features were used:
* HTML, CSS, JavaScript, MongoDB database, Python, Flask, WTF Forms, Config, Heroku, 
* Mobile-first approach
* Tested on Browsers (e.g. Google Chrome and Mozilla Firefox)
* Responsive navigation, including a 'scroll to top button'
* Contact form and option to subscribe for fans to contact the band with enquiries about personal performances
* An 'About' section providing information on the band's history and insight into the group members and who they are
* Audio clips for new and existing fans to listen to their favourite songs (a few on the homepage but options to find more)
* Video clip to watch the band in action
* Social media access links for fans to see what the band are up to on YouTube, Twitter and Facebook

*Additional features in the future will include:*
* additional gallery for fans to see more pictures throughout time of the band
* example and downloadable set lists from previous events
* testimonials from fans who have hired the band for performances



## Structure
***

### Skeleton 

##### Wireframes:

* [Home page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/home-page.jpg "Home page")
* [One Recipe page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/only-one-recipe-page.jpg "One Recipe page")
* [All Recipes page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/look-all-recipes.jpg "All Recipes page")
* [Add Recipe page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/add-recipe.jpg "All Recipes page")
* [Edit Recipe page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/edit-page.jpg "Edit Recipe page")
* [Delete Recipe page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/delete-page.jpg "Delete Recipe page")
* [Search Recipe page](https://github.com/Vicky185/italianrecipe-app/blob/master/static/Wireframes/search-page.jpg "Search Recipe page")

### Surface / Design

##### Fonts

* Sacramento - a cursive font, very much portraying an Italian, classic but also chef theme - *https://fonts.google.com/specimen/Sacramento*

* Raleway - for general text, less standout but also a font style which speaks classic, sleek and in line with the cooking and Italian theme - *https://fonts.google.com/specimen/Raleway*

##### Colours 

![Italian Colour Palette](static/images/colours.jpeg "Italian colour palette")
![Colour Palette](static/images/colours3.png "Colour palette")



## Technologies
***

Below is listed all of the technologies used to create this site:

* Python
* HTML
* CSS
* JavaScript
    ** Scroll to top button - https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
* Flask - as the documentation 
* Flask WTF Forms - for the form fields and input, also as a shortcut
* Config - as the python file to support security
* JQuery
    ** For dropdown and collapsable navbar - https://mdbootstrap.com/docs/jquery/navigation/hamburger-menu/
* Bootstrap - https://getbootstrap.com/
* Google Fonts - https://fonts.google.com/
* Gitpod - as IDE
* GitHub - as the remote backup used on this project and for other project users to view the code
* Heroku - as the deployment method
* MongoDB - as the database used for all information that is uploaded and displayed in each recipe


## Testing
***

#### UX

* The user is able to see a couple of recipes on the home page
* The user is able to search keywords in the search bar, then upon search is taken to a results page
* The user is able to view each recipe individually and clearly view the ingredients/method
* The user is able to view a small image of what the recipe looks like
* The user is able to store/create/upload a new recipe
* The user is able to edit or delete an uploaded recipe
* When the user adds a recipe, they are notified if they have filled the form wrong
* The user is able to have a dropdown menu when on a ipad/mobile device
* The user is able to scroll down to the bottom of the page and quickly scroll up with scroll up button on bottom right of page
* The user is able access all recipes


*Examples:*
* when user clicks 'Click here for more...' button on the small recipe card/snippet, they will be taken to a new page. If they choose to delete they will be asked to confirm. If they ask to edit, they will be taken to a page of the recipe in the form and ready to be updated. If they remove all content from one field, an error will read: 'Please fill in this field'. This is the same when they create a recipe from scratch. 

*For a decription of the different screen sizes, please visit _[here]( "here")_

#### Manual Testing

*Examples:*



# Deployment
***

This project was built using [Gitpod](https://gitpod.io/workspaces/ "Gitpod") and then uploading via Git onto [GitHub](https://github.com/Vicky185/italianrecipe-app "GitHub").

If you want to access the project please log into GitHub and select the 'Milestone Project 1 - The Monkees Website' repository. <enter>
From there you can access the [HTML code and CSS styling](https://ide.c9.io/vls1893/themonkees-site "HTML code and CSS styling"). <enter>
You can also see the site via the 'Settings' tab, then scroll down to 'GitHub Pages' (if link not there, select 'Master branch' from dropdown). <enter>
The site will refresh then you will be able to view it after 5-10 minutes. 

*To add this to your own repository, please go to the 'Code' tab and click the green button 'Clone/Download'*. 


# Credits and Acknowledgements
***

1. Text
* For the *About* section, I used information from [Wikipedia](https://en.wikipedia.org/wiki/The_Monkees "Wikipedia")
2. Media
* For the photos I used various sources:
    ** Carousel - [Image 1](https://ultimateclassicrock.com/more-of-the-monkees/)
    ** Carousel - [Image 2](https://www.post-gazette.com/ae/music/2019/02/21/Peter-Tork-offbeat-bassist-singer-the-Monkees-dies-77-music-television/stories/201902210124)
    ** Micky Dolenz - [Image 3](http://www.fanpop.com/clubs/micky-dolenz/images/31390175/title/micky-dolenz-photo)
    ** Contact page background - [Image 4](https://www.google.com/search?hl=en-GB&q=monkees&tbm=isch&tbs=simg:CAQSlwEJyK_1mQe1Era4aiwELEKjU2AQaBAg9CEIMCxCwjKcIGmIKYAgDEiiwG7gfyx-dG7kbtR_1ZH8gfrBvBH9Av0S-zL6kluC_1NL8YvoyXdL8kvGjCwluZnNKUI0PqPQcJi_1y8AaVTHpyu7cAfH-ezXJ6Nkv-hBwN6TUR4phelmmEBwslsgBAwLEI6u_1ggaCgoICAESBMG4F8gM&sa=X&ved=0ahUKEwi-xbuqvqjiAhU4WRUIHe1hAucQwg4IKygA&biw=1366&bih=608#imgrc=yxEoRp-Qbe8QKM:)
* For the songs/video I used [The Monkees, Youtube](https://www.youtube.com/channel/UCv1oY0OLtsEySHeP1TkYNqA)


3. Acknowledgements

Thank you to my mentor, Spencer Barriball, for his patience and support in leading me to the right direction on my code, links and styling.<enter>
He helped and made lots of great suggestions on improving the site.

Inspiration for the style of the site - 
* [The Beach Boys](https://www.thebeachboys.com/#off-canvas)
* [The Beatles](https://www.thebeatles.com/)

Help with coding and styling the site - 
* [W3Schools](https://www.w3schools.com/)
* [Scrolling to top](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)



