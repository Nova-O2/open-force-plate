# Componentes Selecionados — Force Plate MVP

Data de compra: 2026-04-01
Prazo estimado AliExpress: 20-40 dias (chegada ~21/04–11/05)

## Resumo de Compras

### AliExpress — Comprado 2026-04-01

| # | Item | Loja | Qtd | Unit. (R$) | Total (R$) |
|---|------|------|:---:|:----------:|:----------:|
| 1 | Células de carga Decent DYX-301 500kg | DECENT Load Cell | 4 | 208.99 | 835.96 |
| 2 | Módulo ADS1256 24-bit (ADS1256IDB + ADR03) | Shop1105006670 | 2 | 48.29 | 96.58 |
| 3 | ESP32-S3-DevKitC-1 N16R8 (com pin headers) | Gangda Tong | 2 | 38.19 | 76.38 |
| 4 | TP4056 Type-C com proteção (kit 5) | Shop1105163493 | 1 | 10.10 | 10.10 |
| 5 | MT3608 boost converter (regular) | TianShiKai | 2 | 10.89 | 21.78 |
| 6 | Botão 12mm metal self-locking LED 3-9V | TechEss Electric | 1 | 11.89 | 11.89 |
| 7 | Protoboard 830pts (kit 3) | Aokin Wholesale | 1 | 21.44 | 21.44 |
| 8 | Jumper wires Dupont 20cm flexible 24AWG cobre | CHANZON Official | 1 | 38.59 | 38.59 |
| 9 | Conectores XH 2.54mm 4pin 20cm (F5+M5) | Electrical Wire | 1 | 26.60 | 26.60 |
| 10 | Conectores PH 2.0mm (bateria→TP4056) | Electrical Wire | 1 | 36.69 | 36.69 |
| 11 | Kit resistores 1/4W 1% | — | 1 | — | **FALTA ADICIONAR** |
| | | | | **Subtotal** | **~R$ 1.176** |
| | | | | **Impostos est.** | **~R$ 870** |
| | | | | **Total est.** | **~R$ 2.046** |

### Mercado Livre — Comprado 2026-04-01

| # | Item | Qtd | Total est. (R$) |
|---|------|:---:|:---------------:|
| 1 | Bateria LiPo 3.7V 3000mAh 505080 (3 fios) | 1 | ~35 |
| 2 | Ferro de solda Exbom 60W ajustável + 5 pontas + suporte | 1 | ~70 |
| 3 | Estanho 60/40 com fluxo 0.8mm 80g | 1 | ~20 |
| | | **Subtotal** | **~R$ 125** |

### Comprar local (quando AliExpress chegar)

| # | Item | Qtd | Total est. (R$) |
|---|------|:---:|:---------------:|
| 1 | Placa alumínio 6061 50×60cm 6mm | 1 | ~150 |
| 2 | Parafusos M5×20mm inox + porcas + arruelas (8+8+8) | 1 | ~25 |
| | | **Subtotal** | **~R$ 175** |

### Custo Total do Protótipo

| Fonte | Valor est. (R$) |
|-------|:---------------:|
| AliExpress (produtos + impostos) | ~2.046 |
| Mercado Livre | ~125 |
| Local (alumínio + parafusos) | ~175 |
| **TOTAL PROTÓTIPO** | **~R$ 2.346** |

:::info
Valor unitário de célula de carga (R$ 209) é o maior custo. Para dual plate (Fase 2), adicionar +4 células + 1 ADS1256 ≈ +R$ 900.
:::

---

## Célula de Carga — Decent DYX-301 500 kg (×4)

**Tipo:** F shear beam com pézinho (foot bolt)
**Capacidade:** 500 kg por célula (2000 kg total com 4 unidades)

| Spec | Valor |
|------|-------|
| Output sensitivity | 2.0 ± 0.05 mV/V |
| Zero point output | ±1 %F.S. |
| Non-linearity | 0.03 %F.S. |
| Hysteresis | 0.03 %F.S. |
| Repeatability | 0.03 %F.S. |
| Creep (30 min) | 0.03 %F.S. |
| Temperature sensitivity drift | 0.03 %F.S./10°C |
| Zero temperature drift | 0.05 %F.S./10°C |
| Response frequency | 1 kHz |
| Material | Alloy steel |
| Impedance | 350 Ω |
| Insulation resistance | ≥5000 MΩ/100V DC |
| Working power | DC 5-15V |
| Operating temperature | -20 to 80°C |
| Safety overload | 150% R.C. (750 kg) |
| Extreme overload | 200% R.C. (1000 kg) |
| Cable | Ø5mm × 3m (blindado) |

