---
title: Plano de Desenvolvimento — Force Plate MVP
sidebar_position: 1
---

# Plano de Desenvolvimento — Force Plate MVP

Plataforma única, uniaxial (Fz), 1000 Hz, USB-C + BLE, com software de análise em Python.

---

## Fase 1: Hardware (Semanas 1-3)

### 1.1 Compra de Componentes

Ver [COMPONENTS_SELECTED.md](./COMPONENTS_SELECTED.md) para registro completo das compras (itens, lojas, valores).

### 1.2 Montagem Mecânica

#### Placa superior — 600 × 500 mm, alumínio 6061-T6, 6mm, cantos arredondados R30

- [ ] Adquirir na metalúrgica local (com cantos arredondados R30)
- [ ] Marcar posição dos 8 furos conforme tabela de coordenadas (ver abaixo)
- [ ] Furar 8 furos de **Ø11 mm** (passagem M10)
- [ ] Escarear furos a 90° para **Ø20 mm** (DIN 7991 M10, profundidade ~5,5 mm)
- [ ] Rebarbar furos com lima metal

#### Placa inferior — 527 × 396 mm, alumínio 3mm, cantos chanfrados 15×15 a 45°

Peça única que cobre os furos de fixação das 4 células. Não toca o chão — fica suspensa entre as células e as porcas. Os pézinhos ficam fora da área da placa inferior. Cantos chanfrados para garantir que não obstruam a rosca da célula.

- [ ] Adquirir na metalúrgica local (junto com a superior, com chanfro 15×15 nos 4 cantos)
- [ ] Furar 8 furos de **Ø11 mm** nas mesmas posições relativas da placa superior
- [ ] A placa inferior é centralizada sob a superior

:::tip Estratégia dual (Fase 5)
A placa superior (50×60 cm) foi dimensionada para corte ao meio → 2 placas de 50×30 cm (dimensão similar ao VALD FDLite: 48.5×30 cm). Os furos da Fase 1 já estão no ângulo correto (~62°) para o layout final da Fase 2.
:::

#### Célula de carga — Dimensões (Decent DYX-301 500 kg)

Faixa 300kg–1000kg–2ton da tabela do fabricante:

| Cota | Dimensão | Descrição |
|:----:|:--------:|-----------|
| A | 30 mm | Comprimento total |
| B | 15 mm | Saída do cabo |
| C | **25 mm** | **Distância entre furos de fixação** |
| D | 76 mm | Corpo total |
| E | 30 mm | Largura |
| W | 32 mm | Largura base |
| H | 32 mm | Altura |
| M | **M12 × 1.75** | **Rosca do pézinho** |
| 2-Ø | **Ø13 mm** | **Diâmetro dos furos da célula** (furos nas chapas: Ø11 mm para M10) |
| I | 56 mm | Comprimento da base (apoio) |

#### Juntas de aço (4 unidades — 1 por célula)

Espaçadora entre a célula e a placa superior. Tamanho exato da base da célula.

| Parâmetro | Valor |
|-----------|-------|
| Material | Aço carbono ou inox |
| Espessura | 2 mm |
| Dimensões | **56 × 32 mm** (= base da célula, cotas I × W) |
| Furos | 2× Ø11 mm, espaçados 25 mm entre centros |

**Função:** Distribuir carga e evitar que a célula cave o alumínio (aço > alumínio em dureza). Não usar borracha — amortece o sinal a 1000 Hz.

#### Fixação — Montagem por célula

```
Parafuso Allen M10×45 DIN 7991 (cabeça chata escareada)
        ↓
[Placa SUPERIOR — alumínio 6mm, 600×500mm, R30]  ← furo Ø11mm escareado Ø20 (5,5mm prof.)
        ↓
[Junta — aço 2mm, 56×32mm]                       ← furo Ø11mm
        ↓
[Célula DYX-301 — a ~62°]                        ← furo Ø13mm (da célula)
        ↓
[Placa INFERIOR — alumínio 3mm, 527×396mm]       ← furo Ø11mm
        ↓
Porca M10 + arruela
        ↓
[Pézinho M12×1.75 com colar]  ← rosca na célula, fora da placa inferior, apoia no chão
```

