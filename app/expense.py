from flask_smorest import Blueprint

expenses = [{"date": "2025-08-11", "items": [{"category": "food", "price": 15.99}]}]

blp = Blueprint("expenses", __name__, description="Operations on expenses")

@blp.route("/expense")
def get_expenses():
    return {"expenses": expenses}