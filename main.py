import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart
from button import keyboard, gen
from root import TOKEN
from forma import Form

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(text="Hi there, I'm a bot", reply_markup=keyboard)


    @dp.message()
    async def echo(message: Message, state: FSMContext):
        if message.text == "Register":
            await state.set_state(Form.name)
            await message.answer(text="Enter your name:", reply_markup=ReplyKeyboardRemove())


@dp.message(Form.name)
async def names(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer(text="Enter your age:")


@dp.message(Form.age)
async def genders(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Form.gender)
    await message.answer("Your gender is:", reply_markup=gen)


@dp.message(Form.gender)
async def birthdays(message: Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Form.birthday)
    await message.answer(text="Enter your birthday:",reply_markup=ReplyKeyboardRemove())


@dp.message(Form.birthday)
async def passwords(message: Message, state: FSMContext):
    await state.update_data(birthday=message.text)
    await state.set_state(Form.password)
    await message.answer("Your password is:")


@dp.message(Form.password)
async def finishes(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(Form.finish)
    data = await state.get_data()
    await state.clear()
    await message.answer("Register Done ! ✅")
    name = data.get("name", "Unknown")
    age = data.get("age", "Unknown")
    gender = data.get("gender", "Unknown")
    birthday = data.get("birthday", "Unknown")
    password = data.get("password", "Unknown")

    await message.answer(
        f"Your data is now saved !\nName: {name}, \nAge: {age}, \nGender:{gender}, \nBirthday: {birthday}, \nPassword: {password} ")


@dp.message(Form.finish)
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
