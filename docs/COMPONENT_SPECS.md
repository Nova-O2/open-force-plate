---
title: Especificações Técnicas dos Componentes
sidebar_position: 2
---

# Especificações Técnicas — Force Plate MVP

Ficha de referência consolidada para todos os componentes do projeto. Specs originais dos fabricantes (preservar para calibração, validação e paper metodológico).

**Registro de compra:** ver [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md)
**Montagem e integração:** ver [DEVELOPMENT_PLAN.md](./DEVELOPMENT_PLAN.md)
**Análise estrutural:** ver [STRUCTURAL_ANALYSIS.md](./STRUCTURAL_ANALYSIS.md)

---

## 1. Eletrônica

### 1.1 Células de Carga — Decent DYX-301 500 kg (×4)

**Tipo:** F shear beam com pézinho (foot bolt). Material alloy steel.
**Capacidade:** 500 kg por célula → 2.000 kg (19.620 N) total com 4 unidades.

#### Specs metrológicos

| Parâmetro | Valor |
|-----------|-------|
| Output sensitivity | 2,0 ± 0,05 mV/V |
| Zero point output | ±1 % F.S. |
| Non-linearity | 0,03 % F.S. |
| Hysteresis | 0,03 % F.S. |
| Repeatability | 0,03 % F.S. |
| Creep (30 min) | 0,03 % F.S. |
| Temperature sensitivity drift | 0,03 % F.S. / 10°C |
| Zero temperature drift | 0,05 % F.S. / 10°C |
| Response frequency | 1 kHz |

#### Specs elétricos

| Parâmetro | Valor |
|-----------|-------|
| Impedance | 350 Ω |
| Insulation resistance | ≥ 5000 MΩ @ 100V DC |
| Working power | DC 5–15 V |
| Cable | Ø5 mm × 3 m blindado (4 fios: E+, E−, S+, S−) |

#### Specs mecânicos/ambientais

| Parâmetro | Valor |
|-----------|-------|
| Material | Alloy steel |
| Operating temperature | −20 a 80 °C |
| Safety overload | 150% R.C. (750 kg = 7.355 N) |
| Extreme overload | 200% R.C. (1.000 kg = 9.807 N) |

#### Dimensões (cota do fabricante)

| Cota | Valor | Descrição |
|:----:|:-----:|-----------|
| A | 30 mm | Comprimento total |
| B | 15 mm | Saída do cabo |
| C | 25 mm | Distância entre furos de fixação |
| D | 76 mm | Corpo total |
| E | 30 mm | Largura |
| W | 32 mm | Largura da base |
| H | 32 mm | Altura |
| M | M12 × 1,75 | Rosca do pézinho |
| 2-Ø | Ø13 mm | Diâmetro dos furos da célula |
| I | 56 mm | Comprimento da base (apoio) |

**Avaliação:** Specs de nível profissional. Não-linearidade/histerese de 0,03% superam requisito (<0,05%). Impedância 350 Ω é match perfeito para ADS1256. Tolerância da sensibilidade (±0,05 mV/V) é mais apertada que o padrão (±0,1).

---

### 1.2 ADC — Módulo ADS1256 24-bit (×2: 1 uso + 1 backup/dual)

**Chips integrados:**
- ADC: **ADS1256IDB** (Texas Instruments) — ultra-baixo consumo, alta precisão
- Referência de tensão: **ADR03** 2,5V (Analog Devices) — referência de precisão

| Parâmetro | Valor |
|-----------|-------|
| Resolução | 24 bits |
| Data output rate | até 30 ksps |
| Non-linearity | ±0,0010 % |
| Input modes | 8 single-ended ou 4 diferenciais |
| Analog input range | até 3 V |
| Communication | SPI |
| Operating voltage | 5 V |
| PGA | 1, 2, 4, 8, 16, 32, 64 |

#### Configuração planejada

- Modo: 4 canais diferenciais (1 por célula de carga)
- Taxa efetiva: 1000 Hz por canal (4 ksps multiplexado, dentro dos 30 ksps)
- PGA: 64 (range ±78 mV, ideal para sinal de ~10 mV das células)

**Avaliação:** Módulo com ADR03 na referência é diferencial — referência de precisão reduz ruído comparado a módulos genéricos. Non-linearity de ±0,0010% é 30× melhor que as células (0,03%), portanto o ADC nunca será o gargalo de precisão.

---

### 1.3 Microcontrolador — ESP32-S3-DevKitC-1 N16R8 (×2: 1 uso + 1 backup)

