from flask import Flask, render_template, request, abort
from model import session, News, and_


app = Flask(__name__)


@app.route('/templates/about-us.html', methods=['GET'])
def about():
    return render_template('about-us.html')


@app.route('/templates/sports_news.html', methods=['POST', 'GET'])
def sport_news():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_items = session.query(News).filter(and_(News.Date >= start_date, News.Date <= end_date, News.Theme == "Sport")).all()

        return render_template("category_news.html", news=news_items)
    selected_news = session.query(News).filter_by(Theme='Sport').all()

    return render_template('category_news.html', news=selected_news)


@app.route('/templates/business_news.html', methods=['POST', 'GET'])
def business_news():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_items = session.query(News).filter(and_(News.Date >= start_date, News.Date <= end_date, News.Theme == "Business")).all()

        return render_template("category_news.html", news=news_items)
    selected_news = session.query(News).filter_by(Theme='Business').all()

    return render_template('category_news.html', news=selected_news)


@app.route('/templates/culture_news.html', methods=['POST', 'GET'])
def culture_news():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_items = session.query(News).filter(and_(News.Date >= start_date, News.Date <= end_date, News.Theme == "Culture")).all()

        return render_template("category_news.html", news=news_items)
    selected_news = session.query(News).filter_by(Theme='Culture').all()

    return render_template('category_news.html', news=selected_news)


@app.route('/templates/economics_news.html', methods=['POST', 'GET'])
def economics_news():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_items = session.query(News).filter(and_(News.Date >= start_date, News.Date <= end_date, News.Theme == "Economics")).all()

        return render_template("category_news.html", news=news_items)
    selected_news = session.query(News).filter_by(Theme='Economics').all()

    return render_template('category_news.html', news=selected_news)


@app.route('/templates/politics_news.html', methods=['POST', 'GET'])
def politics_news():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_items = session.query(News).filter(and_(News.Date >= start_date, News.Date <= end_date, News.Theme == "Politics")).all()

        return render_template("category_news.html", news=news_items)
    selected_news = session.query(News).filter_by(Theme='Politics').all()

    return render_template('category_news.html', news=selected_news)


@app.route('/templates/science_news.html', methods=['POST', 'GET'])
def science_news():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_items = session.query(News).filter(and_(News.Date >= start_date, News.Date <= end_date, News.Theme == "Science")).all()

        return render_template("category_news.html", news=news_items)
    selected_news = session.query(News).filter_by(Theme='Science').all()

    return render_template('category_news.html', news=selected_news)


@app.route('/templates/<int:news_id>', methods=['GET'])
def news_detail(news_id):
    selected_news = session.query(News).filter_by(NewsID=news_id).first()
    if selected_news is None:
        abort(404)
    return render_template('news_detail.html', news_item=selected_news)


@app.route('/templates/main.html', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        news_item = session.query(News).filter(and_(News.Date >= start_date,  News.Date <= end_date)).all()

        return render_template("main.html", news=news_item)
    news_item = session.query(News).all()
    return render_template("main.html", news=news_item)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
