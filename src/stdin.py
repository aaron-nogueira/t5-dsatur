import sys
import re

class StdIn:
    _WHITESPACE_PATTERN = re.compile(r'\s+')
    _tokens = (token for line in sys.stdin for token in line.split())
    _next_token = None

    @classmethod
    def _get_next(cls):
        try:
            return next(cls._tokens)
        except StopIteration:
            return None

    @classmethod
    def is_empty(cls):
        if cls._next_token is not None:
            return False
        cls._next_token = cls._get_next()
        return cls._next_token is None

    @classmethod
    def read_string(cls):
        if cls.is_empty():
            raise EOFError("Tentativa de ler de uma entrada vazia.")
        res = cls._next_token
        cls._next_token = None
        return res

    @classmethod
    def read_int(cls):
        return int(cls.read_string())

    @classmethod
    def read_double(cls):
        return float(cls.read_string())

    @classmethod
    def read_float(cls):
        return float(cls.read_string())

    @classmethod
    def read_long(cls):
        return int(cls.read_string())

    @classmethod
    def read_boolean(cls):
        s = cls.read_string().lower()
        if s in ("true", "1"): return True
        if s in ("false", "0"): return False
        raise ValueError(f"Valor booleano inválido: {s}")

    @classmethod
    def read_char(cls):
        # Lê exatamente um caractere do sys.stdin
        char = sys.stdin.read(1)
        if not char:
            raise EOFError("Fim da entrada ao ler char.")
        return char

    @classmethod
    def read_line(cls):
        # Se houver um token pendente no buffer, o comportamento do read_line
        # em implementações de token costuma ser problemático. 
        # Aqui, lemos a próxima linha disponível.
        return sys.stdin.readline().rstrip('\n\r')

    @classmethod
    def has_next_line(cls):
        # Python stdin não tem um 'peek' nativo simples para linhas sem consumir
        return not cls.is_empty()

    @classmethod
    def read_all(cls):
        return sys.stdin.read()

    @classmethod
    def read_all_strings(cls):
        return list(cls._tokens)

    @classmethod
    def read_all_ints(cls):
        return [int(s) for s in cls.read_all_strings()]

    @classmethod
    def read_all_doubles(cls):
        return [float(s) for s in cls.read_all_strings()]

    @classmethod
    def read_all_lines(cls):
        return [line.rstrip('\n\r') for line in sys.stdin.readlines()]

if __name__ == "__main__":
    # Teste interativo simples
    print("Digite uma string: ", end="", flush=True)
    print(f"Sua string: {StdIn.read_string()}")

    print("Digite um int: ", end="", flush=True)
    print(f"Seu int: {StdIn.read_int()}")

    print("Digite um boolean (true/false): ", end="", flush=True)
    print(f"Seu boolean: {StdIn.read_boolean()}")