from selenium.webdriver.common.by import By
import pandas as pd

def extrair_dados(driver):
    print(">>> EXTRAÇÃO INICIADA <<<")

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    dados = []

    for produto in produtos:
        nome = produto.find_element(By.CLASS_NAME, "inventory_item_name").text
        preco = produto.find_element(By.CLASS_NAME, "inventory_item_price").text

        dados.append({
            "Produto": nome,
            "Preco": preco
        })

    df = pd.DataFrame(dados)
    df.to_csv("data/dados_extraidos.csv", index=False)

    print(">>> EXTRAÇÃO FINALIZADA <<<")
    return df
