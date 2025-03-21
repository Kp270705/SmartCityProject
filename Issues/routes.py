from Issues import issues
from flask import request, render_template
from app import db
from app.models import Issue

@issues.route("/issues", methods=["GET", "POST"])
def get_issues():

    if request.method == 'POST':
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        category = request.form.get('category')
        issue_description = request.form.get('issue')
        priority = request.form.get('priority')
        contact = request.form.get('contact')

        issueobj = Issue(category, priority, issue_description, contact, latitude, longitude)

        db.session.add(issueobj)
        db.session.commit()
        print(f"{issue_description} added...")


    return render_template("issues.html")


@issues.route("/myissues")
def my_issues():
    # Fetch issues from the database
    issues_list = Issue.query.all()

    # Pass data to myIssues.html
    return render_template("myIssues.html", issues=issues_list)
