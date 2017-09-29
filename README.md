# Udacity-Item-Catalog
Developed a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication (Google Sign-in). Appropriately mapping HTTP methods to CRUD (Create Read Update and Delete) operations 

# About the Project

The Item Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system. Only Read functionality is available for the users without logging in. Once logged in, users can add items and edit/delete the items added by the user.

# Setup Required

You will need:
<br/>
Python - 2.X <br/>
Vagrant <br/>
VirtualBox <br/>

<br/>
Vagrant virtual machine is required for this project which you can find here: https://github.com/udacity/fullstack-nanodegree-vm 
<br/>
First, fork the fullstack-nanodegree-vm repository so that you have a version of your own within your Github account. Next clone your fullstack-nanodegree-vm repo to your local machine. 
To use the Vagrant virtual machine, then use the command 
```vagrant up``` (powers on the virtual machine) 
followed by 
```vagrant ssh``` (logs into the virtual machine).
Find the catalog folder and replace it with the content of this current repository. Navigate to the catalog folder using
```cd /vagrant/catalog/``` 
<br/>

# Running the Application

1. Initialize Category and Item classes running ```python database_setup.py```
2. Populate the db by running ```python lotsofitems.py```
3. Run the application using ```python project.py```
4. Access and test your application by visiting http://localhost:5000

# Attributions

[Full Stack Foundations course materials](https://github.com/udacity/ud330)
<br/>
[Udacity Discussions](https://discussions.udacity.com/t/gdisconnect-keeps-failing-to-revoke-token/169288/13)
<br/>
Google Sign-in developers documentation
