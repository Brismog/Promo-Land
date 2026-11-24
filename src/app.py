
from flask import Flask, render_template, request
from src.data_loader import load_offers

# PromoLand App
app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/', methods=['GET', 'POST'])
def home():
    offers = load_offers()
    search_results = offers

    if request.method == 'POST':
        brand_name = request.form['brand_name']
        search_results = []

    if brand_name:
        for offer in offers:
            if brand_name.lower() in offer["brand_name"].lower():
                search_results.append(offer)

    # Sort offers from highest discount to lowest
    def get_offer_value(offer):
        return float(offer["offer_value"].replace("%", ""))
    
    search_results = sorted(
        search_results,
        key=get_offer_value,
        reverse=True)

    return render_template('index.html', offers=search_results)


if __name__ == '__main__':
    app.run(debug=True)
