import asyncio
import datetime
from io import BytesIO

from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery, FSInputFile, BufferedInputFile
)

from BD.MongoDB.mongo_db import MongoProblemsRepositoryORM
from Conversation.practice import Practice
from container import prompt_repo
from keyboards.callback_fabric import StartBeliefsFactory

from aiogram.enums import ContentType
from aiogram import Bot, F, Router

# from services.speech_processer import speech_to_voice_with_path
from config_data.config import load_config

# загрузка сценария шагов по сценарию "Определить убедждение \ загон"
from states.main_process import FSMQMainProcess
from models import SystemMessage, UserMessage, AssistantMessage

router = Router()


@router.callback_query(StartBeliefsFactory.filter())
async def start_practise(callback: CallbackQuery,
                         bot: Bot,
                         callback_data: StartBeliefsFactory,
                         data_base,
                         problem_repo: MongoProblemsRepositoryORM,
                         state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id,
                           text='Тут будет какая-нибудь аудиозаглушка пока генерируется текст и аудио, например, ссылка на видео или предварительный сеанс: '
                                '<a href="https://www.youtube.com/watch?v=-e3DOVU7jik">Смотреть видео</a>',
                           parse_mode='HTML')

    print()
    problem = problem_repo.get_problem_by_problem_id(belief_id=callback_data.belief_id).belief
    practice = Practice(belief=problem, prompt_repo=prompt_repo)
    # async for response in practice.do_practice():
    #     await bot.send_message(chat_id=callback.message.chat.id,
    #                            text=response)
    #     await asyncio.sleep(2)
    async for response, audio_data in practice.do_practice():
        if audio_data:
            voice = BufferedInputFile(file=audio_data, filename="voice.mp3")
            await bot.send_voice(chat_id=callback.message.chat.id, voice=voice)
        await bot.send_message(chat_id=callback.message.chat.id,
                                   text=response)
        await asyncio.sleep(2)
    #
    # await GPT.complete(system_message=SystemMessage(content='Ты в роли психолога, а я твой клиент. проведи сеанс и говори дружелюбно'),
    #                    messages=[
    #                             AssistantMessage(content='Привет!'),
    #                             UserMessage(id=0, content='Привет, меня зовут Женя') ],
    #                    temperature=0.25)


# получаем пол пользователя из базы данных
# получаем загон пользователя


@router.callback_query(FSMQMainProcess.first)
async def relax_command(callback: CallbackQuery,
                        bot: Bot,
                        data_base,
                        state: FSMContext):
    ...
