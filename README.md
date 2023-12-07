# The Book Booth:


![The Book Booth Mockup](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c45c26db-6090-40fd-afec-047954dba6fc)


The Book Both is management system to view availabe books at a local phone booth library. The application was created to allow users to view the available books prior to visiting a phone booth library and to add a book that is currently available. 

A phone booth library is a repurposed phone booth to accomodate books for the community to borrow. The idea is that a reader can borrow a book and return it later, or leave another book in it's place. 


# Purpose and Target Audience:
 **Problem Statement:** The Phone booth libraries are located all across the country making it possible for individuals to borrow and donate books to the collections at specified phone booths. The user finds it difficult to know which books are available prior to reaching the phone booth and is unable to communicate to other users that they have added a new book.

**Purpose:** This book management app will list the available books and show if they are available to borrow. Users will also be able to add a book to the collection as well edit and delete the book they added to ensure the application is up-to-date.

**Target Audience:** The primary target audience include avid readers who enjoy using phone booth libraries as well as individuals who want to be apart of a reading community where they can share their thoughts on the books they have completed in the collection.



# Persona and User Stories:

Emma is a passionate reader who loves immersing herself in different worlds through books. She spends most of her free time indulging in her favorite hobby and is always on the lookout for new and exciting reads. She has a phone booth library in her city and would like to view the books that are available to borrow prior to visiting. 

## User Stories:
* As an avid reader I want to be able to browse the available books at The Book Booth before visiting.
* As a user I want to be able to add a book to the collection with the relevant information so that other users can view the latest books available in the phone booth library.
* As a user I want to be able to create an account so that I can view the available books and book details.
*  As an avid reader I want to be able to browse the available books at The Book Booth before visiting.
* As a user I want to be able to edit and delete books that I have added so that the books stay up to date.
* As a user I want to explore new books so that I can discover new books to read.
* As a user I want to be able to read more information about a book so that I can be sure that the book is good choice for me.
* As an admin I want to be able to moderate the book additions so that I can ensure the books are appropriate and relevant to the users.
* As a user I want save money on books by borrowing books that myself and my family can enjoy so that we can spend money on other things we value.

## Wireframe & Initial Design:
### Home Page
![1](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a17458a2-fd0b-45cb-af44-387ed524fef6)

### (Logged in) Browse books
![1](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a4c56a06-3692-467d-813a-ba3797d3087c)

### Add a Book
![Add a book wireframe](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c0379553-0906-4d77-aca6-beb8fc6834d9)

### Book Detail Page

![Book Details Wireframe](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/467fa65e-eb66-4b21-94af-f9090b6a54ab)

## Agile:
This project was created using Agile principles via a projectboard on Github. This is the first time I have implemented Agile as an individual developer.

![project board](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/98b7d24d-7234-4155-af15-df72403659f9)

## Priority Features:

### Home Page:

#### Navbar & Hero Image:
![home](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4f033ade-4485-40c2-ac2d-5fc5641b5cb7)
The landing page provides an introduction to the website with a call to action button encouraging new users to sign up. Signing up and logging in allows them access to view the available books and to add a book to the collection.
The navigation bar is valuable for users as it provides quick and easy access to important sections of the website. The navigation bar includes links to Home, Books, Add a Book, Register/Logout and Sign In. Displaying a hero image using graphics are both aestetic and a node to the repurposed phone booths that have been transformed into local libraries around the country.


#### Registration:

Registration allows users to view the available books and the relevant book details at The Book Booth library. It allows them to add a book as well as edit and delete their addition to ensure the book collection available is updated regularly. 

![signup](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0b6b2b83-d426-4e63-805b-09a6dcdde550)



#### Sign In:

![sign-in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/6a1d9a16-2211-4403-88a1-3ec1b506cef4)


#### Books:

![books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/54c96d8e-6bc3-403f-a8ad-1c4188b60a6e)


#### Add a Book:

![add a book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/8e15c1d9-193f-4032-b147-0969c3b45bab)


The form allows users to easily add a book to the library which will then be visible on the  books page for the users to browse. Users are also able to edit and delete a book they themselves have added giving them full control over their own contributions.


#### Book Details:

![book detail](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e88f0274-670b-4a76-8ef8-7c44a5f440a7)

Users are able to find more information about the book they are interested in. The Book details include the title, author and a brief summary of the book along with an book cover image. This provides users with sufficient information about the book.

#### Sign Out:

#### Footer:

![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fde543e6-0ee2-4c17-b8a8-436d4e824f4d)

Links in the footer redirect to respective social media pages. 
It allows users to stay connected with the The Book Booth on social media platforms, keeping them informed about the any changes that may occur over time.


# Future Features:

* Implement a review system so readers can share their thoughts about books that they have completed. This will give others a better idea of whether the book is a good fit for them. 
* Display if a book is available with a status (Available, Not Available).
*  Allow users to reserve a book beforehand.
* A search engine where users can search for books by title, author and genre.
* Provide locations of nearest libraries.
* Provide a way for the users to engage and form a secure community




## Data Models:


| Book   |            |   |
|----------|:-------------:|------:|
| Title |  CharField |  |
| Author |  CharField   |   FK |
| ISBN | CharField |     |
| User |  CharField | FK |
| Genre |  CharField   |   FK |
| Language | CharField |  FK   |
| Summary |  TextField |  |



| Genre   |            |   |
|----------|:-------------:|------:|
| Category |  CharField | FK |


| Language   |            |   |
|----------|:-------------:|------:|
| Language |  CharField | FK  |

| Author  |            |   |
|----------|:-------------:|------:|
| Name |  CharField | FK  |

## User Flow Chart:
![The Book Booth Flowchart](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7727f007-8e2e-45fc-b955-57e2d50d1e98)

The Flowchart served as an efficent way to make important decisions when creating the app. It helped me narrow down which decision were important for the users and admin as well as establishing the appropriate authentication. It also helped me decide which features were the most important i.e adding a book and viewing a list of books that are available to borrow at The Book Booth Library.

# Validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F) | ![home page validate](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/2ba0ff6e-6159-47e9-ad4c-2fe954589ca8) | Pass: button is a descendant of a tag |
| Books | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fbooks%2F) | ![Validate Books page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b7c018c4-a68a-43ee-97c5-778658bbf705) | Pass: No Errors |
| Add a Book | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fadd_book%2F) | ![validate adda book page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/95eb01b9-22fc-43c4-93de-0ebcd1263467) | Pass: No Errors |
| Sign In| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Flogin%2F) | ![validate sign in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/872629ce-e50d-4870-845b-ed699f9178dc) | Pass: No Errors |
| Register| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![validate sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5e042af-b3d5-4718-bc50-ef319ba1a1c3) | unclosed elements main and div |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=enhttps://jigsaw.w3.org/css-validator/validator) | ![validate css](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/200fc160-1092-4cd0-bba4-2ab1a721eb72) | Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/run.py) | ![screenshot](documentation/py-validation-run.png) | W291 trailing whitespace |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py) | ![screenshot](documentation/py-validation-settings.png) | E501 line too long |
| Blog views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/blog/views.py) | ![screenshot](documentation/py-validation-blog-views.png) | Pass: No Errors |
| Checkout urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/checkout/urls.py) | ![screenshot](documentation/py-validation-checkout-urls.png) | W292 no newline at end of file |
| Profiles models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/profiles/models.py) | ![screenshot](documentation/py-validation-profiles-models.png) | Pass: No Errors |
| x | x | x | repeat for all remaining Python files |




# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including desktop, mobile and tablet size.

Full testing was performed on the following devices:

PC:
* Desktop PC
* Laptop:
* Macbook Air 2018 13.3-inch screen
* Mobile Devices:
* Google Pizel 4a

 Desktop PC tested the site using the following browsers:

* Google Chrome
* Safari
* Microsoft Edge


I can confirm that the site is responsive and looks as expected good on different screen sizes.


# Testing:


# Tools and Technologies Used:
The technologies implemneted in this application included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* ElephantSQL used as the Postgres database.
Heroku used for hosting the deployed back-end site.
* Cloudinary used for online static file storage.
Canva Utilized for collaborative design and prototyping(wireframes).

* Google and Stack Overflow utilized for general research or solving a big, information gathering, and various online tools.


# Languages Used:
* HTML5
* CSS
* Python


# Deployment: 

Deployment
To deploy the project to Heroku, I followed these steps:

* Creating Heroku App:
* Logged into Heroku.
* Selected 'Create New App' from the dashboard.
* Chose a unique app name.
* Selected region based on the location.
* Clicked 'Create App'.
* Connecting to GitHub:

From the Heroku dashboard, navigated to the 'Deploy' tab.
* Under 'Deployment Method', chose 'GitHub'.
* Searched and selected the repository by name.
* Clicked 'Connect'.
* Setting Environment Variables:
* Went to the 'Settings' tab.
* Located 'Config Vars' and clicked 'Reveal Config Vars'.
* Added the necessary variables.

Manual Deployment:

* Went back to the 'Deploy' tab.
* Located 'Manual deploy' at the bottom of the page.
* Clicked 'Deploy Branch' and waited for the build to finish.
* Accessing the App:
* After the deployment was successful, I found and clicked 'Open app' at the top of the app dashboard.
* These steps ensured that the project was successfully deployed to Heroku. 


