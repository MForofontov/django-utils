# Django Utilities

A collection of reusable views, middleware, models and helpers for Django projects.

## Overview

This repository gathers small, self contained examples of common patterns. The code
is intended as a starting point or learning resource that you can easily copy into
an existing Django project.

## Usage

1. Copy the required modules from this repository into your Django app.
2. Include any middleware in the `MIDDLEWARE` setting and add models or views as
   you would normally.
3. Adjust the code to fit your project (import paths, settings, etc.).

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
