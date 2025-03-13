from app import app
from Issues import issues
from login import login
from register import register

import os

app.register_blueprint(issues)
app.register_blueprint(login)
app.register_blueprint(register)



if  __name__ == "__main__":
    app.run(debug=True, port=5001)
