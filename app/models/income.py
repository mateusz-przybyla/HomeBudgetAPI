from app.extensions import db

class IncomeModel(db.Model):
    __tablename__ = "incomes"

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    income_category_assigned_to_user_id = db.Column(
        db.Integer, db.ForeignKey("incomes_category_assigned_to_users.id"), nullable=False
    )
    amount = db.Column(db.Float(precision=2), nullable=False)
    date = db.Column(db.Date, nullable=False)
    comment = db.Column(db.String(100), nullable=True)

    # user = db.relationship("UserModel", back_populates="incomes")
    income_categories = db.relationship("IncomeCategoryAssignedToUsersModel", back_populates="incomes")