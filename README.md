# Capstone-Project-

It is a repository defining  our web application and devlopment  capstone project which will include HTML and Css with Javascript with API  function and database connection  in backend with python and flask . 

## Team Name -- FindSquad
## Team Members -- Nimisha Goyal ,Sakshi Patel

## We are making ---
# Lost & Found App – Home & View Posts Page (Flask + API)

## Overview

This project is a **Lost & Found web application** built using **Flask** and basic APIs. Which includes  the home page serves as the central hub where users can report lost items and interact with others who may have found them.
It is designed to help users report lost items and connect with people who may have found them.

## We both are making are diferent Lost and found app so that each have the knowledge to work .

### MY (Nimisha Goyal)  Side App Work -- 
## All this I have to do only !!

## Home Page Features
### 1. User Profile Display

* Each post is linked to a user profile.
* Displays basic user details such as:
  
  * Username
  * Email  --> for Data Validation 
  * Contact Info --> for Data Validation 
  * Lost Item image upload
  * Item Description

## View Posts Page 
### 2. Lost Item Post

* Users  uploads:
  * Image of the lost item
  * Description (e.g., “Lost black wallet near college gate”)    

### 3. Founder Interaction (Comments Section)
* Other users (finders) can respond directly to a lost item post.
* They can:
  * Reply: *“I found it here…”*
  * Provide location detail

### 4. Image Upload Support
* The owner can edit the original post and can upload it:
  * Lost item image (by owner)
  * Edit the same image (by owner)

### 5. API Integration (Basic)
* Backend APIs handle:
  * Fetching all lost item posts
  * Posting a new lost item
  * Adding comments (found responses)
  * Updating images

### 6. Flask Backend
* Flask is used to:
  * Render the homepage
  * Handle API routes
  * Manage user sessions (basic)
  * Process image uploads

## User Flow (Home Page & View Posts Page Only)
1. User makes profile  in and lands on the homepage.
2. User posts a lost item with an image.
3. Other users scroll through posts.
4. A finder comments on the post:
5. User can edit the post if mistakenly wrong image is uploded.
   * Adds message: *“I found this near XYZ location”*
6. Original user can view responses and take action.
   
## Tech Stack (Basic)
* **Frontend:** HTML, CSS (basic UI)
* **Backend:** Flask (Python)
* **API:** RESTful endpoints for posts and comments
* **Storage:** Local storage / database (e.g., MySQL) through Supabase

## Goal
To create a simple, interactive platform where users can **report lost items and connect with people who may have found them**, all from a single homepage interface.

## Future Enhancements 
1. Authentication system (login/signup)
2. Real-time notifications
3. Location-based filtering
4. Chat system between users
5. Deployment on cloud
