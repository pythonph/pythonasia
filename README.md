# PythonAsia 2026

> Nurturing a community of care, compassion, and growth.  
> The same heart of PyCon APAC, now as PythonAsia.

PythonAsia 2026 is the official website for the PythonAsia conference, built with Django and featuring integration with Pretalx for event management.

## 🚀 Features

- **Modern Django Application**: Built with Django 5.2+ and Python 3.13+
- **Responsive Design**: Tailwind CSS with DaisyUI components for beautiful, mobile-first design
- **Pretalx Integration**: Full integration with Pretalx for conference management
- **Production Ready**: Configured for deployment on Render with PostgreSQL
- **Monitoring**: Sentry integration for error tracking and performance monitoring
- **Static File Optimization**: WhiteNoise for efficient static file serving

## 🏗️ Project Structure

``` bash
pythonasia/
├── app/                    # Django applications
│   ├── home/              # Home page and landing
│   ├── presentations/     # Presentation management
│   ├── speakers/          # Speaker profiles
│   └── sponsors/          # Sponsor information
├── config/                # Django configuration
├── services/              # External service integrations
│   └── pretalx_service.py # Pretalx API integration
├── static/               # Static assets (CSS, images)
├── templates/            # Django templates
├── src/                  # Source CSS files
└── deploy/               # Deployment scripts
```

## 🛠️ Technology Stack

- **Backend**: Django 5.2+
- **Frontend**: Tailwind CSS with DaisyUI
- **Database**: PostgreSQL (production) / SQLite (development)
- **Deployment**: Render
- **Monitoring**: Sentry
- **Package Management**: uv

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- uv (recommended) or pip

### Development Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd pythonasia
   ```

2. **Install dependencies**

   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Set up the database**

   ```bash
   make setup-db
   ```

4. **Set up Tailwind CSS**

   ```bash
   make run-tailwind-setup
   ```

5. **Run the development server**

   ```bash
   # With Tailwind watching for changes
   make run-server-tailwind
   
   # Or just Django
   make run
   ```

The application will be available at `http://localhost:8000`

### Environment Variables

Create a `.env` file in the project root:

```env
# Required for production
SECRET_KEY=your-secret-key-here
DEBUG=False
APP_ENV=production
DATABASE_URL=postgresql://user:password@host:port/database

# Optional
SENTRY_DSN=your-sentry-dsn
PRETALX__BASE_URL=https://your-pretalx-instance.com
PRETALX__API_TOKEN=your-pretalx-api-token
```

## 🎨 Frontend Development

This project uses Tailwind CSS with DaisyUI for styling:

```bash
# Watch for CSS changes
make run-tailwind-watch

# Build CSS for production
make run-tailwind-build

# Configure Tailwind
make run-tailwind-config
```

## 🚀 Deployment

The application is configured for deployment on Render:

1. **Database**: PostgreSQL (free tier)
2. **Web Service**: Python runtime with automatic builds
3. **Static Files**: Served via WhiteNoise

### Manual Deployment

```bash
# Build static files
make run-tailwind-build

# Collect static files
python manage.py collectstatic

# Run migrations
python manage.py migrate
```

## 🔧 Available Commands

```bash
# Development
make run                    # Start Django development server
make run-server-tailwind    # Start server with Tailwind watching
make setup-db              # Create and run migrations

# Code Quality
make run-ruff              # Run Ruff linting and formatting
make run-pre-commit        # Run pre-commit hooks

# Tailwind CSS
make run-tailwind-setup    # Initial Tailwind setup
make run-tailwind-watch    # Watch for CSS changes
make run-tailwind-build    # Build CSS for production
make run-tailwind-config   # Configure Tailwind
```

## 📱 Pretalx Integration

The application integrates with Pretalx for conference management:

- **Event Information**: Fetch event details
- **Submissions**: Manage talk submissions
- **Speakers**: Speaker profiles and information
- **Talks**: Confirmed talks and schedules
- **Feedback**: Submission feedback system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run code quality checks: `make run-ruff`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏢 Organization

**PythonAsia 2026** is co-organized by Python Philippines and the Python community across Asia.

---

For more information about PythonAsia 2026, visit [pythonasia.python.ph](https://pythonasia.python.ph)
