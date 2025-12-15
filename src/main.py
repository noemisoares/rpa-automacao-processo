from src.login import realizar_login
from src.extracao import extrair_dados
from src.tratamento import tratar_dados


def main():
    print(">>> MAIN FOI EXECUTADO <<<")

    driver = realizar_login()
    print("Login realizado.")

    extrair_dados(driver)
    print("Dados extraídos.")

    tratar_dados()
    print("Dados tratados.")

    driver.quit()
    print("Automação finalizada com sucesso.")


if __name__ == "__main__":
    main()
