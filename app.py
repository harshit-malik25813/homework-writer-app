from flask import Flask, render_template, redirect, url_for, request
import helpers
# Initialise the flask application
app = Flask(__name__)
generated_homework = ""


def build_homework_output(form_data):
    # Turn the form answers into one neat block of text.
    sections = [
        helpers.date(),
        helpers.maths(form_data.get("maths", "").strip()),
        helpers.phy(form_data.get("phy", "").strip()),
        helpers.chem(form_data.get("chem", "").strip()),
        helpers.bio(form_data.get("bio", "").strip()),
        helpers.sst(form_data.get("sst", "").strip()),
        helpers.hindi(form_data.get("hindi", "").strip()),
        helpers.eng(form_data.get("eng", "").strip()),
        helpers.additional(form_data.get("additional", "").strip()),
    ]
    return "\n".join(section for section in sections if section)


@app.route("/", methods=["GET", "POST"])
def index():
    # Show the form page.
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    # Read the submitted form and save the formatted homework text.
    global generated_homework
    generated_homework = build_homework_output(request.form)
    # Send the user to the output page after the homework is ready.
    return redirect(url_for("output"))


@app.route("/output", methods=["GET"])
def output():
    # Show the saved homework in a clean output page.
    return render_template("output.html", generated_homework=generated_homework)
