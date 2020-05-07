from pyrogram import Client, Filters


ICOB_BOT = Client(
    api_id=1258237,
    api_hash ="79614db4d649f63199a54a52fe2a0549",    
    session_name = "ramazan",                 
    #bot_token = "1219314018:AAGhWXvv-zYiZ_1XqeF8nafSYr1IL3xUl2I",
    #plugins=dict(root="komutlar")
)

@ICOB_BOT.on_message(Filters.command(["deneme1"]))
def de(client, message):
    liste = []
    for i in client.iter_dialogs():
        liste.append(i)
    print(liste)
    print(len(liste))

ICOB_BOT.run()