from flask import Flask, render_template, request, redirect
import csv
#render_template function allows us to send the html function
app = Flask(__name__) #created an instance of Flask app
# print(__name__) #This is the main file we are running

#Using decorator. Gives us extra tools for our server.
#everytime we encounter a /, define a function and return hello world
# @app.route('/')
# def hello_world():
#     return render_template('index.html')

#@app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
    # return render_template('index.html', name=username, post_id=post_id)

# @app.route('/' or '/works.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
# @app.route('/about') 
# def about():
#     return 'A little bit about me! I am a 25 year old man trying to fulfill his dreams!'

# @app.route('/blog') 
# def blog():
#     return 'These are my blogs!'

# @app.route('/blog/dogs') 
# def blog2():
#     return 'These are my dog blogs!'


@app.route('/' or '/works.html')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
    

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something has gone wrong, Please try again'

    # return render_template('login.html', error=error)

    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # # the code below is executed if the request method
    # # was GET or the credentials were invalid
    # return render_template('login.html', error=error)