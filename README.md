# Tripp's Treasures

Tripp's Treasures is an online e-commerce boutique, selling hand crafted homewares and baby clothes.
Customers can request customisation of each item, making them ideal gifts for friends or loved ones.

-responsive image-

-link to live site with instructions-

## Contents

* [User Experience (UX)](#user-experience-ux)
  * [User Stories](#user-stories)
    * [User Goals](#user-goals)
    * [Site Owner Goals](#site-owner-goals)
* [Design (UXD)](#design-uxd)
  * [Strategy](#strategy)
    * [Project Goal](#project-goal)
  * [Scope](#scope)
    * [Functional Scope](#functional-scope)
    * [Agile Methodology](#agile-methodology)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
  * [Surface](#surface)
    * [Colour Palette](#colour-palette)
    * [Typeography](#typography)
    * [Iconography](#iconography)
* [SEO and Marketing](#seo-search-engine-optimisation-and-marketing)
  * [SEO](#seo)
  * [Marketing](#marketing)
* [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Features](#future-features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
  * [Validator Testing](#validator-testing)
  * [Manual Testing](#manual-testing)
  * [Automated Testing](#automated-testing)
  * [Bugs and Fixes](#bugs-and-fixes)
* [Deployment](#deployment)
* [Credits](#credits)
* [Aknowledgements](#aknowledgements)


## User Experience UX
### User Stories

#### User Goals

* As a site visitor I would like to:
  * Be able to navigate the site without needing to register or login.
    * The site should be intuitive and easy to navigate.
    * I would like to be able to find what I'm looking for by selecting relevant categories.
    * I would like to be able to filter the products available to suit my needs.
    * I would like to be able to find what I need by use of a search bar.
    * I would like to be able to view snapshots of products to easily find products of interest.
    * I would like to be able to view a the full details of a product including, multiple images, full description, sizing information (if necessary), pricing, user ratings, and FAQs.
    * I would like to be able to view related sites without having to find them with a search engine.
    * I would like to easily navigate the site on a smaller screen and access all information available to larger screen users.
    * I would like to be able to register/login to the site from any page.
  * Be able to select a product(s) to purchase.
    * I would like to be able to select sizes for clothing.
    * I would like to select the quantity of products.
    * I would like to be able to request customizations of the products available.
    * I would like to be able to add the selected product(s) to my basket without being automatically directed to it.
  * Be able to review my purchaces before committing to buy.
    * I would like to be able to access my shopping basket from anywhere on the site.
    * On accessing my shopping basket I would like to see a cost breakdown of my selected purchases.
    * I would like to be able to amend or remove any items before committing to buy.
  * Be able to checkout of the site and pay for my purchases.
    * I would like to be able to enter my personal information in a secure environment.
    * I would like to be given the option to not have to repeat myself when entering personal information.
    * I would like to have the option to register with the site to save my personal information for a faster checkout next time I visit the site.
    * I would like to have the option to have my order sent to a different address to the billing address.
    * I would like to have the option to add a gift tag and have the items wrapped.
    * I would like to pay for my purchase using a trusted payment portal.
    * On submitting my order, I would like to receive a confirmation email with my order details and a unique order number.
    * I would like to receive a dispatch confirmation email with and estimated delivery date.
  * Be able to contact the site owner by means of a contact form.
  * Be able to subscribe to a newsletter.
    * Have the option to unsubscribe from the newsletter mailing list.
* As a registered site visitor I would like to:
  * Have the option to login with a social media account for a speedier "1 click" login.
  * Be able to access my account/profile page.
    * I would like to be able to view my personal information.
    * I would like to be able to update my personal information.
    * I would like to be able to delete my personal information.
    * I would like to be able to view my order history and any current orders to track progress.
    * I would like the option to delete my account.
  * Be able to publish reviews and ratings of products I have received.
    * I would like to be able to create a review.
    * I would like to be able to update a review.
    * I would like to be able to delete a review.
    * I would like to be able to rate a product out of 5 stars.

#### Site Owner Goals

* As the site owner I would like to:
  * Provide a site that's highly accessible to all customers.
  * Be able to advertise any offers or relative information to customers by means of an information banner.
  * Be able to gather subscribers for my newsletter by advetising the link on the site.
  * Be able to manage products.
    * I would like to be able to add new products to the site.
    * I would like to be able to update existing products.
    * I would like to be able to delete existing products.
  * Be able to view my workload.
    * I would like to be able to view all current orders in production sorted by date ordered.
    * I would like to be able to change the status of an order when the product has been created.
    * I would like to change the status of an order when the product has been dispatched.
    * I would like to send an order despatched email to the customer when the order is complete.

## Design (UXD)

### Strategy
#### Project Goal

Create an e-commerce website to help a friend sell her handcrafted, customisable gifts to a wider audiance by utilising SEO techniques.

* __Is the content culturally appropriate?__
  * Yes. Users would only visit the site if they wanted to purchase a unique handcrafted gift.
* __Is the content relevant?__
  * Yes. All content is relevant to the project goal.
* __Can we track and catalogue the content in an intuitive way?__
  * Yes. All content is stored in a database and accessed via categories, filtering or search criteria.
* __Is the technology appropriate?__
  * Yes. The site will be created using Python and the Django framework, designed for the easy creation of full stack websites.
* __Why are we so special? What sets us apart?__
  * We offer a range of unique handcrafted gifts customised to the customer's liking.
* __Tech Considerations?__
  * The site will be built using [Python](https://www.python.org/) with the [Django framework](https://www.djangoproject.com/), [JavaScript](https://www.javascript.com/) & [HTML](https://html.com/semantic-markup/). [CSS](https://www.w3.org/Style/CSS/Overview.en.html) will be used alongside [Bootstrap](https://getbootstrap.com/) for site responsiveness over different screen sizes. [PostgreSQL](https://www.postgresql.org/) will be used to host site information & [AWS S3](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23storage&trk=9845b571-f118-41f9-ae80-53f3364524c4&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|GB|EN|Text&s_kwcid=AL!4422!3!489216385180!e!!g!!aws%20s3&ef_id=CjwKCAjwkMeUBhBuEiwA4hpqEJmK52Rp_outs9Ama8hbA1IhA0MOr-OkiPis4BSWVAuobKN7yEmQsRoCSNMQAvD_BwE:G:s&s_kwcid=AL!4422!3!489216385180!e!!g!!aws%20s3&awsf.Free%20Tier%20Types=*all) will host site images. [Stripe](https://stripe.com/gb) will be used to handle secure payments. The site will be hosted from [Heroku](https://id.heroku.com/login) and [Github](https://github.com/) will be used for version control and Agile methodology.
* __Why would a user want this?__
  * A user would want to use this site to purchase unique customisable handcrafted gifts for friends or loved ones.
### Scope

* __What does the user want to accomplish?__.
  * The user wants to purchase a unique handcrafted gift, customised to thier liking.
* __What does the user need to do in order to achieve their objective?__
  * The user needs to navigate to their product of choice, choose the size (if necessary), Write a short description of how they would like the product to be customised, review their purchase, fill in the checkout form, submit payment details, and receive a confirmation of purchase email.
* __What constraints does the site/app have to fall within?__
  * A limited build time.
* __What dynamic constraints do we have to meet?__
  * Customer preferences/mind-changes for features/UI.
#### Functional Scope
Entity Relationship Diagram
![ERD](readme_images/entity_relationship_diagram.png)
#### Agile Methodology
The development of this project was managed with Agile Methodology, utilising [GitHub's](https://github.com/) Milestones tool to manage Epics, the Issues tool to manage User Stories, and the Projects tool to map out the User Stories on a Kanban board.
* The project can be viewed [here](https://github.com/mwarddev/tripps_treasures/projects/1).
* The Epics can be viewed [here](https://github.com/mwarddev/tripps_treasures/milestones).
* The User Stories can be viewed [here](https://github.com/mwarddev/tripps_treasures/issues).
### Structure
From the top down, the site will consist of the following:
  * A fixed info banner at the top of the page.
  * Medium screens and greater:
    * Navbar with site logo and title.
    * Fixed categories.
    * Main content area.
    * Footer (not fixed).

  * Small screens:
    * Site logo and title (moves with scroll).
    * Sticky navbar (takes the place of the site logo and title on scroll)contains a search bar, shopping basket, and dropdown menu (account, baby clothes, gifts for her, gifts for him, gifts for pets).
    * Current category or page title + filter options (if applicable).
    * Fixed categories.
    * Main content area.
    * Footer (not fixed).
  
### Skeleton
Wireframe layouts for the site were created using [balsamiq](https://balsamiq.com/). View the wireframes [here](readme_images/wireframes.pdf).
### Surface
#### Colour Palette
![treasure_palette](readme_images/treasure_palette.png)
The colour palette for this site was generated using [coolors.co](https://coolors.co/).
#### Typography
The typography for this site has been selected from [Google Fonts](https://fonts.google.com/). The Special Elite font has been selected for headers and the Roboto font has been selected for all other text.
#### Iconography
The site logo was created by Sherry Tripp, the site owner. ![Logo](readme_images/tripps_treasures_logo.jpg) All other iconograpy has been obtained from [Font Awesome](https://fontawesome.com/).
## SEO (Search Engine Optimisation) and Marketing
### SEO
### Marketing
## Features
### Existing Features
### Future Features 
## Technologies Used
## Testing
### Validator Testing
### Manual Testing
### Automated Testing
### Bugs and Fixes
## Deployment
## Credits
## Aknowledgements

