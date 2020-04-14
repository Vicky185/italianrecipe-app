# Italian Gluttony 

## A Recipe Manager Application for Italian Cuisine Lovers.

### An application manager which uses Python to relate to a MongoDB database.
In this app, users will be able to view, add/create/upload, share, edit and delete all family, famous and favourite italian recipes.  

_[Visit the website here](http://italia-recipes-app.herokuapp.com/index "Visit the website here")_

The website app is fully responsive and uses Mongo DB to hold a user's recipes collection. Any user can search for recipes using the search box, can view all recipes, can create, edit and delete recipes. 

The 'Recipes' page, lists and shows all recipes in the order that they are uploaded. This page also has pagination which increases with the more recipes added. 

Each recipe is held in a 'card' which is a snippet of what each single recipe holds. Each individual recipe page can be found through these card snippets. It will load a single page for the recipe entry into the database. At the bottom of the page the user can edit or delete the recipe. 


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
* register and login options, to add additional security and to allow users to subscribe and have more visible ownership over their Recipes
* options to share the recipe snippet on social media
* advanced search field
* italian recipe blog - insights into the most popular options



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
    *Scroll to top button - https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
* Flask - as the documentation 
* Flask WTF Forms - for the form fields and input, also as a shortcut
* Config - as the python file to support security and adding secret key
* JQuery
    * For dropdown and collapsable navbar - https://mdbootstrap.com/docs/jquery/navigation/hamburger-menu/
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
* The user is able to see the menu clearly and access the other pages on the site
* The user is able to search keywords in the search bar, then upon a keyword search, the user is taken to a search results page
* The user is able to view each recipe individually and clearly view the ingredients/method
* The user is able to view a small image of what the recipe looks like
* The user is able to store/create/upload a new recipe
* The user is able to edit or delete a previously uploaded recipe
* When the user adds a recipe, they are notified if they have filled the form wrong
* The user is able to have a dropdown menu when on a ipad/mobile device
* The user is able to scroll down to the bottom of the page and quickly scroll up with scroll up button on bottom right of page
* The user is able access all recipes through the menu and see clearly when their recipe has been updated/added/deleted.

*Examples:*
* when user clicks 'Click here for more...' button on the small recipe card/snippet, they will be taken to a new page. If they choose to delete they will be asked to confirm. If they ask to edit, they will be taken to a page of the recipe in the form and ready to be updated. If they remove all content from one field, an error will read: 'Please fill in this field'. This is the same when they create a recipe from scratch. 

*For a decription of the different screen sizes, please visit _[here](https://github.com/Vicky185/italianrecipe-app/blob/master/descriptionofscreens.md "here")_

#### Manual Testing

My tests to ensure that all is working:
* Deployment to Heroku and loading the Home page. All worked and the styles were present. 

* Click on the 'Click for more button' on each and all of the cards to check that the wiring to the database was working and located/loaded the correct information for that recipe. 

* Create Recipe - Tested that it was an empty form to open up with. Entered correct information and checked that once added, it opened the all recipes page, and the recipe was added to the end of the list of recipes. In addition, when filling out the form the test was to check if there was an error that the fields were all filled out and filled out correctly. If error, then you can't progress to upload the recipe and screen smoothly scrolls up to that field. When you create a recipe, the new information is committed to the database and uploaded and added to the all recipes page to which the user is redirected. 

* Edit Button - On the individual recipe page, tested that this loaded in the site and took you to a form very similar to 'Create' form. Edited one field to check it would register and removed information to check if error on empty field. When you click update the data on that recipe is changed and committed to the database. This then redirects the user back to the all recipes page. 

* Delete Button - On the individual recipe page, tested that the delete button would take user through to new page asking them to confirm they wish to delete the recipe from the database. Once deleted, the recipe is removed from the database and will no longer be found through search and the all recipes page. 

* All Recipes on both the home page, through the 'click here for more button' and on the search are done so by searching for any recipes on the page and getting their ID number and going to that recipe details page and then looking at the recipe page contents.

* As the site is built with a responsive design it works for mobiles and I have checked it on iphones and android. I have also check it on a Surface Pro, Desktop Laptop and a Mini Ipad. I have also tested it on various browsers.


# Deployment
***

This project was built and coded using [Gitpod](https://gitpod.io/workspaces/ "Gitpod") and then uploading via Git onto [GitHub](https://github.com/Vicky185/italianrecipe-app "GitHub"). For version control, GIT was used and then all uploaded to Github.

This project also used a MongoDB database and this was connected to Heroku (on the heroku app, the connection between GitHub and Heroku was activated to facilitate deployment and testing). The details of the database connection are found in the app.py file and requirements.txt - the project uses the os class environ method to point to Heroku to the project's config variable (MONGODB_URI) to keep the production database connection string a secret and to add security. In addition to a requirements.txt file, this project also used a Procfile to help Heroku recognise the commands which were being run by the app's dynos. It was also used to help Heroku understand how to run different parts of the app, including app.py. 

On first deployment, the requirements.txt file was forgotten as was the Procfile and so there were errors with the coding. However, this was rectified and whenever new packages were added, the requirements.txt file was updated. Google and the Code Institute's course walkthrough helped me realise this! To deploy I followed the following:
* git add .
* git commit -m "commit message"
* git push
_At this stage, due to the connection between my heroku and github, once committed to github the app was deployed automatically to Heroku._

When the app was running, the database was loaded manually using the create_recipe function/form. 


If you want to access the project code and view the repository please log into GitHub and go to select the 'Vicky185/italianrecipe-app' repository. <enter>
From there you can access the [HTML Templates, the Static files including CSS and also the Python files](https://github.com/Vicky185/italianrecipe-app "Italian Recipe App"). <enter>
 <enter>
 *To add this to your own repository, please go to the 'Code' tab and click the green button 'Clone/Download'*. 


If you want to access the project through Heroku, please search: [Heroku App File](https://dashboard.heroku.com/apps/italia-recipes-app "Italia Recipe App").



# Credits and Acknowledgements
***

1. Text and Recipe Content
* For all of the **recipes** section, I used information from [BBC Good Food](https://www.bbcgoodfood.com/ "BBC Good Food")

2. Media
* For the photos I used various sources:
    * Home Page - [Pexels](https://www.pexels.com/photo/group-of-people-making-toast-3184183/ "Pexels"))
    * Recipes/Card Images - [Recipes](https://www.pexels.com/search/italian/ "Pexels"))
    * Recipes/Card Images - [BBC Good Food Images](https://www.bbcgoodfood.com/ "BBC Good Food")

3. Acknowledgements

Thank you to my mentor, Spencer Barriball, for his patience and support in leading me to the right direction on my code, links and styling. He also really helped me grapply with Python, especially introducing me to the wtf forms and how they can help the process and make the fields really neat on a page. <enter>
He helped and made lots of great suggestions on improving the site.

Inspiration for the style of the site - 
* [Food Gawker](https://foodgawker.com/)
* [Not without salt](http://notwithoutsalt.com/)

Help with coding and styling the site - 
* [W3Schools](https://www.w3schools.com/)
* [Scrolling to top](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
* [StackOverflow](https://stackoverflow.com/)


