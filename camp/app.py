from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", passwd="0000", db="camping", charset="utf8")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    location = request.args.get('location') or request.form.get('location')
    cursor = db.cursor()

    tables = ['단양', '보은', '영동', '옥천', '음성', '제천', '증평', '진천', '청주', '충주']
    result = []

    if location in tables:
        query = f"SELECT name FROM {location}"
    else:
        for table in tables:
            query = f"SELECT name FROM {table} WHERE name LIKE '%{location}%'"
            cursor.execute(query)
            result += cursor.fetchall()

        return render_template('search.html', result=result)

    cursor.execute(query)
    result = cursor.fetchall()
    return render_template('search.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
