
def generate_balance_sheet_insights(query: str, balance_sheet_docs: list[str], groq_client):
    system_message = (
        "You are an AI assistant that analyzes balance sheet data and provides insights. "
        "Use the context provided below to give meaningful insights.\n\n"
        "CONTEXT:\n"
        "\n---\n".join(balance_sheet_docs)
    )
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]
    
    chat_response = groq_client.chat.completions.create(
        model="llama3-8b-8192",  # Specify the model, 
        messages=messages
    )
    
    return chat_response.choices[0].message.content

def generate_income_statement_insights(query: str, incomes_statement_docs: list[str], groq_client):
    system_message = (
        "You are an AI assistant that analyzes income statement data and provides insights. "
        "Use the context provided below to give meaningful insights.\n\n"
        "CONTEXT:\n"
        "\n---\n".join(incomes_statement_docs)
    )
    
    # Define the conversation messages with the system context and user query
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]
    
    chat_response = groq_client.chat.completions.create(
        model="llama3-8b-8192",  
        messages=messages
    )

    return chat_response.choices[0].message.content