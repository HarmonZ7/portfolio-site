from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/Projects')
def projects():
    data_projects = [
        {
            "title": "Movie Revenue & Budget Analysis (Excel)",
            "description": "Conducted detailed financial analysis on movie datasets using Excel to uncover relationships between budgets and revenue performance. Extracted actionable insights through pivot tables, charts, and advanced formulas to support data-driven storytelling.",
            "link": "https://github.com/HarmonZ7/data-portfolio/tree/main/movie-analysis"
        },
        {
            "title": "Food Consumption & COVID-19 Impact (Tableau Storyboard)",
            "description": "Created an interactive Tableau storyboard to visualize the impact of COVID-19 on food consumption patterns across multiple industries. Utilized complex datasets to highlight trends, anomalies, and industry-specific effects during the pandemic.",
            "link": "https://github.com/HarmonZ7/data-portfolio/tree/main/food-covid-storyboard"
        },
        {
            "title": "Museum Paintings & Artists Analysis (SQL + Tableau)",
            "description": "Developed complex SQL queries to transform and aggregate museum data spanning paintings and artists, creating three normalized tables. Visualized key insights using Tableau dashboards, supporting cultural and historical data exploration.",
            "link": "https://github.com/HarmonZ7/data-portfolio/tree/main/museum-sql-analysis"
        },
        {
            "title": "Car Fuel Efficiency Insights (Python & Jupyter)",
            "description": "Analyzed vehicle data using Python libraries (Pandas, Seaborn, Matplotlib) to identify factors influencing fuel efficiency. Built visualizations and performed exploratory data analysis to uncover trends in car performance",
            "link": "https://github.com/HarmonZ7/data-portfolio/tree/main/car-data-eda"
        },
        # {
        #     "title": "Spotify Data ETL Pipeline",
        #     "description": "Extracted streaming history from Spotify API and transformed it into a PostgreSQL data warehouse.",
        #     "link": "#"
        # },
        # {
        #     "title": "Real-Time Weather API Pipeline",
        #     "description": "Ingested weather data into BigQuery using Airflow and visualized trends with Looker Studio.",
        #     "link": "#"
        # }
    ]
    return render_template('projects.html', projects=data_projects)

@main.route('/About')
def about():
    return render_template('about.html')