from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Substitua pelo seu token
TOKEN = '7504190633:AAEMyZoh3dnDdxZzqB2Q0iwDk2oxo2AVYuM'

# Função que será chamada quando o comando "/start" for enviado
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Olá, eu sou seu bot!')

# Função para o comando "/ajuda"
async def ajuda(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Aqui está a ajuda! Use /start para iniciar o bot.')

def main():
    # Criação do Application com o token
    application = Application.builder().token(TOKEN).build()

    # Adiciona os handlers para os comandos "/start" e "/ajuda"
    start_handler = CommandHandler('start', start)
    ajuda_handler = CommandHandler('ajuda', ajuda)
    application.add_handler(start_handler)
    application.add_handler(ajuda_handler)

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()
