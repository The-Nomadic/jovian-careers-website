from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOB = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Kollam, Kerala',
        'salary': 'Rs. 10,00,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'TVM, Kerala',
        'salary': 'Rs. 12,00,000',
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Work from home',
        'salary': 'Rs. 10,00,000',
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Chennai, Tamil Nadu',
        'salary': 'Rs. 16,00,000',
    },
    {
        'id': 5,
        'title': 'Python Developer',
        'location': 'TVM, Kerala',
        'salary': 'Rs. 12,00,000',
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOB, company_name="New Gens")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOB)


if __name__ == "__main__":
    app.run(debug=True)
