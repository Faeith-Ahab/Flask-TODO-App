# Import the library, enable template, add request object(at the first addition of a request, add an accessor)
# the code is appended according to the functions required to run.

from flask import Flask, render_template, request, redirect, url_for #

# Create the app

app = Flask(__name__, template_folder="templates")

tasks=[]

# Create the instance

@app.route('/')
def index():
    return render_template("index.html")


# Create a decorator[@app] new task [post method]
# Function must be on the same indentation as the decorator

# Methods on the http protocol, create a variable that is going to store our task, we need a request object which has various methods we can pass through

@app.route('/add_task', methods=['POST'])
def create_task():
    task = request.form.get('task')      # value must be descriptive depending on what the field is, ie. task
    tasks.append(task)                   # Add item to list by appending
    return redirect(url_for("index"))    # redirect always has a particular path or URL
                                         # It exists in Flask, there it is imported.
                                         # URL is also a function
    

# Enable debug mode

if __name__ == '__main__':
   app.run(debug=True)
   
   