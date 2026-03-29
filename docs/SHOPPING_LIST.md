---
title: Lista de Compras — Force Plate MVP
sidebar_position: 2
---

# Lista de Compras — Force Plate MVP

Componentes para plataforma de força única, uniaxial, 1000 Hz.

:::info
Preços estimados em março/2026. AliExpress tem os melhores preços mas leva 20-40 dias. Amazon BR é mais rápido mas mais caro.
:::

---

## Eletrônica — Núcleo

| # | Componente | Qtd | Preço unit. (est.) | Total (est.) | Onde comprar |
|---|-----------|-----|-------------------|-------------|--------------|
| 1 | **ADS1256 módulo** (24-bit ADC, 8 canais) | 1 | R$ 50-80 | R$ 50-80 | AliExpress: buscar "ADS1256 module" |
| 2 | **ESP32-S3-DevKitC-1** (N16R8 — 16MB flash, 8MB PSRAM) | 1 | R$ 35-60 | R$ 35-60 | AliExpress: buscar "ESP32-S3-DevKitC" |
| 3 | **Células de carga tipo S 200 kg** (com cabo blindado) | 4 | R$ 25-60 | R$ 100-240 | AliExpress: buscar "S type load cell 200kg" |

**Subtotal eletrônica núcleo: R$ 185-380**

:::warning
Atenção ao comprar células de carga: evitar as mais baratas sem certificado de calibração. Preferir vendedores com >95% de avaliação positiva e especificação de sensibilidade (normalmente 2.0 ± 0.1 mV/V).
:::

---

## Eletrônica — Alimentação

| # | Componente | Qtd | Preço unit. (est.) | Total (est.) | Onde comprar |
|---|-----------|-----|-------------------|-------------|--------------|
| 4 | **Bateria LiPo 3.7V 2000mAh** (conector JST) | 1 | R$ 25-40 | R$ 25-40 | AliExpress / Amazon BR |
| 5 | **TP4056 módulo carregador** (com proteção) | 1 | R$ 5-10 | R$ 5-10 | AliExpress |
| 6 | **Regulador de tensão 3.3V** (AMS1117-3.3) | 1 | R$ 3-5 | R$ 3-5 | AliExpress |
| 7 | **Chave liga/desliga** (slide switch) | 1 | R$ 2-5 | R$ 2-5 | AliExpress |

**Subtotal alimentação: R$ 35-60**

---

## Eletrônica — Acessórios

| # | Componente | Qtd | Preço unit. (est.) | Total (est.) | Onde comprar |
|---|-----------|-----|-------------------|-------------|--------------|
| 8 | **Protoboard 830 pontos** | 1 | R$ 10-15 | R$ 10-15 | AliExpress / Amazon BR |
| 9 | **Jumper wires** (kit M-M, M-F, F-F) | 1 kit | R$ 10-20 | R$ 10-20 | AliExpress |
| 10 | **Conectores JST-XH 4 pinos** (para células de carga) | 8 | R$ 1-2 | R$ 8-16 | AliExpress |
| 11 | **Cabo USB-C** (para programação + carga) | 1 | R$ 10-15 | R$ 10-15 | Amazon BR |
| 12 | **LED RGB** (indicador de status) | 2 | R$ 1-2 | R$ 2-4 | AliExpress |
| 13 | **Resistores sortidos** (kit) | 1 | R$ 8-15 | R$ 8-15 | AliExpress |

**Subtotal acessórios: R$ 48-85**

---

## Estrutura Mecânica

| # | Componente | Qtd | Preço unit. (est.) | Total (est.) | Onde comprar |
|---|-----------|-----|-------------------|-------------|--------------|
| 14 | **Placa de alumínio 6061** (60×40 cm, 6 mm) | 2 | R$ 80-150 | R$ 160-300 | Metalúrgica local / Mercado Livre |
| 15 | **Parafusos M5 × 20 mm** (inox) + porcas + arruelas | 16+16+16 | R$ 0.50-1 | R$ 25-50 | Parafusaria / Mercado Livre |
| 16 | **Espaçadores de alumínio** (M5, 10 mm) | 8 | R$ 2-5 | R$ 16-40 | Parafusaria |
| 17 | **Pés de borracha antiderrapante** | 4 | R$ 3-5 | R$ 12-20 | Amazon BR / ferragem |
| 18 | **Caixa/enclosure** para eletrônica (3D-print ou comprada) | 1 | R$ 20-40 | R$ 20-40 | Impressão 3D / AliExpress |

**Subtotal estrutura: R$ 233-450**

---

## Ferramentas Necessárias (se não tiver)

| Ferramenta | Necessidade | Preço (est.) |
|-----------|------------|-------------|
| Ferro de solda + estanho | Obrigatório | R$ 50-100 |
| Multímetro | Obrigatório | R$ 40-80 |
| Chaves Allen M5 | Obrigatório | R$ 15-25 |
| Furadeira + brocas metal | Para furar alumínio | R$ 100-200 (se não tiver) |

---

## Resumo de Custos

| Categoria | Mínimo | Máximo |
|-----------|--------|--------|
| Eletrônica núcleo | R$ 185 | R$ 380 |
| Alimentação | R$ 35 | R$ 60 |
| Acessórios | R$ 48 | R$ 85 |
| Estrutura mecânica | R$ 233 | R$ 450 |
| **TOTAL** | **R$ 501** | **R$ 975** |

:::info Alternativa para prototipagem
Para testar a eletrônica antes de investir em alumínio, usar 2 placas de MDF 18 mm (~R$ 30 cada). Funciona para validar firmware/software, mas não para uso final (MDF absorve umidade e deforma).
:::

---

## Prioridade de Compra

**Pedido 1 — AliExpress (fazer agora, chega em 20-40 dias):**
- ADS1256 módulo
- ESP32-S3-DevKitC
- 4× células de carga 200 kg tipo S
- TP4056 + bateria LiPo
- Conectores, jumpers, protoboard

**Pedido 2 — Local (enquanto espera o AliExpress):**
- 2× placas de alumínio 60×40 cm, 6 mm
- Parafusos, espaçadores, pés de borracha
- MDF para protótipo (opcional)
- Ferramentas (se necessário)

---

## Alternativas de Componentes

### Célula de carga — opções

| Tipo | Capacidade | Preço | Observação |
|------|-----------|-------|-----------|
| **Tipo S (recomendado)** | 200 kg | R$ 25-60 | Mais precisa, design robusto |
| Tipo barra (bar) | 200 kg | R$ 15-30 | Mais barata, menos precisa |
| Tipo botão (button) | 200 kg | R$ 40-80 | Compacta, boa para plataformas finas |
| Tipo disco (SparkFun TAL221) | 200 kg | R$ 80-120 | Boa qualidade, mais cara |

### ESP32 — variantes

| Variante | Preço | Recomendação |
|----------|-------|-------------|
| **ESP32-S3-DevKitC (N16R8)** | R$ 35-60 | **Melhor escolha** — BLE 5.0, mais memória |
| ESP32-DevKitC (original) | R$ 25-40 | Funciona, mas BLE 4.2 (menor throughput) |
| ESP32-C3 | R$ 20-30 | Single-core, pode ser limitante |
