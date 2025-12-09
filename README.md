# Truth Food 🍽️

A social platform for sharing real, measured information about restaurant food portions. Help diners make informed decisions with actual portion sizes, weights, and serving recommendations.

## 📖 About

Ever wondered if a restaurant dish is "really enough for 4 people" or "too much for 2"? Truth Food provides verified, measured data about food portions at restaurants so you can make clear decisions before ordering.

### Key Features

- **Real Measurements**: Actual weights, portion sizes, and dimensions
- **Verified Reviews**: Community-driven content with trustable user validation
- **Portion Recommendations**: Clear guidance on servings per dish
- **Restaurant Database**: Comprehensive collection of dishes and establishments
- **Trust System**: Verified users after accuracy validation

## 🚀 Getting Started

### Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/marthox/truth-food.git
cd truth-food
```

2. Copy the environment template and configure your secrets:

```bash
cp .env.example .env
```

3. Generate a new SECRET_KEY (replace the value in `.env`):

```bash
uvx --from django django-admin shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

4. Install dependencies:

```bash
uv sync
```

5. Run migrations:

```bash
uv run python manage.py migrate
```

6. Create a superuser (optional):

```bash
uv run python manage.py createsuperuser
```

7. Start the development server:

```bash
uv run python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the application.

## 🛠️ Tech Stack

- **Framework**: Django 6.0
- **API**: Django REST Framework 3.16+
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Package Manager**: uv

## 📝 Environment Variables

Required environment variables (see `.env.example`):

- `SECRET_KEY`: Django secret key for cryptographic signing
- `DEBUG`: Debug mode (True for development, False for production)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts (production)

## 🗺️ Roadmap

- [x] Project setup and configuration
- [ ] User authentication and profiles
- [ ] Restaurant and dish models
- [ ] Measurement submission system
- [ ] Trust and verification system
- [ ] Public API for measurements
- [ ] Mobile-responsive UI
- [ ] Image upload for dishes
- [ ] Search and filtering
- [ ] User reputation system

## 🤝 Contributing

Currently in early development. The platform will initially be single-user, with multi-user verification features coming in future releases.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

### Marthox

- GitHub: [@marthox](https://github.com/marthox)

---

**Note**: This is an early-stage project focused on providing truthful, measured information about restaurant food portions to help diners make informed decisions.
