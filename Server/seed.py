from app import app

from models import db, Insights

if __name__ == '__main__':
    with app.app_context():

        print("deleting tables...")

        Insights.query.delete()

        db.session.commit()


        insight = [
            Insights(
                lights = "yellow",
                category = "Investigate",
                notes = "interest rate",
                cur_response = "N/A Call/Email",
                prev_response = "",
                organization_id = 1,
                credit_limit = 100000,
                approval_date = "11/1/2025",
                current_balance = 10000,
                name = "Practice Name MD",
                current_month = 50000,
                last_month = 75000,
                two_months_ago = 25000,
                three_months_ago = 100000,
                one_year_ago = 10000,
            ),
            Insights(
                lights = "yellow",
                category = "Investigate",
                notes = "interest rate",
                cur_response = "N/A Call/Email",
                prev_response = "",
                organization_id = 1,
                credit_limit = 100000,
                approval_date = "11/1/2025",
                current_balance = 10000,
                name = "Practice Name MD",
                current_month = 50000,
                last_month = 75000,
                two_months_ago = 25000,
                three_months_ago = 100000,
                one_year_ago = 10000,
            ),
        ]

        db.session.add_all(insight)
        db.session.commit()