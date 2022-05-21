from flask import Flask,render_template,request,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from add_data_form import Add_Form
import sqlite3


app=Flask(__name__)
app.secret_key=b'263433102'
bootstrap=Bootstrap(app)

@app.route("/")
def home_page():
    sqlite_connection=sqlite3.connect('shop.db')
    cursor=sqlite_connection.cursor()
    data=cursor.execute("Select * from Product")
    return render_template('home.html',database_rows=data)


@app.route("/add_data",methods=['GET','POST'])
def add_data():
    form=Add_Form(request.form)
    if request.method=='POST':
        form_product_ID=form.product_ID.data
        form_list_ID=form.list_ID.data
        form_prodName=form.prodName.data
        form_date_sold=form.date_sold.data
        form_descript=form.descript.data
        #print(form_product_ID,form_list_ID,form_prodName,form_date_sold,form_descript)
        sqlite_connection = sqlite3.connect('shop.db')
        cursor = sqlite_connection.cursor()
        sql_command="Insert into Product values('{ID}','{List}','{Name}','{sold}','{descript}')"\
            .format(ID=form_product_ID,List=form_list_ID,Name=form_prodName,sold=form_date_sold,descript=form_descript)
        cursor.execute(sql_command)
        sqlite_connection.commit()
        sqlite_connection.close()
        flash('Row successfully added!','success')
        return redirect(url_for('home_page'))
    return render_template('add_data.html',title='Add Data', form=form)


@app.route("/edit_data/<product_id>",methods=['GET','POST'])
def edit_data(product_id):
    form=Add_Form(request.form)
    if request.method=='GET':
        sqlite_connection=sqlite3.connect('shop.db')
        cursor = sqlite_connection.cursor()
        database_string='''SELECT * FROM Product WHERE Product_ID="{id}";'''.format(id=product_id)
        data=cursor.execute(database_string)
        for product in data:
            form.product_ID=product[0]
            form.list_ID.data=product[1]
            form.prodName.data=product[2]
            form.date_sold.data=product[3]
            form.descript.data=product[4]
        cursor.close()
        sqlite_connection.close()
    if request.method=='POST':
        form_list_ID=form.list_ID.data
        form_prodName=form.prodName.data
        form_date_sold=form.date_sold.data
        form_descript=form.descript.data
        #print(form_list_ID,form_prodName,form_date_sold,form_descript)
        sqlite_connection = sqlite3.connect('shop.db')
        cursor = sqlite_connection.cursor()
        sql_command='''UPDATE Product SET product_List_ID='{List}', product_Name='{Name}', date_Sold='{sold}',description='{descript}' WHERE Product_ID="{id}"'''\
            .format(id=product_id,List=form_list_ID,Name=form_prodName,sold=form_date_sold,descript=form_descript)
        cursor.execute(sql_command)
        sqlite_connection.commit()
        sqlite_connection.close()
        flash('Row successfully edited!','success')
        return redirect(url_for('home_page'))
    return render_template('add_data.html',title='Edit data',form=form)


@app.route("/delete_data/<product_id>")
def delete_data(product_id):
    sqlite_connection = sqlite3.connect('shop.db')
    cursor = sqlite_connection.cursor()
    database_string = '''DELETE FROM Product WHERE Product_ID="{id}";'''.format(id=product_id)
    cursor.execute(database_string)
    sqlite_connection.commit()
    sqlite_connection.close()
    flash('Row successfully deleted!', 'success')
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    app.run(debug=True)
