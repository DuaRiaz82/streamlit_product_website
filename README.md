# TechCart Store

A simple Streamlit-based e-commerce landing page for a tech products store. The app presents featured products, category navigation, company information, and a WhatsApp-based ordering flow for customers.

## Overview

TechCart is a lightweight product showcase website built with Python and Streamlit. It is designed for small online stores that want a quick, easy-to-launch storefront without a full backend or database.

## Features

- Responsive single-page layout with menu tabs
- Home section with brand messaging and CTAs
- Product cards for featured items
- Product pricing and basic descriptions
- WhatsApp order links for fast customer checkout
- Clean, modern design for a product catalog

## Tech Stack

- Python
- Streamlit
- WhatsApp link generation using Python's urllib

## Project Structure

```text
streamlit_product_website/
├── app.py
├── earbuds.png
├── laptop.png
├── mouse.png
├── README.md
```

## Installation

1. Clone the repository.
2. Create and activate a virtual environment (optional but recommended).
3. Install the required dependency:

```bash
pip install streamlit
```

## Run the App

From the project folder, run:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually http://localhost:8501).

## App Details

The application includes:

- Home: store introduction and brand highlights
- Products: featured product cards with images, prices, and buy buttons
- Categories: category section placeholder
- About: store information section
- Contact: contact area placeholder

## WhatsApp Ordering

Each product has a WhatsApp order button that creates a pre-filled message with the product name and price. This makes it easy for customers to contact the seller directly.

## Notes

This project is intentionally simple and serves as a starter storefront for small businesses or learning projects. It can be expanded with:

- a real product database
- inventory management
- payment integration
- login/admin panel
- customer reviews

## License

This project is for educational/demo purposes and can be customized for personal or business use.
