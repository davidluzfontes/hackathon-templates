from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """Render the main page."""
    return render_template("text_app.html")

@app.route('/submit', methods=['POST'])
def submit():
    """Handle text submissions and display them."""
    user_input = request.form.get('user_input')  # Get the text from the input field named 'user_input'
    return render_template("text_app.html", user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
