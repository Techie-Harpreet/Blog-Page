# Django Blog Project

This is a **Django-based Blog Project** where users can view, search, and filter blog posts. Admins can manage blog content, including adding blog posts with images, categories, and more.

## Features

- **Image Uploads**: Admins can upload images for each blog post and the homepage slider.
- **Blog Post Management**: Admins can create, edit, or delete blog posts with an image.
- **Category Filter**: Blog posts can be filtered by category.
- **Search**: Search for blog posts by title.
- **User Authentication**: Admin panel and other features are restricted to logged-in users.
- **Admin Panel**: Manage blog posts, categories, and images.

## Project Screenshots

Here are some images of the project:

### Homepage
![Homepage](https://raw.githubusercontent.com/Techie-Harpreet/Blog-Page/refs/heads/main/Images/homepage.png)

### Single Blog Post
![Single Blog Post](https://raw.githubusercontent.com/Techie-Harpreet/Blog-Page/refs/heads/main/Images/blogpost.png)

### Admin Panel
![Admin Panel](https://raw.githubusercontent.com/Techie-Harpreet/Blog-Page/refs/heads/main/Images/admin.png)

These images show the main features of the blog, including blog posts, categories, and admin controls.

## Installation

### Prerequisites

- Python 3.11
- pip
- Django
- Pillow (required for image handling)

### Step-by-Step Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Techie-Harpreet/Blog-Page.git
    cd Blog-Page-main
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/Mac
    env\Scripts\activate     # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Pillow** (required for image handling):
    ```bash
    pip install Pillow
    ```

5. **Set Up the Database**:
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
    Access the project at `http://127.0.0.1:8000/`.


## License

This project is licensed under the **MIT License**.

---

## Contact Information

For any queries, suggestions, or issues, feel free to reach out to us:

- **Email**: contact@harpreetsinghbansal.com
- **GitHub Repository**: [Your GitHub Repo Link](https://github.com/Techie-Harpreet/Blog-Page)