**Parafusos necessários:** 8× M10×45 DIN 7991 + 8× porcas M10 + 8× arruelas (2 por célula)

#### Layout das células — ~62° (ângulo da diagonal Fase 2)

Células orientadas na diagonal da meia-placa (300×500mm), com pé no canto e cabo para o centro. Angulação já posicionada para Fase 2 (corte ao meio).

```
    ←──────────── 600 mm ────────────→
    ┌────────────────┬────────────────┐ ↑
    │  pé            │           pé   │ │
    │    ╲C1         │        C2╱     │ │
    │      ╲         │        ╱       │ │
    │                │                │ 500mm
    │      ╱         │        ╲       │ │
    │    ╱C3         │        C4╲     │ │
    │  pé            │           pé   │ │
    └────────────────┴────────────────┘ ↓
                   CORTE
```

#### Coordenadas dos furos (origem: canto inferior esquerdo)

| Célula | Ponto | X (mm) | Y (mm) |
|:------:|:-----:|:------:|:------:|
| C1 | Pé | 40.0 | 460.0 |
| C1 | Furo 1 | 56.7 | 428.1 |
| C1 | Furo 2 | 68.3 | 406.0 |
| C2 | Pé | 560.0 | 460.0 |
| C2 | Furo 1 | 543.3 | 428.1 |
| C2 | Furo 2 | 531.7 | 406.0 |
| C3 | Pé | 40.0 | 40.0 |
| C3 | Furo 1 | 56.7 | 71.9 |
| C3 | Furo 2 | 68.3 | 94.0 |
| C4 | Pé | 560.0 | 40.0 |
| C4 | Furo 1 | 543.3 | 71.9 |
| C4 | Furo 2 | 531.7 | 94.0 |

Todos os furos nas chapas: **Ø11 mm** (passagem M10). Na placa superior: escareados a 90° para Ø20 mm (DIN 7991). Mesmas posições relativas na placa inferior.

**Desenhos de fabricação:** regenerar via `python3 cad/fabrication_drawings.py` → 5 PDFs em `cad/` (chapas, pézinho, junta, montagem)

#### Pézinho torneado com colar (×4) — Peça única usinada

| Parte | Dimensão |
|-------|:--------:|
| Rosca | M12×1.75, Ø12mm, **32mm** comprimento (= altura célula) |
| Colar | **Ø20mm, 5mm** altura (batente — encosta na célula) |
| Chanfro | Ø20→Ø60, 6mm altura (~17°) |
| Base | Ø60mm, **8mm** espessura |
| Borracha | Ø60mm, 1mm neoprene (colada após usinagem) |
| Material | Aço carbono ou inox (barra Ø60mm) |
| Altura total | **52mm** (rosca + colar + chanfro + base + borracha) |

**Sem contra-porca.** O colar funciona como batente mecânico — impede que o pé rosqueie além da altura da célula e reforça a transição rosca/chanfro. Altura ajustada por rosqueamento. Peso da plataforma trava.

**Fabricação:** encomendar em torneiro mecânico. Desenho: `cad/fab_pezinho.pdf`

#### Checklist de montagem mecânica

