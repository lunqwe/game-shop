import pandas as pd
from .models import Product

class DatabasePlaceholder():
    def get_data(file_path):
        display_type_dict = {
            'Настольная игра': "table_game",
            "Конструктор": "constructor"
        }
        df = pd.read_excel(file_path)
        data = []
        for index, row in df.iterrows():
            title = row['Название'].strip()
            price = row['Цена']
            print(price)
            display_price = f"{price:.2f}"
            print(display_price)
            article = str(row['Артикуль']).strip()
            description = row['Описание'].strip()
            display_type = display_type_dict[row['Тип']]

            
            
            data.append({'title': title, "price": display_price, "article": article, "description": description, "display_type": display_type})

        return data    
    
    def save_data(data):
        for product_data in data:
            Product.objects.create(**product_data)
