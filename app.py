from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'Location': 'mumbai, Hyd',
        'Salary':'Rs. 10,00000'
    },
    {
        'id': 2,
        'title': 'Web Developer',
        'Location': 'Delhi, kolkata',
        
    },
    {
        'id': 3,
        'title': 'Full Stack Developer',
        'Location': 'Hyderabad, pune',
        'Salary':'Rs. 15,00000'
    },
    {
        'id': 1,
        'title': 'Backend Engineer',
        'Location': 'remote',
        'Salary':'Rs. 17,00000'
    }
]

@app.route("/")
def hello_jovian():
    return render_template("home.html", jobs=JOBS, company_name= 'Jovian')
    
@app.route("/api/jobs")
def list_job():
    return jsonify(JOBS)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0" ,debug= True)

