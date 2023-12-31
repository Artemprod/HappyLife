from datetime import datetime
from pathlib import Path
from typing import Any
import os

from aiogram.fsm.context import FSMContext

from BD.DBinterface import MongoDataBaseRepositoryInterface
from BD.MongoDB.datat_enteties import DialogMessage, Dialog, Belief
from BD.MongoDB.mongo_enteties import Client
from aiogram.types import Message
from aiogram import Bot
from pydub import AudioSegment

from container import root_dir
from lexicon.LEXICON_RU import LEXICON_RU


async def save_user_if_not_exist(message: Message, data_base: MongoDataBaseRepositoryInterface) -> None:
    try:
        if not data_base.client_repository.check_client_in_database(message.chat.id):
            data_base.client_repository.save_client_to_database(Client(
                telegram_id=message.chat.id,
                name=message.from_user.first_name,
                date_of_first_using=datetime.now(),
                date_of_last_visiting=datetime.now(),
                beliefs=[]

            ))
            if data_base.client_repository.check_client_in_database(message.chat.id):
                print(f"Пользовтель c id: {message.chat.id,} \nименем: {message.from_user.first_name} добавлен в базу")
    except Exception as e:
        print(e.args,
              'что то не так с сохранением нового пользователя в базу данных')


async def save_answer(message: Message,
                      data_to_save: Any,
                      data_base: MongoDataBaseRepositoryInterface):
    answer = {}
    answer['define_problem'] = {
        'answer_date': datetime.now(),
        'client_answers': data_to_save}
    try:
        data_base.client_repository.save_all_client_answers_by_id(message.chat.id, answer)
        print(f"Ответ: {answer} \n от пользователя"
              f" {message.from_user.first_name} \n{message.chat.id} "
              f"\nСохранен в базу даных ")
    except Exception as e:
        print("\n что то пошло не так при сохранении ответа")


async def load_voice_messages(message: Message, bot: Bot):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_on_disk = os.path.normpath(os.path.join(root_dir, 'user_voices', f"{file_id}.ogg"))
    folder_path = os.path.dirname(file_on_disk)
    if not os.path.exists(folder_path):
        # Если папка не существует, создаем ее
        os.makedirs(folder_path)
    await bot.download_file(file_path, destination=file_on_disk)
    return file_on_disk


async def add_dialog_data(state: FSMContext, message_time, bot_question: str = None, user_answer: str = None, ) -> None:
    """
    Функция добовляет сообщения в state словарь
    """
    data = await state.get_data()
    step = await state.get_state()
    dialog = data.get('dialog')
    dialog.messages.append(DialogMessage(
        number=len(dialog.messages) + 1,
        time=message_time.strftime("%H:%M:%S"),
        bot_question=bot_question,
        user_answer=user_answer,
        step=str(step)
    ))
    try:
        await state.update_data(dialog=dialog)
        print(f"Сообщение добавлено в список на шаге {step}\n")
    except Exception as e:
        print(f"что то пошло не так с обновлением данных для state на на шаге {step}\n", e.args, e.message)


async def get_data_to_save(state: FSMContext):
    data = await state.get_data()
    dialog: Dialog = data.get('dialog')
    belief_id = data.get('belief_id')
    # belief: Belief = data.get('belief')
    dialog.executed_time.end_time = datetime.now().time()
    print()
    # belief.dialogs.append(dialog)
    # return belief


async def get_audio_duration(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        duration_in_seconds = len(audio) / 1000  # Преобразование миллисекунд в секунды
        return duration_in_seconds
    except Exception as e:
        print(f"Ошибка при измерении длительности аудио: {str(e)}")
        return None