**Avaliação:** Specs de nível profissional. Não-linearidade e histerese de 0.03% superam o requisito (<0.05%). Impedância 350 Ω é match perfeito para ADS1256. Sensibilidade 2.0 ± 0.05 mV/V tem tolerância mais apertada que o padrão (±0.1).

---

## ADC — Módulo ADS1256 24-bit 8 canais (×2: 1 uso + 1 backup/dual)

**Chips integrados:**
- ADC: **ADS1256IDB** (Texas Instruments) — ultra-baixo consumo, alta precisão
- Referência de tensão: **ADR03** 2.5V (Analog Devices) — referência de precisão

| Spec | Valor |
|------|-------|
| Resolução | 24 bits |
| Data output rate | até 30 ksps |
| Non-linearity | ±0.0010% |
| Input modes | 8 single-ended ou 4 diferenciais |
| Analog input range | até 3V |
| Communication | SPI |
| Operating voltage | 5V |
| PGA | 1, 2, 4, 8, 16, 32, 64 |

**Configuração planejada:**
- Modo: 4 canais diferenciais (1 por célula de carga)
- Taxa efetiva: 1000 Hz por canal (4 ksps multiplexado, dentro dos 30 ksps)
- PGA: 64 (range ±78 mV, ideal para sinal de ~10 mV das células)

**Avaliação:** Módulo com ADR03 na referência é diferencial — referência de precisão reduz ruído comparado a módulos genéricos. Non-linearity de ±0.0010% é 30× melhor que as células (0.03%), então o ADC nunca será o gargalo de precisão.

---

## Microcontrolador — ESP32-S3-DevKitC-1 N16R8 (×2: 1 uso + 1 backup)

| Spec | Valor |
|------|-------|
| Processador | Dual-core Xtensa LX7, 240 MHz (CoreMark: 1181.60 dual) |
| Flash | 16 MB |
| PSRAM | 8 MB |
| SRAM | 512 KB + 16 KB RTC |
| ROM | 384 KB |
| Bus | 128-bit data bus, SIMD support |
| WiFi | 802.11 b/g/n (2.4 GHz, up to 150 Mbps) |
| Bluetooth | BLE 5.0 + Mesh (125 Kbps, 500 Kbps, 1 Mbps, 2 Mbps) |
| USB | 1× full speed USB OTG (USB-C nativo) |
| GPIO | 45 |
| SPI | 4× SPI (+ Dual SPI, Quad SPI, Octal SPI, QPI, OPI) |
| I2C | 2× |
| UART | 3× |
| ADC interno | 2× 12-bit SAR, 20 canais (não usado — temos ADS1256 externo) |
| Sensor temp. | 1× interno |
| Timers | 4× 54-bit universal + 1× 52-bit system + 3× Watchdog |
| DMA | Universal (5 RX + 5 TX channels) |
| Alimentação | 5V via USB-C |

**Por que N16R8:** Memória de sobra para buffer de dados a 1000 Hz, firmware complexo, e futuro (OTA updates, logging local, dual plate). Variante N8R2 funciona mas sem margem.

**Verificado via spec sheet do vendedor (2026-04-01):** CPU, BLE e periféricos confirmados compatíveis com todos os requisitos do projeto.

---

## Bateria — LiPo 3.7V 3000mAh (×1)

| Spec | Valor |
|------|-------|
| Tipo | Polímero de lítio (LiPo) |
| Código | 505080 |
| Tensão | 3.7V nominal |
| Capacidade | 3000 mAh |
| Dimensões | 5 × 50 × 80 mm |
| Fios | 3 (positivo, negativo, NTC/termistor) |
| Autonomia estimada | ~3-4h de uso contínuo a 1000 Hz |
| Carregamento | Via TP4056 Type-C |
| Fornecedor | Mercado Livre (Brasil) |

**Nota:** 3º fio é NTC (termistor) — usar apenas + e - no TP4056. NTC pode ser conectado ao ESP32 para monitoramento de temperatura da bateria (futuro).

---

## Carregador — TP4056 Type-C com proteção (×5 kit, usar 1)

| Spec | Valor |
|------|-------|
| Modelo | TP4056 com proteção contra descarga/sobrecorrente |
| Entrada | 5V via USB Type-C |
| Tensão de corte | 4.2V ± 1% |
| Corrente máxima de carga | 1000 mA |
| Proteção descarga | 2.5V |
| Proteção sobrecorrente | 3A |
| Dimensões | 2.6 × 1.7 cm |
| Quantidade | Kit 5 unidades (1 uso + 4 spare) |
| Fornecedor | AliExpress |

