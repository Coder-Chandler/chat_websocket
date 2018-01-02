from flask import session, redirect, url_for, render_template, request
from . import main
from app.main.utils import log


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get('name') is not None:
        log('/ request(POST) ', request)
        session['name'] = request.form['name']
        log('session ->', session)
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        log('/ request(GET) ', request)
        return render_template('index.html')


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    log('/chat request', request)
    if name == '':
        return redirect(url_for('.index'))
    return render_template('chat.html')