- [ ] Adquirir placa superior alumínio 6061-T6, 600×500 mm, 6 mm, cantos R30
- [ ] Adquirir placa inferior alumínio, 527×396 mm, 3 mm, cantos chanfrados 15×15
- [ ] Adquirir/fabricar 4 juntas de aço 56×32 mm, 2 mm (2× Ø11, 25mm entre centros)
- [ ] Encomendar 4 pézinhos torneados com colar (ver specs acima + `cad/fab_pezinho.pdf`)
- [ ] Adquirir parafusos Allen M10×45 DIN 7991 (cabeça chata) + porcas M10 + arruelas (8+8+8)
- [ ] Adquirir broca Ø11 mm + escareador 90° para M10 (Ø20)
- [ ] Cortar/adquirir 4 discos borracha Ø60mm × 1mm (neoprene)
- [ ] Furar 8 furos Ø11 mm nas placas (2 por canto, espaçamento 25 mm)
- [ ] Escarear os 8 furos da placa superior (Ø20, 90°, profundidade 5,5 mm)
- [ ] Rebarbar furos
- [ ] Colar borracha nos pézinhos
- [ ] Montar: parafuso DIN 7991 → placa superior (escareado) → junta → célula → placa inferior → porca M10 + arruela
- [ ] Rosquear pézinhos nas células (até o colar encostar)
- [ ] Apoiar no piso rígido e plano
- [ ] Nivelar (ajustar pézinhos por rosqueamento) — usar nível de bolha
- [ ] Testar rigidez — plataforma não pode fletir sob carga

#### Reforço estrutural — Seção caixão (2 tubos quadrados)

A chapa superior de 6mm sozinha deflecte ~21mm sob carga de DJ (120kg, 5×BW) — inaceitável para plataforma de força. A solução é criar uma **seção caixão**: as duas chapas (superior e inferior) funcionam como flanges de uma viga, conectadas por 2 tubos quadrados de alumínio colados com epóxi estrutural.

| Parâmetro | Valor |
|-----------|-------|
| Tubo | Alumínio quadrado 30×30 ou 35×35×2mm (conforme disponibilidade) |
| Quantidade | 2 tubos, ~527mm cada (comprimento da chapa inferior) |
| Posição | Longitudinal (eixo X), a Y=194mm e Y=306mm da chapa superior |
| Fixação | Cola epóxi estrutural (Araldite Professional ou equivalente) |
| Calços | Se tubo < gap entre chapas, usar calços de alumínio para igualar altura |

**Resultado:** I aumenta de 9.000 mm⁴ (chapa sozinha) para ~1.060.000 mm⁴ (118× mais rígido). Deflexão cai de 21mm para **<0.2mm** em todos os cenários.

```
Vista em corte (seção caixão):
╔══════════════════════════╗  ← chapa superior 6mm (flange)
║    ┌────┐        ┌────┐  ║
║    │tubo│        │tubo│  ║  ← 2 tubos colados (alma)
║    │ 1  │        │ 2  │  ║     ~35mm altura
║    └────┘        └────┘  ║
╚══════════════════════════╝  ← chapa inferior 3mm (flange)
```

**Montagem dos tubos:**

- [ ] Montar um canto (1 célula + parafusos + chapas) para medir o gap real entre chapas
- [ ] Adquirir 2 tubos quadrados de alumínio (~527mm cada). Tamanho ideal: gap medido ±1mm
- [ ] Se tubo menor que gap: fabricar calços (chapas finas de alumínio cortadas a 35×527mm)
- [ ] Lixar faces de colagem (lixa 80, superfícies foscas)
- [ ] Desengordurar com álcool isopropílico
- [ ] Aplicar epóxi estrutural nas 4 faces de colagem (topo e base de cada tubo)
- [ ] Posicionar tubos a Y=194mm e Y=306mm (ref. chapa superior), paralelos ao eixo longo
- [ ] Prensar com grampos/sargentos por 24h (cura do epóxi)
- [ ] Verificar alinhamento e planicidade após cura

:::info Análise estrutural completa
Scripts de cálculo em `cad/structural_analysis.py`, `cad/material_comparison.py`, `cad/reinforcement_analysis.py` e `cad/box_section_analysis.py`. Deflexão e tensão verificadas para cenários até DJ 7×BW (120kg), com FS > 10 em todos os casos.
:::

:::warning
Piso rígido e plano obrigatório. Superfícies irregulares, carpetes ou pisos flexíveis comprometem a leitura. Em caso de piso inadequado, usar base de MDF ou compensado como apoio nivelador.
:::

### 1.3 Montagem Eletrônica

#### Arquitetura de alimentação

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

