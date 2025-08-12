from app.extensions import db

class PaymentMethodDefaultModel(db.Model):
    __tablename__ = "payment_methods_default"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class PaymentMethodAssignedToUserModel(db.Model):
    __tablename__ = "payment_methods_assigned_to_users"

    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # user = db.relationship("UserModel", back_populates="payment_methods")
    expenses = db.relationship('ExpenseModel', back_populates="payment_methods", lazy='dynamic')