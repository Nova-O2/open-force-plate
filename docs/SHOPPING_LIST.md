---
title: Lista de Compras — Force Plate MVP
sidebar_position: 2
---

# Lista de Compras — Force Plate MVP

Componentes para plataforma de força única, uniaxial, 1000 Hz, USB-C + BLE.

:::info
Preços estimados em abril/2026. AliExpress tem os melhores preços mas leva 20-40 dias. Amazon BR é mais rápido mas mais caro.
:::

---

## Eletrônica — Núcleo

| # | Componente | Qtd | Preço unit. (est.) | Total (est.) | Onde comprar |
|---|-----------|-----|-------------------|-------------|--------------|
| 1 | **ADS1256 módulo** (24-bit ADC, 8 canais) | 1 | R$ 50-80 | R$ 50-80 | AliExpress: buscar "ADS1256 module" |
| 2 | **ESP32-S3-DevKitC-1** (N16R8 — 16MB flash, 8MB PSRAM) | 1 | R$ 35-60 | R$ 35-60 | AliExpress: buscar "ESP32-S3-DevKitC" |
| 3 | **Células de carga tipo F shear beam 500 kg** (com pézinho e cabo blindado) | 4 | R$ 30-60 | R$ 120-240 | AliExpress: buscar "F type shear beam load cell 500kg" |

**Subtotal eletrônica núcleo: R$ 205-380**

:::warning
Atenção ao comprar células de carga: escolher tipo F shear beam com pézinho integrado (foot bolt). Capacidade 500 kg por célula (2000 kg total — equivale ao VALD FDLite). Evitar as mais baratas sem certificado de calibração. Preferir vendedores com >95% de avaliação positiva e especificação de sensibilidade (normalmente 2.0 ± 0.1 mV/V).
:::

---

## Eletrônica — Alimentação

| # | Componente | Qtd | Preço unit. (est.) | Total (est.) | Onde comprar |
|---|-----------|-----|-------------------|-------------|--------------|
| 4 | **Bateria LiPo 3.7V 2000mAh** (conector JST) | 1 | R$ 25-40 | R$ 25-40 | AliExpress / Amazon BR |
| 5 | **TP4056 módulo carregador** (com proteção) | 1 | R$ 5-10 | R$ 5-10 | AliExpress |
| 6 | **Boost converter MT3608** (step-up 3.7V→5V, ajustável) | 1 | R$ 3-8 | R$ 3-8 | AliExpress: buscar "MT3608 step up module" |
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
| 14 | **Placa de alumínio 6061** (50×60 cm, 6 mm) — apenas topo | 1 | R$ 100-180 | R$ 100-180 | Metalúrgica local / Mercado Livre |
| 15 | **Parafusos M5 × 20 mm** (inox) + porcas + arruelas | 8+8+8 | R$ 0.50-1 | R$ 12-25 | Parafusaria / Mercado Livre |
| 16 | **Caixa/enclosure** para eletrônica (3D-print ou comprada) | 1 | R$ 20-40 | R$ 20-40 | Impressão 3D / AliExpress |

**Subtotal estrutura: R$ 112-215**

:::info
Com células F shear beam com pézinho, não é necessária placa inferior — os pés das células apoiam diretamente no piso. Requer superfície de piso rígida e plana.
:::

:::tip Estratégia dual
A chapa de 50×60 cm foi dimensionada para ser cortada ao meio na Fase 2, gerando 2 plataformas de 50×30 cm (dimensão próxima ao VALD FDLite: 48.5×30 cm). Basta adicionar +4 células de carga de 500 kg e um segundo ADS1256 (ou usar os 8 canais do mesmo ADS1256) para ter um sistema dual para assimetrias bilaterais.
:::

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
| Eletrônica núcleo | R$ 205 | R$ 380 |
| Alimentação | R$ 35 | R$ 60 |
| Acessórios | R$ 48 | R$ 85 |
| Estrutura mecânica | R$ 132 | R$ 245 |
| **TOTAL** | **R$ 420** | **R$ 770** |

:::info Alternativa para prototipagem
Para testar a eletrônica antes de investir em alumínio, usar 1 placa de MDF 18 mm (~R$ 30) como topo. Funciona para validar firmware/software, mas não para uso final (MDF absorve umidade e deforma).
:::

---

## Prioridade de Compra

**Pedido 1 — AliExpress (fazer agora, chega em 20-40 dias):**
- ADS1256 módulo
- ESP32-S3-DevKitC
- 4× células de carga tipo F shear beam 500 kg (com pézinho)
- TP4056 + bateria LiPo
- Conectores, jumpers, protoboard

**Pedido 2 — Local (enquanto espera o AliExpress):**
- 1× placa de alumínio 50×60 cm, 6 mm (apenas topo — cortável ao meio para dual 50×30)
- Parafusos M5
- MDF para protótipo (opcional)
- Ferramentas (se necessário)

---

## Alternativas de Componentes

### Célula de carga — opções

| Tipo | Capacidade | Preço | Observação |
|------|-----------|-------|-----------|
| **Tipo F shear beam com pézinho (recomendado)** | 500 kg | R$ 30-60 | Montagem simples, elimina placa inferior, padrão em balanças comerciais. 4×500=2000 kg (equiv. VALD FDLite) |
| Tipo S | 500 kg | R$ 35-70 | Precisa, mas requer 2 placas (superior + inferior) |
| Tipo barra (bar) | 500 kg | R$ 20-40 | Mais barata, menos precisa |
| Tipo botão (button) | 500 kg | R$ 50-100 | Compacta, boa para plataformas finas |