**Modo USB-C (primário):** 5V direto do USB alimenta tudo. MT3608 inativo.
**Modo bateria (BLE):** MT3608 converte 3.7V→5V. Tudo funciona sem cabo.

**⚠️ MT3608 — ANTES DO PRIMEIRO USO:** Girar o trimpot azul ~20 voltas no sentido anti-horário para iniciar com tensão baixa. Conectar multímetro em VOUT+/VOUT- e girar lentamente no sentido horário até ler **5.0V**. Só então conectar ao circuito. Saída alta pode danificar ESP32 ou ADS1256.

#### Diagrama de sinal

```
Célula 1 (E+,E-,S+,S-)──┐                                    ┌──► BLE ──► PC/App
Célula 2 (E+,E-,S+,S-)──┼──► ADS1256 ──SPI──► ESP32-S3 ──────┤
Célula 3 (E+,E-,S+,S-)──┤     (24-bit)        (firmware)      └──► USB-C ──► PC/App
Célula 4 (E+,E-,S+,S-)──┘     1000 Hz
```

**Configuração:** 4 canais diferenciais (1 por célula). PGA=64 (range ±78 mV).

#### Conexões SPI (ADS1256 → ESP32-S3)

| ADS1256 | ESP32 GPIO |
|---------|:----------:|
| SCLK | 18 |
| MOSI (DIN) | 23 |
| MISO (DOUT) | 19 |
| CS | 5 |
| DRDY | 4 |

#### Checklist de montagem eletrônica

- [ ] Montar circuito de alimentação no protoboard (TP4056 → MT3608 → barramento 5V)
- [ ] Ajustar MT3608 para 5.0V (multímetro!)
- [ ] Conectar botão on/off entre MT3608 e barramento
- [ ] Conectar ESP32-S3 ao protoboard (5V pin + GND)
- [ ] Conectar ADS1256 ao protoboard (AVDD 5V + GND)
- [ ] Ligar ADS1256 ao ESP32-S3 via SPI (5 fios — ver tabela acima)
- [ ] Soldar/conectar 4 células de carga ao ADS1256 (E+, E-, S+, S- por célula)
- [ ] Conectar bateria LiPo ao TP4056 (B+, B-, ignorar fio NTC)
- [ ] Conectar LEDs indicadores (status, alimentação)
- [ ] Testar alimentação em ambos os modos (USB-C e bateria)
- [ ] Validar leitura de todas as 4 células (valor bruto no serial monitor)

### 1.4 Resolução Teórica do Sistema

```
4× DYX-301 500 kg = 2000 kg total = 19.620 N full scale
Sensibilidade: 2.0 mV/V × 5V = 10 mV full scale por célula
ADS1256 PGA=64: range ±78 mV
Effective bits at 1000 Hz: ~17-18 bits

Por canal (500 kg / 4.905 N):
  17 eff bits: 4.905 / 131.072 = 0.037 N
  18 eff bits: 4.905 / 262.144 = 0.019 N

Combinado (2000 kg / 19.620 N):
  17 eff bits: ~0.15 N
  18 eff bits: ~0.075 N

Comparativo VALD FDLite: ~0.15 N → igualamos ou superamos
```

---

## Fase 2: Firmware (Semanas 2-4)

### 2.1 Setup do Ambiente

- [ ] Instalar PlatformIO (VS Code ou CLI)
- [ ] Criar projeto ESP32-S3 com framework Arduino
- [ ] Adicionar biblioteca ADS1256 (ou implementar driver SPI)

### 2.2 Aquisição de Dados

- [ ] Implementar leitura contínua do ADS1256 a 1000 Hz
- [ ] Validar taxa real com osciloscópio ou contador de amostras
- [ ] Implementar buffer circular para suavizar jitter
- [ ] Adicionar timestamp (microssegundos) a cada amostra

### 2.3 Comunicação USB-C + BLE

- [ ] Implementar USB CDC (serial) no ESP32-S3 via USB-C nativo
  - Modo primário: USB-C para máxima confiabilidade e throughput
  - Protocolo serial: mesmos pacotes que BLE
