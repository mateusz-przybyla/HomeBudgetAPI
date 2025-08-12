from app.extensions import db

class ExpenseCategoryDefaultModel(db.Model):
    __tablename__ = "expenses_category_default"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ExpenseCategoryAssignedToUserModel(db.Model):
    __tablename__ = "expenses_category_assigned_to_users"

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    limit = db.Column(db.Float(), nullable=True)