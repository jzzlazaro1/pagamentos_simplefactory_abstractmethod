from abc import ABC, abstractmethod

# Hierarquia de pagamentos

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor: float):
        pass

class PagamentoOnlineCartao(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagamento Online.",end=" ")
        print(f"Pagando R$ {valor:.2f} com cartão.")

class PagamentoOnlinePix(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagamento Online.",end=" ")
        print(f"Enviando PIX para valor de R$ {valor:.2f}.")

class PagamentoOfflineCartao(Pagamento):
    def pagar(self, valor: float):
        print(f"Pagamento Offline.",end=" ")
        print(f"Pagando R$ {valor:.2f} com cartão.")

class PagamentoOfflineBoleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento Offline.",end=" ")

      
def realizar_pagamento(tipo: str, forma: str, valor: float):
    factory = PagamentoFactory()
    pagamento = factory.criarPagamento(tipo, forma)
    pagamento.pagar(valor)


if __name__ == "__main__":
    realizar_pagamento("online", "pix", 120.0)         # PIX online
    realizar_pagamento("online", "cartao", 300.0)      # Cartão online
    realizar_pagamento("offline", "boleto", 500.0)     # Boleto offline
    realizar_pagamento("offline", "cartao", 75.25)     # Cartão offline
        print(f"Gerando boleto para R$ {valor:.2f}.")