- [ ] Implementar BLE GATT server no ESP32
  - Modo secundário: BLE para uso sem fio (portabilidade)
- [ ] Definir characteristics (BLE) / comandos (USB):
  - `force_data` (notify/stream) — stream de dados em tempo real
  - `sample_rate` (read/write) — configurar taxa
  - `tare` (write) — zerar plataforma
  - `calibration` (read/write) — fator de calibração
  - `battery` (read) — nível de bateria
- [ ] Protocolo de pacotes: [timestamp_us(4B) | force_raw(4B) | force_N(4B)]
- [ ] Detecção automática: se USB-C conectado → usa USB; senão → BLE
- [ ] Testar throughput BLE — 1000 Hz × 12 bytes = 12 KB/s (dentro do limite BLE)
- [ ] Testar throughput USB-C — sem limitação prática a 1000 Hz

### 2.4 Calibração

- [ ] Implementar rotina de tare (zero com plataforma vazia)
- [ ] Implementar calibração com peso conhecido:
  1. Plataforma vazia → registrar zero
  2. Peso conhecido (ex: 20 kg) → registrar leitura
  3. Calcular fator: `force_N = (raw - zero) × (peso_kg × 9.81) / (raw_peso - zero)`
- [ ] Salvar calibração na EEPROM/NVS do ESP32
- [ ] Implementar multi-point calibration (0, 20, 40, 60, 80 kg) para linearidade

---

## Fase 3: Software — App Python (Semanas 3-6)

### 3.1 Aquisição via BLE

- [ ] Usar `bleak` (Python) para conectar ao ESP32
- [ ] Implementar recepção de stream BLE em thread separada
- [ ] Buffer de dados com timestamps
- [ ] Logging em CSV: `timestamp_us, force_raw, force_N`

### 3.2 Visualização em Tempo Real

- [ ] Dashboard com `matplotlib` ou `pyqtgraph` (mais rápido):
  - Gráfico força × tempo (rolling window)
  - Força atual (N e kg)
  - Indicador de pico
  - Status de conexão BLE
- [ ] Alternativa web: Streamlit ou FastAPI + WebSocket + Chart.js

### 3.3 Análise de Saltos

Usar/adaptar o pacote `force-plate-jump-analyses` ou implementar:

- [ ] **Detecção automática de fases:**
  1. Quieto (quiet standing)
  2. Fase excêntrica (unweighting)
  3. Fase concêntrica (propulsão)
  4. Voo (flight)
  5. Aterrissagem (landing)

- [ ] **Métricas CMJ/SJ:**
  - Jump height (impulso-momento e tempo de voo)
  - Peak force (N e N/kg)
  - Rate of force development (RFD) — pico e média
  - Net impulse (N·s)
  - Time to peak force (ms)
  - Mean power (W e W/kg)
  - Velocidade de decolagem (m/s)

- [ ] **Métricas DJ:**
  - RSI (reactive strength index) = jump height / contact time
  - RSI modificado = jump height / total contraction time
  - Contact time (ms)
  - Flight time (ms)

- [ ] **Relatório automático:**
  - Gerar PDF/HTML com gráficos e métricas
  - Comparação com normativas (se disponíveis)
  - Histórico do atleta

### 3.4 Exportação de Dados

- [ ] CSV com dados brutos (timestamp, force_N)
- [ ] JSON com métricas calculadas
- [ ] Formato compatível com Pyomeca/c3d (opcional)

---

## Fase 4: Validação (Semanas 5-8)

### 4.1 Validação Técnica

- [ ] Verificar linearidade com pesos conhecidos (0-100 kg em incrementos de 10 kg)
- [ ] Verificar drift temporal (medir 10 min contínuos com peso fixo)
- [ ] Verificar taxa de amostragem real (contar amostras em janela de tempo)
- [ ] Verificar ruído (desvio padrão em repouso)
- [ ] Teste de histerese (carga/descarga)

### 4.2 Validação Científica (paper)

