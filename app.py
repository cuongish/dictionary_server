import sqlite3 as sql
from flask import abort
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask_expects_json import expects_json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
schema = {
    "type": "object",
    "properties": {
        "key": {"type": "string"},
        "value": {"type": "number"}
    },
    "required": ["key", "value"]
}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/save', methods=['POST'])
@expects_json(schema)
def save():
    if request.is_json:
        content = request.get_json()
        try:
            with sql.connect("dict") as con:
                cur = con.cursor()
                cur.execute("REPLACE INTO dict (key,value) VALUES (?, ?)", (content['key'], content['value']))
                con.commit()
                msg = f'{content} successfully updated to dictionary server', 200
        except:
            con.rollback()
            msg = "An error in insert operation"
        finally:
            con.close()
            return msg


@app.route('/load/<string:key>', methods=['GET'])
def load(key):
    try:
        with sql.connect("dict") as con:
            cur = con.cursor()
            cur.execute("SELECT value FROM dict WHERE key = ?", key)
            con.commit()
            results = jsonify(value=cur.fetchone()[0])
            return results
    except:
        con.rollback()
        abort(404, "No value is saved for the given key, try again!")
    finally:
        con.close()


if __name__ == '__main__':
    app.run()
