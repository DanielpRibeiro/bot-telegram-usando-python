import telebot

CHAVE_API =""

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["obrigado"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, "Por nada!! Estamos aqui para ajudar :)")


@bot.message_handler(commands=["opcao1"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, """
Nosso email: programacaoweb@fanap.edu.br

/opcao2 Verificar Número Telefone
/opcao3 Informações Gerais
/opcao4 Encerrar Chat
                 """)


@bot.message_handler(commands=["opcao2"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, """
Nosso contato é +55 (62) 97846-5457

/opcao1 Verificar E-mail
/opcao3 Informações Gerais
/opcao4 Encerrar Chat
""")


@bot.message_handler(commands=["opcao3"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, """
Informações Gerais:

Escolha uma opção para continuar (Clique no item):
/disciplina Verificar disciplina cursada
/horario_aula Verificar Horário de aula
/dia_aula Verificar dia de aula

/opcao4 Encerrar Chat

    
Responder qualquer outra coisa não irá funcionar""")
    
@bot.message_handler(commands=["opcao4"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, "Chat encerrado. Espero ter ajudado :)")

    
    # informações Gerais
@bot.message_handler(commands=["disciplina"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, "Disciplina: Programação WEB")


@bot.message_handler(commands=["horario_aula"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, "18:50 às 22:00 horas")

@bot.message_handler(commands=["dia_aula"])
def opcao1 (mensagem):
    bot.reply_to(mensagem, "Dia de aula: Toda Segunda-feira")





def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)

def responder(mensagem):
    texto="""
        Olá, esse é o BOT Programação Web
    
Escolha uma opção para continuar (Clique no item):
/opcao1 Verificar E-mail
/opcao2 Verificar Número Telefone
/opcao3 Informações Gerais
/opcao4 Encerrar Chat
    
Responder qualquer outra coisa não irá funcionar
    """
    bot.reply_to(mensagem, texto)
    

bot.polling()
