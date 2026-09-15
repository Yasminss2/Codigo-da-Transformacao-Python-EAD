# ==========================================
# 1. EXCEÇÕES PERSONALIZADAS (Camada de Domínio)
# ==========================================
class SaldoInsuficienteError(Exception):
    """Lançada quando a conta não possui saldo suficiente para o saque."""
    pass


class LimiteDiarioExcedidoError(Exception):
    """Lançada quando o valor ultrapassa o limite diário permitido."""
    pass


# ==========================================
# 2. REGRA DE NEGÓCIO (Camada de Serviço)
# ==========================================
class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float, limite_diario: float = 1000.0):
        self.titular = titular
        self._saldo = saldo_inicial
        self.limite_diario = limite_diario
        self._total_sacado_hoje = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo

    def realizar_saque(self, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")

        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente. Saldo atual disponível: R$ {self._saldo:.2f}"
            )

        if (self._total_sacado_hoje + valor) > self.limite_diario:
            disponivel_hoje = self.limite_diario - self._total_sacado_hoje
            raise LimiteDiarioExcedidoError(
                f"Limite diário excedido. Valor máximo ainda disponível hoje: R$ {disponivel_hoje:.2f}"
            )

        self._saldo -= valor
        self._total_sacado_hoje += valor
        return self._saldo


# ==========================================
# 3. INTERFACE DE TERMINAL (Camada de Aplicação)
# ==========================================
def menu_terminal():
    conta = ContaBancaria(titular="Yasmin Santos", saldo_inicial=500.0, limite_diario=300.0)

    print(f"=== BANCO YASMIN - Bem-vindo(a), {conta.titular} ===")

    while True:
        print(f"\nSaldo disponível: R$ {conta.saldo:.2f}")
        opcao = input("Deseja realizar um saque? (s/n): ").strip().lower()

        if opcao != 's':
            print("\nOperação finalizada. Volte sempre!")
            break

        try:
            valor_input = float(input("Digite o valor do saque: R$ "))
            novo_saldo = conta.realizar_saque(valor_input)
            print(f"[SUCESSO] Saque efetuado! Novo saldo: R$ {novo_saldo:.2f}")

        except ValueError as err:
            print(f"[ERRO DE ENTRADA] {err}")

        except SaldoInsuficienteError as err:
            print(f"[FALHA NO SAQUE] {err}")

        except LimiteDiarioExcedidoError as err:
            print(f"[BLOQUEIO DE LIMITE] {err}")


# ==========================================
# EXECUÇÃO DO SISTEMA
# ==========================================
if __name__ == "__main__":
    menu_terminal()