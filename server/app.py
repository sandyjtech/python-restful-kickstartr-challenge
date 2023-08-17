from flask import Flask, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Project, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Note: `app.json.compact = False` Configures JSON responses to print on indented lines
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


class Projects(Resource):
    ## INDEX
    def get(self):
        projects = [project.to_dict() for project in Project.query.all()]
        return make_response(projects, 200)

    ## CREATE
    def post(self):
        data = request.get_json()
        new_project = Project(
            name=data["name"],
            details=data["details"],
        )
        ##new_project = Project(**data)
        db.session.add(new_project)
        db.session.commit()
        return make_response(new_project.to_dict(), 201)


api.add_resource(Projects, "/projects")


class ProjectById(Resource):
    ## SHOW
    def get_by_id(self, id):
        project = Project.query.filter(Project.id == id).first().to_dict()
        return make_response(project, 200)

    ## UPDATE
    def patch(self, id):
        data = request.get_json()
        #project = Project.query.filter(Project.id == id).first()
        project = Project.query.get_or_404(id)
        
        for key, value in data.items():
            setattr(project, key, value)
        db.session.add(project)
        db.session.commit()

        return make_response(project.to_dict(), 202)

    ## DESTROY
    def delete(self, id):
        project = Project.query.filter(Project.id == id).first()
        db.session.delete(project)
        db.session.commit()

        return make_response("", 204)


api.add_resource(ProjectById, "/projects/<int:id>")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
