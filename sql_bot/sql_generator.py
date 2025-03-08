def generate_sql(entities):
    table = entities.get("TABLE", "users")  # Default table
    columns = entities.get("COLUMNS", "*")
    condition = entities.get("CONDITION", "")

    query = f"SELECT {columns} FROM {table}"
    if condition:
        query += f" WHERE {condition}"
    
    return query
