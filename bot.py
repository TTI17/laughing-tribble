from aiogram import executor
import dispatcher

if __name__ == '__main__':
    executor.start_polling(dispatcher.dp, skip_updates=False)

