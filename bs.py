from flask import Flask , render_template , redirect ,request ,url_for

app = Flask(__name__, template_folder='templates')

todos = [{"task" :"sample todo 1" , "done": False}]
       

@app.route('/')
def home():
       return render_template('index.html', todos=todos)

@app.route('/add' , methods = ['POST'])
def add():
       todo_task = request.form.get('todo_task')
       todos.append({"task": todo_task , "done": False})
       return redirect(url_for('home'))

@app.route('/edit/<int:home>' , methods = ['GET' , 'POST'])
def edit(home):
       todo_task = todos[home]
       if request.method == 'POST':
              todo_task['task'] = request.form.get('todo_task')
              return redirect(url_for('home'))
       else:
              return render_template('edit.html' , todo=todo_task, home=home)
       
@app.route('/check/<int:home>')
def check(home):
       todos[home]['done'] = not todos[home]['done']
       return redirect(url_for('home'))

@app.route('/delete/<int:home>')
def delete(home):
       todos.pop(home)
       return redirect(url_for('home'))


if __name__ == '__main__':
       app.run(debug=True)