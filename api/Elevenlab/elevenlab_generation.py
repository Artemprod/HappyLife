import asyncio
import json
import os
from datetime import datetime
from aiohttp import ClientSession
import aiofiles

api_base_url_v1 = os.environ.get("ELEVEN_BASE_URL", "https://api.elevenlabs.io/v1")


class ElevenLabsClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._session = None  # Initialize session lazily

    async def _get_session(self):
        if self._session is None:
            self._session = ClientSession()
        return self._session

    async def text_to_speech_without_save_bites(self, text: str, voice: str) -> bytes:
        session = await self._get_session()
        url = f"{api_base_url_v1}/text-to-speech/{voice}?output_format=mp3_44100_128"
        data = {"text": text, "model_id": 'eleven_multilingual_v2'}
        headers = {"xi-api-key": self.api_key}

        async with session.post(url, json=data, headers=headers) as response:
            if response.status != 200:
                try:
                    error_info = await response.json()
                except json.JSONDecodeError:
                    error_info = await response.text()
                raise Exception(f"Error with ElevenLabs API: {response.status} - {error_info}")

            audio_data = await response.read()
            return audio_data

    async def text_to_speech_save_audio(self, text: str, voice: str, chat_id: int, message_id: int) -> str:
        session = await self._get_session()  # Дожидаемся получения сессии
        url = f"{api_base_url_v1}/text-to-speech/{voice}?output_format=mp3_44100_128"
        data = {"text": text, "model_id": 'eleven_multilingual_v2'}
        headers = {"xi-api-key": self.api_key}

        async with session.post(url, json=data, headers=headers) as response:
            if response.status != 200:
                try:
                    error_info = await response.json()
                except json.JSONDecodeError:
                    error_info = await response.text()
                raise Exception(f"Error with ElevenLabs API: {response.status} - {error_info}")

            audio_data = await response.read()

        filename = self._generate_filename(chat_id, message_id)
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        async with aiofiles.open(filename, 'wb') as file:
            await file.write(audio_data)

        return filename

    def _generate_filename(self, chat_id: int, message_id: int) -> str:
        timestamp = datetime.now().strftime("%Y%H%M%S")
        return os.path.normpath(os.path.join(
            os.path.dirname(__file__), 'temp_docs', 'outcome_voices',
            f'{chat_id}_{message_id}_{timestamp}.mp3'
        ))

    async def close(self):
        if self._session is not None:
            await self._session.close()

if __name__ == '__main__':
    async def main():
        t = """
        Привет! Я рад, что ты обратился ко мне за помощью. Давай сделаем что-то уникальное и позитивное, чтобы помочь тебе изменить свою жизнь к лучшему. Сейчас я приглашаю тебя закрыть глаза и представить себя на месте самого расслабленного и довольного собой человека, которым ты когда-либо был.
    
    Представь, что ты находишься на прекрасном пляже, где у тебя есть возможность просто отдохнуть и расслабиться. Ты слышишь шум моря и чувствуешь, как теплый песок ласкает твои ступни. Понимаешь, что в этот момент у тебя есть все время в мире, чтобы насладиться каждым вдохом свежего морского воздуха и каждым прикосновением легкого бриза к твоей коже.
    
    Во время этого регрессивного гипноза, твое подсознание начинает осознавать, что привычка считать себя лентяем - всего лишь негативное убеждение, которое не имеет никаких доказательств. Вместо этого, оно начинает перепрограммироваться на более конструктивное и положительное убеждение.
        """
        client = ElevenLabsClient(api_key="5f2bc6d5c50fb21a4eb49e22101df60d")
        try:
            filename = await client.text_to_speech_save_audio(text=t, voice="6KRMgjFXxbSUozoIyons",
                                                   chat_id=123, message_id=1)
            print(f"Generated file: {filename}")
        finally:
            await client.close()



    asyncio.run(main())
