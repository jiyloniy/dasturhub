from aiogram import Router,types
from aiogram.filters import Command
import logging
from database import db_operations
logger = logging.getLogger(__name__)
start_router = Router(name='start')

@start_router.message(Command('start'))
async def start(message : types.Message):
    username = message.from_user.username or ''
    user_id= message.from_user.id
    admin = False
    user =  db_operations.create_user(checkadmin=admin,user_id=user_id,username=username) 
    print(user)
    if user is None:
        await message.answer('xush kelibsiz')
    else:
        await message.answer(f'{message.from_user.id}')