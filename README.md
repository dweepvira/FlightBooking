# Flight Booking System

## Overview
The Flight Booking System is a web-based application developed for a travel agency to streamline the process of booking flights and managing customer interactions. Built with a Django backend and a responsive frontend, this system allows users to plan their trips, contact the agency, and view testimonials from other satisfied clients.

## Features
### User-Facing Features
- **Flight Booking Form:**
  - Users can input their travel details, such as destination, travel dates, and number of travelers.
  - All information is securely sent to the travel agency for processing.

- **Contact Form:**
  - Provides an easy way for users to get in touch with the agency for inquiries or support.

- **User Testimonials:**
  - Displays feedback from previous clients to build trust and showcase customer satisfaction.

### Admin Features
- **Trip Management:**
  - View and manage incoming trip requests.

- **Contact Queries:**
  - Access and respond to user-submitted inquiries.

- **Testimonial Moderation:**
  - Manage user testimonials for display on the platform.

## Technologies Used
### Frontend
- **HTML5**, **CSS3**, and **JavaScript** for a responsive and user-friendly interface.
- **Bootstrap** for styling and layout consistency.

### Backend
- **Django Framework** for robust backend logic and database management.
- **SQLite** (default Django database) for development; configurable for other databases.

## Installation
### Prerequisites
Ensure the following tools are installed on your system:
- Python 3.8+
- Django 4.0+

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/flight-booking-system.git
   cd flight-booking-system
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open `http://127.0.0.1:8000` in your web browser.

## Folder Structure
```
flight-booking-system/
├── flight_booking/        # Main Django application
├── static/                # Static files (CSS, JavaScript, images)
├── templates/             # HTML templates
├── db.sqlite3             # Default SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Contributing
We welcome contributions to improve the Flight Booking System. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of your changes.
