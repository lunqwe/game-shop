import pandas as pd
# Укажите путь к файлу Excel
# file_path = 'data.xlsx'

# # Загрузите данные из файла Excel в объект DataFrame
# df = pd.read_excel(file_path)

# for index, row in df.iterrows():
#     title = row['Название'].strip()
#     price = int(row['Цена'])
#     display_price = f'{price}.00 $'
#     article = str(row['Артикуль']).strip()
#     description = row['Описание'].strip()
    
#     print(title, "\n", display_price, "\n", article, "\n", description, "\n end", )

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
            price = int(row['Цена'])
            display_price = f'{price}.00 ₴'
            article = str(row['Артикуль']).strip()
            description = row['Описание'].strip()
            display_type = display_type_dict[row['Тип']]

            
            
            data.append({'title': title, "price": display_price, "article": article, "description": description, "display_type": display_type})

        return data    
    
    def save_data(data):
        pass
        # Product.objects.create(**data)

# print(DatabasePlaceholder.get_data('data.xlsx'))

    