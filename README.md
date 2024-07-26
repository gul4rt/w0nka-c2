# Wonka C2

![usage](https://github.com/user-attachments/assets/3266b876-cd59-4d19-b565-627305e5de69)

W0nka é uma estrutura de comando e controle (C2) criada para fins didáticos. Por meio do uso de sockets, o servidor envia comandos para um agente, que por sua vez os executa e retorna a saída dos mesmos.

![server-client](https://github.com/user-attachments/assets/69aa4412-d03c-46f3-92ec-441501e0b897)

Sinta-se a vontade para abrir uma issue ou até mesmo enviar um pull-request ;)

Referencias:

https://docs.python.org/3/howto/sockets.html

https://attack.mitre.org/tactics/TA0011/

Futuras atualizações:

\- Uso de criptografia assimétrica durante a comunicação (gerando as chaves no processo de compilação do binário)

\- Múltiplas sessões

## Requisitos:

\- Python3

\- Build-essential

## Compilação:

Para compilar o agente malicioso use a seguinte linha de comando:

cd ./agent && make agent

## Modo de uso:

./agent 

python3 server.py

### Comandos básicos:

O W0nka possui 4 comandos básicos:

\- Help: exibe o menu de ajuda

\- Start: liga o servidor, que por sua vez fica aguardando a conexão do agente para o envio de comandos

\- Show: mostra o atual setup do C2, como: chaves de criptográfia, ip do alvo, ip local, porta local, etc... \*Em desenvolvimento =)\*

\- Exit: sai do programa (pode ser substituido pelo atalho: ctrl+c)


