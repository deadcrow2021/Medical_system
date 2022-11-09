from django.core.management.base import BaseCommand
from django.conf import settings
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types.reply_keyboard import *
import time
from home.models import *
from phonenumber_field.phonenumber import PhoneNumber
from asgiref.sync import sync_to_async


bot = Bot(token=settings.API_TOKEN)
dp = Dispatcher(bot)


async def get_greeting_mes() -> str:
    hours = time.localtime().tm_hour
    if 0 <= hours <= 6:
        return "Доброй ночи!"
    elif 6 <= hours <= 12:
        return "Доброго утра!"
    elif 12 <= hours <= 18:
        return "Добрый день!"
    else:
        return "Добрый вечер!"


# @dp.message_handler(Text(equals="Пойти нахер"))
@dp.message_handler(content_types=["contact"])
async def phone_number(message: types.Message):
    try:
        number = "+" + message.contact.phone_number if \
                    message.contact.phone_number[0] == "7" else \
                    message.contact.phone_number
        phone = PhoneNumber.from_string(number)
        patient: Patient = await Patient.objects.aget(telephone=phone)
        tguser = await sync_to_async(TelegramUsers)(patient=patient, tg_user_id=message.from_user.id)
        await sync_to_async(tguser.save)()
        # await sync_to_async(TelegramUsers(patient=patient, tg_user_id=message.from_user.id).save, thread_sensitive=False)()
        await message.answer(f"Спасибо, {patient.get_full_name()}, вы были найдены в базе данных", reply_markup=types.ReplyKeyboardRemove())
    except Exception as ex:
        print(f'{ex=}')
        await message.answer(f"Вы не были найдены в базе данных\nПопробуйте зарегистрироваться в больнице")


@dp.message_handler(commands=['start'])
async def start_mes(message: types.Message):
    # keyborad = types.InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [
    #             types.InlineKeyboardButton(text="привет", callback_data="a")
    #         ]
    #     ]
    # )
    await message.answer(f"Вас приветствует бот Регионального Акушерского мониторинга")
    try:
        user = await TelegramUsers.objects.select_related('patient').aget(tg_user_id=message.from_user.id)
        await message.answer(f"{await get_greeting_mes()} {await sync_to_async(user.patient.get_full_name)()}", reply_markup=types.ReplyKeyboardRemove())
    except Exception as ex:
        kb = [
            [types.KeyboardButton(text="Отправить номер телефона", request_contact=True)],
        ]
        keyborad = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
        await message.answer(f"Для начала, пожалуйста, передайте свой номер телефона для поиска вас в базе данных пациентов\n"
                            f"Если вы ещё не зарегистрированны, обратитесь в ближайшую больницу",
                            reply_markup=keyborad)


@dp.message_handler(commands=['commands'])
async def show_commands(message: types.Message):
    await message.answer("/start\n/help\n/commands\n/show_reception_notes")


@dp.message_handler(commands=['help'])
async def show_commands(message: types.Message):
    await message.answer("Первая помощь")


@dp.message_handler(commands=['show_reception_notes'])
async def show_commands(message: types.Message):
    patient = (await TelegramUsers.objects.select_related('patient').aget(tg_user_id=message.from_user.id)).patient
    answer = ""
    cnt = 1
    async for i in ReceptionNotes.objects.prefetch_related('patient').prefetch_related('doctor').filter(patient=patient):
        answer += f"{cnt}. {i.doctor} {await sync_to_async(i.date_meeting.strftime)('%d.%m.%y %H:%M')}\n"
        cnt += 1
    await message.answer(f"{answer}")


# @dp.message_handler(commands=['start', 'help'])
# @dp.message_handler(content_types=["any"])
@dp.message_handler()
async def send_welcome(message: types.Message):
    user = types.User.get_current()
    # contact = types.Contact.get_current()
    await message.answer(f"Hello\nI'm echo_bot\n{user=}")


class Command(BaseCommand):
    help = "Starting telegram bot @ul_akineo_med_bot"
    
    def handle(self, *ags, **options):
        executor.start_polling(dp, skip_updates=True)