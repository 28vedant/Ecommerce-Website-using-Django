# Shapee E-commerce Platform

## Description

Shapee is a full-fledged e-commerce platform built using Django framework. It provides a seamless shopping experience for both customers and administrators. Customers can browse through a wide range of products, add them to their carts, make secure payments, and track their orders. Administrators have access to product management functionalities, allowing them to add new products, update existing ones, and manage orders.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/shapee.git
    ```

2. Navigate into the project directory:

    ```bash
    cd shapee
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Set up Razorpay:

    - Sign up for a [Razorpay](https://razorpay.com/) account.
    - Generate API keys from the Razorpay dashboard.
    - Update the Razorpay API keys in the Django settings file (`settings.py`):
        ```python
        RAZORPAY_API_KEY = 'your_api_key'
        RAZORPAY_API_SECRET = 'your_api_secret'
        ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

1. Access the application in your web browser at `http://localhost:8000`.
2. Sign up for a new account or sign in if you already have one.
3. Explore the different product categories and browse through products.
4. Add desired products to your cart and proceed to checkout.
5. Make payment using the integrated Razorpay payment gateway.
6. View your order history to track previous purchases.

## Features

### Customer Features:
- **User Authentication**: Sign up, sign in, and sign out functionalities for customers.
- **Product Browsing**: Browse products categorized into various sections such as electronics, clothing, shoes, etc.
- **Cart Management**: Add products to cart, update cart items, and remove items from the cart.
- **Secure Payments**: Integration with Razorpay for secure payment processing.
- **Order Tracking**: View order history and track the status of orders.

### Administrator Features:
- **Product Management**: Add new products, update existing product details, and delete products.
- **Order Management**: View all orders, mark orders as shipped, and manage order statuses.

## Screenshots

### Home Page
![Screenshot 1](https://github.com/28vedant/Ecommerce-Website-using-Django/assets/109358399/5321159c-c5e0-4c48-a6b8-ac12b37f2644)
### User Login
![Screenshot 2](https://github.com/28vedant/Ecommerce-Website-using-Django/assets/109358399/cb1e3216-396b-4bdf-950d-d3c87753af03)
### Registeration Page
![Screenshot (3)](https://github.com/28vedant/Ecommerce-Website-using-Django/assets/109358399/6b3d2888-f462-4d84-9983-4f8122f287bc)

### Add to Cart PAge
![Screenshot (4)](https://github.com/28vedant/Ecommerce-Website-using-Django/assets/109358399/1708ac12-c9ae-4108-b4d7-a82c541831a6)


## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

