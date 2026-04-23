import sys

class StdOut:
    # Em Python, o locale padrão para formatação de strings costuma ser 
    # controlado pelo sistema, mas as f-strings e format() seguem 
    # por padrão o comportamento de ponto decimal (US).

    @staticmethod
    def println(x=""):
        """Imprime um objeto e pula uma linha."""
        print(x)

    @staticmethod
    def print(x=""):
        """Imprime um objeto sem pular linha e força a atualização do buffer (flush)."""
        print(x, end="", flush=True)

    @staticmethod
    def printf(format_str, *args):
        """
        Imprime uma string formatada (estilo C) e força o flush.
        Exemplo: StdOut.printf("%d + %d = %d\n", a, b, soma)
        """
        sys.stdout.write(format_str % args)
        sys.stdout.flush()

if __name__ == "__main__":
    # Teste unitário das funcionalidades
    StdOut.println("Test")
    StdOut.println(17)
    StdOut.println(True)
    StdOut.printf("%.6f\n", 1.0/7.0)