| Parâmetro | Valor |
|-----------|-------|
| Processador | Dual-core Xtensa LX7, 240 MHz (CoreMark: 1181,60 dual) |
| Flash | 16 MB |
| PSRAM | 8 MB |
| SRAM | 512 KB + 16 KB RTC |
| ROM | 384 KB |
| Bus | 128-bit data bus, SIMD support |
| WiFi | 802.11 b/g/n (2.4 GHz, até 150 Mbps) |
| Bluetooth | BLE 5.0 + Mesh (125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps) |
| USB | 1× full speed USB OTG (USB-C nativo) |
| GPIO | 45 |
| SPI | 4× SPI (+ Dual SPI, Quad SPI, Octal SPI, QPI, OPI) |
| I2C | 2× |
| UART | 3× |
| ADC interno | 2× 12-bit SAR, 20 canais (não usado — temos ADS1256 externo) |
| Sensor temp. interno | 1× |
| Timers | 4× 54-bit universal + 1× 52-bit system + 3× Watchdog |
| DMA | Universal (5 RX + 5 TX channels) |
| Alimentação | 5V via USB-C |

**Por que N16R8:** Memória de sobra para buffer de dados a 1000 Hz, firmware complexo e futuro (OTA updates, logging local, dual plate). Variante N8R2 funciona mas sem margem.

#### Conexões SPI (ADS1256 ↔ ESP32-S3)

| ADS1256 | ESP32 GPIO |
|---------|:----------:|
| SCLK | 18 |
| MOSI (DIN) | 23 |
| MISO (DOUT) | 19 |
| CS | 5 |
| DRDY | 4 |

**Verificado via spec sheet do vendedor (2026-04-01):** CPU, BLE e periféricos confirmados compatíveis com todos os requisitos do projeto.

---

### 1.4 Bateria — Pack Li-ion 1S2P 3,7V 5200 mAh (×2)

**Modelo:** Pack retangular Li-ion 1S2P (2× células 18650 em paralelo) com BMS integrada
**Fornecedor:** EPB Energia Portátil Brasil (loja oficial — ENERGIAPORTATILBRASIL, Mercado Livre)
**Compra:** 2026-04-04 — 2 unidades × R$ 26,71 = R$ 53,42
**Status:** aguardando chegada

| Parâmetro | Valor |
|-----------|-------|
| Tipo | Íon de lítio (Li-ion) |
| Arquitetura | 1S2P (2 células 18650 em paralelo) |
| Capacidade nominal | 5200 mAh |
| Capacidade por célula | 2600 mAh (18650 padrão) |
| Tensão nominal | 3,7 V |
| Tensão totalmente carregada | 4,2 V |
| Tensão de corte (BMS) | tipicamente 2,5–3,0 V |
| BMS integrada | Sim (proteção sobrecarga/descarga/curto-circuito) |
| Conector | JST-XH-2P (2,54 mm) — vermelho=+, preto=− |
| Dimensões | 36 × 19 × 65 mm (rectangular) |
| Peso | ~90 g |
| Energia | 19,24 Wh |
| **Densidade energética** | **432 Wh/L** ✅ realista |
| Garantia | 3 meses (vendedor) |

#### Verificação de honestidade das specs

| Check | Resultado |
|---|:---:|
| Densidade < 700 Wh/L (limite teórico Li-ion) | ✅ 432 Wh/L |
| Geometria consistente com 2× 18650 (36×18×65 mm esperado) | ✅ bate |
| Peso consistente com 2× 18650 (~90g esperado) | ✅ bate exato |
| Capacidade/célula coerente com mercado (2000–3500 mAh) | ✅ 2600 mAh típico |

**Autonomia estimada** (draw real ~215 mA @ 3,7V):
- Capacidade 5.200 mAh (rotulada) → **~24 h**
- Capacidade pessimista 4.000 mAh → ~18,6 h
- Meta do projeto: 3-4 h → **6-8× de folga**

#### Adaptação do conector

