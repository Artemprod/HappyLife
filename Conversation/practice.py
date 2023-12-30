import logging

from BD.MongoDB.mongo_db import PromptRepository
from BD.MongoDB.mongo_enteties import Problem, UserPrompt
from api.ChatGPT import GPTMessage, GPTOptions
from api.ChatGPT.gpt_message import GPTRole
from api.ChatGPT.openai_chat_complete import GPTClient
from environs import Env
import os
from datetime import datetime
from elevenlabs import generate, save, set_api_key
from environs import Env

from api.Elevenlab.elevenlab_generation import ElevenLabsClient
from container import prompt_repo


class Practice:
    MODEL_3 = "gpt-3.5-turbo-1106"
    MODEL_4 = "gpt-4"
    MODEL_4_8K = "gpt-4-0613"
    MODEL_3_16 = "gpt-3.5-turbo-16k"
    MODEL_GPT_4_LIMIT = 8192
    MODEL_GPT_3_LIMIT = 16385

    def __init__(self, belief: str, prompt_repo: PromptRepository, max_context_messages: int = 3):
        self.__belief = belief
        self.__prompt_repo = prompt_repo
        self.__max_context_messages = max_context_messages

    async def do_practice(self):
        """
        Делает практику
        1. Загружает юзер промпт
        2. загружает системный промпт
        3. загружает загон
        4. объеденят систеный + юзер + загон
        ЦИКЛ:
            5. По циклу сгенерированых сообщений отправляет запрос к гпт
            6. в каждом цикле генерирует их полученого сообщение аудио голос Димы
            7. отправляет голос во вне
            8. ответ от гпт дополнятся в списко сообщений
        КОНЕЦ ЦИКЛА
        """
        gpt_client = await self.__load_gpt()
        elevanlab_client = await self.__load_elevenlab()
        system_prompt = await self.__create_one_system_message()
        user_messages = await self.__create_list_of_messages()
        context = []

        for message in user_messages:
            context += [message]

            response = await gpt_client.complete(messages=context,
                                                 system_message=system_prompt,
                                                 temperature=1)

            assistant_message = await self.__create_assistant_message(cht_gpt_response=response)
            context.append(assistant_message)
            voice_generation = await elevanlab_client.text_to_speech_without_save_bites(text=response, voice='6KRMgjFXxbSUozoIyons',)
            yield response, voice_generation

    async def __create_one_system_message(self) -> GPTMessage:
        system_prompt_mongo_object: UserPrompt = await self.__load_system_prompt()
        prompt = await self.__insert_problem_if_exists(prompt=system_prompt_mongo_object.prompt,
                                                       problem=self.__belief)
        message = GPTMessage(role=GPTRole.SYSTEM, content=prompt)
        return message

    async def __create_one_user_message(self, user_prompt: UserPrompt) -> GPTMessage:
        prompt = await self.__insert_problem_if_exists(prompt=user_prompt.prompt, problem=self.__belief)
        message = GPTMessage(role=GPTRole.USER, content=prompt)
        return message

    @staticmethod
    async def __create_assistant_message(cht_gpt_response: str) -> GPTMessage:
        message = GPTMessage(role=GPTRole.ASSISTANT, content=cht_gpt_response)
        return message

    # При условии что системное сообщение одно
    # TODO сделть то же самое если системных сообщений много если лист. Даст гибкость
    async def __create_list_of_messages(self) -> list[GPTMessage]:

        user_prompts: list[UserPrompt] = await self.__load_user_prompts()
        messages = []
        for prompt in user_prompts:
            message = await self.__create_one_user_message(user_prompt=prompt)
            messages.append(message)
            print()
        return messages

    @staticmethod
    async def __insert_problem_if_exists(prompt: str, problem: str) -> str:
        """
        Функция проверяет наличие плейсхолдера {problrm} в тексте промпта.
        Если плейсхолдер есть, она вставляет вместо него значение из переменной problem.
        Если плейсхолдера нет, возвращает исходный текст промпта.

        :param prompt: Текст промпта, возможно, содержащий плейсхолдер {problrm}.
        :param problem: Значение для вставки вместо плейсхолдера.
        :return: Промпт с заменённым значением или исходный промпт.
        """
        print()
        if '{problem}' in prompt:
            return prompt.format(problem=problem)
        else:
            return prompt

    async def __load_user_prompts(self) -> list[UserPrompt]:
        try:
            user_prompts = await self.__prompt_repo.get_all_user_prompts()
            return user_prompts
        except Exception as e:
            print(e, "Ошибка загрузки юзер промптов")

    async def __load_system_prompt(self) -> UserPrompt:
        try:

            system_prompts = await self.__prompt_repo.get_system_prompt()
            return system_prompts
        except Exception as e:
            print(e, "Ошибка загрузки системного промпта")

    async def __load_gpt_options(self) -> GPTOptions:
        api_key = await self.__load_gpt_api_key()
        option = GPTOptions(api_key=api_key,
                            max_message_count=self.__max_context_messages)
        return option

    async def __load_gpt(self) -> GPTClient:
        options = await self.__load_gpt_options()
        client = GPTClient(options=options)
        return client

    async def __load_elevenlab(self) -> ElevenLabsClient:
        return ElevenLabsClient(api_key=await self.__load_elevan_lab_api_key())

    @staticmethod
    async def __load_gpt_api_key():
        env = Env()
        env.read_env(".env")
        try:
            return env("OPENAI_API_KEY")
        except Exception as e:
            print("Ошибка загрузки ключа гпт")

    @staticmethod
    async def __load_elevan_lab_api_key():
        env = Env()
        env.read_env(".env")
        print()
        try:
            return env("ELEVEN_API_KEY")
        except Exception as e:
            print("Ошибка загрузки ключа элеванлаб")


if __name__ == '__main__':
    belief = "Я мвло получаю денег "

    a = Practice(belief=belief, prompt_repo=prompt_repo)
    a.do_practice()
