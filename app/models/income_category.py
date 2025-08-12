from app.extensions import db

class IncomeCategoryDefaultModel(db.Model):
    __tablename__ = "incomes_category_default"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class IncomeCategoryAssignedToUserModel(db.Model):
    __tablename__ = "incomes_category_assigned_to_users"

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # user = db.relationship("UserModel", back_populates="incomes_category")
    incomes = db.relationship("IncomeModel", back_populates="incomes_category", lazy="dynamic")