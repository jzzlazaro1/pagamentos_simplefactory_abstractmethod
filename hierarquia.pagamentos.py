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
        print(f"Gerando boleto para R$ {valor:.2f}.")

class PagamentoFactory:

    def criarPagamento(self, tipo: str, forma: str) -> Pagamento:
        """Cria instância de Pagamento com base no tipo e forma."""
        tipo = tipo.lower()
        forma = forma.lower()

        match tipo:
            case "online":
                # pagamento online: suporta cartão e PIX, por exemplo
                match forma:
                    case "pix":
                        return PagamentoOnlinePix()
                    case "cartao":
                        return PagamentoOnlineCartao()
                    case _:
                        raise ValueError(f"'Forma de pagamento online, não suportada: {forma}'")
            case "offline":
                # pagamento offline: cartão e boleto, por exemplo
                match forma:
                    case "boleto":
                        return PagamentoOfflineBoleto()
                    case "cartao":
                        return PagamentoOfflineCartao()
                    case _:
                        raise ValueError(f"'Forma de pagamento offline, não suportada: {forma}'")
