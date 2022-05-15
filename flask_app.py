from flask import Flask,render_template,request,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from add_data_form import Add_Form
import sqlite3


app=Flask(__name__)
app.secret_key=b'263433102'
bootstrap=Bootstrap(app)

@app.route("/")
def template_test():
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
        return redirect(url_for('template_test'))
    return render_template('add_data.html',title='Add Data', form=form)


@app.route("/edit_data/<int:product_id>")
def edit_data(product_id):
    form=Add_Form(request.form)
    form.product_ID=product_id
    return render_template('add_data.html',title='Edit data',form=form)


if __name__ == '__main__':
    app.run(debug=True)
