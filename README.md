# Art-hive

## Overview 

Art-hive is a family friendly web application for organising, preserving, and celebrating your child’s artwork. Instead of letting masterpieces pile up or get lost, Art-hive provides a digital “hive” where each child can have their own profile and gallery. Parents can easily upload, view, and manage their children’s creations in a secure, private, and visually engaging environment. The app is designed with accessibility, ease of use, and a playful bee/honey theme to make the experience fun for all ages.

## Features

- **Child Profiles:** Organise artwork by creating separate profiles for each child.
- **Honeycomb Gallery:** View artworks in a unique, responsive hexagonal grid inspired by a beehive.
- **Artwork Upload & Management:** Upload images (HEIC, JPEG, PNG), add titles and descriptions, and edit or delete artworks.
- **Secure Image Hosting:** All images are stored and served via Cloudinary for speed and security.
- **Accessibility:** Keyboard navigable, ARIA roles, and tested for screen reader compatibility.
- **Privacy:** All galleries and profiles are private to the logged-in user.
- **Responsive Design:** Layout adapts seamlessly to mobile, tablet, and desktop screens.
- **User Authentication:** Secure registration, login, and logout for parents.
- **Dashboard:** Manage children and their galleries from a central dashboard.
- **Edit & Delete:** Easily edit or remove child profiles and individual artworks.

<img src="gallery/static/assets/dashboard.png" alt="child profile dashboard" width="400"/>  <img src="gallery/static/assets/hive-gallery.png" alt="Hexagon hive gallery" width="400"/>

## User Experience Design

Art-hive was designed with families in mind, focusing on simplicity, accessibility, and a playful visual identity. The user experience is shaped by the following principles:

- **Simplicity:** The interface is clean and intuitive, making it easy for parents and children to navigate, upload, and manage artwork without technical barriers.
- **Accessibility:** All features are keyboard navigable, include ARIA roles, and have been tested for screen reader compatibility. Colour contrast and font choices ensure readability for all users.
- **Playful Theme:** The honeycomb gallery and bee inspired visuals create a fun, engaging environment that appeals to children and families.
- **Mobile First:** The layout is fully responsive, ensuring a seamless experience on mobile, tablet, and desktop devices.
- **Feedback & Validation:** Forms provide clear validation messages and feedback, helping users correct errors and complete actions confidently.
- **Privacy by Default:** All galleries and profiles are private to the logged-in user, with clear messaging about data security and privacy.
- **Guided Flows:** Registration, login, and CRUD operations are designed as step-by-step flows, minimising confusion and supporting new users.

### Example User Stories

- As a parent, I want to easily upload and organise my child’s artwork, so I can preserve their creations in one place.
- As a user, I want the gallery to look fun and engaging, so my child enjoys viewing their artwork.
- As a parent, I want to access the app on my phone or tablet, so I can upload photos of artwork directly from my device.
- As a user, I want clear feedback if I make a mistake in a form, so I can fix it quickly.
- As a parent, I want to know my child’s artwork is private and secure, so I feel confident using the app.
- As a user with accessibility needs, I want to navigate the app with a keyboard and screen reader, so I can use all features independently.

The overall goal is to make preserving and celebrating children’s artwork a joyful, stress-free experience for every family.

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

## Live Demo

