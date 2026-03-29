---
title: Plano de Desenvolvimento — Force Plate MVP
sidebar_position: 1
---

# Plano de Desenvolvimento — Force Plate MVP

Plataforma única, uniaxial (Fz), 1000 Hz, BLE, com software de análise em Python.

---

## Fase 1: Hardware (Semanas 1-3)

### 1.1 Compra de Componentes

Ver [SHOPPING_LIST.md](./SHOPPING_LIST.md) para lista completa com links e preços.

### 1.2 Montagem Mecânica

- [ ] Cortar/adquirir 2 placas de alumínio 60×40 cm (superior + inferior)
- [ ] Fixar 4 células de carga nos cantos com parafusos M5
- [ ] Garantir espaçamento de ~10 mm entre placas (deformação das células)
- [ ] Adicionar pés de borracha antiderrapante na placa inferior
- [ ] Testar rigidez — a plataforma não pode fletir sob carga

**Nota sobre materiais:** alumínio 6061-T6 (6 mm espessura) é ideal. Alternativa mais barata: MDF 18 mm para prototipagem rápida (não para uso final).

### 1.3 Montagem Eletrônica

- [ ] Soldar/conectar 4 células de carga ao ADS1256
  - Cada célula: E+ (excitação), E- (GND), S+ (sinal+), S- (sinal-)
  - Configuração: 4 células em paralelo como ponte de Wheatstone completa
  - Alternativa: 4 canais individuais no ADS1256 (permite COP)
- [ ] Conectar ADS1256 ao ESP32-S3 via SPI
  - SCLK → GPIO 18
  - MOSI (DIN) → GPIO 23
  - MISO (DOUT) → GPIO 19
  - CS → GPIO 5
  - DRDY → GPIO 4
- [ ] Conectar bateria LiPo + módulo de carga TP4056
- [ ] Montar em protoboard primeiro, PCB depois

### 1.4 Diagrama de Ligação

```
Célula 1 (E+,E-,S+,S-)──┐
Célula 2 (E+,E-,S+,S-)──┼──► ADS1256 ──SPI──► ESP32-S3 ──BLE──► PC/App
Célula 3 (E+,E-,S+,S-)──┤     (24-bit)        (firmware)
Célula 4 (E+,E-,S+,S-)──┘     1000 Hz
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

### 2.3 Comunicação BLE

- [ ] Implementar BLE GATT server no ESP32
- [ ] Definir characteristics:
  - `force_data` (notify) — stream de dados em tempo real
  - `sample_rate` (read/write) — configurar taxa
  - `tare` (write) — zerar plataforma
  - `calibration` (read/write) — fator de calibração
  - `battery` (read) — nível de bateria
- [ ] Protocolo de pacotes: [timestamp_us(4B) | force_raw(4B) | force_N(4B)]
- [ ] Testar throughput BLE — 1000 Hz × 12 bytes = 12 KB/s (dentro do limite BLE)

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

## Fase 5: Produto (Futuro)

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
