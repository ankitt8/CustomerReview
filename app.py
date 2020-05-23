from flask import Flask, render_template, flash, request, redirect
from forms import ReviewForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec0a1a65504ca45f1fc7fd9f3431a574'
@app.route('/', methods=['GET', 'POST'])
def index():



    form = ReviewForm()
    print(request.method)
    if request.method == 'POST':

        if form.validate_on_submit():
            form_data_list = [form.username.data, form.product_name.data, form.product_review.data]
            print(f'User name {form.username.data}')
            print(f'Product Name {form.product_name.data}')
            print(f'Product Review {form.product_review.data}')
            with open('static/data/reviews.csv', 'a+', newline='') as write_obj:
                csv_writer = csv.writer(write_obj)
                csv_writer.writerow(form_data_list)

            form.username.data = ''
            form.product_name.data = ''
            form.product_review.data = ''
            print(f'submitted successfully')
            print('hi')
            # flash('Review Posted Successfully!', category='info')
            return redirect('/')

    with open('static/data/reviews.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        reviews = []
        for row in data:
            if first_line:
                first_line = False
            else:
                reviews.append(dict(username=row[0], product_name=row[1], product_review=row[2]))


    return render_template('index.html', form=form, reviews=reviews)

if __name__=='__main__':
    app.run(port=8080, debug=True)