### ESP32 — variantes

| Variante | Preço | Recomendação |
|----------|-------|-------------|
| **ESP32-S3-DevKitC (N16R8)** | R$ 35-60 | **Melhor escolha** — BLE 5.0, mais memória |
| ESP32-DevKitC (original) | R$ 25-40 | Funciona, mas BLE 4.2 (menor throughput) |
| ESP32-C3 | R$ 20-30 | Single-core, pode ser limitante |

---

## Links AliExpress — Custo-Benefício (março/2026)

:::info
Links pesquisados em 28/03/2026. Preços podem variar. Sempre verificar avaliações do vendedor (>95%) e especificações antes de comprar.
:::

### Eletrônica — Núcleo

| # | Componente | Link | Preço aprox. | Observação |
|---|-----------|------|-------------|-----------|
| 1 | **ADS1256 módulo** | [ADS1256 24-bit ADC](https://www.aliexpress.com/item/32790159444.html) | ~US$ 13.55 | Melhor preço — verificar se é módulo completo |
| 1 | | [ADS1256 alternativa](https://www.aliexpress.com/item/1005001269602221.html) | ~US$ 17.50 | Vendedor com mais reviews |
| 2 | **ESP32-S3-DevKitC-1** | [ESP32-S3 N8/N16R8](https://www.aliexpress.com/item/1005003819366900.html) | ~US$ 22 | Múltiplas variantes — selecionar **N16R8** |
| 2 | | [ESP32-S3 Espressif oficial](https://www.aliexpress.com/item/1005003979778978.html) | ~US$ 22 | Loja oficial Espressif |
| 3 | **Células de carga F shear beam 500 kg** (×4) | Buscar "F type shear beam load cell 500kg foot" | ~US$ 18-25/un | Shear beam com pézinho — verificar sensibilidade 2.0 ± 0.1 mV/V |
| 3 | | Buscar "platform scale load cell 500kg foot" | ~US$ 20-30/un | Alternativa — célula de balança de plataforma com pé integrado |

### Eletrônica — Alimentação

| # | Componente | Link | Preço aprox. | Observação |
|---|-----------|------|-------------|-----------|
| 4 | **Bateria LiPo 3.7V 2000mAh** | [LiPo 505060 2000mAh](https://www.aliexpress.com/item/32985608127.html) | ~US$ 5 | Verificar conector JST |
| 4 | | [LiPo 103454 2000mAh](https://www.aliexpress.com/item/4001274116010.html) | ~US$ 4 | Alternativa |
| 5 | **TP4056 carregador** | [TP4056 kit 5pcs](https://www.aliexpress.com/item/32797834680.html) | ~US$ 0.93 | Kit 5 un., ótimo custo — preferir **Type-C** |
| 5 | | [TP4056 Type-C avulso](https://www.aliexpress.com/item/32467578996.html) | ~US$ 1 | Versão Type-C |
| 6 | **Boost converter MT3608** | Buscar "MT3608 step up boost converter module" | ~US$ 0.50-1.50 | Ajustar trimpot para 5.0V antes de usar |
| 7 | **Chave liga/desliga** | [SS12D00 kit 20pcs](https://www.aliexpress.com/item/4001207529493.html) | ~US$ 0.58 | Kit 20 un., vários tamanhos |

### Eletrônica — Acessórios

| # | Componente | Link | Preço aprox. | Observação |
|---|-----------|------|-------------|-----------|
| 8 | **Protoboard 830 pontos** | [MB-102 830pts](https://www.aliexpress.com/item/32526011079.html) | ~US$ 2.24 | Modelo padrão |
| 9 | **Jumper wires kit** | [Dupont M-M/M-F/F-F](https://www.aliexpress.com/item/32825558073.html) | ~US$ 0.57 | Kit básico, bom preço |
| 9 | | [Kit 310pcs completo](https://www.aliexpress.com/item/4001362869482.html) | ~US$ 2.06 | Kit mais completo com headers |
| 10 | **Conectores JST-XH 4 pinos** | [JST-XH 2.54mm 4pin c/ cabo](https://www.aliexpress.com/item/4000781846277.html) | ~US$ 1.50/par | 26AWG, 20 cm |
| 13 | **Kit resistores** | [600pcs 30 valores 1/4W 1%](https://www.aliexpress.com/item/1005003117726705.html) | ~US$ 3 | Suficiente para o projeto |
| 13 | | [2600pcs 130 valores](https://www.aliexpress.com/item/32865017857.html) | ~US$ 12 | Kit completo para lab |

### Dicas de Compra

1. **Células de carga** — item mais crítico. Escolher tipo F shear beam **500 kg** com pézinho integrado (foot bolt) — padrão em balanças comerciais. 4×500=2000 kg total. Exigir especificação de sensibilidade **2.0 ± 0.1 mV/V**
2. **ESP32-S3** — confirmar variante **N16R8** (16 MB flash + 8 MB PSRAM) na seleção do produto
3. **TP4056** — preferir versão **Type-C** em vez de Micro USB
4. **ADS1256** — confirmar que é módulo completo (placa + chip), não só o chip avulso
5. Adicionar tudo ao carrinho e aplicar **cupons do AliExpress** — normalmente há desconto em compras acima de US$ 20
