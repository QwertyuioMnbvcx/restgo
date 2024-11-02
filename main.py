from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/city')
def city_page():
    return render_template('city.html')

@app.route('/logIn_signIn')
def registation_page():
    return render_template('logIn_signIn.html')


@app.route('/user')
def user_page():
    return render_template('user.html')


@app.route('/business_account')
def business_aaccount_page():
    return render_template('business_aaccount.html')


if __name__ == '__main__':
    app.run(debug=True)


