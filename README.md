# Blog Project - Django

A full-featured blog application built with Django that allows users to create, read, update, search blog posts with image thumbnails, searching and pagination.

## Features

- **User Authentication**: Sign up, login, and logout functionality
- **Blog Posts Management**: 
  - Create new blog posts with title, content, author, and thumbnail images
  - View all posts with pagination (3 posts per page)
  - View individual post details
  - Update existing posts (login required)
- **Search Functionality**: Search posts by title or content
- **Image Upload**: Upload and display thumbnail images for blog posts
- **Responsive Design**: Clean and modern UI with static CSS and JavaScript

## Tech Stack

- **Backend**: Django
- **Database**: SQLite
- **Image Processing**: Pillow
- **Python**

## Project Structure

```
Blog/
├── blogproject/
│   ├── blogproject/          # Main project settings
│   │   ├── settings.py       # Django settings
│   │   ├── urls.py          # Root URL configuration
│   │   └── ...
│   ├── posts/               # Blog posts app
│   │   ├── models.py        # Post model
│   │   ├── views.py         # Post views (home, detail, create, update, search)
│   │   ├── forms.py         # Post creation form
│   │   ├── urls.py          # Post URL patterns
│   │   ├── templates/       # Post templates
│   │   └── static/          # CSS, JS, images
│   ├── users/               # User authentication app
│   │   ├── views.py         # Authentication views
│   │   ├── forms.py         # Login and registration forms
│   │   └── urls.py          # Auth URL patterns
│   ├── templates/           # Global templates
│   │   └── users/          # User auth templates
│   ├── media/               # Uploaded media files
│   │   └── thumbnails/     # Post thumbnails
│   └── manage.py           # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Usage

### Accessing the Application

- **Home Page**: `http://127.0.0.1:8000/` - View all blog posts
- **About Page**: `http://127.0.0.1:8000/about/`
- **Services Page**: `http://127.0.0.1:8000/services/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

### User Features

1. **Sign Up**: Navigate to `/auth/signup/` to create a new account
2. **Login**: Navigate to `/auth/login/` to log in
3. **Create Post**: After logging in, go to `/create_post` to create a new blog post
4. **View Posts**: Browse all posts on the home page with pagination
5. **Search**: Use the search functionality to find posts by title or content
6. **Update Post**: Click on a post to view details, then update if you're logged in


## Key URLs

- `/` - Home page (all posts)
- `/about/` - About page
- `/services/` - Services page
- `/create_post` - Create new post (login required)
- `/post/<post_id>` - View post details
- `/post/update/<post_id>/` - Update post (login required)
- `/search/?q=<query>` - Search posts
- `/auth/login/` - User login
- `/auth/signup/` - User registration
- `/auth/logout/` - User logout

## Models

### Post Model
- `title`: CharField (max 225 characters)
- `content`: TextField
- `author`: CharField (max 255 characters)
- `thumbnail`: ImageField (uploaded to 'thumbnails' folder)
- `date_created`: DateTimeField (auto-generated)
