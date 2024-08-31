from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


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
            ("📍 Трекер-коды", "traker-codes"),
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

    @staticmethod
    async def admins_pages(admins, page):
        navigation_buttons = [InlineKeyboardButton(text="◀️", callback_data=f"prev_{page}"),
                              InlineKeyboardButton(text="❌", callback_data="menu_admin"),
                              InlineKeyboardButton(text="▶️", callback_data=f"next_{page}")]
        
        add_buttons = [InlineKeyboardButton(text="➕ Добавить", callback_data="add_admin")]

        menu = InlineKeyboardBuilder()

        start_index = (page) * 7
        end_index = min(start_index + 7, len(admins))
        
        for uid, url, status in admins[start_index:end_index]:
            menu.row(InlineKeyboardButton(text=f"#{uid} t.me/{url} ({status})", callback_data=f"order_{uid}_{page}"))

        menu.row(*add_buttons)
        menu.row(*navigation_buttons)

        return menu.as_markup()
