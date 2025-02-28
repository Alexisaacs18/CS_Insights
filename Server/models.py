from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Insights(db.Model):
    __tablename__ = "insights"  # Changed to lowercase for convention

    id = db.Column(db.Integer, primary_key=True)
    lights = db.Column(db.String(255))
    category = db.Column(db.String(255))  # Fixed typo
    notes = db.Column(db.String(1000))
    cur_response = db.Column(db.String(1000))
    prev_response = db.Column(db.String(1000))
    organization_id = db.Column(db.Integer, nullable=False)
    credit_limit = db.Column(db.Numeric(10, 2), default=0)
    approval_date = db.Column(db.String(100))
    current_balance = db.Column(db.Numeric(10, 2), default=0)
    name = db.Column(db.String(255))
    current_month = db.Column(db.Integer, default=0)
    last_month = db.Column(db.Integer, default=0)
    two_months_ago = db.Column(db.Integer, default=0)
    three_months_ago = db.Column(db.Integer, default=0)
    one_year_ago = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "lights": self.lights,
            "category": self.category,
            "notes": self.notes,
            "cur_response": self.cur_response,
            "prev_response": self.prev_response,
            "organization_id": self.organization_id,
            "credit_limit": self.credit_limit,
            "approval_date": self.approval_date,
            "current_balance": self.current_balance,
            "name": self.name,
            "current_month": self.current_month,
            "last_month": self.last_month,
            "two_months_ago": self.two_months_ago,
            "three_months_ago": self.three_months_ago,
            "one_year_ago": self.one_year_ago
        }