from app.extensions import db

class ExpenseModel(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    expense_category_assigned_to_user_id = db.Column(
        db.Integer, db.ForeignKey("expenses_category_assigned_to_users.id"), nullable=False
    )
    payment_method_assigned_to_user_id = db.Column(
        db.Integer, db.ForeignKey("payment_methods_assigned_to_users.id"), nullable=False
    )
    amount = db.Column(db.Float(precision=2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    comment = db.Column(db.String(100), nullable=False)