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

### 2.1 Materiais

#### Chapas — Alumínio 5052-F

| Propriedade | Valor |
|-------------|-------|
| Módulo de elasticidade (E) | 70.300 MPa |
| Tensão de escoamento (σ_y) | 90 MPa |
| Coeficiente de Poisson (ν) | 0,33 |
| Densidade (ρ) | 2.680 kg/m³ |

:::info Mudança de liga (Rev. 2.0)
Liga original: 6061-T6 (σ_y = 276 MPa). Substituída por 5052-F por disponibilidade local. O módulo de elasticidade é praticamente igual (~70 GPa), então a **deflexão não muda**. A redução na tensão de escoamento é compensada pela folga estrutural da seção caixão (FS > 4 em todos os cenários).
:::

#### Tubos de reforço — Aço carbono 1020

| Propriedade | Valor |
|-------------|-------|
| Módulo de elasticidade (E) | 200.000 MPa |
| Tensão de escoamento (σ_y) | 250 MPa |
| Densidade (ρ) | 7.850 kg/m³ |
| Razão modular (n = E_aço/E_al) | 2,845 |

:::info Mudança de material (Rev. 2.0)
Tubos originais: alumínio 35×35×2 mm. Substituídos por aço carbono pela disponibilidade local. Tubos de alumínio são difíceis de encontrar no mercado regional; aço é padrão em qualquer casa de ferro. A troca aumenta a rigidez da seção caixão em ~23% com acréscimo de +1,4 kg no peso total.
:::

### 2.2 Geometria

