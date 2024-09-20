import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # URL вашего приложения (для тестирования используем localhost)
    app_url = "http://localhost:8000/index.html"
    
    # Создаем кнопку, которая будет открывать ваше приложение
    keyboard = [[InlineKeyboardButton("Запустить Хакер Симулятор", web_app=WebAppInfo(url=app_url))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text("Нажмите кнопку, чтобы запустить игру:", reply_markup=reply_markup)

def main() -> None:
    # Замените 'YOUR_BOT_TOKEN' на реальный токен вашего бота
    application = Application.builder().token('7206382652:AAF4KLAQLdXu_4yOhyF2cI2hkDikQVSyjv0').build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()