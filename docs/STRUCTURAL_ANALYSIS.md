---
title: Memória de Cálculo — Análise Estrutural
sidebar_position: 3
---

# Memória de Cálculo — Análise Estrutural da Plataforma de Força

**Data:** 2026-04-04
**Revisão:** 1.0
**Autor:** Aldo Seffrin + Claude Code (análise assistida)

---

## 1. Objetivo

Verificar a integridade estrutural da chapa superior da plataforma de força sob cargas de operação (atletas em pé, saltos CMJ e DJ), determinando deflexão máxima, tensão e fator de segurança. Definir reforço estrutural necessário.

---

## 2. Dados de Entrada

### 2.1 Material — Alumínio 6061-T6

| Propriedade | Valor |
|-------------|-------|
| Módulo de elasticidade (E) | 68.900 MPa |
| Tensão de escoamento (σ_y) | 276 MPa |
| Coeficiente de Poisson (ν) | 0,33 |
| Densidade (ρ) | 2.700 kg/m³ |

### 2.2 Geometria

| Componente | Dimensões |
|------------|-----------|
| Chapa superior | 600 × 500 × 6 mm, Al 6061-T6, cantos R30 |
| Chapa inferior | 527 × 396 × 3 mm, Al, cantos chanfrados 15×15 |
| Tubo de reforço | 30×30 ou 35×35 × 2 mm, Al, 527mm comprimento, ×2 |
| Furos | Ø11 mm (M10 DIN 7991), escareados Ø20 na chapa superior |

### 2.3 Apoios (Células de Carga)

Centros dos pares de furos (referência: canto inferior esquerdo da chapa superior):

| Célula | X (mm) | Y (mm) |
|:------:|:------:|:------:|
| C1 (sup-esq) | 62,5 | 417,1 |
| C2 (sup-dir) | 537,5 | 417,1 |
| C3 (inf-esq) | 62,5 | 83,0 |
| C4 (inf-dir) | 537,5 | 83,0 |

**Vão entre apoios:**
- Eixo X: 537,5 − 62,5 = **475,0 mm**
- Eixo Y: 417,1 − 83,0 = **334,1 mm**

### 2.4 Cenários de Carga

| Cenário | Massa (kg) | Multiplicador | Força (N) |
|---------|:----------:|:-------------:|:---------:|
| Atleta leve — em pé | 70 | 1,0× | 687 |
| Atleta médio — em pé | 85 | 1,0× | 834 |
| Atleta pesado — em pé | 120 | 1,0× | 1.177 |
| Atleta médio — CMJ pico | 85 | 3,0× | 2.502 |
| Atleta pesado — CMJ pico | 120 | 3,0× | 3.532 |
| Atleta pesado — DJ pico | 120 | 5,0× | 5.886 |
| Atleta pesado — DJ extremo | 120 | 7,0× | 8.240 |

**Cenário crítico de projeto:** DJ 5×BW com atleta de 120 kg → **P = 5.886 N**

---

## 3. Modelo de Cálculo

### 3.1 Modelo adotado

Placa retangular de Kirchhoff sobre 4 apoios pontuais, com carga concentrada no centro (pior caso). Solução por série dupla de Fourier (Navier) para placa simplesmente apoiada, com fator de correção de 1,8× para apoios pontuais (mais flexíveis que bordas apoiadas).

### 3.2 Rigidez flexural da placa

$$D = \frac{E \cdot t^3}{12 \cdot (1 - \nu^2)}$$

Para t = 6 mm:

$$D = \frac{68.900 \times 6^3}{12 \times (1 - 0,33^2)} = \frac{68.900 \times 216}{12 \times 0,8911} = \frac{14.882.400}{10,693} = 1.391.763 \text{ N·mm}$$

### 3.3 Deflexão — Série de Navier (centro da placa)

$$w_{max} = \frac{4P}{ab\pi^4 D} \sum_{m=1,3,5...} \sum_{n=1,3,5...} \frac{1}{\left[\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2\right]^2}$$

Com a = 475 mm, b = 334 mm, convergência com 80 termos.

Fator de correção para apoios pontuais: **×1,8** (conservador).

---

## 4. Resultados — Chapa Sem Reforço (6 mm)

| Cenário | P (N) | Deflexão (mm) | Tensão (MPa) | FS |
|---------|:-----:|:-------------:|:------------:|:--:|
| 120 kg em pé | 1.177 | 2,55 | 188,2 | 1,5 |
| 85 kg CMJ 3× | 2.502 | 5,41 | 399,8 | 0,7 |
| 120 kg DJ 5× | 5.886 | 12,73 | 940,9 | 0,3 |

:::danger FALHA
A chapa de 6 mm sem reforço apresenta deflexão de **12,7 mm** e tensão **3,4× acima do escoamento** no cenário de DJ. Estruturalmente inaceitável para plataforma de força.
:::

---

## 5. Estudo de Materiais Alternativos

Avaliação comparativa para o cenário crítico (DJ 5×BW, 120 kg):

