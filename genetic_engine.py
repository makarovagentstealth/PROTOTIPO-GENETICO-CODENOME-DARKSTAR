import random
import math
import sys

# [1] Modelagem Genética Baseada em DNA
class GeneticEngine:
    def __init__(self, tissue_type: str):
        self.tissue_type = tissue_type  # 'male' ou 'female'
        self.genes = {
            # Genes fictícios baseados em funções reais (ex.: CYP19A1 para estrogênio)
            'ESR1': {'sequence': 'ATGCGTA', 'hormone': 'estrogen', 'level': 50.0},
            'AR': {'sequence': 'TAGCTAG', 'hormone': 'testosterone', 'level': 30.0},
            'PRL': {'sequence': 'GGGACCC', 'hormone': 'prolactin', 'level': 20.0}
        }
        self.acoustic_signal = None  # Frequência acústica simulada (Hz)

    # [2] Mutação por SNPs com influência quântica (decoerência simulada)
    def apply_snp(self, gene: str, position: int):
        if gene not in self.genes:
            raise ValueError("Gene não encontrado.")
        
        seq = list(self.genes[gene]['sequence'])
        bases = ['A', 'T', 'C', 'G']
        original_base = seq[position]
        bases.remove(original_base)
        
        # Simulação de probabilidade quântica (colapso de função de onda)
        prob = math.sin(random.uniform(0, math.pi)) ** 2  # Probabilidade não clássica
        new_base = random.choices(bases, weights=[prob, 1-prob, 1-prob], k=1)[0]
        seq[position] = new_base
        self.genes[gene]['sequence'] = ''.join(seq)
        self._update_hormone_level(gene)

    # [3] Atualização de hormônios baseada na mutação
    def _update_hormone_level(self, mutated_gene: str):
        hormone = self.genes[mutated_gene]['hormone']
        delta = random.normalvariate(0, 0.1)  # Variação Gaussiana
        self.genes[mutated_gene]['level'] *= (1 + delta)

    # [4] Resposta a estímulos acústicos (simulação de biohacking)
    def acoustic_activation(self, frequency: float):
        self.acoustic_signal = frequency
        for gene in self.genes:
            # Liberação hormonal proporcional à frequência (ex.: ultrassom terapêutico)
            if 20000 <= frequency <= 30000:  # Faixa de ultrassom
                self.genes[gene]['level'] *= 1.05

    # [5] Estado atual do sistema
    def status_report(self):
        report = f"=== Tecido Mamário ({self.tissue_type.capitalize()}) ===\n"
        for gene, data in self.genes.items():
            report += f"Gene {gene} ({data['hormone']}): Nível = {data['level']:.2f}, DNA = {data['sequence']}\n"
        if self.acoustic_signal:
            report += f"Sinal Acústico Ativo: {self.acoustic_signal} Hz\n"
        return report
