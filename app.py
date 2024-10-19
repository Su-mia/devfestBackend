import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import groq  
from generation import generate_balance_sheet_insights , generate_income_statement_insights


app = Flask(__name__)
CORS(app)

groq_client = groq.Client(api_key="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")


@app.route('/generate_insights', methods=['POST'])
def generate_insights():
    balance_sheet_data = request.json.get('balance_sheet_data')
    query = request.json.get('query', "Please analyze this balance sheet and provide insights.")  

    balance_sheet_docs = [f"Assets: {balance_sheet_data['assets']}", f"Liabilities: {balance_sheet_data['liabilities']}", f"Equity: {balance_sheet_data['equity']}" , f"result: {balance_sheet_data['result']}"]

    insights = generate_balance_sheet_insights(query, balance_sheet_docs, groq_client)

    result = {
        "balance_sheet": balance_sheet_data,
        "insights": insights
    }

    return jsonify(result)

@app.route('/generate_insights_income', methods=['POST'])
def generate_insights_income():
    income_statement_data = request.json.get('income_statement_data')
    query = request.json.get('query', "Please analyze this income statement and provide insights.")

    # Prepare documents for insights generation
    income_statement_docs = [
        f"Revenue: {income_statement_data['revenue']}",
        f"Cost of Goods Sold: {income_statement_data['cost_of_goods_sold']}",
        f"Gross Profit: {income_statement_data['gross_profit']}",
        f"Operating Expenses: {income_statement_data['operating_expenses']}",
        f"Operating Income: {income_statement_data['operating_income']}",
        f"Other Income: {income_statement_data['other_income']}",
        f"Taxes: {income_statement_data['taxes']}",
        f"Net Income: {income_statement_data['net_income']}"
    ]

    insights = generate_income_statement_insights(query, income_statement_docs, groq_client)

    result = {
        "income_statement": income_statement_data,
        "insights": insights
    }

    return jsonify(result)

app.run(host="0.0.0.0", port=80)

