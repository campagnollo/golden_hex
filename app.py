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

@app.route('/videos')
def videos():
    """
    Renders the home page.

    Returns:
        str: The rendered template for the home page.
    """
    return render_template('videos.html')

@app.route('/products')
def products():
    """
    Renders the product page.

    Returns:
        str: The rendered template for the product page.
    """
    return render_template('products.html')

@app.route('/exciting-news-we-moved-expanded')
def moved():
    """
    Renders the exciting news page.

    Returns:
        str: The rendered template for the exciting news page.
    """
    return render_template('exciting-news-we-moved-expanded.html')

@app.route('/new_year_favorite_menu')
def new_year_favorite_menu():
    """
    Renders the new year favorite menu page.

    Returns:
        str: The rendered template for the new year favorite menu page.
    """
    return render_template('new_year_favorite_menu.html')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug='True', host='0.0.0.0', port=8080)
