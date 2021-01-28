from flask import Flask, redirect, render_template, request, url_for

import csv
app = Flask(__name__)
# print(app)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#for database.txt 
def write_to_file(data):
    with open('./database.txt','a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = db.write(f'\n {email},{subject},{message}')
#for csv 
def write_to_csv(data):
    with open('database.csv', mode='a') as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_w = csv.writter(db2,delimiter = ',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_w.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'try again'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)

