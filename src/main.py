import sys
from inn import In
from graph import Graph
from dsatur import GraphColoringDSatur
from stdout import StdOut
from stdin import StdIn
class Main:
    @staticmethod
    def main():
        if len(sys.argv) < 2:
            print("Erro: informe o arquivo de entrada.")
            print("Exemplo: python main.py ../dados/brasil.txt")
            return

        try:
            in_data = In(sys.argv[1])
            graph = Graph(sys.argv[1])
            dsatur = GraphColoringDSatur(graph)

            print("Grafo carregado:")
            print(graph)
            print()

            dsatur.color()

            print("Ordem de coloração:")
            order = dsatur.get_coloring_order()
            print(" -> ".join(map(str, order)))
            print()

            print("Cores finais de cada vértice:")
            print("Vértice | Cor")
            print("--------|----")
            for v in range(graph.V()):
                print(f"{v:7} | {dsatur.get_color(v)}")
            print()

            total_colors = dsatur.get_color_count()
            print(f"Total de cores utilizadas: {total_colors}")

            is_valid = dsatur.is_valid_coloring()
            print(f"A coloração produzida é válida? {'Sim' if is_valid else 'Não'}")

        except Exception as e:
            print(f"Ocorreu um erro ao processar o grafo: {e}")

if __name__ == "__main__":
    Main.main()