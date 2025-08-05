from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Substitua pelo seu token
TOKEN = '7504190633:AAEMyZoh3dnDdxZzqB2Q0iwDk2oxo2AVYuM'

# Função que será chamada quando o comando "/start" for enviado
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Olá, eu sou seu bot!')

def main():
    # Criação do Application com o token
    application = Application.builder().token(TOKEN).build()

    # Adiciona o handler para o comando "/start"
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Inicia o bot e começa a escutar as mensagens
    application.run_polling()

if __name__ == '__main__':
    main()
ajuda_handler = CommandHandler('ajuda', ajuda)
info_handler = CommandHandler('info', info)
application.add_handler(ajuda_handler)
application.add_handler(info_handler)
