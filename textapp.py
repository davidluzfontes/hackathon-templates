from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    """Render the main page."""
    return render_template("text_app.html")


matches = []


@app.route('/match/create')
def create_match():
    matches.append({
        'id': len(matches) + 1,
        'red_score': 0,
        'blue_score': 0,
        'round': 1,
        'red_move': None,
        'blue_move': None,
    })

    return render_template("match.html", match=matches[-1], side='red')

@app.route('/match/join')
def join_match():
    match_id = request.args.get('id')
    if not match_id:
        abort(404)

    match = matches[int(match_id) - 1]

    return render_template("match.html", match=match, side='blue')


@app.route('/match/<match_id>')
def get_match_data(match_id):
    return render_template("match.html", match=matches[int(match_id) - 1], side=request.args.get('side'))


@app.route('/match/submit', methods=['POST'])
def submit_move():
    match_id = request.form.get('id')
    side = request.form.get('side')
    move = request.form.get('move')

    match = matches[int(match_id) - 1]

    if side == 'red':
        if match['red_move']:
            return render_template("match.html", match=match, side=side)
        match['red_move'] = move
    elif side == 'blue':
        if match['blue_move']:
            return render_template("match.html", match=match, side=side)
        match['blue_move'] = move
    else:
        return render_template("match.html", match=match, side=side)

    if match['red_move'] and match['blue_move']:
        if match['red_move'] == match['blue_move']:
            pass
        elif match['red_move'] == 'rock':
            if match['blue_move'] == 'paper':
                match['blue_score'] += 1
            else:
                match['red_score'] += 1
        elif match['red_move'] == 'paper':
            if match['blue_move'] == 'scissors':
                match['blue_score'] += 1
            else:
                match['red_score'] += 1
        elif match['red_move'] == 'scissors':
            if match['blue_move'] == 'rock':
                match['blue_score'] += 1
            else:
                match['red_score'] += 1

        match['red_move'] = None
        match['blue_move'] = None
        match['round'] += 1

    return render_template("match.html", match=match, side=side)


@app.route('/submit', methods=['POST'])
def submit():
    """Handle text submissions and display them."""
    user_input = request.form.get('user_input')  # Get the text from the input field named 'user_input'
    return render_template("text_app.html", user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
