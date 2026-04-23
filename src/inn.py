import sys
import os
import re
import urllib.request
import socket

class In:
    _CHARSET_NAME = "UTF-8"
    _WHITESPACE_PATTERN = re.compile(r'\s+')

    def __init__(self, name=None):
        self._buffer = ""
        self._tokens = []
        
        if name is None:
            self._stream = sys.stdin
        elif isinstance(name, str):
            if os.path.exists(name):
                self._stream = open(name, 'r', encoding=self._CHARSET_NAME)
            elif name.startswith(('http://', 'https://')):
                response = urllib.request.urlopen(name)
                content = response.read().decode(self._CHARSET_NAME)
                from io import StringIO
                self._stream = StringIO(content)
            else:
                raise ValueError(f"Nao foi possivel abrir: {name}")
        elif isinstance(name, socket.socket):
            content = name.recv(4096).decode(self._CHARSET_NAME)
            from io import StringIO
            self._stream = StringIO(content)
        else:
            self._stream = name

    def exists(self):
        return self._stream is not None

    def is_empty(self):
        if not self._tokens:
            line = self._stream.readline()
            if not line:
                return True
            self._tokens = self._WHITESPACE_PATTERN.split(line.strip())
            if self._tokens == ['']: self._tokens = []
        return not self._tokens and not self._has_more_content()

    def _has_more_content(self):
        pos = self._stream.tell()
        has_more = bool(self._stream.read(1))
        self._stream.seek(pos)
        return has_more

    def read_line(self):
        return self._stream.readline().rstrip('\n')

    def read_all(self):
        return self._stream.read()

    def read_string(self):
        if self.is_empty():
            raise EOFError("Nao ha mais tokens disponiveis")
        return self._tokens.pop(0)

    def read_int(self):
        return int(self.read_string())

    def read_double(self):
        return float(self.read_string())

    def read_float(self):
        return float(self.read_string())

    def read_long(self):
        return int(self.read_string())

    def read_boolean(self):
        s = self.read_string().lower()
        if s in ("true", "1"): return True
        if s in ("false", "0"): return False
        raise ValueError(f"Valor booleano invalido: {s}")

    def read_all_strings(self):
        return self._WHITESPACE_PATTERN.split(self.read_all().strip())

    def read_all_lines(self):
        return [line.rstrip('\n') for line in self._stream.readlines()]

    def read_all_ints(self):
        return [int(s) for s in self.read_all_strings() if s]

    def read_all_doubles(self):
        return [float(s) for s in self.read_all_strings() if s]

    def close(self):
        if self._stream != sys.stdin:
            self._stream.close()

if __name__ == "__main__":
    url_name = "https://introcs.cs.princeton.edu/java/stdlib/InTest.txt"
    print(f"Lendo de: {url_name}")
    try:
        in_stream = In(url_name)
        print(in_stream.read_all())
        in_stream.close()
    except Exception as e:
        print(f"Erro: {e}")