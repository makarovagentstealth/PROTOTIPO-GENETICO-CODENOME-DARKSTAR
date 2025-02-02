import argparse
import random
import sys
from genetic_engine import GeneticEngine  # Importação adicionada

class QuantumInjector:
    def __init__(self, genetic_engine):
        self.genetic_engine = genetic_engine
        self.entangled_genes = []  # Simulação de entrelaçamento quântico

    # [1] Entrelaçamento quântico entre genes (modelo hipotético)
    def quantum_entanglement(self, gene1: str, gene2: str):
        if gene1 not in self.genetic_engine.genes or gene2 not in self.genetic_engine.genes:
            raise ValueError("Gene inválido.")
        self.entangled_genes.append((gene1, gene2))

    # [2] Injeção de mutação com superposição quântica
    def inject_superposition_mutation(self):
        if not self.entangled_genes:
            raise ValueError("Genes não entrelaçados.")
        
        # Escolha de gene entrelaçado via "decoerência simulada"
        gene_pair = random.choice(self.entangled_genes)
        target_gene = random.choice(gene_pair)
        position = random.randint(0, len(self.genetic_engine.genes[target_gene]['sequence']) - 1)
        
        # Aplica mutação em superposição (ambos genes até medição)
        print(f"Estado Quântico: Mutação em superposição ({gene_pair[0]} ↔ {gene_pair[1]})")
        self.genetic_engine.apply_snp(target_gene, position)
        print(f"Colapso de Função de Onda: Mutação em {target_gene} (Posição {position})")

    # [3] Interface de linha de comando
    @staticmethod
    def cli_interface():
        parser = argparse.ArgumentParser(description="Injetor de Mutação Quântica")
        parser.add_argument("--entangle", nargs=2, help="Entrelaçar dois genes (ex.: ESR1 AR)")
        parser.add_argument("--inject", action="store_true", help="Injetar mutação quântica")
        return parser.parse_args()

if __name__ == "__main__":
    # Configuração do sistema
    tissue_type = 'female' if random.random() > 0.5 else 'male'
    engine = GeneticEngine(tissue_type)  # Agora a classe GeneticEngine é reconhecida
    injector = QuantumInjector(engine)
    args = QuantumInjector.cli_interface()

    try:
        if args.entangle:
            injector.quantum_entanglement(*args.entangle)
            print(f"Entrelaçamento Quântico: {args.entangle[0]} ↔ {args.entangle[1]}")
        if args.inject:
            injector.inject_superposition_mutation()
        
        print("\n" + engine.status_report())
    except Exception as e:
        print(f"Erro: {str(e)}", file=sys.stderr)