| Material | Espessura | Peso chapa | Custo est. | Deflexão | FS |
|----------|:---------:|:----------:|:----------:|:--------:|:--:|
| Al 6061-T6 | 6 mm | 4,86 kg | R$ 194 | 12,72 mm | 0,3 |
| Al 6061-T6 | 15 mm | 12,15 kg | R$ 486 | 0,81 mm | 2,1 |
| Aço 1020 | 10 mm | 23,55 kg | R$ 283 | 0,97 mm | 1,2 |
| Aço 1045 | 10 mm | 23,55 kg | R$ 353 | 0,95 mm | 1,9 |
| Aço 1045 | 12 mm | 28,26 kg | R$ 424 | 0,55 mm | 2,7 |
| Inox 304 | 12 mm | 28,80 kg | R$ 1.008 | 0,58 mm | 1,1 |

**Conclusão:** Chapa única (sem reforço) exige espessura elevada — 15 mm em alumínio (+R$ 292, +7,3 kg) ou 10-12 mm em aço (+18-23 kg). Alternativa: reforço estrutural.

---

## 6. Análise de Reforços Estruturais

### 6.1 Opções avaliadas

| Opção | Conceito | Peso add. | Custo | Deflexão DJ 5× |
|-------|----------|:---------:|:-----:|:---------------:|
| Nervuras Al 3×50×6mm | Barras coladas sob a chapa | +1,5 kg | ~R$ 78 | 0,27 mm |
| Quadro tubular aço 30×30 | Moldura soldada | +6,2 kg | ~R$ 124 | 0,43 mm |
| **Seção caixão 2 tubos** | **Chapas + tubos colados** | **+0,75 kg** | **~R$ 50** | **0,18 mm** |

### 6.2 Solução adotada — Seção caixão

As duas chapas (superior 6 mm + inferior 3 mm) funcionam como flanges de uma viga-caixão, conectadas por **2 tubos quadrados de alumínio** colados com epóxi estrutural.

```
╔══════════════════════════╗  ← chapa superior 6 mm (flange)
║    ┌────┐        ┌────┐  ║
║    │tubo│        │tubo│  ║  ← 2 tubos 30×30 ou 35×35×2 mm (alma)
║    │ 1  │        │ 2  │  ║
║    └────┘        └────┘  ║
╚══════════════════════════╝  ← chapa inferior 3 mm (flange)
```

**Posição dos tubos (ref. chapa superior):**
- Tubo 1: Y = 194 mm (longitudinal, eixo X)
- Tubo 2: Y = 306 mm (longitudinal, eixo X)
- Comprimento: 527 mm (= largura da chapa inferior)
- Distância mínima às células: ~100 mm (sem interferência)

---

## 7. Cálculo da Seção Caixão

### 7.1 Geometria da seção composta

Referência: base da chapa inferior (y = 0)

| Componente | Área (mm²) | Centróide y (mm) |
|------------|:----------:|:----------------:|
| Chapa inferior (300×3 mm) | 900 | 1,5 |
| Tubo 1 (35×35×2 mm) | 264 | 20,5 |
| Tubo 2 (35×35×2 mm) | 264 | 20,5 |
| Chapa superior (300×6 mm) | 1.800 | 41,0 |
| **Total** | **3.228** | — |

**Largura efetiva adotada:** 300 mm (conservador — plate effective width)
**Altura total da seção:** 44 mm (3 + 35 + 6)

### 7.2 Centróide da seção composta

$$\bar{y} = \frac{\sum A_i \cdot y_i}{\sum A_i} = \frac{900 \times 1,5 + 2 \times 264 \times 20,5 + 1800 \times 41,0}{3228} = \frac{85.974}{3.228} = 26,6 \text{ mm}$$

### 7.3 Momento de inércia (Steiner)

| Componente | I_próprio (mm⁴) | A·d² (mm⁴) | I_total (mm⁴) |
|------------|:---------------:|:-----------:|:--------------:|
| Chapa inferior | 675 | 567.009 | 567.684 |
| Tubo 1 | 48.092 | 9.823 | 57.915 |
| Tubo 2 | 48.092 | 9.823 | 57.915 |
| Chapa superior | 5.400 | 373.248 | 378.648 |
| **TOTAL** | — | — | **1.062.162** |

**Ganho de rigidez:** I_caixão / I_chapa = 1.062.162 / 9.000 = **118×**

### 7.4 Resultados — Seção caixão com 2 tubos 35×35×2 mm

| Cenário | P (N) | Deflexão (mm) | Tensão (MPa) | FS |
|---------|:-----:|:-------------:|:------------:|:--:|
| 70 kg em pé | 687 | 0,021 | 2,0 | 135 |
| 85 kg em pé | 834 | 0,025 | 2,5 | 111 |
| 120 kg em pé | 1.177 | 0,036 | 3,5 | 79 |
| 85 kg CMJ 3× | 2.502 | 0,076 | 7,4 | 37 |
| 120 kg CMJ 3× | 3.532 | 0,108 | 10,5 | 26 |
| **120 kg DJ 5×** | **5.886** | **0,180** | **17,5** | **15,7** |
| 120 kg DJ 7× (extremo) | 8.240 | 0,251 | 24,5 | 11,2 |

