# Estado do projeto

**Atualizado:** 2026-11-11 · **Versão:** `v3.1.0-rc1` · **Fase:** 1 (hardware), eletrônica

Fonte única do estado atual. O histórico dia a dia fica no [`PROJECT_LOG.md`](./PROJECT_LOG.md); as mudanças por versão, no [`CHANGELOG.md`](../CHANGELOG.md).

## Onde estamos

- **Mecânica pronta** desde 2026-06-08: estrutura colada (chapas Al 5052-F + seção caixão inox 304), 4 cantos montados, calços de 2 mm. Montada sem torquímetro.
- **Retomado em 2026-11-10**, depois de cinco meses parado. Os componentes eletrônicos estão todos em mãos desde abril.
- **Revisão pré-eletrônica (2026-11-10):** a pinagem dos documentos era do ESP32 clássico e foi refeita para o ESP32-S3 (#5).
- **S1 concluído em 2026-11-11:** barramento a 5,01 V pela bateria (MT3608) e 4,99 V pelo USB, estáveis, medidos **sem carga**. Bancada montada na protoboard; detalhes e cores dos fios no [`PROJECT_LOG.md`](./PROJECT_LOG.md). O botão veio sem trava e ficou de fora (#10).
- **Firmware do S2 pronto para a bancada** (PR #9, aberto até o teste no hardware).

## Próximos passos (milestone `v3.1.0`)

| Etapa | Issue | O que fecha |
|---|---|---|
| ~~S1: bancada de alimentação~~ ✅ 2026-11-11 | #1 | 5,0 V estáveis no barramento, por USB e por bateria (uma fonte de cada vez) |
| S2: SPI ESP32-S3 ↔ ADS1256 | #2 | Barramento conferido sob carga (ESP32 ligado) + leitura de registradores + 1 célula respondendo a carga |
| Botão com trava | #10 | Botão de trava entre a bateria e o MT3608; não bloqueia S2–S4 |
| S3: 4 canais a 1000 Hz | #3 | Taxa real medida, ruído em repouso medido nos dois modos de alimentação |
| S4: pré-checagem + 1ª calibração | #4 | Erro < 0,5% com cargas conhecidas → tag `v3.1.0` |

## Riscos e pendências em aberto

- **Taxa de amostragem (S3):** 4 canais × 1000 Hz cabem no ADS1256 só na taxa mais ruidosa. Se a resolução medida não segurar, plano B: caixa de junção somando as 4 células num canal só ([`DEVELOPMENT_PLAN.md`](./DEVELOPMENT_PLAN.md) §1.3).
- **Caminho de alimentação:** USB e MT3608 não podem alimentar o barramento ao mesmo tempo. A ligação definitiva (diodos ou chave) fica para a Fase 6.
- **Nível lógico do módulo ADS1256:** medir o DVDD antes de ligar o SPI.
- **Alimentação sob carga:** o S1 mediu o barramento sem carga. Repetir com o ESP32-S3 ligado no início do S2.
- **Cores dos fios fora do padrão na bancada:** o VOUT+ do MT3608 é marrom (marcado com fita) e o IN− da TP4056 também. Conferir pela placa antes de mexer nos trilhos.
- **Bancada parada:** sem botão, o MT3608 drena o pack. Tirar o OUT+ da TP4056 do trilho ao terminar.
- **Referência de carga para o S4:** pesos que somem 80 kg, conferidos numa balança confiável, ainda a definir.
- **Torque não verificado:** reaperto instrumentado opcional antes do S4.
