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
- Prerequisites
- Local Setup
- Environment Variables
- Database Migration
- Running the App Locally

## Deployment
- Cloud Platform Used
- Deployment Steps
- Production Settings (Security, DEBUG, etc.)

## Usage
- User Roles & Permissions
- How to Register/Login
- CRUD Operations

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

## License

## Acknowledgements