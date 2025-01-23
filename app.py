"""
Flask app for web services.

"""

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "password"


@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        str: The rendered template for the home page.
    """
    return render_template('home.html')


@app.route('/story')
def story():
    """
    Renders the story page.

    Returns:
        str: The rendered template for the story page.
    """
    return render_template('story.html')


@app.route('/blog')
def blog():
    """
    Renders the blog page.

    Returns:
        str: The rendered template for the blog page.
    """
    return render_template('blog.html')


@app.route('/forum')
def forum():
    """
    Renders the forum page.

    Returns:
        str: The rendered template for the forum page.
    """
    return render_template('forum.html')


@app.route('/contact')
def contact():
    """
    Renders the contact page.

    Returns:
        str: The rendered template for the contact page.
    """
    return render_template('contact.html')

@app.route('/media')
def media():
    """
    Renders the home page.

    Returns:
        str: The rendered template for the home page.
    """
    return render_template('media.html')


if __name__ == '__main__':
    app.run(debug=True)