:::info
Deflexão máxima < 0,2 mm em todos os cenários, incluindo DJ extremo. FS > 10 em todas as condições.
:::

### 7.5 Sensibilidade ao tamanho do tubo

| Tubo | I total (mm⁴) | Deflexão DJ 5× | Diferença |
|------|:-------------:|:--------------:|:---------:|
| 35×35×2 mm | 1.062.159 | 0,180 mm | referência |
| 30×30×2 mm + calços | ~1.010.000 | ~0,189 mm | +5% |

Diferença desprezível — ambos os tamanhos atendem com folga.

---

## 8. Verificação da Colagem

### 8.1 Cisalhamento na interface tubo-chapa

| Parâmetro | Valor |
|-----------|-------|
| Cortante máximo (V = P/2) | 2.943 N |
| Primeiro momento de área (Q_top) | 25.920 mm³ |
| Fluxo cisalhante (q = VQ/I) | 71,6 N/mm |
| Largura de colagem (2 tubos × 35 mm) | 70 mm |
| Tensão na cola (τ = q/b) | **1,02 MPa** |
| Resistência do epóxi estrutural | 20–30 MPa |
| **Fator de segurança colagem** | **> 20** |

### 8.2 Especificação da cola

- Tipo: epóxi bicomponente estrutural (Araldite Professional, Loctite EA 9461 ou equivalente)
- Resistência ao cisalhamento: ≥ 20 MPa
- Preparação: lixar superfícies (lixa 80), desengordurar (álcool isopropílico)
- Cura: 24h sob pressão (grampos/sargentos)

---

## 9. Critérios de Aceitação

| Critério | Limite | Resultado | Status |
|----------|:------:|:---------:|:------:|
| Deflexão máxima (DJ 5×BW) | < 0,5 mm | 0,18 mm | ✅ |
| Deflexão máxima (CMJ 3×BW) | < 0,2 mm | 0,08 mm | ✅ |
| Fator de segurança (DJ 5×) | ≥ 2,0 | 15,7 | ✅ |
| FS colagem (DJ 5×) | ≥ 3,0 | > 20 | ✅ |

---

## 10. Decisão de Projeto

### Problema
A chapa superior de 6 mm de alumínio sem reforço deflecte 12,7 mm sob carga de DJ (120 kg, 5×BW) — inaceitável para plataforma de força (precisão de medição).

### Alternativas avaliadas
1. Aumentar espessura (15 mm Al ou 10 mm aço) — pesado e/ou caro
2. Nervuras coladas — eficaz mas menos elegante
3. Quadro tubular de aço — bom mas pesado (+6 kg) e requer soldagem
4. **Seção caixão com tubos quadrados** — melhor relação custo-peso-rigidez

### Solução adotada
2 tubos quadrados de alumínio (30×30 ou 35×35×2 mm) colados com epóxi estrutural entre as duas chapas, criando seção caixão com I = 1.062.000 mm⁴ (118× a chapa sozinha).

### Impacto

| Parâmetro | Sem reforço | Com reforço | Melhoria |
|-----------|:----------:|:----------:|:--------:|
| Deflexão DJ 5× | 12,73 mm | 0,18 mm | **71×** |
| FS estrutural | 0,3 | 15,7 | **52×** |
| Peso adicional | — | +0,75 kg | — |
| Custo adicional | — | ~R$ 55 | — |

---

## 11. Limitações do Modelo

1. **Modelo analítico** — série de Navier com fator de correção empírico (1,8×) para apoios pontuais. Para validação definitiva, recomenda-se FEA ou teste físico.
2. **Carga pontual** — o modelo assume carga concentrada no centro (pior caso). Na realidade, o pé do atleta distribui a carga em ~200-300 cm², reduzindo a deflexão real.
3. **Largura efetiva** — adotada 300 mm (conservador). A contribuição real das chapas pode ser maior.
4. **Colagem ideal** — assume transferência perfeita de cisalhamento pela cola. A preparação da superfície é crítica.
5. **Não considera efeitos dinâmicos** — cargas de impacto (DJ) são transientes e a inércia do sistema atenua picos.

---

## 12. Referências

- Timoshenko, S. P., Woinowsky-Krieger, S. (1959). *Theory of Plates and Shells*, 2nd Ed. McGraw-Hill.
- Young, W. C., Budynas, R. G. (2002). *Roark's Formulas for Stress and Strain*, 7th Ed. McGraw-Hill.
- Scripts de cálculo: `cad/structural_analysis.py`, `cad/material_comparison.py`, `cad/reinforcement_analysis.py`, `cad/box_section_analysis.py`

---

## 13. Histórico de Revisões

| Rev. | Data | Descrição |
|:----:|:----:|-----------|
| 1.0 | 2026-04-04 | Análise completa: chapa sem reforço, comparativo de materiais, solução seção caixão |