- [ ] Protocolo: N ≥ 20 participantes
- [ ] Comparar com plataforma comercial (Kistler, AMTI, ou similar disponível)
- [ ] Testes: CMJ, SJ, DJ em ambas as plataformas (ordem randomizada)
- [ ] Análise: ICC, Bland-Altman, CV%, SEM
- [ ] Alvo: ICC ≥ 0.95, CV% < 5%

---

## Fase 5: Dual Force Plate (Futuro)

- [ ] Cortar chapa 50×60 cm ao meio → 2 placas de 50×30 cm (dimensão similar ao VALD FDLite: 48.5×30 cm)
- [ ] Adicionar +4 células de carga F shear beam 500 kg
- [ ] Expandir leitura: usar os 8 canais do ADS1256 (4+4) ou adicionar segundo ADS1256
- [ ] Adaptar firmware para 2 plataformas independentes (força L + força R)
- [ ] Implementar métricas de assimetria bilateral no software

## Fase 6: Produto (Futuro)

- [ ] Design de PCB customizada (substituir protoboard)
- [ ] Enclosure 3D-printed ou injetado
- [ ] App mobile (Flutter/React Native)
- [ ] Documentação para reprodução (open-source hardware)
- [ ] Página no site Nova O2

---

## Decisões de Arquitetura

### Por que ESP32-S3 e não Teensy 4.1?

| Critério | ESP32-S3 | Teensy 4.1 |
|----------|----------|------------|
| Custo | R$ 30-50 | R$ 150-200 |
| WiFi/BLE integrado | ✅ | ❌ (precisa de módulo extra) |
| Performance SPI | Suficiente para 1000 Hz | Melhor (600 MHz) |
| Ecossistema Arduino | ✅ | ✅ |
| Disponibilidade BR | Fácil (AliExpress) | Difícil |

Para plataforma única a 1000 Hz, o ESP32-S3 é mais que suficiente.

### Por que células F shear beam e não tipo S?

| Critério | F shear beam (com pézinho) | Tipo S |
|----------|---------------------------|--------|
| Montagem | Simples — pé no chão, placa em cima | Requer 2 placas (superior + inferior) |
| Peso total | ~7 kg (1 placa 50×60) | ~13 kg (2 placas) |
| Custo | Menor (~R$ 120-200 a menos) | Maior (segunda placa + espaçadores + pés) |
| Uso comercial | Padrão em balanças de plataforma | Comum em sistemas de tração/compressão |
| Precisão | Equivalente para aplicação uniaxial | Equivalente |
| Requisito extra | Piso rígido e plano | Nenhum (placa inferior nivela) |

A célula F shear beam com pézinho é o padrão da indústria de balanças de plataforma. Simplifica a montagem, reduz custo e peso, e é comprovada em milhões de dispositivos comerciais. A única desvantagem é a dependência de um piso adequado, facilmente contornável.

### Por que ADS1256 e não HX711?

- HX711: máximo 80 Hz — **insuficiente** para análise de saltos
- ADS1256: até 30.000 Hz, 24-bit — padrão em force plates de pesquisa

### Configuração das células de carga

**Opção A — Bridge único (4 em paralelo):**
- Mais simples, 1 canal no ADC
- Dá apenas força total vertical
- Suficiente para MVP

**Opção B — 4 canais independentes:**
- Cada célula em canal separado do ADS1256
- Permite calcular COP (Center of Pressure) via momentos
- Mais complexo, mas mais informação
- **Recomendado** — o ADS1256 tem 8 canais, usar 4 não adiciona custo

**Decisão: Opção B** — ler 4 canais independentes (250 Hz cada no modo multiplexado, ou 1000 Hz com configuração adequada).

---

## Referências Técnicas

- [ADS1256 Datasheet](https://www.ti.com/lit/ds/symlink/ads1256.pdf)
- [ESP32-S3 Technical Reference](https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf)
- [can-can-group/forceplate-hardware-code](https://github.com/can-can-group/forceplate-hardware-code)
- [force-plate-jump-analyses (Python)](https://github.com/stevenhirsch/force-plate-jump-analyses)
