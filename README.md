# Trendify: Product Recommendation System

Trendify is a machine learning-based product recommendation system designed to enhance customer experiences by providing relevant product recommendations. The system supports three types of recommendations:
1. **Automatic**: Recommendations generated automatically based on user behavior.
2. **Frequently Bought Together**: Products frequently bought together with the current product.
3. **Manual**: Allows users to manually select recommended products for each product.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API](#api)
- [Testing](#testing)
- [Contributors](#contributors)
- [License](#license)

---

## Project Overview
The system uses machine learning algorithms to predict relevant products based on past purchasing behaviors and product characteristics. It is initially designed for integration with Shopify, where store owners can offer automated, frequently bought together, or manual product recommendations.

---

## Features
- **Automatic Recommendations**: Machine learning-based suggestions.
- **Frequently Bought Together**: Suggests products often purchased together.
- **Manual Recommendations**: Admins can manually curate recommended products for each product.
- **Scalable**: Can be integrated into any eCommerce platform using its API.
- **Data-Driven**: Learns from customer behavior and sales data to improve recommendation accuracy over time.

---

## Tech Stack
- **Backend**: Python, Flask (for API)
- **Machine Learning**: K-Nearest Neighbors (KNN), pandas, scikit-learn
- **Database**: MongoDB (for storing product data and recommendations)
- **Frontend**: To be integrated separately with Shopify or other platforms

---

## Setup Instructions

### Prerequisites:
1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Git**: Ensure Git is installed to clone the repository.
3. **Virtual Environment (optional)**: Recommended for dependency management.

### Steps:

1. **Clone the Repository**  
   Clone the project from GitHub using:
   ```bash
   git clone https://github.com/yourusername/trendify.git
