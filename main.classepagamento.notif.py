from abc import ABC, abstractmethod

# Classes de Pagamento
class Pagamento(ABC):
    @abstractmethod
    def processarPagamento(self, valor: float) -> str:
        pass

class PagamentoCartao(Pagamento):
    def processarPagamento(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com cartão de crédito."

class PagamentoBoleto(Pagamento):
    def processarPagamento(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com boleto bancário."

class PagamentoPix(Pagamento):
    def processarPagamento(self, valor: float) -> str:
        return f"Pagamento de R${valor:.2f} realizado com Pix."

class PagamentoFactory(ABC):
    @abstractmethod
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        pass

class FactoryPagamentoOnline(PagamentoFactory):
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        if tipo_pagamento == "cartao":
            return PagamentoCartao()
        elif tipo_pagamento == "pix":
            return PagamentoPix()
        else:
            raise ValueError(f"Tipo de pagamento online não suportado: {tipo_pagamento}")

class FactoryPagamentoOffline(PagamentoFactory):
    def criarPagamento(self, tipo_pagamento: str) -> Pagamento:
        if tipo_pagamento == "boleto":
            return PagamentoBoleto()
        else:
            raise ValueError(f"Tipo de pagamento offline não suportado: {tipo_pagamento}")

# Classes de Notificação
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

# Código do Cliente para demonstração de pagamento
def realizar_pagamento(factory_type: str, payment_method: str, valor: float) -> str:
    factory: PagamentoFactory = None
    if factory_type == "online":
        factory = FactoryPagamentoOnline()
    elif factory_type == "offline":
        factory = FactoryPagamentoOffline()
    else:
        raise ValueError(f"Tipo de fábrica de pagamento não suportado: {factory_type}")

    pagamento = factory.criarPagamento(payment_method)
    return pagamento.processarPagamento(valor) # Corrigido: 'pagar' para 'processarPagamento'

if __name__ == "__main__":
    print("\033[35m--- Demonstração do Cliente com Abstract Factory (Pagamento Corrigido) ---\033")
    print(realizar_pagamento("online", "pix", 120.0))         # PIX online
    print(realizar_pagamento("online", "cartao", 300.0))      # Cartão online
    print(realizar_pagamento("offline", "boleto", 500.0))     # Boleto offline
    # A linha abaixo causaria um ValueError porque FactoryPagamentoOffline não suporta 'cartao'.
    # print(realizar_pagamento("offline", "cartao", 75.25)) # Cartão offline

    # Demonstração adicional para notificações
    print("\n\033[35m--- Demonstração do Cliente com Fábricas Concretas de Notificação ---\033")
    email_factory = EmailNotificacaoFactory()
    email_notifier = email_factory.criarNotificacao()
    print(email_notifier.enviar("cliente@exemplo.com", "Sua fatura corrigida está disponível."))

    sms_factory = SMSNotificacaoFactory()
    sms_notifier = sms_factory.criarNotificacao()
    print(sms_notifier.enviar("+559988776655", "Seu pedido corrigido foi despachado!"))

    whatsapp_factory = WhatsAppNotificacaoFactory()
    whatsapp_notifier = whatsapp_factory.criarNotificacao()
    print(whatsapp_notifier.enviar("+5511999998888", "Nova promoção exclusiva para você!"))

    print('\033[32m Demonstração concluída.\033')
