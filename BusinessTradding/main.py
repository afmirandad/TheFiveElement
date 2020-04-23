import pymysql
import json
from flask import Flask, request, render_template, flash, redirect
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from BusinessTradding.appFirst import appFirst
from BusinessTradding.api.db_config import mysql
from BusinessTradding.forms.formulario import FormInicio


# Instancia con un objeto llamado __name__
appFirst.config['SECRET_KEY'] = 'you-will-never-guess'

# Fuentes de datos
with open('datas/items.json') as json_file :
    itemsData = json.load(json_file)


@appFirst.route('/', methods=['GET', 'POST'])
@appFirst.route('/<name>/', methods=['GET', 'POST'])
@appFirst.route('/<name>/<lastName>', methods=['GET', 'POST'])
@appFirst.route('/<name>/<lastName>/<int:age>', methods=['GET', 'POST'])
def miperro(name='Felipe', lastName='Miranda', age=11) :
    # tambien se pueden hacer uso de listas, diccionatios y tuplas, al final
    # tambien se pueden agregar custom headers dentro del JSON
    return render_template('index.html', name=name.upper(), lastName=lastName.upper(), age=age, list=itemsData), {
        'Server' : 'Andres' }


# Endpoints API REST

@appFirst.route('/api/users')
def users() :
    try :
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM bt_users")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e :
        print(e)
    finally :
        cursor.close()
        conn.close()


@appFirst.route('/api/user/<int:id>')
def user(id) :
    try :
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM bt_users WHERE U_idUser=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e :
        print(e)
    finally :
        cursor.close()
        conn.close()


@appFirst.route('/api/user/update', methods=['POST'])
def update_user() :
    try :
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _email = _json['email']
        _password = _json['pwd']
        # validate the received values
        if _name and _email and _password and _id and request.method == 'POST' :
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (_name, _email, _hashed_password, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else :
            return not_found()
    except Exception as e :
        print(e)
    finally :
        cursor.close()
        conn.close()


@appFirst.route('/api/user/add', methods=['POST'])
def add_user() :
    try :
        _json = request.json
        _user = _json['user']
        _name = _json['name']
        _city = _json['city']
        _typeD = _json['type']
        _doc = _json['doc']
        _addre = _json['addre']
        _zone = _json['zone']
        _mobile = _json['mobile']
        _fix = _json['fix']
        _pass = _json['pass']
        _date = _json['date']
        _sex = _json['sex']
        _imgd = _json['imgd']
        _imga = _json['imga']
        # validate the received values
        if _name and _email and _password and request.method == 'POST' :
            # do not save password as a plain text
            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO `bt_tradding`.`bt_users` (`U_username`, `U_nameUser`, `U_city`, `U_email`, `U_typeDoc`, `U_document`, `U_address`, `U_Neight`, `U_mobile`, `U_fixPhone`, `U_password`, `U_birthDate`, `U_sex`, `U_imgDoc`, `U_imgAddress`) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
            data = (_user, _name, _city, _typeD, _doc, _addre, _zone, _mobile, _fix, _pass, _date, _sex, _imgd, _imga,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else :
            return not_found()
    except Exception as e :
        print(e)
    finally :
        cursor.close()
        conn.close()


@appFirst.route('/api/user/delete/<int:id>')
def delete_user(id) :
    try :
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e :
        print(e)
    finally :
        cursor.close()
        conn.close()


@appFirst.errorhandler(404)
def not_found(error=None) :
    message = {
        'status' : 404,
        'message' : 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@appFirst.route('/login',methods=['GET', 'POST'])
def login():
  form = FormInicio()
  if(form.validate_on_submit()):
    flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(form.nombre.data, form.recordar.data))
    return 'gracias'
  return render_template('loginuser.html', form=form)


# Registro de productos

@appFirst.route('/api/product/add')
def add_product() :
    try :
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e :
        print(e)
    finally :
        cursor.close()
        conn.close()

if __name__ == '__main__' :
    appFirst.run(port=8181, debug=True)
