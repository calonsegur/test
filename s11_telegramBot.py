import telegram
import s10_getStockPrice as getStockPrice

# 본인의 토큰주소를 입력하시오
token = '1930940408:AAHlRWewqhHVzzJLc2UvNbGvJkkphoulCa4'

bot=telegram.Bot(token)
#my_id=bot.getUpdates()[0].message.chat.id

my_id=1770308001

stocks=getStockPrice.setPrice(getStockPrice.stocks)
print(stocks)

text_lst = []
for _key, _value in stocks.items():
    _price = _value['price']
    text_lst.append(f'{_key} 현재가: {_price}')
# print(text_lst)
_text4tele='\n'.join(text_lst)
bot.send_message(chat_id=my_id, text=_text4tele)
bot.send_message(chat_id=my_id, text='Hello python ')