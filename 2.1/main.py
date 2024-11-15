from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
DATABASE = 'database.db'
con = sqlite3.connect('database.db', check_same_thread=False)
cur = con.cursor()

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        task_task = request.form['task']

        try:
            if(request.form['is_active'] == 'on'):
                task_isActive = True
            else:
                task_isActive = False
        except:
            task_isActive = False


        try:
            cur.execute("INSERT INTO tasks (task, is_active )VALUES (? , ?)", (task_task, task_isActive))
            con.commit()
            return redirect('/')
        except:
            return 'Error in adding new task'

    else:
        tasks = cur.execute("SELECT * FROM tasks").fetchall()
        return render_template('index.html', tasks=tasks)



@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = cur.execute("SELECT * FROM tasks").fetchall()
    return jsonify(tasks), 200

@app.route('/tasks/<int:id>', methods=['GET'])
def list_task(id):
    tasks = cur.execute("SELECT * FROM tasks WHERE id = " + str(id)).fetchall()
    if tasks:
        return jsonify(tasks), 200
    else:
        return 'Not Existing', 404

@app.route('/tasks/create/<string:task>/<string:isActive>', methods=['PUT'])
def create_task(task, isActive):
    try:
        cur.execute("INSERT INTO tasks (task, is_active )VALUES (? , ?)", (task, isActive))
        con.commit()
        return 'Added', 201
    except:
        return 'Error in adding new task', 404

@app.route('/tasks/update/<int:id>/<string:task>/<string:isActive>', methods=['POST'])
def update_task(id, task, isActive):
    try:
        cur.execute("UPDATE tasks SET task = ?, is_active = ? WHERE id = ?", (task, isActive, id))
        con.commit()
        return 'uppdated', 200
    except Exception as error:
        return error, 404

@app.route('/delete/<int:id>')
def delete(id):
    try:
        cur.execute("DELETE FROM tasks WHERE id = " + str(id))
        con.commit()
        return redirect('/')
    except Exception as error:
        return error, 404

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):

    task = cur.execute("SELECT * FROM tasks WHERE id = " + str(id)).fetchall()[0]
    if request.method == 'POST':
        task_task = request.form['task']
        try:
            if (request.form['is_active'] == 'on'):
                task_isActive = True
            else:
                task_isActive = False
        except:
            task_isActive = False

        try:
            cur.execute("UPDATE tasks SET task = ?, is_active = ? WHERE id = ?", (task_task, task_isActive, id))
            con.commit()
            return redirect('/')
        except Exception as error:
            print(error)
            return 'error with update'


    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)