| Componente | Dimensões |
|------------|-----------|
| Chapa superior | 600 × 500 × 6,35 mm (1/4"), Al 5052-F, cantos R30 |
| Chapa inferior | 527 × 396 × 3 mm, Al 5052-F, cantos chanfrados 15×15 |
| Tubo de reforço | 35×35 × 2 mm, aço carbono 1020, 527mm comprimento, ×2 |
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

Para t = 6,35 mm (Al 5052-F):

$$D = \frac{70.300 \times 6,35^3}{12 \times (1 - 0,33^2)} = \frac{70.300 \times 256,0}{12 \times 0,8911} = \frac{17.997.000}{10,693} = 1.683.000 \text{ N·mm}$$

:::note
D aumentou ~21% vs projeto original (1.392.000 N·mm com 6061-T6 6mm) — efeito combinado de E ligeiramente maior e espessura 6,35 mm.
:::

### 3.3 Deflexão — Série de Navier (centro da placa)

$$w_{max} = \frac{4P}{ab\pi^4 D} \sum_{m=1,3,5...} \sum_{n=1,3,5...} \frac{1}{\left[\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2\right]^2}$$

Com a = 475 mm, b = 334 mm, convergência com 80 termos.

Fator de correção para apoios pontuais: **×1,8** (conservador).

---

## 4. Resultados — Chapa Sem Reforço (6,35 mm, Al 5052-F)

| Cenário | P (N) | Deflexão (mm) | Tensão (MPa) | FS |
|---------|:-----:|:-------------:|:------------:|:--:|
| 120 kg em pé | 1.177 | 2,11 | 168,0 | 0,5 |
| 85 kg CMJ 3× | 2.502 | 4,48 | 357,0 | 0,3 |
| 120 kg DJ 5× | 5.886 | 10,52 | 840,0 | 0,1 |

:::danger FALHA
A chapa de 6,35 mm sem reforço apresenta deflexão de **10,5 mm** e tensão **9,3× acima do escoamento** no cenário de DJ. Ainda pior que com 6061-T6 em termos de FS, pois a redução de σ_y (90 MPa) supera o ganho de espessura. Reforço estrutural é obrigatório.
:::

---

## 5. Estudo de Materiais Alternativos

Avaliação comparativa para o cenário crítico (DJ 5×BW, 120 kg):

| Material | Espessura | Peso chapa | Custo est. | Deflexão | FS |
|----------|:---------:|:----------:|:----------:|:--------:|:--:|
| Al 5052-F | 6,35 mm | 5,11 kg | R$ 150 | 10,52 mm | 0,1 |
| Al 6061-T6 | 6 mm | 4,86 kg | R$ 194 | 12,72 mm | 0,3 |
| Al 6061-T6 | 15 mm | 12,15 kg | R$ 486 | 0,81 mm | 2,1 |
| Aço 1020 | 10 mm | 23,55 kg | R$ 283 | 0,97 mm | 1,2 |
| Aço 1045 | 10 mm | 23,55 kg | R$ 353 | 0,95 mm | 1,9 |
| Aço 1045 | 12 mm | 28,26 kg | R$ 424 | 0,55 mm | 2,7 |
| Inox 304 | 12 mm | 28,80 kg | R$ 1.008 | 0,58 mm | 1,1 |

**Conclusão:** Chapa única (sem reforço) exige espessura elevada — 15 mm em alumínio ou 10-12 mm em aço. A liga 5052-F tem FS ainda menor que 6061-T6 por chapa sozinha. Alternativa: reforço estrutural (seção caixão).

---

## 6. Análise de Reforços Estruturais

### 6.1 Opções avaliadas

| Opção | Conceito | Peso add. | Custo | Deflexão DJ 5× |
|-------|----------|:---------:|:-----:|:---------------:|
| Nervuras Al 3×50×6mm | Barras coladas sob a chapa | +1,5 kg | ~R$ 78 | 0,27 mm |
| Quadro tubular aço 30×30 | Moldura soldada | +6,2 kg | ~R$ 124 | 0,43 mm |
| Seção caixão 2 tubos Al | Chapas + tubos Al colados | +0,75 kg | ~R$ 50 | 0,18 mm |
| **Seção caixão 2 tubos aço** | **Chapas Al + tubos aço colados** | **+2,18 kg** | **~R$ 25** | **0,14 mm** |

:::info Evolução do projeto (Rev. 2.0)
O design original usava tubos de alumínio 35×35×2mm — a solução mais leve (+0,75 kg). Na prática, tubos quadrados de alumínio são difíceis de encontrar no mercado regional brasileiro. Tubos de aço são produto de prateleira em qualquer casa de ferro. A troca adiciona 1,4 kg mas **aumenta a rigidez em 23%** e **reduz o custo** (aço é mais barato que alumínio por metro).
:::

### 6.2 Solução adotada — Seção caixão (tubos de aço)

As duas chapas de alumínio 5052-F (superior 6,35 mm + inferior 3 mm) funcionam como flanges de uma viga-caixão, conectadas por **2 tubos quadrados de aço carbono 1020** colados com epóxi estrutural.

```
╔══════════════════════════╗  ← chapa superior Al 5052-F 6,35 mm (flange)
║    ┌────┐        ┌────┐  ║
║    │tubo│        │tubo│  ║  ← 2 tubos aço 1020 35×35×2 mm (alma)
║    │ 1  │        │ 2  │  ║
║    └────┘        └────┘  ║
╚══════════════════════════╝  ← chapa inferior Al 5052-F 3 mm (flange)
```

**Posição dos tubos (ref. chapa superior):**
- Tubo 1: Y = 194 mm (longitudinal, eixo X)
- Tubo 2: Y = 306 mm (longitudinal, eixo X)
- Comprimento: 527 mm (= largura da chapa inferior)
- Distância mínima às células: ~100 mm (sem interferência)

---

## 7. Cálculo da Seção Caixão

### 7.1 Método — Seção transformada

Como a seção caixão combina dois materiais (chapas de alumínio + tubos de aço), utilizamos o **método da seção transformada**: as áreas de aço são convertidas para áreas equivalentes de alumínio pela razão modular n = E_aço / E_al = 200.000 / 70.300 = **2,845**.

:::info Evolução do cálculo (Rev. 2.0)
Na Rev. 1.0 (seção toda em alumínio), o cálculo era direto com um único material. A seção transformada é necessária quando se misturam materiais — técnica padrão em estruturas compostas (ex: concreto armado, vigas mistas aço-madeira).
:::

### 7.2 Geometria da seção composta (transformada para alumínio)

Referência: base da chapa inferior (y = 0)
Altura total: 3 + 35 + 6,35 = **44,35 mm**

| Componente | Material | Área real (mm²) | n | Área transf. (mm²) | Centróide y (mm) |
|------------|----------|:---------------:|:---:|:-------------------:|:----------------:|
| Chapa inferior (300×3 mm) | Al 5052-F | 900 | 1,0 | 900 | 1,50 |
| Tubo 1 (35×35×2 mm) | Aço 1020 | 264 | 2,845 | 751 | 20,50 |
| Tubo 2 (35×35×2 mm) | Aço 1020 | 264 | 2,845 | 751 | 20,50 |
| Chapa superior (300×6,35 mm) | Al 5052-F | 1.905 | 1,0 | 1.905 | 41,18 |
| **Total** | — | **3.333** | — | **4.307** | — |

**Largura efetiva adotada:** 300 mm (conservador — plate effective width)

### 7.3 Centróide da seção transformada

$$\bar{y} = \frac{\sum A_{tr,i} \cdot y_i}{\sum A_{tr,i}} = \frac{900 \times 1,5 + 2 \times 751 \times 20,5 + 1905 \times 41,18}{4307} = \frac{110.584}{4.307} = 25,7 \text{ mm}$$

### 7.4 Momento de inércia transformado (Steiner)

| Componente | I_próprio transf. (mm⁴) | A_tr·d² (mm⁴) | I_total (mm⁴) |
|------------|:-----------------------:|:--------------:|:--------------:|
| Chapa inferior Al | 675 | 526.203 | 526.878 |
| Tubo 1 aço (×n) | 136.822 | 20.076 | 156.898 |
| Tubo 2 aço (×n) | 136.822 | 20.076 | 156.898 |
| Chapa superior Al | 6.401 | 458.267 | 464.668 |
| **TOTAL** | — | — | **1.305.342** |

**Comparação com Rev. 1.0:**

| Versão | I_total (mm⁴) | EI (×10⁹ N·mm²) | Ganho |
|--------|:-------------:|:----------------:|:-----:|
| Rev. 1.0 — toda Al, 6 mm | 1.062.162 | 73,2 | referência |
| **Rev. 2.0 — Al 5052-F 6,35 mm + aço** | **1.305.342** | **91,8** | **+25%** |

**Ganho de rigidez vs chapa sozinha:** I_caixão / I_chapa_6.35mm = 1.305.342 / 6.401×(300/300) ≈ **~150×**

### 7.5 Resultados — Seção caixão Rev. 2.0 (Al 5052-F + tubos aço)

| Cenário | P (N) | Deflexão (mm) | Tensão no Al (MPa) | FS (σ_y = 90 MPa) |
|---------|:-----:|:-------------:|:------------------:|:------------------:|
| 70 kg em pé | 687 | 0,017 | 1,7 | 53 |
| 85 kg em pé | 834 | 0,020 | 2,2 | 41 |
| 120 kg em pé | 1.177 | 0,029 | 3,1 | 29 |
| 85 kg CMJ 3× | 2.502 | 0,061 | 6,5 | 14 |
| 120 kg CMJ 3× | 3.532 | 0,086 | 9,2 | 9,8 |
| **120 kg DJ 5×** | **5.886** | **0,143** | **15,3** | **5,9** |
| 120 kg DJ 7× (extremo) | 8.240 | 0,200 | 21,4 | 4,2 |

:::info
Deflexão máxima < 0,2 mm em todos os cenários, incluindo DJ extremo. FS > 4 em todas as condições — mesmo com a liga 5052-F (σ_y = 90 MPa), a seção caixão garante ampla margem de segurança.
:::

**Comparação Rev. 1.0 → Rev. 2.0 (cenário crítico DJ 5×, 120 kg):**

| Parâmetro | Rev. 1.0 (Al 6061-T6, tubos Al) | Rev. 2.0 (Al 5052-F, tubos aço) |
|-----------|:-------------------------------:|:--------------------------------:|
| Deflexão | 0,180 mm | **0,143 mm** (−21%) |
| Tensão no Al | 17,5 MPa | **15,3 MPa** (−13%) |
| FS | 15,7 | **5,9** (σ_y menor) |
| Peso tubos | 0,75 kg | **2,18 kg** (+1,4 kg) |

### 7.6 Sensibilidade ao tamanho do tubo

| Tubo | I transf. (mm⁴) | Deflexão DJ 5× | Diferença |
|------|:----------------:|:--------------:|:---------:|
| Aço 35×35×2 mm | 1.305.342 | 0,143 mm | referência |
| Aço 30×30×2 mm | ~1.240.000 | ~0,150 mm | +5% |

Diferença desprezível — ambos os tamanhos atendem com folga. Preferir 35×35 se disponível.

---

## 8. Verificação da Colagem

### 8.1 Cisalhamento na interface tubo-chapa (aço→alumínio)

| Parâmetro | Valor |
|-----------|-------|
| Cortante máximo (V = P/2) | 2.943 N |
| Primeiro momento de área transformado (Q_top) | 29.537 mm³ |
| Fluxo cisalhante (q = VQ/I_tr) | 66,6 N/mm |
| Largura de colagem (2 tubos × 35 mm) | 70 mm |
| Tensão na cola (τ = q/b) | **0,95 MPa** |
| Resistência do epóxi estrutural | 20–30 MPa |
| **Fator de segurança colagem** | **> 21** |

:::note
A interface aço↔alumínio via epóxi é bem estabelecida na engenharia. O aço tem rugosidade natural que favorece a adesão mecânica. Preparação: lixar ambas as superfícies (lixa 80), desengordurar com álcool isopropílico, aplicar epóxi e curar 24h sob pressão de grampos.
:::

### 8.2 Especificação da cola

- Tipo: epóxi bicomponente estrutural (Araldite Professional, Loctite EA 9461 ou equivalente)
- Resistência ao cisalhamento: ≥ 20 MPa
- Preparação: lixar superfícies (lixa 80), desengordurar (álcool isopropílico)
- Cura: 24h sob pressão (grampos/sargentos)

---

## 8.3 Verificação de Bearing Stress nos Apoios

Verificação de esmagamento localizado nos pontos de contato entre as chapas, calços de aço e células de carga — modo de falha distinto da flexão global.

### 8.3.1 Caminho de carga

```
Pé do atleta
    ↓
Chapa superior Al 6 mm
    ↓ (contato face-a-face)
Calço de aço 56×32×2 mm
    ↓ (contato face-a-face)
Topo da célula de carga (boss M10)
    ↓
Corpo da célula DYX-301
    ↓
Calço inferior + chapa inferior
```

A carga vertical de compressão é transferida por **contato direto face-a-face** entre chapa→calço→célula. O parafuso M10 DIN 7991 **não carrega a força do salto** — apenas mantém o sanduíche unido e resiste a componentes laterais (GRF horizontal).

### 8.3.2 Tensão de esmagamento no alumínio (sob o calço)

| Parâmetro | Valor |
|-----------|-------|
| Força por célula (DJ 5×BW, 120 kg) | 1.472 N |
| Área do calço (56 × 32 mm) | 1.792 mm² |
| **Pressão de contato no Al** | **0,82 MPa** |
| Tensão de escoamento Al 5052-F (σ_y) | 90 MPa |
| Bearing yield Al 5052-F (~1,5× σ_y) | ~135 MPa |
| **Fator de segurança** | **165×** |

**Cenário extremo (DJ 7×BW, 120 kg):** 2.060 N/célula → 1,15 MPa → FS = 117×.

### 8.3.3 Função dos calços de aço

Os calços de aço 56×32×2 mm foram dimensionados especificamente para este modo de falha:

1. **Espalhamento de carga** — distribuem a força do boss da célula (~Ø25-30 mm, ~600 mm²) sobre 1.792 mm², reduzindo pressão 3×
2. **Proteção do alumínio** — interface aço↔alumínio evita marca/fluência ao longo de milhares de ciclos de salto
3. **Coplanaridade** — absorvem pequenas imperfeições de planicidade, evitando contato pontual

### 8.3.4 Cisalhamento lateral no parafuso (GRF horizontal)

| Parâmetro | Valor |
|-----------|-------|
| GRF horizontal (~10-15% vertical) | ~220 N/célula |
| Parafusos por célula | 2 |
| Cisalhamento por parafuso | 110 N |
| Capacidade M10 cl. 8.8 (A_s × 0,6 × σ_ut) | ~27.800 N |
| **Fator de segurança** | **> 250** |

### 8.3.5 Fadiga

Tensão cíclica no calço de aço: 0,82 MPa, muito abaixo do limite de fadiga do aço carbono (150-200 MPa) → **vida infinita** (> 10⁶ ciclos).

### 8.3.6 Critérios de aceitação (bearing)

| Critério | Limite | Resultado | Status |
|----------|:------:|:---------:|:------:|
| Pressão Al sob calço (DJ 5×) | < 100 MPa | 0,82 MPa | ✅ |
| FS esmagamento Al 5052-F (DJ 7×) | ≥ 3,0 | 165× | ✅ |
| FS cisalhamento parafuso | ≥ 3,0 | > 250 | ✅ |
| Fadiga calço (10⁶ ciclos) | < 150 MPa | 0,82 MPa | ✅ |

---

## 9. Critérios de Aceitação

| Critério | Limite | Resultado | Status |
|----------|:------:|:---------:|:------:|
| Deflexão máxima (DJ 5×BW) | < 0,5 mm | 0,14 mm | ✅ |
| Deflexão máxima (CMJ 3×BW) | < 0,2 mm | 0,06 mm | ✅ |
| Fator de segurança (DJ 5×) | ≥ 2,0 | 5,9 | ✅ |
| FS colagem (DJ 5×) | ≥ 3,0 | > 21 | ✅ |

---

## 10. Decisão de Projeto

### Problema
A chapa superior de 6 mm de alumínio sem reforço deflecte 12,7 mm sob carga de DJ (120 kg, 5×BW) — inaceitável para plataforma de força (precisão de medição).

### Alternativas avaliadas
1. Aumentar espessura (15 mm Al ou 10 mm aço) — pesado e/ou caro
2. Nervuras coladas — eficaz mas menos elegante
3. Quadro tubular de aço — bom mas pesado (+6 kg) e requer soldagem
4. **Seção caixão com tubos quadrados** — melhor relação custo-peso-rigidez

### Solução adotada (Rev. 2.0)
2 tubos quadrados de **aço carbono 1020** (35×35×2 mm) colados com epóxi estrutural entre as duas chapas de alumínio 5052-F, criando seção caixão com I_transformado = 1.305.342 mm⁴ (~150× a chapa sozinha).

:::info Evolução do design
Rev. 1.0: tubos de alumínio (I = 1.062.000 mm⁴, +0,75 kg, ~R$50).
Rev. 2.0: tubos de aço (I_tr = 1.305.000 mm⁴, +2,18 kg, ~R$25). Motivado pela disponibilidade local — tubos de alumínio são difíceis de encontrar no mercado regional, enquanto aço é produto de prateleira.
:::

### Impacto (Rev. 2.0)

| Parâmetro | Sem reforço | Com reforço Rev. 2.0 | Melhoria |
|-----------|:----------:|:--------------------:|:--------:|
| Deflexão DJ 5× | 10,52 mm | 0,14 mm | **75×** |
| FS estrutural (5052-F) | 0,1 | 5,9 | **59×** |
| Peso adicional | — | +2,18 kg | — |
| Custo adicional | — | ~R$ 25 | — |

---

## 11. Limitações do Modelo

1. **Modelo analítico** — série de Navier com fator de correção empírico (1,8×) para apoios pontuais. Para validação definitiva, recomenda-se FEA ou teste físico.
2. **Carga pontual** — o modelo assume carga concentrada no centro (pior caso). Na realidade, o pé do atleta distribui a carga em ~200-300 cm², reduzindo a deflexão real.
3. **Largura efetiva** — adotada 300 mm (conservador). A contribuição real das chapas pode ser maior.
4. **Colagem ideal** — assume transferência perfeita de cisalhamento pela cola. A preparação da superfície é crítica, especialmente na interface aço↔alumínio.
5. **Não considera efeitos dinâmicos** — cargas de impacto (DJ) são transientes e a inércia do sistema atenua picos.
6. **Corrosão galvânica** — o contato aço↔alumínio pode gerar corrosão galvânica em ambientes úmidos. Mitigação: a camada de epóxi entre as superfícies atua como isolante. Para uso em laboratório/academia indoor, risco desprezível.

---

## 12. Referências

- Timoshenko, S. P., Woinowsky-Krieger, S. (1959). *Theory of Plates and Shells*, 2nd Ed. McGraw-Hill.
- Young, W. C., Budynas, R. G. (2002). *Roark's Formulas for Stress and Strain*, 7th Ed. McGraw-Hill.
- Scripts de cálculo: `cad/structural_analysis.py`, `cad/material_comparison.py`, `cad/reinforcement_analysis.py`, `cad/box_section_analysis.py`

---

## 13. Histórico de Revisões

| Rev. | Data | Descrição |
|:----:|:----:|-----------|
| 1.0 | 2026-04-04 | Análise completa: chapa sem reforço, comparativo de materiais, solução seção caixão (Al 6061-T6, tubos Al) |
| 1.1 | 2026-04-04 | Adicionada Seção 8.3 — verificação de bearing stress nos apoios (chapa↔calço↔célula) |
| 2.0 | 2026-04-06 | Atualização de materiais por disponibilidade local: chapas Al 5052-F 6,35mm (substitui 6061-T6 6mm), tubos aço 1020 (substitui Al). Recálculo completo com seção transformada. Todos os critérios atendidos com folga (FS ≥ 4,2). |
