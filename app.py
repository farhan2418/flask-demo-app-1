from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@app.route('/', methods = ['POST', 'GET'])
def index():
    import IPython;IPython.embed()
    from models import db
    from models.todo import Todo
    if request.method == 'POST':
        task_content = request.form.get('content')
        new_task = Todo(content = task_content)

        try: 
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'there was an error, and we don\'t know it'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = tasks)

if __name__ == "__main__":
    app.run(debug=True)