from abc import ABC, abstractmethod
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, destino: str, mensagem: str) -> str:
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self, destino: str, mensagem: str) -> str:
        return f"E-mail enviado para {destino} com a mensagem: '{mensagem}'."

class NotificacaoSMS(Notificacao):
    def enviar(self, destino: str, mensagem: str) -> str:
        return f"SMS enviado para {destino} com a mensagem: '{mensagem}'."

class NotificacaoWhatsApp(Notificacao):
    def enviar(self, destino: str, mensagem: str) -> str:
        return f"Mensagem de WhatsApp enviada para {destino} com a mensagem: '{mensagem}'."

class NotificacaoFactory(ABC):
    @abstractmethod
    def criarNotificacao(self) -> Notificacao:
        pass

class EmailNotificacaoFactory(NotificacaoFactory):
    def criarNotificacao(self) -> Notificacao:
        return NotificacaoEmail()

class SMSNotificacaoFactory(NotificacaoFactory):
    def criarNotificacao(self) -> Notificacao:
        return NotificacaoSMS()

class WhatsAppNotificacaoFactory(NotificacaoFactory):
    def criarNotificacao(self) -> Notificacao:
        return NotificacaoWhatsApp()
