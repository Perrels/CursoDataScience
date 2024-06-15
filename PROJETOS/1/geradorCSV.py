import pandas as pd
import random

# Lista de dados fictícios
streets = ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E"]
cities = ["Cidade X", "Cidade Y", "Cidade Z"]
property_details = ["Detalhe A", "Detalhe B", "Detalhe C"]
price_formats = ["R$", "\n mês", "R$ \n", "por mês", "reais"]

data = []
for _ in range(50):
    street = random.choice(streets)
    city = random.choice(cities)
    property_detail = random.choice(property_details)
    quartos = random.randint(1, 5)
    banheiros = random.randint(1, 3)
    vagas = random.randint(0, 2)
    price_value = random.randint(1000, 5000)
    price_format = random.choice(price_formats)
    if price_format.strip():
        price = f"{price_value} {price_format.strip()}"
    else:
        price = f"{price_value}{price_format}"
    
    data.append([street, city, property_detail, quartos, banheiros, vagas, price])

# Criar DataFrame
df = pd.DataFrame(data, columns=["Street", "City", "propertycard_detailsvalue", "quartos", "banheiros", "vagas", "price"])

# Salvar para CSV
csv_path = "C:/Users/pablo/OneDrive/Documentos/Cursos_Estudos/DATA SCIENCE SANTANDER CODERS/CursoDataScience/testeCsv.csv"
df.to_csv(csv_path, index=False)

csv_path