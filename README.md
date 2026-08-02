# URL Shortener

A Flask application that creates short URLs and tracks visits.

## Features

- Create short URLs
- Redirect users to original URLs
- Track click statistics
- Validate submitted URLs
- Rate limit requests

## Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy Core
- pytest
- mypy

## Demo

https://url.matijas.dev

## Deployment

Containerized with Docker and deployed using Coolify.

## Running Locally

Clone the repository:

```bash
git clone https://github.com/matijasdev/url_shortener.git
cd url_shortener
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file with the required environment variables:

```env
HOST_URL=http://localhost:5000
DATABASE=your_database_url
SECRET_KEY=your_secret_key
```

Replace the values with your own configuration.

Run the application:

```bash
flask --app main run
```

## Testing

Run tests with:

```bash
python -m pytest
```

## Type Checking

Run mypy with:

```bash
mypy .
```