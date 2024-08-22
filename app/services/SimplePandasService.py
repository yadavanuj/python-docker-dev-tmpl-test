import pandas as pd

data = {
        'Name': ['John', 'Emily', 'Charles', 'Diana'],
        'Age': [28, 22, 35, 46]
    }
df = pd.DataFrame(data)

def serve():
    return df.to_dict(orient='records')