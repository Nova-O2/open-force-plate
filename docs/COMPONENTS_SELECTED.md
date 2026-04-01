# Componentes Selecionados — Force Plate MVP

Data de compra: 2026-04-01
Fornecedor: AliExpress
Valor total estimado: R$ 830,54 (com descontos, frete grátis)

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
| Processador | Dual-core Xtensa LX7, 240 MHz |
| Flash | 16 MB |
| PSRAM | 8 MB |
| WiFi | 802.11 b/g/n |
| Bluetooth | BLE 5.0 |
| USB | USB-C nativo (CDC) |
| GPIO | 45 |
| SPI | 4 interfaces |
| Alimentação | 5V via USB-C |

**Por que N16R8:** Memória de sobra para buffer de dados a 1000 Hz, firmware complexo, e futuro (OTA updates, logging local, dual plate). Variante N8R2 funciona mas sem margem.

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
