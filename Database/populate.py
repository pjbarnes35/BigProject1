def insert_data(cr):
    # Define your questions and answers for each category
    strategic_management_data = [
        ("What is SWOT analysis?", "SWOT analysis is a strategic planning technique used to identify Strengths, Weaknesses, Opportunities, and Threats."),
        ("Define Porter's Five Forces.", "Porter's Five Forces is a framework for analyzing the competitive forces within an industry."),
        # Add more questions and answers for the Strategic Management category
    ]
    digital_marketing_data = [
        ("What is SEO?", "SEO stands for Search Engine Optimization, which involves optimizing websites to rank higher in search engine results."),
        ("Explain the concept of PPC advertising.", "PPC (Pay-Per-Click) advertising is a model of internet marketing where advertisers pay a fee each time their ad is clicked."),
        # Add more questions and answers for the Digital Marketing category
    ]
    personal_sales_data = [
        ("What is the difference between features and benefits in sales?", "Features are characteristics of a product or service, while benefits are the advantages or value that customers gain from those features."),
        ("What is the AIDA model?", "The AIDA model is a framework used in sales and marketing that describes the stages a customer goes through in the buying process: Attention, Interest, Desire, Action."),
        # Add more questions and answers for the Personal Sales category
    ]
    information_systems_data = [
        ("What is a database?", "A database is a structured collection of data organized for easy access, retrieval, and management."),
        ("Explain the client-server model.", "The client-server model is a distributed application structure where tasks or workloads are divided between servers and clients."),
        # Add more questions and answers for the Information Systems category
    ]

    # Insert data into each category's table
    for category_data in [
        ("Strategic_Management", strategic_management_data),
        ("Digital_Marketing", digital_marketing_data),
        ("Personal_Sales", personal_sales_data),
        ("Information_Systems", information_systems_data)
    ]:
        category, data = category_data
        for question, answer in data:
            cursor.execute(f"INSERT INTO {category} (question, answer) VALUES (?, ?)", (question, answer))