Pack sai com **JST-XH-2P (2,54 mm)**; TP4056 usa **JST-PH (2,0 mm)**. Duas opções:
1. Trocar conector: dessoldar JST-XH do pack, soldar JST-PH (kit PH 2.0mm já comprado no AliExpress, item #10)
2. Soldar fios direto nos pads B+/B− do TP4056 (mais robusto)

#### Histórico

- **01/04:** comprada bateria BGB Energy 3.7V rotulada 3000 mAh (Karina Mayumi, ML) — identificada overclaim de capacidade (densidade implícita 720 Wh/L, acima do limite teórico). Capacidade real estimada: 1.000-1.500 mAh.
- **04/04:** iniciada devolução BGB + compra de 2 packs EPB 1S2P 5200 mAh com specs honestas verificadas.

**Lesson learned:** para baterias Li-ion/LiPo, sempre calcular densidade energética antes de comprar (capacidade × tensão / volume). Pack com >400 Wh/L em LiPo pouch ou >700 Wh/L em Li-ion cilíndrica é muito provavelmente overclaim.

---

### 1.5 Carregador — TP4056 Type-C com proteção (×5 kit)

| Parâmetro | Valor |
|-----------|-------|
| Modelo | TP4056 com proteção contra descarga/sobrecorrente |
| Entrada | 5V via USB Type-C |
| Tensão de corte | 4,2V ± 1% |
| Corrente máxima de carga | 1000 mA |
| Proteção descarga | 2,5V |
| Proteção sobrecorrente | 3A |
| Dimensões | 2,6 × 1,7 cm |

**Conexão:** B+ e B− → bateria LiPo. OUT+ e OUT− → MT3608 boost (3,7V→5V) → ESP32 + ADS1256. USB Type-C → carregamento.
**LED:** Vermelho = carregando. Verde = completo.

---

### 1.6 Boost Converter — MT3608 Step-Up 3,7V→5V (×2)

| Parâmetro | Valor |
|-----------|-------|
| Modelo | MT3608 DC-DC Step-Up |
| Entrada | 2–24 V DC |
| Saída | 5–28 V DC (ajustável via trimpot) |
| Corrente máx. | 2 A |
| Eficiência | ~93% |
| Dimensões | ~36 × 17 × 14 mm |

**Função:** Converte 3,7V da bateria LiPo para 5V estáveis. Necessário porque ADS1256 (AVDD) exige 4,75–5,25 V e o regulador onboard do ESP32 DevKit precisa de ~4,5V mínimo de entrada.

:::danger ANTES DO PRIMEIRO USO
Girar o trimpot azul ~20 voltas no sentido anti-horário para iniciar com tensão de saída baixa. Conectar multímetro nos pinos VOUT+/VOUT− e girar lentamente no sentido horário até ler **5,0 V**. Só então conectar ao circuito. Saída alta pode danificar ESP32 ou ADS1256.
:::

---

### 1.7 Botão Liga/Desliga — 12 mm Metal LED (×1)

| Parâmetro | Valor |
|-----------|-------|
| Tipo | Push button metal, 12 mm |
| Modo | Fixed self-locking (latching — trava ligado/desligado) |
| Tensão LED | 3–9 V (compatível com 3,7–5V do circuito) |
| Material | Metal |
| LED | Integrado (acende quando ligado) |

**Função:** Interruptor geral da plataforma. Corta alimentação entre MT3608 e o restante do circuito.

---

## 2. Mecânica — Estrutura

### 2.1 Chapa superior — Alumínio 6061-T6

| Parâmetro | Valor |
|-----------|-------|
| Dimensões | 600 × 500 × 6 mm |
| Material | Al 6061-T6 |
| Cantos | R30 arredondados |
| Furos | 8× Ø11 mm, escareados Ø20 mm × 5,5 mm profundidade (90°) |
| Peso | ~4,86 kg |
| Desenho técnico | `cad/fab_chapa_superior.pdf` |

#### Propriedades do Al 6061-T6

| Propriedade | Valor |
|-------------|-------|
| Módulo de elasticidade (E) | 68.900 MPa |
| Tensão de escoamento (σ_y) | 276 MPa |
| Coeficiente de Poisson (ν) | 0,33 |
| Densidade (ρ) | 2.700 kg/m³ |

---

### 2.2 Chapa inferior — Alumínio 3 mm

| Parâmetro | Valor |
|-----------|-------|
| Dimensões | 527 × 396 × 3 mm |
| Material | Al (6061 ou 5052) |
| Cantos | Chanfrados 15 × 15 mm a 45° |
| Furos | 8× Ø11 mm |
| Peso | ~1,67 kg |
| Desenho técnico | `cad/fab_chapa_inferior.pdf` |

---

### 2.3 Juntas de aço (×4)

| Parâmetro | Valor |
|-----------|-------|
| Material | Aço carbono ou inox |
| Dimensões | 56 × 32 × 2 mm |
| Furos | 2× Ø11 mm, entre-centros 25 mm |
| Função | Espaçadora entre célula e chapa superior (distribui carga, evita esmagamento do Al) |
| Desenho técnico | `cad/fab_junta.pdf` |

**Nota:** não usar borracha — amortece o sinal dinâmico a 1000 Hz.

---

### 2.4 Pézinhos torneados com colar (×4) — peça única usinada

| Parte | Dimensão |
|-------|:--------:|
| Rosca | M12 × 1,75, Ø12 mm, 32 mm comprimento (= altura célula) |
| Colar | Ø20 mm, 5 mm altura (batente — encosta na célula) |
| Chanfro | Ø20 → Ø60 mm, 6 mm altura (~17°) |
| Base | Ø60 mm, 8 mm espessura |
| Borracha | Ø60 mm × 1 mm neoprene (colada após usinagem) |
| Altura total | 52 mm |
| Material | Aço carbono ou inox (barra Ø60 mm) |
| Desenho técnico | `cad/fab_pezinho.pdf` |

**Função:** Apoio/nivelamento. Sem contra-porca — colar funciona como batente mecânico, peso da plataforma trava a posição.

---

### 2.5 Reforço estrutural — Tubos quadrados (×2)

| Parâmetro | Valor |
|-----------|-------|
| Material | Alumínio extrudado |
| Seção | 30×30×2 mm ou 35×35×2 mm (conforme disponibilidade) |
| Comprimento | ~527 mm cada |
| Quantidade | 2 tubos |
| Posição | Longitudinal (eixo X), a Y=194 mm e Y=306 mm da chapa superior |
| Fixação | Cola epóxi estrutural |

**Função:** Cria seção caixão com as duas chapas (flanges). I_total = 1.062.162 mm⁴ (118× rigidez da chapa sozinha).

---

### 2.6 Parafusos — M10 × 50 DIN 7991 (×8)

| Parâmetro | Valor |
|-----------|-------|
| Norma | DIN 7991 (cabeça chata escareada Allen) |
| Dimensão | M10 × 50 mm |
| Classe | 8.8 (mínimo) |
| Cabeça | Ø20 mm (coincide com escareamento da chapa superior) |
| Acompanha | Porca M10 + arruela (×8 cada) |

---

### 2.7 Epóxi estrutural

| Parâmetro | Valor |
|-----------|-------|
| Tipo | Epóxi bicomponente estrutural |
| Marcas compatíveis | Araldite Professional, Loctite EA 9461 ou equivalente |
| Resistência ao cisalhamento | ≥ 20 MPa (tipicamente 20-30 MPa) |
| Cura | 24 h sob pressão (grampos/sargentos) |
| Preparação | Lixar superfícies (lixa 80), desengordurar (álcool isopropílico) |

---

## 3. Sistema Completo — Resolução Teórica

```
4× DYX-301 500 kg = 2000 kg total = 19.620 N full scale
Sensibilidade: 2,0 mV/V × 5V = 10 mV full scale por célula
ADS1256 PGA=64: range ±78 mV
Effective bits at 1000 Hz: ~17-18 bits

Por canal (500 kg / 4.905 N):
  17 eff bits: 4.905 / 131.072 = 0,037 N
  18 eff bits: 4.905 / 262.144 = 0,019 N

Combinado (2000 kg / 19.620 N):
  17 eff bits: ~0,15 N
  18 eff bits: ~0,075 N
```

**Comparativo VALD FDLite:** ~0,15 N → **igualamos ou superamos**.

---

## 4. Arquitetura de Alimentação

```
                          ┌──► ESP32 DevKit (5V pin → onboard reg → 3.3V)
USB-C 5V ──► TP4056 ──┐  │
              │        ├──┤
         Bateria 3.7V ─┘  │
              │            └──► ADS1256 (AVDD 5V)
              ▼
         MT3608 (3.7V→5V) ──► mesmo barramento 5V
                                    │
                               [Botão on/off] ──► barramento
```

- **Modo USB-C (primário):** 5V direto do USB alimenta tudo. MT3608 inativo.
- **Modo bateria (BLE):** MT3608 converte 3,7V→5V. Tudo funciona sem cabo.

---

## 5. Ferramentas e Acessórios de Prototipagem

### Solda e medição

| Item | Spec |
|------|------|
| Ferro de solda | Exbom 60W, ajustável, 5 pontas, com suporte |
| Estanho | 60/40 (Sn/Pb) com fluxo interno, 0,8 mm, 80 g |
| Multímetro | Kit multímetro + caneta tensão + alicate amperímetro |
| Temperatura de solda | 300–350 °C para componentes eletrônicos |

### Prototipagem

| Item | Spec |
|------|------|
| Protoboard | 830 pontos |
| Jumper wires | Dupont 20 cm, flexible, 24 AWG cobre, M-M/M-F/F-F |
| Conectores | XH 2,54 mm, 4 pinos, 20 cm, F5 + M5 |
| Kit resistores | 1/4 W 1%, valores sortidos (300 pcs) |

---

## 6. Histórico de Revisões

| Rev. | Data | Descrição |
|:----:|:----:|-----------|
| 1.0 | 2026-04-04 | Consolidação inicial de todos os specs — recuperação do git (commit 3f66aa7^) + integração de dimensões mecânicas do DEVELOPMENT_PLAN e propriedades estruturais do STRUCTURAL_ANALYSIS |
