from flask import request, render_template


def api_routes(endpoints):
    @endpoints.route('/home', methods=['GET'])
    def home():
        return render_template("index.html")

    return endpoints
