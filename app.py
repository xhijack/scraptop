import json

from flask import Flask, jsonify
from flask import render_template
from flask import request
from flask import send_from_directory

from scraptop.database import db_session, init_db
from scraptop.models import ProductTokopedia, Scraper

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello():
    init_db()
    scraper = Scraper.query.first()
    if scraper:
        shop_id = scraper.shop_id
    else:
        shop_id = ""

    return render_template("index.html", shop_id=shop_id)


@app.route("/scrape", methods=['POST'])
def register():
    brand_id = request.form.get('brand_id', '')
    by = request.form.get('by', '')

    session = db_session()

    scraper = Scraper.query.first()
    if not scraper:
        scraper = Scraper(shop_id=brand_id)
    else:
        scraper.shop_id = brand_id
    session.add(scraper)
    session.commit()

    return render_template("index.html", shop_id=scraper.shop_id)


@app.route("/list", methods=['GET'])
def list():
    products = ProductTokopedia.query.all()
    prods = []

    for product in products:
        images = json.loads(product.images)
        imgs = []
        i = 0
        for image in images:
            i += 1
            imgs.append("<a href='../static/result/images/{0}' target='_blank'>[{1}]</a>".format(image['path'], i))

        prods.append({
            'title': product.title,
            'price': product.price,
            'weight': product.weight,
            'categories': product.categories,
            'seller': product.seller,
            'link_url': "<a href='{url}'>Klik Me<a/>".format(url=product.link_url),
            'location': product.location,
            'images': imgs,
        })

    return jsonify(prods)


@app.route("/items", methods=['GET'])
def items():
    return render_template('list.html')


# @app.route("/download", methods=['GET'])
# def download():
#     return send_from_directory(directory='static/result', filename='result.csv')

if __name__ == '__main__':
    app.run(debug=True)