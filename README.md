# PriceMonitor

PriceMonitor is a web application designed to allow registered users to track prices of items on Amazon. When the product's price drops to or below a specified amount, the system notifies the user.

## Features

- **User Authentication**: Custom user model to allow registration and authentication using email instead of a username.
  
- **CRUD Operations**: Users can add, view, edit, and remove items they wish to monitor.

- **Price Monitoring**: Uses web scraping to periodically fetch the current price of a product from Amazon using its URL.

- **Notification System**: Notifies users when the desired price matches or is lower than the current price.

- **Responsive UI**: Makes use of Foundation and Bootstrap for a responsive and modern user interface.

## Setup Instructions

1. **Clone the repository**
```bash
   git clone git@github.com:indranandjha1993/ecom_price_monitor.git
```

2. **Navigate into the directory**
```base
    cd ecom_price_monitor 
```

3. **Install required Python packages**
```base
    pip install -r requirements.txt
```
4. **Run migrations**
```base
    python manage.py migrate
```

5. **Run migrations**
```base
    python manage.py runserver
```

6. **Access the application at http://127.0.0.1:8000/**

## Pages

* Home Page: Welcomes the users with a general landing page.
* Register: Allows new users to register for the application.
* Login: Existing users can login using their credentials.
* Profile: Displays the user's profile information.
* Add Item: Allows users to add a new item to monitor.
* View Items: Displays the list of items a user is monitoring with options to fetch the current price, edit the item, or delete it.

## Note
As the app uses web scraping to fetch prices from Amazon, be aware of the potential legal and ethical concerns related to web scraping. Always consult Amazon's robots.txt file and Terms of Service before deploying such an application in a production environment.