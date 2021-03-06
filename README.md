[![GitHub]](https://github.com/marks530/fruit_and_veg_store.git)


<h1 align="center">Full Stack Framework Milestone 4 Project with Django  

<h2 align="center">Product :fruit : </h2>

## Project Introduction 

### *Title: **(https://marks530-fruitnveg1.herokuapp.com/)** - a fruit and vegetable e-Commerce website for anonymous and registered users*

*Full Stack Frameworks Milestone Project - Django*

This is a shopping site for users to purchase fresh fruit and vegetables

In line with the CI project requirements as well as CRUD methods, the site is aiming to build, and expand on, what has been taught in the CI course. 

for External Tester*

*For the **Code Institute testing purposes**,  log into the site as the **Admin/SuperUser**, using the following details*: 
- Username: **ms1234**   
- Password: **!zIPS123z!** 

*Also, for the sake of further testing, please only use the test number **`4242_4242_4242_4242`** when entering credit card number when paying for products using [Stripe](https://stripe.com/en-ie)



# **Table of Contents**

- [**Project Introduction**](#project-introduction)
- [**Demo**](#demo)
- [**Project Purpose and Scope**](#project-purpose-and-scope) 
- [**UX**](#ux)
    - [**User Stories**](#user-stories)
- [**Design**](#design)
- [**Wireframes**](#wireframes)
- [**Database**](#database)
- [**Features**](#features)
	- [Existing features](#existing-features)	        
    - [Languages](#languages)
    - [Libraries and Other Programs Used](#libraries-and-other-programs-used])
- [**Testing**](#testing)	
    - [Validation](#validation)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
	)
	
	


## Demo

[The project is available on this link.](https://marks530-fruitnveg1.herokuapp.com/)

![Products View](/media/readme_images/Home_Page_Mockup.jpeg "All Products View" )




### **Project Purpose and Scope**

Following the *CI Assessment Handbook 2022*, the aim of this project is to:

- *build a full-stack site based around business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service*

I aimed to stick to this goal and the following section summarises what was needed in terms of requirements to complete the project. This excerpt was taken and adapted, from the **CI project requirements** documentation:

-	Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
-	Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
-	Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models...
-	User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so.
-	User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism)...
- 	Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc...
-	Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
-	Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
-	Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
-	Version Control: Use Git & GitHub for version control.
-	Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
-	Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
-	Security: Make sure to not include any passwords or secret keys in the project repository. 


### **Further Technical Insight** 

The site is built using the [Django](https://www.djangoproject.com/) Framework. Also the following languages were employed :

* HTML
* CSS
* JavaScript 
* Python 
* Bootstrap 

These languages are incorporated along with a relational database management system [PostgreSQL](https://www.postgresql.org/). The site is deployed via [Heroku](https://dashboard.heroku.com/) cloud hosting platform. Media and Static files are hosted via the [AWS S3 platform](https://aws.amazon.com/s3/). The site has the [Stripe](https://stripe.com/ie) payment system software fully integrated. 

# **UX** 

As specified in the project requirements, the aim of this project is to aid the Users to manage and contribute to a common dataset. So naturally, a massive consideration would be on the User experience and the ease with which Users can navigate the site.

The aim was to create a simple, efficient and compact User friendly site, using intuitive design, clear and concise text and enticing colour images to attract and retain users. The simple layout would facilitate a pleasant experience and hopefully entice Users to return and/or recommend the site to friends or colleagues.   

# **User Stories**

In order to best display the User stories I decided to create a table with the following headings

**(1) The User**:
    - as a shopper who is anonymous or a registered User

    - Browsing the site

    - Registration and User Profiles

    - Sorting and Searching

    - Purchasing and Checkout

**(2) The Site Owner**:

    - Administering the Site

#### Browsing
| Site User/Site Admin | Function | Summary |
| :------------------: | :------: | :---: |
|Shopper | View a list of Products | Select an item to purchase |
|Shopper | View Product details | View a Product image, rating and description |
|Shopper | Select a Product | Select an item by weight or quantity |
|Shopper | View a total list of Purchases | Update or remove an item from the list |


#### Registration and User Profiles
| Site User/Site Admin | Function | Summary |
| :------------------: | :------: | :---: |
|Shopper | Register for an Account | Receive an email configuration after registering |
|Shopper | Create a User Profile | View stored personal details in a Profile |
|Shopper | Receive an email configuration after registering | Confirm Registration was successful |
|Shopper | Securely login or logout | Edit and Update personal information |
|Shopper | View a list of Products | Select an item to purchase |



#### Sorting and Searching
| Site User/Site Admin | Function | Summary |
| :------------------: | :------: | :---: |
|Shopper | Sort products by category, rating, price | View resulting list |
|Shopper | Search for a Product by name or description | View resulting list |
|Shopper | Any Products search | See the number of search results |
|Shopper | Select the product by weight or quantity | View resulting list |



#### Purchasing and Checkout
| Site User/Site Admin | Function | Summary |
| :------------------: | :------: | :---: |
|Shopper | Receive a confirmation message after each Product selection | Continue shopping or proceed to Checkout |
|Shopper | Search for a Product by name or description | View resulting list |
|Shopper | Any Products search | See the number of search results |


#### Admin and Product management
| Site User/Site Admin | Function | Summary |
| :------------------: | :------: | :---: |
| Site Owner | Add a Product via the web interface | Add new Products to the shop |
| Site Owner | Edit or Update a product via the web interface | Change product price, description, images and rating |
| Site Owner | Delete a product | Remove items from the shop using the web interface |
| Site Owner | Add a Product using the Django Admin interface | Add new Products to the shop |
| Site Owner | Edit or Update using the Django Admin interface| Change product price, description, images and rating |
| Site Owner | Delete a product using the Django Admin interface| Remove items from the shop |


# Design

#### Font/Typography

The Lato font family from Google Fonts was used throughout the site

#### Colour Scheme and Imagery

The background colour of #555 was used and the images were taken from the Unsplash site 
[Unsplash](https://unsplash.com/s/photos/vegetables/) and credit was given to each of the image providers

## **Wireframes**

Wireframes are really important for a developer to design how it will look and function. I used the app [Balsamiq](https://balsamiq.com/) to build my wireframes. I find it to be a really intuitive and user friendly application, which allows a user to build wireframes simply and efficiently. These wireframes provide the basis and first picture of the evolving website.

### Home Page

![Desktop](media/readme_images/Landing_page_resizes.png)

### Products Page on an iPad

![ipad](media/readme_images/ipad_resized.png)

### Products Page on an iPhone

![iphone](media/readme_images/iphone_resized.png)


## **Database**

**PostgreSQL**

I am using the PostgreSQL database in line with the example demonstrated in the course. [PostgreSQL](https://www.postgresql.org/) also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.


### **Database Schema

![Database Scheme](media/readme_images/DB_diagram.jpeg)
# **Features**

## **Existing features**

The following page elements are explained to guide the user to around the site.

- Navbar
    -  The Navbar is a constant on the site. It allows the user to navigate and on smaller (mobile) displays it adapts to the viewport via Hamburger icon. All the main functionality on 
the site can be enacted via the navbar and so it provides a stable and reliable aspect to the site layout and logic. The User logo in the top right hand side of the page switches between My Account and Register/Login depending on whether the User has logged in or not.



**1. Home Page** 

The landing page contains a banner image and a simple message as well as links and buttons helping the user to navigate the site. The User can choose to shop and search the site in an anonymous mode or decide to register or login using the Register/Login button. 
The Navbar which is present throughout the site contains a search window where the user can enter a search term usually a product name or part of a name and the results will be displayed. The other elements in the Navbar allow the user to select the entire list of products "All Products" or select by category Fruit, Vegetable, Juice or Spices. As mentioned in the last paragraph the Register/Login button is displayed when the user is anonymous and the My Account button when the user is authenticated.

**2. Products Page** 

The main page on the site where the user can view and scroll to see all the products available to purchase. The products are displayed in a card format with an image, short description, price, category and rating. Clicking on the product image takes the user to the product detail page. If the user is a superuser he/she will see an Edit|Delete option to edit or delete products.

For all users there are many filters they can use to sort products. In this way the user can quickly organize products to suit their needs.


  >  -  Price low to high
  >  -  Price high to low
  >  -  Rating low to high
  >  -  Rating high to low
  >  -  Name A-Z
  >  -  Name Z-A
  >  -  Category A-Z
  >  -  Category Z-A
   



**3.Product Detail Page**

This page displays a single product with its image and product information including a description. For the superuser the Edit|Delete option is also available. Products can be purchased by weight or quantity and the corresponding buttons will be displayed.

**4. Login Page**

If a user already has registered, they can log into the site to access and begin shopping. They can enter their username and password and pressing the login button. If a user can't recall their password, they can follow the reset password logic. 

**3. Register Page**

A site user who would like to sign up for an account, they need to provide their email, a username and a password with password confirmation. Once the user successfully registers they can follow the `My Profile` link to fill in their contact and delivery details.

**4. Reset Password Page**

This page allows a user (who already has registered successfully) to recover a lost password by entering in their email (must be valid to receive an email from the site), follow the link generated on the email to a page to enter in a new password with password confirm, so that the user can continue shopping.

**5. My Profile Page:**

Once a user registers, they can fill in the form on this page and their details are saved and stored in the database . The values are automatically validated while the form is being filled out. The user can update their profile if any detail has changed.


**6. Shopping Bag Page**

A users shopping bag is part of the Navbar content and is available throughout the site and is the link which takes the user to the Bag page. It can either be empty or have contents. The bag logo also includes an amount in euros of the value of the contents of the bag. If the bag is empty the amount is ???0.00, otherwise the value of the items in the bag is displayed. Clicking the bag link in the Navbar will take the user to the Shopping Bag page.
Once on the bag page the user is presented with the contents of the bag ie the items selected for purchase.
The user can decide to `Go to secure Checkout` or amend the contents of the bag or choose to `Keep Shopping`. The same options as those
The bag items are stored in the session when the user has selected an item to purchase. A standard feature on e-commerce sites but an interesting adaptation nevertheless. It may also lend itself to reminding users that they have something in their basket that perhaps they want to purchase. However, when the user logs out, all the carts contents are lost. 

**8. Checkout (Payment) Page**
 
This page gives the user a condensed view of their purchases including the order total, delivery charges and the grand total in Euros.
The user is prompted to complete a form with full name email address and delivery information.
At the top of the page the user sees an order summary (a count of product quantity and/or product weight in kgs) and thumbnail image of the product.
After a user has selected a product or products to add to their bag the user can decide to amend the quantity or the weight, 
either increase, decrease and/or remove products. Upon clicking the amend button, the user stays on the bag page and can see the adjusted amount of their bag.
Once the user has selected products to purchase and confirmed the quantity, the must enter their details correctly on the payment form (which applies Stripe
logic) and they can then click the `Complete Order` button which, as its linked to the Stripe backend logic, which confirm their payment, sending the user 
to the Products page with the message - You have successfully paid! Your products are on their way! . If the form details are incorrect, the user will be 
prompted with a red/warning message specifying which form detail needs to be correctly entered. 

**9. Reset-Password Page**

A registered user can choose to reset their password if they wish or have forgotten it. This button is found on both the login and register pages. Upon clicking it, a user is brought to main reset password page where they can follow the simple procedure, which will eventually send an email (to the address they registered with) with a link to reassign a new password to their old account. 
    
    
**10. Add Products Page**

This option is only available to Administrators or superusers and is reached from the user logo menu and by selecting the 'Product Management` link. 
The superuser is presented with a form to describe the product in the database. The form elements marked with an asterisk are required. 
    

**11. Thanks/Order Reference Page**

After a successful payment the user is presented with a "Thank You" page with the order history details.
The user can return to the shopping area and continue shopping or finish up with the transaction.

**12. Toasts**

The Django web frameworks comes with a messaging system that allows us to store messages that we can check for on each page load. If there are some messages, we can display them to the user.
The toasts messaging system is used to return success info error and warning messages throughout the site.

```
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

```
Code snippet courtesy of [Pythonprogramming](https://pythonprogramming.net/messages-django-tutorial/)

### Github - Version Control


### Github and VSCode

The site code and apps are hosted on [Github](https://github.com/marks530/fruit_and_veg_store.git). This project was built and tested on the IDE [VSCode](https://code.visualstudio.com/). I started the project with Gitpod but found I was wasting a lot of time having to restart the workspace each it was idle for any length of time. I was also having to re-import all of the dependencies and adapters required to run the apps. So I switched the working environment to VSCode. 
 
### Clone Repository for Local Use

Steps to clone a repo on Github:

1. Go to my repository on https://github.com/marks530/fruit_and_veg_store.git
2. Click the `Clone or download` button
3. In HTTPS, copy the clone url
4. Return to VSCode
5. Open a folder on my Computer and run the command `pipenv shell` from the terminal to create a virtual environment on the local computer.
6. Command - `git clone https://github.com/marks530/fruit_and_veg_store.git` and enter to connect to Github repository.
7. Create a gitignore file to store files for local use only. Later in the project I had to create a env.py file to store local environment variables.
8. Once the Django framework has been installed use the following commands to get the app up and running.

        `python3 manage.py makemigrations` 
        then:
        `python3 manage.py migrate`
        *and to create a superuser with username and password(twice)*
        `python3 manage.py createsuperuser`
`
**Terminal Commands**

- Use the `git init` command to initialize my local repository.
- Afterward I used the `git push origin master` pushing my code to the master branch.
- And so after my repo was initialized, I used the commands: `git add . ` (to add all) or `git add ReadMe` (to add a specific file) 
- And then the command`git commit -m "initial commit"`(and with every commit followed by any comments) to `add` and `commit` files to Github.  
- Then, I would use the `git push origin master` or just `git push` commands to push my significant updates to the remote Github repository.

## Deployment to Heroku
The project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud [Heroku](https://dashboard.heroku.com/apps) in a range of programming languages. Python was the language used for this project.

The following process was undertaken to successfully deploy the project on the Heroku:
[**The Deployed Heroku site can be found here**](http://marks530-fruitnveg1.herokuapp.com/)

- Heroku requires the following two files
    - A **requirements.txt** file is needed to run the installed dependencies, so to create and commit this file, the following command was used: 
    `$  pip3 freeze --local > requirements.txt`.
    - A **Procfile** is needed to direct the Heroku app to the file that it needs to run. Use the echo command the output the string
    `$  echo web: python app.py > Procfile`
    Remove the blank line to avoid problems running on Heroku.

The application was created and name simply "marks530-fruitnveg1" on my Heroku profile. 
Set up automatic deployment to GitHub using the "Connect to GitHub" method as the Deployment method.
But before setting *Enable Automatic Deployment* click on the Settings tab and  select *Reveal Config Vars* to securely tell Heroku which variables are required

After creating my env.py file which was added to .gitignore file, I added the following in to the *reveal config vars* area.


- Finally, select *Enable Automatic Deployment*  to deploy my code from GitHub to the Heroku app.

After any big changes, advancements on my code, I would push my code to the Heroku app to check if it was functioning. 

I found the Heroku CLI to be useful at times for example to make a backup of the database.

```
heroku pg:backups:capture
heroku pg:backups:download

```

### **Languages**

-   [Python](https://www.python.org/) - the main backend programming language used. Python is a [interpreted, object-oriented, high-level programming language](https://www.python.org/doc/essays/blurb/). Python is used in tandem with Django to construct the views and main site logic.
-   [HTML5](https://en.wikipedia.org/wiki/HTML5) I used HTML to define structure and layout of the site;
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - is used as the stylesheet language for styling and rendering.
-   [Javascript](https://www.javascript.com/) - is the renowned programming scripting language and the main libraries are JS.


### **Frameworks**

-   [Django](https://www.djangoproject.com/) - is a high-level Python Web framework that used the MVT system 

### **Libraries and Other Programs Used**
1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used heavily as the main library to style the site. I availed particular from the grid system and the buttons, among many other functions.
2. [Google Fonts:](https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap)
    - I felt Google Fonts was extremely important to improve the look and UX of the site. I used the `Roboto Mono` font which I found to be perfectly fitted to the technical *machine* styling I was looking for. The first time I switched the font (from the standard default bootstrap font), I was really taken aback by how much the site look and professional feel was improved by the font.
3. [Font Awesome:](https://fontawesome.com/)
    - I used Font Awesome heavily on all pages on my website. I like the sleek icon style and feels it gives a boost to the UX
4. [jQuery:](https://jquery.com/)
    - jQuery CDN library was used to assign functionality to Bootstrap elements 
5. [Git:](https://git-scm.com/)
    - Using Git on the Gitpod IDE for version control, to commit and push code to Github
6. [GitHub:](https://github.com/)
    - Pushing with my git commands, my entire project code is store on Github
7. [Balsamiq](https://balsamiq.com/) 
    - was used to create my wireframes
8.  [django-storages](https://django-storages.readthedocs.io/en/latest/) & [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - were libraries used to connect Django to AWS S3 Buckets to host media. Both found on `requirments.txt`
9. [django-forms-bootstrap ](https://pypi.org/project/django-forms-bootstrap/)
    - a library used to adapt the standard django forms into bootstrap styling. Listed on `requirments.txt`.

- **Databases, Hosting, API???s, Mockups:**

    - [PostgreSQL](https://www.postgresql.org/) - a relational db management system, hosted on Heroku;
    - [SQLite](https://en.wikipedia.org/wiki/SQLite) - a lightweight db management system that runs locally on Django (used mainly for testing)
    - [Heroku](https://dashboard.heroku.com/apps) ??? The site is hosted on Heroku platform
    - [Stripe API](https://stripe.com/en-ie)  ??? Used to make secure payments
    - [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) ??? Used to generate site mockup for different view ports (Mac)
    - [DBDiagram]( https://dbdiagram.io/home) ??? Diagram tool used to describe the database as a diagram using the native language


### AWS S3 Bucket

#### Setting up the S3 Bucket

1. Go to [AWS](https://aws.amazon.com) and sign up for an account
2. Go to your profile and select [S3](https://aws.amazon.com/s3/) and create a bucket, giving it a title of your choice
3. Go to the *properties* tab and and select *static web hosting*
4. Go to the *permissions* tab and change the *CORS Config* (CORS = Cross Origin Resource String)
5. Also in *permissions* section, change the *bucket policy* to the following (snippet) - making sure to add personal *bucket name*:
 6. Click on **IAM** (Identity & Access Management i.e. how a user manages access), create a new *group*  and add your bucket to it.
7. Create a *new policy* (in the *group IAM*), to the JSON section and click *import managed policy*, choose "AmazonS3FullAccess" and select import. Make sure to replace the resource string **'*'**.
8. Click *review policy* and click *create policy*
9. Now add *policy* to *group*
10. Create a *user*, give *programmatic access*, choose a *group* and click *create*
11. Finally, make sure to download CSV file with the *access keys* and other important details.

### Adding AWS S3 to Django

This step enables the *Django* project to have access to the *S3 Bucket*. Public and Private keys must be added to the `settings.py` via the `env.py` so the static files can be moved to S3.

1. Install the necessary libraries and correct versions (depending on Django project version):

    ```
    sudo pip3 install django-storages==1.9.1
    sudo pip3 install boto3==1.12.31
    ```
2. To the `settings.py` file, add `storages` to **INSTALLED_APPS** section.

3. Then add the following  S3 bucket details to the `settings.py`:
    
    ```python
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }
    
    AWS_STORAGE_BUCKET_NAME = '<bucket-name>'
    AWS_S3_REGION_NAME = '<region-name>'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_SECRET_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_ACL = None # removes boto warning
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    ```

#### Adding the Media to AWS S3

1. Create a `custom_storages.py` with 2 classes for both Static and Media (files) locations. Underneath is the code snippet:

    ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION

    ```
2. Next, you must go to the `settings.py` to configure the static and media files `location` and `storage`
    ``python
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    ```
3. Finally, in your Command Line Terminal, run the following command to push the static files to the S3 Bucket - `python3 manage.py collectstatic` 

# **Testing**

I tested the platform on a number of devices (ipad, iphone, Purchasing laptop) as well as all the screen sizes on Chrome Devtools. I also tested the sites pages in other browsers including Safari and Firefox. 

As a shopper and a site user I ran the following tests and exercises as an Anonymous User
     

       1.   Verify that as an anonymous user the User icon in the top right reads Register/Login
       2.   Browse the site and view a Product
       3.   Use the Shop Now button to view the Products
       4.   Use the dropdown menus to view a selection of products
       5.   Use all the sort options to view the products according to price rating or Category
       6.   Test the ascending and descending selectors
       7.   Select a product to view, add to the bag and increment its quantity
       8.   Select a product to view, add to the bag and increment its weight
       9.   Test the decrement buttons do not go below 1
       10.  Test the increment buttons do not go above 99
       11.  Select multiple products to view and add to the bag
       12.  Check the products are in the Toast message each time a product is added or selected
       13.  Check that the products are displayed with their respective weight or quantity
       14.  Use the Keep Shopping button to continue shopping from the bag Page
       15.  Use Go to Bag button on the Toast message
       16.  Check the contents of the Shopping Bag Page
       17.  Use the Keep Shopping button on the Bag page to continue shopping
       18.  Test the Adjust Bag button with the Update and Remove buttons
       19.  Verify that the items have been adjusted or removed
       20.  Proceed to the Checkout page with the Secure Checkout button
       21.  Verify the the item list is correct and the products are described with their respective quantities      
       22.  Check the Adjust Bag button returns to the Shopping Bag page
       23.  Use the Secure Checkout button to go to the Checkout page
       24.  Test the form is working by entering incorrect values
       25.  Test the form is working with correct values and use the 4242 Credit card to complete the transaction
       26.  Check the Thanks page has the correct Order information and the success Toast message displays
       27.  Use the Register option from the User icon and register a new account
       28.  Test the Login option takes you to the login Page
       29.  Try to login with false details
       30.  Use the All Products dropdown options to sort products according to Price Rating and Category

As a shopper and a site user I ran the following tests and exercises as a Registered User  

      1. From the User icon in the Navbar use the Register option to create a new account with a temporary email
      2. Verify the email and go to My Profile and create a Profile
      3. Check all of the above (that are applicable) as a registered user

As a Superuser or Administrator 

     1. Login to the Site with Superuser credentials
     2. In the All Products page test the Edit and Delete options
     3. Edit a product by changing a detail and verify it worked
     4. I choose not to delete a product for testing purposes
     5. Verify that the Alert Toast message occurred

### **Validation**

-   [PEP8](http://pep8online.com/)
     - PEP8 was the tool I tested my Python code on. I received  plenty warnings such as:
        > `W292	10	44	no newline at end of file`
        > `line too long (80 > 79 characters)` 
        > `trailing whitespace . . `

        I did my best to remove as much of the warnings as possible.

-   [JSHint](https://jshint.com/) 
     
     JavaScript code completed testing without any errors.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input+with_options) 
    - The feedback from this code validator was confusing as I had to ignore the errors from the Jinja templating engine. I passed my html pages into the validator in any case.
    I was able to resolve the majority of the errors without too much trouble. This error was recurring over several pages in this case base.html.
    [base.html](media/readme_images/Error_sequence_base_html.jpeg)

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    * I added my css code into the validator and it stated: 
            > W3C CSS Validator results for TextArea (CSS level 3 + SVG)
    Congratulations! No Error Found.
    ![CSSValidation](media/readme_images/CSS_validation.jpeg)
    ![CSSWarnings](media/readme_images/css_warnings.jpeg)
    

- [Google Mobile-Friendly Test site](https://search.google.com/test/mobile-friendly)
    - Positive feedback from this site, which stated:
    > Page is mobile friendly. This page is easy to use on a mobile device
    ![Google Mobile-Friendly Test](media/readme_images/google_mobile_friendly_test.jpeg)



## Credits

- I found [Stackoverflow](https://stackoverflow.com/) to be an invaluable resource

- [css-tricks](https://css-tricks.com//) was another site I found to be useful

- [Corey Schafer](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) as always very informative

- [Unsplash](https://unsplash.com/s/photos/vegetables/) was the source of the product images which were very kindly made available by the image providers.


