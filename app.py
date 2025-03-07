from app import app
from Issues import issues
from login import login

app.register_blueprint(issues)
app.register_blueprint(login)

if  __name__ == "__main__":
    app.run(debug=True, port=5001)
