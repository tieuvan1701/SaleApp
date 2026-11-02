from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    return render_template("index.html", prods=dao.load_products(q=q, cate_id=cate_id))

@app.route("/product/<int:id>")
def details(id):
    return render_template("product-detail.html")

@app.context_processor
def common_attribute():
    return {
        "cates":dao.load_categories()
    }
if __name__=="__main__":
    app.run(debug=True, port=5001)