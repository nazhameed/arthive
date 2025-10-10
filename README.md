# Art-hive

## Overview 

Art-hive is a family friendly web application for organizing, preserving, and celebrating your child’s artwork. Instead of letting masterpieces pile up or get lost, Art-hive provides a digital “hive” where each child can have their own profile and gallery. Parents can easily upload, view, and manage their children’s creations in a secure, private, and visually engaging environment. The app is designed with accessibility, ease of use, and a playful bee/honey theme to make the experience fun for all ages.

## Features

## Screenshots / Demo

## Tech Stack

- Python 3
- Django
- Bootstrap 5
- HTML5 & CSS3
- JavaScript (for interactivity)
- Cloudinary (image hosting)
- PostgreSQL (production database)
- SQLite (local development)
- Heroku (cloud deployment)
- Git (version control)
- GitHub (repository hosting)

## Setup & Installation

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- **Python 3.8+** ([Download Python](https://www.python.org/downloads/))
- **pip** (comes with Python, for installing dependencies)
- **Git** ([Download Git](https://git-scm.com/downloads))
- **Virtualenv** (recommended, install with `pip install virtualenv`)
- **Cloudinary account** (for image hosting, [Sign up here](https://cloudinary.com/users/register/free))
- **PostgreSQL** (for production, optional for local dev)
- **Heroku CLI** (for deployment, [Install guide](https://devcenter.heroku.com/articles/heroku-cli))

> _Note: For local development, SQLite is used by default. Cloudinary and PostgreSQL are required for production deployment._

## Local Setup

Follow these steps to set up Art-hive for local development:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nazhameed/arthive.git
   cd arthive
   ```
2. ## Environment Variables

To run Art-hive locally or in production, you need to set up environment variables for sensitive information and third-party services. Create a `.env` file in the project root and add the following:

```
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://username:password@host:port/dbname
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

Replace the placeholders with your actual secret key, database URL, and Cloudinary credentials. For development, you can use SQLite and a dummy secret key, but remember to switch to a real database and secure key for production.


3. ## Database Migration

After setting up your environment variables and installing dependencies, apply the database migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. ## Running the App Locally

Once you have installed dependencies, set up environment variables, and run migrations, start the Django development server:

```bash
python manage.py runserver
```

Check your terminal for the correct local development URL after running the server.

## Deployment

### Cloud Platform Used

Art-hive is deployed on [Heroku](https://www.heroku.com/).

### Deployment Steps

1. **Prepare the App for Production**
    - Ensure all dependencies are listed in `requirements.txt`.
    - Set up `Procfile` for Heroku to run the Django app.
    - Configure `settings.py` to use environment variables for sensitive data.

2. **Set Up Heroku**
    - Create a new Heroku app via the Heroku Dashboard or CLI.
    - Add Heroku Postgres and Cloudinary add-ons (or configure external Cloudinary).

3. **Configure Environment Variables**
    - Set the following environment variables in Heroku:
      - `SECRET_KEY`
      - `DEBUG` (set to `False`)
      - `DATABASE_URL` (provided by Heroku Postgres)
      - `CLOUDINARY_URL` (from your Cloudinary account)
      - Any other required secrets (e.g., email credentials)

4. **Static Files**
    - Set `DISABLE_COLLECTSTATIC=1` in Heroku config vars to skip static file collection (if using only Cloudinary for media).
    - Alternatively, configure static files hosting if needed.

5. **Deploy**
    - Push your code to Heroku using Git:
      ```
      git push heroku main
      ```
    - Run database migrations:
      ```
      heroku run python manage.py migrate
      ```

6. **Check the App**
    - Visit your Heroku app URL to verify deployment.

### Production Settings

- `DEBUG = False` for security.
- All secrets and credentials are managed via environment variables.
- `ALLOWED_HOSTS` includes the Heroku app domain.
- Database is configured via `DATABASE_URL`.
- Media files (artwork images) are uploaded and stored securely on Cloudinary. The app uses the `CLOUDINARY_URL` environment variable to connect to your Cloudinary account for all media storage and retrieval.
- Static file collection is disabled (`DISABLE_COLLECTSTATIC=1`) unless configured otherwise.


## Using Art-Hive

### User Roles & Permissions
- **Parent (User):** Each registered user is a parent/carer who can create, view, edit, and delete their own child profiles and artworks.
- **Privacy:** All galleries and child profiles are private to the logged in user. No other users can view or modify your data.
- **Access Control:** You must be logged in to access the dashboard, add/edit children, or upload artwork. Unauthenticated users can only see the login and registration pages.

### How to Register/Login
1. **Register:**
   - Click the "Sign Up" or "Register" link on the homepage or login page.
   - Fill in your username, email, and password.
   - After registering, you can log in with your credentials.
2. **Login:**
   - Click the "Login" link.
   - Enter your username and password.
   - Upon successful login, you are redirected to your dashboard.
3. **Logout:**
   - Click the "Logout" button in the navigation bar to securely end your session.

### CRUD Operations
- **Children:**
  - **Create:** Add a new child profile from your dashboard.
  - **Read:** View all your children and their galleries on the dashboard.
  - **Update:** Edit a child's name or age from the dashboard.
  - **Delete:** Remove a child profile (and all associated artworks) from the dashboard.
- **Artworks:**
  - **Create:** Add new artwork to a child's gallery by uploading an image, title, and description.
  - **Read:** View all artworks for each child in a honeycomb gallery layout.
  - **Update:** Edit the title, description, or image of an artwork.
  - **Delete:** Remove an artwork from a child's gallery.

> **Note:** All actions are protected. Users can only manage their own children and artworks. Forms include validation and error messages for a smooth user experience.

## Data Model

Art-hive uses a simple, well-structured data model to organise users, children, and their artwork:

- **User** (Django built-in): Represents a parent account. Each user can create and manage multiple child profiles.

- **Child**
  - `name`: The child’s name
  - `age`: (optional) The child’s age
  - `parent`: Linked to the User who owns the profile
  - **Relationship:** Each User can have many Children, but each Child belongs to only one User (parent account).
  - Each Child profile is private to a single User and cannot be shared between accounts.

- **Artwork**
  - `title`: Title of the artwork (required)
  - `description`: Description of the artwork (required)
  - `image`: Uploaded image file (stored via Cloudinary)
  - `created_at`: Date/time the artwork was added
  - `child`: Linked to the Child profile
  - **Relationship:** Each Child can have many Artworks

**Diagram:**

<img src="gallery/static/assets/erd.png" alt="Entity relationship diagram" width="400"/>

## Accessibility & UX
- Accessibility Features
- Responsive Design

## Testing
- How to Run Tests
- Test Coverage

## AI Assistance Reflection
- How AI Was Used for Code, Debugging, Optimization, and Testing

## Known Issues / Limitations

## Contributing

This project is not open for public contributions. If you have feedback or spot an issue, please contact the author directly at naz.hameed@sky.com 

## License

This project is proprietary and is not licensed for public use, modification, or redistribution.

All rights reserved © Naz Hameed 2025.

## Acknowledgements

- Developed by [Your Name]
- Powered by Django, Bootstrap, Cloudinary, and PostgreSQL
- Icons by [Bootstrap Icons](https://icons.getbootstrap.com/)
- Fonts by [Google Fonts](https://fonts.google.com/)
- Hexagon CSS inspired by [CSS-Tricks](https://css-tricks.com/hexagons-and-beyond-flexible-responsive-grid-patterns-sans-media-queries/)
- Thanks to open-source contributors and the Stack Overflow community
- AI assistance via GitHub Copilot

## Hexagon Gallery Design

Art-hive features a unique “honeycomb” gallery layout, where each artwork is displayed inside a hexagonal cell mimicking the look of a real beehive. This playful design is both visually engaging and technically challenging to implement.

### How It Works

- **CSS Grid & Custom Properties:**  
  The gallery uses CSS Grid to arrange artwork cells in a responsive, staggered honeycomb pattern. Custom CSS variables control the size and spacing of each hexagon, adapting to different screen sizes.

- **Hexagon Shape:**  
  Each cell uses the `clip-path` property to create a perfect hexagon, allowing images and content to fit neatly inside. This avoids the need for SVGs or images for the shape itself.

- **Staggered Rows:**  
  Rows are offset using CSS transforms, so the hexagons interlock just like a real hive. This required careful calculation of widths, heights, and margins to avoid gaps or overlap.

- **Accessibility:**  
  Each hexagon is keyboard accessible and includes ARIA roles for screen readers, ensuring the gallery is usable by everyone.

- **Responsive Design:**  
  The honeycomb grid automatically adjusts the number of columns and the size of each hexagon based on the device, so it looks great on mobile, tablet, and desktop.

### Technical Challenges

- **Hexagon Math:**  
  Laying out hexagons in a grid is more complex than squares or rectangles. It required custom CSS variables and media queries to keep the pattern seamless at all sizes.
- **Image Cropping:**  
  Ensuring artwork images fit inside the hexagon without distortion or important details being cut off.
- **Performance:**  
  The design avoids heavy JavaScript, relying on modern CSS for smooth, fast rendering.

### Reflection

Designing and implementing the responsive hexagon (honeycomb) gallery was by far the hardest and most time consuming part of this project. Achieving a seamless, accessible, and fully responsive honeycomb layout with pure CSS required research, experimentation, and debugging especially to handle image cropping, staggered rows, and different screen sizes. While challenging and frustrating at times, it was also the most rewarding aspect, as it gives Art-hive its unique visual identity and playful user experience.

