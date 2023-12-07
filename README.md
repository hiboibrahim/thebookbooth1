# The Book Booth:


![The Book Booth Mockup](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c45c26db-6090-40fd-afec-047954dba6fc)


The Book Both is management system to view availabe books at a local phone booth library. The application was created to allow users to view the available books prior to visiting a phone booth library and to add a book that is currently available. 

A phone booth library is a repurposed phone booth to accomodate books for the community to borrow. The idea is that a reader can borrow a book and return it later, or leave another book in it's place. 


# Purpose and Target Audience:
 **Problem Statement:** The Phone booth libraries are located all across the country making it possible for individuals to borrow and donate books to the collections at specified phone booths. The user finds it difficult to know which books are available prior to reaching the phone booth and is unable to communicate to other users that they have added a new book.

**Purpose:** This book management app will list the available books and show if they are available to borrow. Users will also be able to add a book to the collection as well edit and delete the book they added to ensure the application is up-to-date.

**Target Audience:** The primary target audience include avid readers who enjoy using phone booth libraries as well as individuals who want to be apart of a reading community where they can share their thoughts on the books they have completed in the collection.



# Persona and User Stories:

Emma is a passionate reader who loves immersing herself in different worlds through books. She spends most of her free time indulging in her favorite hobby and is always on the lookout for new and exciting reads. She has a phone booth library in her city and would like to view the books that are available to borrow prior to visiting. She also appreciates book reviews to give her a better idea of whether the book is right for her and enjoys sharing her thoughts on the books that she has read with others.

## User Stories:
* As an avid reader I want to be able to browse the available books at The Book Booth before visiting.
* As a user I want to be able to add a book to the collection with the relevant information so that other users can view the latest books available in the phone booth library.
* As a user I want to be able to create an account so that I can view the available books and book details.
*  As an avid reader I want to be able to browse the available books at The Book Booth before visiting.
* As a member I want to be able to edit and delete books that I have added so that the books stay up to date.

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
This project was created using Agile prinicipes via a projectboard on Github. This is the first time I have implemented Agile as an individual developer

add project board and link to vboard

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


#### Sign Out:

#### Books:

![books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/54c96d8e-6bc3-403f-a8ad-1c4188b60a6e)


#### Add a Book:

![add a book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/8e15c1d9-193f-4032-b147-0969c3b45bab)


The form allows users to easily add a book to the library which will then be visible on the  books page for the users to browse. Users are also able to edit and delete a book they themselves have added giving them full control over their own contributions.


#### Book Details:

![book detail](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e88f0274-670b-4a76-8ef8-7c44a5f440a7)

Users are able to find more information about the book they are interested in. The Book details include the title, author and a brief summary of the book along with an book cover image. This provides users with sufficient information about the book.




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


# Validation
## HTML
I have used W3 to validate all of my HTML pages.
| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F) | ![screenshot]![home page validate](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/2ba0ff6e-6159-47e9-ad4c-2fe954589ca8)
 | Pass: button is a descendant of a tag |
| Books | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fbooks%2F) | ![screenshot]![Validate Books page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b7c018c4-a68a-43ee-97c5-778658bbf705)
 | Pass: No Errors |
| Add a Book | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fadd_book%2F) | ![screenshot]![validate adda book page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/95eb01b9-22fc-43c4-93de-0ebcd1263467)
 | Pass: No Errors |
| Sign In| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](![validate sign in ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/872629ce-e50d-4870-845b-ed699f9178dc)
) | Pass: No Errors |
| Register| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot]![validate sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5e042af-b3d5-4718-bc50-ef319ba1a1c3)
 | unclosed elements main and div |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](![validate css](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/200fc160-1092-4cd0-bba4-2ab1a721eb72)
) | Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.




## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Books | Add a Book | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-about.png) | ![screenshot](documentation/browser-chrome-contact.png) | ![screenshot](documentation/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-about.png) | ![screenshot](documentation/browser-firefox-contact.png) | ![screenshot](documentation/browser-firefox-etc.png) | Works as expected |

| Safari | ![screenshot](documentation/browser-safari-home.png) | ![screenshot](documentation/browser-safari-about.png) | ![screenshot](documentation/browser-safari-contact.png) | ![screenshot](documentation/browser-safari-etc.png) | Minor CSS differences |
|  |Microsoft Edge ![screenshot]![microsoft edge browser](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/8e98bcba-7190-4459-9869-6c7407b640aa)
 | ![screenshot](documentation/browser-safari-about.png) | ![screenshot](documentation/browser-safari-contact.png) | ![screenshot](documentation/browser-safari-etc.png) | Minor CSS differences |


# Testing:

## Responsiveness:
Development tools were used to test responsiveness on varying sized devices including desktop, mobile and tablet size.


## Technologies Used:
The technologies implemneted in this application included HTML5, CSS, Bootstrap, Python and Django.





