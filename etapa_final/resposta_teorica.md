# Projeto Integrado Final: Controle de Temperatura de uma Estufa Industrial

## 1. Proposta do Sistema
O sistema escolhido para a modelagem e controle é uma **Estufa Industrial de Aquecimento**. Este é um sistema térmico clássico de primeira ordem, amplamente utilizado na indústria para secagem de materiais, cura de polímeros e esterilização. O objetivo do projeto é manter a temperatura interna da estufa no *setpoint* desejado, rejeitando perturbações externas (como a abertura da porta).

## 2. Escolha do Microcontrolador e Arquitetura
Para a implementação física deste sistema, a arquitetura escolhida baseia-se no microcontrolador **ESP32**. 

* **Justificativa da Escolha:** O ESP32 possui processamento de núcleo duplo de 240 MHz (suficiente para rodar o algoritmo PID em tempo real), conversores A/D de 12 bits, geradores de sinal PWM em hardware e conectividade Wi-Fi nativa. O Wi-Fi permite que o ESP32 atue como um nó de Internet das Coisas (IoT), enviando os dados de temperatura para um sistema Supervisório (SCADA) via protocolo MQTT.
* **Atuador:** Relé de Estado Sólido (SSR) controlado via sinal PWM do ESP32 para modular a potência de uma resistência elétrica de aquecimento.
* **Sensor:** Termopar tipo K acoplado a um módulo MAX6675 (comunicação SPI), garantindo leitura precisa em altas temperaturas.

## 3. Diagrama de Blocos do Sistema

O diagrama abaixo ilustra a arquitetura da malha de controle fechada implementada no microcontrolador:

```mermaid
graph LR
    R(Setpoint <br/> Temperatura Desejada) -->|+| E((Erro))
    E --> C[Controlador PID <br/> Algoritmo no ESP32]
    C -->|Sinal de Controle <br/> PWM| A[Atuador <br/> Relé SSR + Resistência]
    A --> P[Planta <br/> Estufa Térmica]
    P -->|Temperatura Atual| S[Sensor <br/> Termopar MAX6675]
    S -->|-| E