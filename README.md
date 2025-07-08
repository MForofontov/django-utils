# Django Utilities

A collection of reusable views, middleware, models and helpers for Django projects.

## Overview

This repository gathers small, self contained examples of common patterns. The code
is intended as a starting point or learning resource that you can easily copy into
an existing Django project.

## Requirements

- **Python**: 3.9 or later.
- **Dependencies**: install the packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Usage

1. Copy the required modules from this repository into your Django app.
2. For models or serializers, add their containing package to `INSTALLED_APPS` in
   your `settings.py`.
3. For middleware, include the dotted path in the `MIDDLEWARE` list.
   ```python
   MIDDLEWARE = [
       ...,
       "middlewares.APIVersioningMiddleware",
   ]
   ```
4. Adjust imports and settings to fit your project structure.

### Environment variables

Some modules change behaviour based on environment variables. Set
`DJANGO_ENV=production` to enable secure cookie handling in the custom token
views. Make sure required Django settings such as `SECRET_KEY` and
`EMAIL_VERIFICATION_SALT` are configured as well.

Each module is independent and does not rely on packaging or installation.

## Modules

### api_views

Example REST API views built with `django-rest-framework`. They demonstrate tasks
such as currency conversion, file upload handling and token generation.

### middlewares

A set of standalone Django middleware classes covering features like CORS, request
logging and rate limiting. Add any of these to your `MIDDLEWARE` list to enable the
behaviour.

### models

Reusable model mixins and base classes, including audit trails, soft deletion and a
custom user model.

### serializers

Serializers used by some of the example views, primarily for JWT authentication
workflows or basic data validation.

### tokens

Helpers for generating verification tokens.

## License

Distributed under the terms of the [GNU General Public License v3](LICENSE).
