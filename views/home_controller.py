from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        """metod dlya zagryzki shablona glavnoi sranici"""
        return render_template('home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        """metod dlya zagryzki shablona sranici pro sait"""
        return render_template('home/about.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        """metod dlya zagryzki shablona sranici contactov"""
        return render_template('home/contact.html')

    @staticmethod
    @app.route('/teachers')
    def teachers():
        """metod dlya zagryzki shablona sranici contactov"""
        return render_template('home/teachers.html')

    @staticmethod
    @app.route('/child')
    def child():
        """metod dlya zagryzki shablona sranici contactov"""
        return render_template('home/child.html')

    @staticmethod
    @app.route('/parent')
    def parent():
        """metod dlya zagryzki shablona sranici contactov"""
        return render_template('home/parent.html')