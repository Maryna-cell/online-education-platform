# Education Portal

### Project Description
This project is a fully-featured educational online platform developed with Django. The primary goal of the project is to demonstrate key web development skills, from creating a flexible Content Management System (CMS) to implementing real-time asynchronous functionalities and setting up a complete production environment. The project serves as a comprehensive portfolio piece showcasing a wide range of skills.

### Key Features
* **Flexible CMS:** Implemented a Content Management System (CMS) using class-based views and mixins to create courses and modules.
* **Content Management:** The system allows for managing various types of content (videos, images, files) using model inheritance and formsets.
* **Security & Permissions:** Implemented Django groups and permissions to restrict access to views.
* **Custom Authentication:** A custom authentication system was created for the platform.
* **Dynamic Management:** Drag-and-drop functionality with JavaScript and Django allows for easy reordering of modules and their content.
* **Student Registration:** A system for student registration and course enrollment is in place.
* **Asynchronous Chat:** A real-time chat is implemented using **Django Channels**, WebSockets, and an asynchronous consumer, ensuring responsiveness and scalability.
* **Chat Persistence:** Chat message history is saved, providing a robust and user-friendly experience.
* **Performance Optimization:** The Django caching framework is used with Redis and Memcached backends to improve application performance.
* **RESTful API:** A RESTful API is integrated using Django REST framework for programmatic interaction with the project.
* **Custom Commands & Middleware:** Developed custom management commands to automate tasks and custom middleware for request/response processing.
* **Production Environment:** The project is production-ready, with configurations for **Docker Compose, NGINX, uWSGI, and Daphne**.

### Technologies
The project was developed using the following technologies:
* **Python:** The core programming language.
* **Django:** The web framework for rapid development.
* **Django Channels:** For asynchronous functionalities and WebSockets.
* **Docker Compose:** For managing the production environment.
* **NGINX, uWSGI, Daphne:** For production deployment.
* **Redis & Memcached:** Used as backends for caching and the channel layer.
* **Pillow:** An image processing library.
* **Django REST framework:** For building the RESTful API.
* **SQLite:** For local development.

### Running the project
Follow these instructions to run the project on your computer using Docker:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Maryna-cell/online-education-platform.git](https://github.com/Maryna-cell/online-education-platform.git)
    cd educa
    ```
2.  **Build the Docker images:**
    ```bash
    docker-compose build
    ```
3.  **Run the containers:**
    ```bash
    docker-compose up -d
    ```
4.  **Apply database migrations:**
    ```bash
    docker-compose exec web python manage.py migrate
    ```
5.  **Create a superuser (optional):**
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```
The project will be available in your browser at `http://127.0.0.1:8000/` or a custom domain configured in NGINX.

---
**Note:** For the asynchronous features (chat) to work correctly, a Redis container is automatically configured and run by Docker Compose.
