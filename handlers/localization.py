
def start_message(user_id: int) -> str:
    return (f'<b>Привет, {user_id}!</b>\n'
            '<b>Данный бот создан для поиска фото в Google</b>')
    
def get_description() -> str:
    return '<b>Введите описание фото:</b>'

def photo_search() -> str:
    return '<b><i>⏳ Поиск...</i></b>'