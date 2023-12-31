# Smart Mingle

Smart Mingle is an application designed to revolutionize event management. It streamlines the process of organizing
events by offering effective planning. Aimed at simplifying the complexities of event coordination, Smart Mingle caters
to various event types, from intimate gatherings to large-scale functions. Its user-friendly interface make it an ideal
solution for both professional event planners and individuals seeking a hassle-free event management experience.
![MockupImage](docs/images/mockup.png)

[View Smart Mingle Platform now](https://smart-mingle-00648c22d190.herokuapp.com/)

# Table of Contents
1. [Smart Mingle](#smart-mingle)
2. [User Experience (UX)](#user-experience-ux)
3. [Project Initial Design](#project-initial-design)
   - [Project Goals](#project-goals)
   - [Agile Methodology](#agile-methodology)
   - [Target Audience](#target-audience)
4. [Database Schema](#database-schema)
5. [Security Features](#security-features)
   - [User Authentication](#user-authentication)
   - [Login Required](#login-required)
   - [Properly GET and POST applied](#properly-get-and-post-applied)
   - [CSRF Protection](#csrf-protection)
6. [Features](#features)
   - [Dynamic Event Display](#dynamic-event-display)
   - [User Interaction](#user-interaction)
   - [Event Management](#event-management)
   - [Event Details and Customization](#event-details-and-customization)
   - [Search Functionality](#search-functionality)
   - [User Authentication and Profile Management](#user-authentication-and-profile-management)
   - [User Profile Personalization](#user-profile-personalization)
   - [Event Modification](#event-modification)
   - [Error Handling](#error-handling)
7. [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Databases Used](#databases-used)
   - [Frameworks Used](#frameworks-used)
   - [Javascript libraries](#javascript-libraries)
   - [Authentication](#authentication)
   - [Technologies Used](#technologies-used-1)
8. [Deployment and Local Development](#deployment-and-local-development)
   - [Local Development](#local-development)
   - [ElephantSQL Database](#elephantsql-database)
   - [Cloudinary](#cloudinary)
   - [Heroku Deployment](#heroku-deployment)
9. [Unit Tests](#unit-tests)
   - [Pytest Setup for Django Project](#pytest-setup-for-django-project)
10. [Testing](#testing)
11. [View on Desktop](#view-on-desktop)
12. [View on Mobile](#view-on-mobile)
13. [References](#references)
    - [Docs](#docs)
    - [Credits](#credits)

## User Experience (UX)

Smart Mingle offers a user experience that is intuitive and engaging, making event planning an enjoyable and seamless
process for its users.

## Project Initial Design

I have used [Balsamiq](https://balsamiq.com/) for the initial design

- ![MockupImage](docs/images/wireframe.png)

## Smart Mingle Application Flow

The Smart Mingle flowchart outlines the user's journey through the application, detailing the process from the entry point to the completion of various functionalities.


### Home Interaction
- **Home Page**: Upon arrival, users are greeted with the Home Page showcasing upcoming events and social media links for broader engagement.
- **Event Selection**: Users can browse and select from the listed upcoming events for more details.
- **Social Media Links**: Direct links are available for users to connect with Smart Mingle on various social media platforms.

### Search Functionality
- **Search Bar**: A feature that allows users to search for events directly from the Home Page.
- **Search Results**: The application displays results on a separate Search Page with pagination support.
- **Event Details**: From the search results, users can click on any event to view its full details.

### Event Detail View
- **Event Page**: Displays comprehensive details about a specific event.
- **Recommended Events**: Suggests a list of related events that users might be interested in.

### Signup/Login Process
- **Signup**: New users can register by filling out a form and completing an email verification process.
- **Login**: Returning users can log in to access their profile and manage events. There's also a password reset feature which includes email verification for security.

### Profile Management
- **Profile Overview**: Authenticated users can view and edit their profiles, including personal information and events.
- **Event Management**: Options are available for users to update or delete their listed events.

### Event Creation
- **Create Event**: Users can add new events through the Create Event Page, which prompts them to enter event details.
- **Confirmation**: After submission, a confirmation page indicates the successful creation of the event.

### Event Update
- **Edit Event**: Users can modify details of their events on the Update Event Page.
- **Update Confirmation**: Post-update, the application confirms the successful modification of the event details.

### Contact Process
- **Contact Us**: A dedicated page is provided for users to submit inquiries or feedback.
- **Submission Confirmation**: After submitting the contact form, users receive confirmation that their details have been successfully recorded.

![Flowchart](docs/images/flowchart.png)

### Project Goals

The project goals for Smart Mingle are centered around creating a comprehensive and user-friendly event management
platform. This includes developing features that cater to various event planning needs, ensuring ease of use for a
diverse user base, and incorporating robust technologies for reliable performance. The overarching aim is to enhance the
event planning experience by providing a seamless, efficient, and intuitive tool that addresses common challenges faced
in event management.

### Agile Methodology

The initial user stories for Smart Mingle were crafted to define essential features, laying the groundwork for early
development stages. This process, following Agile principles, allowed for prioritizing key functionalities and noting
additional features for future inclusion. Agile methodology facilitated task organization and prioritization, utilizing
GitHub's Project Boards for efficient management. By drafting epics and corresponding user stories, the project's
direction was clearly defined, with progress tracked through various stages on the Project Board and tasks categorized
by significance.

![Project Board](docs/images/project/1.png)

![Project Board](docs/images/project/2.png)

![Project Board](docs/images/project/3.png)


Detailed look can be found in the [project board](https://github.com/users/hirakhan95/projects/1)

### Target Audience

The target audience for Smart Mingle includes a wide range of users, from professional event planners to individuals
looking to organize personal events. The application aims to cater to those seeking an efficient and streamlined process
for managing various types of events, whether they are corporate gatherings, social celebrations, or community events.
It's designed to be accessible and user-friendly, appealing to both experienced organizers and those new to event
planning.

## Database Schema

![Schema](docs/images/model/1.png)

## Security Features

### User Authentication

Smart Mingle could employ Django Allauth for robust user authentication. This system manages user registration, login,
logout, and account management functions.

### Login Required

Important features like event details, user profiles, and booking management can be secured to ensure that only
authenticated users can access and modify their event-related information.

### Properly GET and POST applied

All views are only provided with proper GET or POST methods allowed to restrict unrequired calls and secure the system.

### CSRF Protection

The application can integrate Django's CSRF protection to guard against Cross-Site Request Forgery attacks, enhancing
the security of user sessions and form submissions.

## Features

### Dynamic Event Display
- **Home Page Event Showcase**: The home page dynamically displays a selection of events, categorizing them into focus and unfocus sections for a diverse and engaging user experience.
   ![image](docs/images/desktop/1.png)

### User Interaction
- **Contact Page**: Provides a dedicated page for users to contact the site administrators, enhancing user engagement and support.
- **Contact Form Submission**: Handles the submission of contact forms, ensuring user queries or feedback are recorded and addressed.
   ![image](docs/images/desktop/2.png)

### Event Management
- **Event Creation**: Logged-in users can create events, with a straightforward interface that includes various event categories like Corporate, Exhibition, Sport, and more.
- **Event Success Handling**: After event creation, the site confirms success to the user, ensuring a smooth and informative event creation process.
   ![image](docs/images/desktop/19.png)

### Event Details and Customization
- **Event Detail View**: Detailed views for each event are available, including suggestions for similar events, enriching the user's browsing experience.
- **Image Upload and Processing**: Integrates with Cloudinary for image uploads, allowing event organizers to add visual appeal to their events.
- **Date and Time Handling**: Events are handled with precise date and time settings, ensuring accurate scheduling and display.
   ![image](docs/images/desktop/18.png)

### Search Functionality
- **Robust Search**: Users can search for events based on title, location, or category, making event discovery easier and more efficient.
- **Pagination**: Implements pagination in search results, enhancing user experience by organizing content into manageable chunks.
   ![image](docs/images/desktop/11.png)   

### User Authentication and Profile Management
- **Login and Signup Pages**: Dedicated pages for user authentication, supporting a secure and personalized user experience.
- **User Profile Management**: Users can update their profiles, including personal details and event management, fostering a sense of community and ownership.
   ![image](docs/images/desktop/3.png)

### User Profile Personalization
- **Profile Editing**: Users can edit their profiles, enhancing the personalization of the user experience.
- **Profile Picture Handling**: Integrates with Cloudinary for profile picture uploads and transformations, allowing users to customize their profile appearances.
   ![image](docs/images/desktop/17.png)

### Event Modification
- **Delete Event**: Allows logged-in users to delete their events, giving them control over the content they manage.
- **Update Event**: Users can update event details, ensuring that information remains current and accurate. 

### Error Handling
- **Custom Error Pages**: Custom handlers for 404 and 500 errors provide a user-friendly experience even when encountering issues.
   ![image](docs/images/desktop/24.png)


## Technologies Used

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Databases Used

* [ElephantSQL](https://www.elephantsql.com/) - Postgres database
* [Cloudinary](https://cloudinary.com/) - Online static file storage

### Frameworks Used

* [Django](https://www.djangoproject.com/) - Python framework
* [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Booststrap 

### Javascript libraries

* [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Bootstrap
* [TinyMce](https://www.tiny.cloud/) - Tiny MCE

### Authentication

* [AllAuth](https://docs.allauth.org/en/latest/) - AllAuth

### Technologies Used

* [Github](https://github.com/) - Storing the code online.
* [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the site.
* [Google Fonts](https://fonts.google.com/) - Import main font the website.
* [JSHint](https://jshint.com/) - Used to validate JavaScript.
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML.
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS.
* [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python.

## Deployment and Local Development

* PyCharm - For django development on Python
* VSCode -  For user interface on HTML, CSS, JavaScript

### Local Development

#### How to Fork

1. Log in(or Sign Up) to Github
2. Go to repository for this project
3. Click the fork button in the top right corner

#### How to Clone

1. Log in(or Sign Up) to Github
2. Go to repository for this project
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link
   shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for
   the cloned directory.
5. Type the following command in the terminal (after the git clone you will need to paste the link you copied in step 3
   above)
6. Set up a virtual environment.
7. Install the packages from the requirements.txt file - run Command pip3 install -r requirements.txt

### ElephantSQL Database

1. Click Create New Instance to start a new database.
2. Provide a name (this is commonly the name of the project: tribe).
3. Select the Tiny Turtle (Free) plan.
4. You can leave the Tags blank.
5. Select the Region and Data Center closest to you.
6. Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary

1. For Primary interest, you can choose Programmable Media for image and video API.
2. Optional: edit your assigned cloud name to something more memorable.
3. On your Cloudinary Dashboard, you can copy your API Environment Variable.
4. Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key.

### Heroku Deployment

* Log into Heroku account or create an account.
* Click the "New" button at the top right corner and select "Create New App".
* Enter a unique application name
* Select your region
* Click "Create App"

#### Prepare environment and settings.py

* In your workspace, create an env.py file in the main directory.
* Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
* Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
* Comment out the default database configuration.
* Save all files and make migrations.
* Add the Cloudinary URL to env.py
* Add the Cloudinary libraries to the list of installed apps.
* Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage
  path.
* Link the file to the templates directory in Heroku.
* Change the templates directory to TEMPLATES_DIR
* Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

#### Add the following Config Vars in Heroku:

* SECRET_KEY - This can be any Django random secret key
* CLOUDINARY_URL - Insert your own Cloudinary API key
* PORT = 8000
* DISABLE_COLLECTSTATIC = 1 - this is temporary, and can be removed for the final deployment
* DATABASE_URL - Insert your own ElephantSQL database URL here

#### Heroku needs two additional files to deploy properly

* requirements.txt
* Procfile

#### Deploy

1. Make sure DEBUG = False in the settings.py
2. Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
3. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy
   Branch to deploy manually. Manually deployed branches will need re-deploying each time the GitHub repository is
   updated.
4. Click 'Open App' to view the deployed live site.

Site is now live

## Unit Tests

# Pytest Setup for Django Project

This project uses `pytest` for running tests. Pytest is a powerful testing framework for Python that allows you to write
simple yet scalable test cases.

## Setting Up Pytest

### 1. Install pytest and pytest-django

If not already installed, you can install these packages using pip:

```bash
pip install pytest pytest-django
```

### 2. Create Database

Create database for testing you can also use docker to create one using following command

```bash
docker run -it -d --name <database-name> -p <port>:<port> -e POSTGRES_PASSWORD=<password> <user-name>
```

### 3. Provide credentials

Provide following configuration in env.py

````bash
os.environ['TEST_DB_NAME'] = < TEST_DB_NAME >
os.environ['TEST_DB_USERNAME'] = < TEST_DB_USERNAME >
os.environ['TEST_DB_PASSWORD'] = < TEST_DB_PASSWORD >
os.environ['TEST_DB_HOST'] = < TEST_DB_HOST >
os.environ['TEST_DB_PORT'] = < TEST_DB_PORT >
````

### 4. Running Tests 
To run your tests, use the following command in your terminal:

```bash
pytest
```

### Note !!
1. Ensure your test database is set up and accessible.
2. When running tests, ensure your environment variables are correctly set, especially if you're using a separate test database configuration.


## Testing

Please see [TESTING.md](docs/TESTING.md) the detailed testing performed.

## View on Desktopn

Please see [DESKTOP DESIGN](docs/DESIGN_DESKTOP.md)

## View on Mobile

Please see [MOBILE DESIGN](docs/DESIGN_MOBILE.md)

## References

### Docs

* [Code Institute](https://learn.codeinstitute.net/dashboard)
* [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Django docs](https://docs.djangoproject.com/en/4.2/)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
* [Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)
* [Cloudinary](https://cloudinary.com/documentation/diagnosing_error_codes_tutorial)
* [Pytest](https://docs.pytest.org/en/7.4.x/)

### Credits

* [Ilustrated Pics](https://www.freepik.com/)
* [Event Images](https://openai.com/dall-e-2)
* [Stack Overflow](https://stackoverflow.com/)
* [Github Corner](https://gist.github.com/lyoshenka)
