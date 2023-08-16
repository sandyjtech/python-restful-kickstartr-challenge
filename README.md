# RESTFUL challenge

### Kickstartr
Welcome to Kickstartr. Assume we have a model called `Project` that inherits from `db.Model` and `SerializerMixin`, a corresponding table called `projects`, and a Flask application called `app`. Your application also initializes an `api` object from `flask_restful` and has the appropriate Resource class(es) and HTTP methods for constructing a RESTful API.

For each of the five actions below, write out the corresponding:

- HTTP Verb and URL (ie `GET '/dogs'`)
- corresponding CRUD action (ie `READ`)
- corresponding view method on your resource (i.e. `def get(self):`)
- corresponding SQLAlchemy query method(s) (ie. `.all()`)

### Actions

1. Displays all of the projects
2. Displays information about one project
3. Creates a new project based on given parameters
4. Updates an existing project with given parameters
5. Deletes an existing project

### BONUS
Build out the above as a full RESTful Flask API with a model, migration, routes, resource classes and view methods.
