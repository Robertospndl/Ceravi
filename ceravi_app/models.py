from django.forms import CharField, Field
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# As classes do modelo do sistema são definidas neste arquivo  models.py

#Classe Usuário
class Usuario(models.Model):
    idUsuario = models.IntegerField(unique=True)
    tipo = models.IntegerField()
    nome = models.CharField(max_length=1024)
    email = models.EmailField(primary_key=True)
    senha = models.CharField(max_length=1024)

    #Métodos da classe (apenas para o UC login)

    @staticmethod 
    def validarSenha(senhaBanco, senha):
        return senhaBanco == senha

    @staticmethod 
    def validarEmail(email):
        #consulta no banco de dados se existe uma pesssoa cadastrada com o email informado
        try:
            return Usuario.objects.get(email=email) #caso a pessoa seja encontrada, todos os atributos são retornados na variável usuario
        except ObjectDoesNotExist:
            return False #pessoa não está cadastrada

    @staticmethod 
    def logar(email, senha):
        usuario = Usuario.validarEmail(email)

        if usuario and Usuario.validarSenha(usuario.senha, senha): #Verificando se a senha está correta
            return usuario
        
        return False        