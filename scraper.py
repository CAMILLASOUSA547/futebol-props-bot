from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def iniciar_driver():
    options = Options()
    options.headless = True  # Rodar sem abrir janela
    driver = webdriver.Chrome(options=options)
    return driver

def pegar_cartoes(driver, url):
    driver.get(url)
    time.sleep(5)  # Espera carregar

    cartoes = driver.find_elements(By.XPATH, "//div[contains(text(),'Cartões')]/following::div[contains(@class,'player-name')]")
    jogadores_cartoes = [jogador.text for jogador in cartoes]
    return jogadores_cartoes

def main():
    url = 'https://www.oddschecker.com/br/futebol'  # Ajuste para a página certa
    driver = iniciar_driver()

    cartoes = pegar_cartoes(driver, url)
    print("Jogadores com odds de cartões:")
    for jogador in cartoes:
        print(jogador)

    driver.quit()

if __name__ == "__main__":
    main()
