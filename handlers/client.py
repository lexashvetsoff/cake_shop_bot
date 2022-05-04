from aiogram import types, Dispatcher


async def command_start(message : types.Message):
    await message.answer('Собери сой торт сам!')


def register_handlers_client(dispatcher : Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])