**Conexão:** B+ e B- → bateria LiPo. OUT+ e OUT- → MT3608 boost (3.7V→5V) → ESP32 + ADS1256. USB Type-C → carregamento.
**LED:** Vermelho = carregando. Verde = completo.

---

## Boost Converter — MT3608 Step-Up 3.7V→5V (×1)

| Spec | Valor |
|------|-------|
| Modelo | MT3608 DC-DC Step-Up |
| Entrada | 2-24V DC |
| Saída | 5-28V DC (ajustável via trimpot) |
| Corrente máx. | 2A |
| Eficiência | ~93% |
| Dimensões | ~36 × 17 × 14 mm |
| Fornecedor | AliExpress |

**Função:** Converte 3.7V da bateria LiPo para 5V estáveis. Necessário porque ADS1256 (AVDD) exige 4.75-5.25V e o regulador onboard do ESP32 DevKit precisa de ~4.5V mínimo de entrada.

**Configuração:** Ajustar trimpot para saída de **5.0V** antes de conectar ao circuito. Medir com multímetro.

**Arquitetura de alimentação:**
```
                          ┌──► ESP32 DevKit (5V pin → onboard reg → 3.3V)
USB-C 5V ──► TP4056 ──┐  │
              │        ├──┤
         Bateria 3.7V ─┘  │
              │            └──► ADS1256 (AVDD 5V)
              ▼
         MT3608 (3.7V→5V) ──► mesmo barramento 5V
```

**Modo USB-C:** 5V direto do USB alimenta tudo. MT3608 inativo (entrada > saída).
**Modo bateria (BLE):** MT3608 converte 3.7V→5V. Tudo funciona sem cabo.

**⚠️ ANTES DO PRIMEIRO USO:** Girar o trimpot azul ~20 voltas no sentido anti-horário para iniciar com tensão de saída baixa. Depois, conectar multímetro nos pinos VOUT+/VOUT- e girar lentamente no sentido horário até ler **5.0V**. Só então conectar ao circuito. Se não fizer isso, a saída pode estar em tensão alta e danificar o ESP32 ou ADS1256.

---

## Botão Liga/Desliga — 12mm Metal LED (×1)

| Spec | Valor |
|------|-------|
| Tipo | Push button metal, 12mm |
| Modo | Fixed self-locking (latching — trava ligado/desligado) |
| Tensão LED | 3-9V (compatível com 3.7-5V do circuito) |
| Material | Metal |
| LED | Integrado (acende quando ligado) |
| Fornecedor | AliExpress |

**Função:** Interruptor geral da plataforma. Corta alimentação entre TP4056/MT3608 e o restante do circuito.
**Posição no circuito:** Entre saída do MT3608 (5V) e o barramento de alimentação (ESP32 + ADS1256).

---

## Resolução Teórica do Sistema Completo

```
4× DYX-301 500 kg = 2000 kg total = 19,620 N full scale
Sensibilidade: 2.0 mV/V × 5V = 10 mV full scale por célula
ADS1256 PGA=64: range ±78 mV
Effective bits at 1000 Hz: ~17-18 bits

Por canal (500 kg / 4,905 N):
  17 eff bits: 4,905 / 131,072 = 0.037 N
  18 eff bits: 4,905 / 262,144 = 0.019 N

Combinado (2000 kg / 19,620 N):
  17 eff bits: ~0.15 N
  18 eff bits: ~0.075 N

Comparativo VALD FDLite: ~0.15 N
→ Igualamos ou superamos a resolução VALD
```

---

## Ferramentas — Solda e Medição

| Item | Spec | Fornecedor |
|------|------|-----------|
| Ferro de solda | Exbom 60W, ajustável, 5 pontas, com suporte | Mercado Livre |
| Estanho | 60/40 (Sn/Pb) com fluxo interno, 0.8mm, 80g | Mercado Livre |
| Multímetro | Existente (mede tensão DC) | Já possui |

**Temperatura de solda:** 300-350°C para componentes eletrônicos.

---

## Acessórios de Prototipagem

| Item | Spec | Fornecedor |
|------|------|-----------|
| Protoboard | 830 pontos, kit 3 unidades | AliExpress |
| Jumper wires | Dupont 20cm, flexible, 24AWG cobre, M-M/M-F/F-F | AliExpress |
| Conectores | XH 2.54mm, 4 pinos, 20cm, Female 5 + Male 5 | AliExpress |
| Kit resistores | 1/4W 1%, valores sortidos | AliExpress |
