from flask_wtf import Form
from wtforms import StringField, BooleanField, IntegerField


class Add_Form(Form):
    product_ID=IntegerField('Product ID')
    list_ID=IntegerField('Product List ID')
    prodName=StringField('Product Name')
    date_sold=IntegerField('Date Sold')
    descript= StringField('Descript')