Try Art-hive here: [https://arthive-3f3b6382fabb.herokuapp.com/](https://arthive-3f3b6382fabb.herokuapp.com/)

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

To run Art-hive locally or in production, you need to set up environment variables for sensitive information and third party services. Create a `.env` file in the project root and add the following:

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

## Agile Development Process

Art-hive was developed using Agile principles, with all work tracked on a GitHub Project board. The MoSCoW method (Must have, Should have, Could have, Won’t have) was used to prioritize features and guide development.

- **Project Board:**  
  All tasks, user stories, and bugs were managed on a GitHub Project board with columns for Todo, In Progress, and Done. This provided clear visibility and progress tracking throughout the project.
  [GitHub Project board](https://github.com/users/nazhameed/projects/8)

- **MoSCoW Prioritization:**  
  Features and tasks were categorized as Must have, Should have, Could have, or Won’t have for this release. This ensured that core functionality was delivered first, while allowing flexibility for enhancements.


<img src="gallery/static/assets/project-board.png" alt="Github project board" width="400"/>

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

## Accessibility 

Art-hive was tested with [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) to ensure high standards for performance, accessibility and best practices.

### Lighthouse Best Practices: Troubleshooting & Improvement

When first running a Lighthouse audit, Art-hive received a **Best Practices** score of 78. The main issues identified were:

- Use of insecure image URLs (HTTP instead of HTTPS) for some resources.
- Missing or misconfigured Content Security Policy (CSP) headers.
- Minor accessibility or code warnings flagged by Lighthouse.

#### Troubleshooting Steps

- Used AI assistance (GitHub Copilot) to help diagnose, debug, and resolve the issues flagged by Lighthouse.
- Updated all image and static asset URLs to use HTTPS.
- Integrated and correctly configured the `django-csp` middleware to set a strict, modern CSP header.
- Ensured all Cloudinary images are served securely and allowed by the CSP.
- Reviewed and fixed any additional warnings flagged by Lighthouse.

After these changes, a new Lighthouse audit showed a **Best Practices** score of **100**.

<img src="gallery/static/assets/lighthouse.png" alt="Lighthouse report for Art-hive" width="400"/>

This process helped ensure Art-hive follows web best practices for security, reliability, and user experience.


## Testing

Art-hive was thoroughly tested manually to ensure a robust, user friendly, and accessible experience.

### Manual Testing
- All major user stories and features were tested using a structured test case table (see below and image).
- Tests were performed on multiple browsers (Chrome, Firefox, Safari) and devices (desktop, tablet, mobile).
- Edge cases, form validation, and error handling were checked for all forms and user actions.
- Accessibility was manually checked using keyboard navigation and screen reader tools.

<img src="gallery/static/assets/test-cases.png" alt="Manual testing table" width="400"/>

### Test Coverage
- Manual testing covers all core functionality, user flows, and cross-device compatibility.
- Automated tests will be included in future versions to further improve reliability and maintainability.

### Validation

Art-hive’s HTML and CSS were validated using the official W3C validators to ensure standards compliance and cross-browser compatibility.

- **HTML Validation:** All main pages were checked using the [W3C Markup Validation Service](https://validator.w3.org/).
- **CSS Validation:** Stylesheets were checked using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

Below is a screenshot showing successful validation:

<img src="gallery/static/assets/html-validation.png" alt="Manual testing table" width="400"/>

<img src="gallery/static/assets/css-validation.png" alt="Manual testing table" width="400"/>



## AI Assistance Reflection

As part of the AI Augmented Full Stack Development course, I used GitHub Copilot as an interactive assistant during development. Rather than generating large amounts of code automatically, I mainly used AI to guide me through specific problems step by step. I described issues or goals, and Copilot provided targeted suggestions, explanations, or code snippets in response to my instructions.

AI was most helpful for:
- Explaining error messages and configuration issues (e.g., CSP, static files)
- Suggesting best practices for security and deployment
- Providing code examples or troubleshooting tips when I asked for them

All major design, coding, and testing decisions were made by me, with AI acting as a responsive support tool that I could consult as needed. This approach allowed me to stay in control of the project while benefiting from AI’s ability to clarify concepts and accelerate problem solving.

## Known Issues / Limitations

- **HEIC Browser Support:** Some browsers do not natively support HEIC images. Art-hive uses Cloudinary’s automatic format conversion, but if Cloudinary fails to convert, HEIC images may not display in all browsers.
- **No Public Sharing:** Galleries and artwork are private to each user; there is currently no option for public or shared galleries.
- **No Automated Testing:** All testing was performed manually. Automated tests (unit, integration, accessibility) are planned for future versions.
- **No Email Verification:** User registration does not include email verification or password reset functionality.
- **Limited User Roles:** Only parent (user) accounts are supported; there are no admin or child logins.
- **Performance on Large Galleries:** The honeycomb gallery is optimised for moderate numbers of artworks. Very large galleries may impact performance or layout.
- **No Internationalisation:** The app is currently English-only and does not support multiple languages.

## Future Improvements

- **Automated Testing:** Add unit, integration, and accessibility tests to improve reliability and maintainability.
- **Email Verification & Password Reset:** Implement email verification during registration and password reset functionality for users.
- **Public/Shared Galleries:** Allow users to optionally share galleries or artworks with others via public or private links.
- **Public Artwork Carousel:** Enable parents to mark selected artworks as public, which will then be featured in a public carousel on the homepage.
- **Admin Dashboard:** Add an admin interface for site management and moderation.
- **Child/Family Accounts:** Support additional user roles, such as child logins or family sharing.
- **Bulk Upload:** Enable uploading of multiple artworks at once.
- **Gallery Sorting & Filtering:** Allow users to sort and filter artworks by date, title, or tags.
- **Internationalisation:** Add support for multiple languages.
- **Dark Mode:** Provide a dark theme option for user comfort.
- **Performance Optimisation:** Enhance gallery performance for users with large numbers of artworks.
- **Leaderboard & Gamification:** Introduce a leaderboard to highlight top contributors (e.g., most uploads, most public artworks) and add gamified features such as badges, achievements, or streaks to encourage engagement and creativity.


## Contributing

This project is not open for public contributions. If you have feedback or spot an issue, please contact the author directly at naz.hameed@sky.com 

## License

This project is proprietary and is not licensed for public use, modification, or redistribution.

All rights reserved © Naz Hameed 2025.

## Acknowledgements

- Developed by Naz Hameed
- Powered by Django, Bootstrap, Cloudinary, and PostgreSQL
- Icons by [Bootstrap Icons](https://icons.getbootstrap.com/)
- Fonts by [Google Fonts](https://fonts.google.com/)
- Hexagon CSS inspired by [CSS-Tricks](https://css-tricks.com/hexagons-and-beyond-flexible-responsive-grid-patterns-sans-media-queries/)
- Thanks to open-source contributors and the Stack Overflow community
- AI assistance via GitHub Copilot

