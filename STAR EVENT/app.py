from flask import Flask, render_template
app = Flask(__name__,static_folder='static')


@app.route('/')
def login():
    return render_template('login.html')
@app.route('/aboutus')
def naveen():
    return render_template('aboutus.html',video_filename="navven.mp4")


if __name__ =='__main__':
     app.run(debug=True)
