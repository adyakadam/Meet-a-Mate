from flask import Flask, render_template, request
app = Flask(__name__)

mentors = {
    "9":    {
                "name": "Rinkle Carpenter",
                "grade": "9",
                "insta" : "rinkleinmyeyes",
                "email": "r1nkl@yahoo.com",
                "phone": "345-496-9983"
            },
    "10":   {
                "name": "Senapi",
                "grade": "10",
                "insta" : "rinkleinmyeyes",
                "email": "r1nkl@yahoo.com",
                "phone": "345-496-9983"
            },
    "11":   {
                "name": "Prence Gilamn",
                "grade": "11",
                "insta" : "princeofw1rld",
                "email": "prencelm@yahoo.com",
                "phone": "567-486-9383"
            },
    "12":    {
                "name": "Jane Cline",
                "grade": "12",
                "insta" : "rinkleinmyeyes",
                "email": "r1nkl@yahoo.com",
                "phone": "345-496-9983"
            }
}

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/')
def idea():
    return render_template('idea.html')

@app.route('/mate')
def find_a_mate():
    return render_template('findamentor.html')

@app.route("/findmatch", methods=['POST'])
def find_match():
    user_name = request.form["name"]
    grade = request.form["grade"]
    insta_id = request.form["insta"]
    print(f'Name: {user_name}')
    print(f'Insta: {insta_id}')
    print(f'Grade: {grade}')
    #process results and display back to user!
    selected_mentor = mentors[grade]
    print(selected_mentor)

    result_dict = {
        "user" : {
            "name": user_name,
            "insta_id": insta_id
        },
        "mentor_matches":[
            selected_mentor
        ]
    }
    return render_template('find_matches.html', results=result_dict)