from aiogram.utils.keyboard import InlineKeyboardBuilder


class UserInlineKb:
    @staticmethod
    async def main_menu():
        buttons = [
            ("🔎 Проверить трек-код", "check_code"),
            ("❓ Как сделать заказ ❓", "why_order")
        ]

        menu = InlineKeyboardBuilder()

        for text, callback_data in buttons:
            menu.button(text=text, callback_data=callback_data)
        return menu.adjust(1).as_markup()
    
    @staticmethod
    async def main_menu_admin():
        buttons = [
            ("🔎 Проверить трек-код", "check_code"),
            ("❓ Как сделать заказ ❓", "why_order"),
            ("📍 Трекер-коды", "thaker-codes"),
            ("🕵️ Управление администраторами", "change_admins"),
        ]

        menu = InlineKeyboardBuilder()

        for text, callback_data in buttons:
            menu.button(text=text, callback_data=callback_data)
        return menu.adjust(1).as_markup()
    
    @staticmethod
    async def check_sub(url: str):
        buttons = [
            ("Подписаться", url)
        ]

        menu = InlineKeyboardBuilder()

        for text, url in buttons:
            menu.button(text=text, url=url)
        menu.button(text="Подписан", callback_data="done_sub")

        return menu.adjust(1).as_markup()
    

    @staticmethod
    async def info_track():
        buttons = [
            ("❗️Информация о статусах заказов", "get_info"),
            ("❌", "cancel")
        ]

        menu = InlineKeyboardBuilder()
        
        for text, callback_data in buttons:
            menu.button(text=text, callback_data=callback_data)
        return menu.adjust(1).as_markup()
    
    @staticmethod
    async def cancel_menu():
        buttons = [
            ("❌", "new_code")
        ]

        menu = InlineKeyboardBuilder()
        
        for text, callback_data in buttons:
            menu.button(text=text, callback_data=callback_data)
        return menu.adjust(1).as_markup()
