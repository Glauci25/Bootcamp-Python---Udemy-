class QuizBrain: #controla quais perguntas já foram feitas, quais vêm a seguir e como apresentar essas perguntas ao usuário
    def __init__(self,lista_perguntas):
        self.numero = 0 #em qual pergunta o quiz está 
        self.lista = lista_perguntas #recebe a lista de perguntas do banco

    def next_question(self):
        pergunta_atual = self.lista[self.numero] #essa variável é um OBJETO da classe PERGUNTA
        score = self.numero
        self.numero += 1
        user_resposta = input(f'Q.{self.numero}: {pergunta_atual.texto} (True/False): ').title()
        if user_resposta == pergunta_atual.resposta:
            print('Você acertou!')
            score += 1
        else:
            print(f'Erraste!')
            score = score
        print(f'A resposta certa é {pergunta_atual.resposta}.')
        print(f'Pontuação atual: {score}.')

    def remain(self):
        if self.numero == len(self.lista):
            print('Acabou o Quiz!')
            return False
        else:
            return True
        