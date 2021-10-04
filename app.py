# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Play-Store-API/blob/main/LICENSE

from flask import Flask, redirect, render_template, request, jsonify, json 
import play_scraper


app = Flask(__name__, template_folder="public")
docs = "<a href='https://github.com/FayasNoushad/Play-Store-API'>documentation</a>."


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/details/", methods=['GET'])
def app_details():
    query = request.args.get('query')
    if query is not None:
        details = play_scraper.details(query)
        if details is None:
            return jsonify(
                {"error": f"No details found, Read the {docs}."}
            )
        if details is not None:
            return jsonify(details)
    else:
        return jsonify(
            {"error": f"Query is None, Read the {docs}."}
        )


@app.route("/collection/", methods=['GET'])
def search_app_collection():
    collection_name = request.args.get('collection')
    if collection_name and collection_name not in play_scraper.lists.COLLECTIONS:
        return jsonify(
            {"error": f"No collection name found, Read the full {docs}."}
        )
    category_name = request.args.get('category')
    if not category_name or category_name not in play_scraper.lists.CATEGORIES:
        category_name = None
    results = play_scraper.collection(
        collection = collection_name,
        category = category_name
    )
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": f"Something wrong, Read the {docs}."}
        )


@app.route("/developer/", methods=['GET'])
def search_app_developer():
    query = request.args.get('query')
    results = play_scraper.developer(query)
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": f"Something wrong, Read the {docs}."}
        )


@app.route("/suggestions/", methods=['GET'])
def search_app_suggestions():
    query = request.args.get('query')
    results = play_scraper.suggestions(query)
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": f"Something wrong, Read the {docs}."}
        )


@app.route("/search/", methods=['GET'])
def search_apps():
    query = request.args.get('query')
    results = play_scraper.search(query)
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": f"Something wrong, Read the {docs}."}
        )


@app.route("/similar/", methods=['GET'])
def similar_apps():
    query = request.args.get('query')
    results = play_scraper.similar(query)
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": f"Something wrong, Read the {docs}."}
        )


@app.route("/categories/")
def categories_list():
    results = play_scraper.categories()
    if results is not None:
        return jsonify(results)
    else:
        return jsonify(
            {"error": f"Something wrong, Read the {docs}."}
        )


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, use_reloader=True, threaded=True)
