import os
from icrawler.builtin import GoogleImageCrawler

from aiogram.types.input_file import FSInputFile
from aiogram.types import Message


async def get_google_img(message: Message) -> None:
    for file in (os.listdir('google/img')):
        os.remove(f'google/img/{file}')
        
    filters = dict(type='photo')
    crawler = GoogleImageCrawler(
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': 'google/img'})
    crawler.crawl(keyword=message.text, max_num=2, filters=filters)
    
    for photo in (os.listdir('google/img')):
        await message.answer_photo(FSInputFile(f'google/img/{photo}'))
        os.remove(f'google/img/{photo}')
        
        
async def run_searching(message: Message) -> None:
    try:
        await get_google_img(message)
    except:
        await get_google_img(message)
    