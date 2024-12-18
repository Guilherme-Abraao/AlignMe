# AlignMe

O propósito do sistema é monitorar a postura do usuário e notificá-lo quando houver variações posturais que possam causar dores nas costas, ombros, pescoço e outros. Desse modo, o sistema utiliza sensores para captar esses ângulos com maior precisão, esses dados são enviados para a camada de processamento e armazenamento dos dados, até que, por fim, sejam enviadas notificações ao usuário, através de um aplicativo móvel quando necessário. 


### 📚 Estrutura de Pastas

        Arquitetura/

            # Documento de descrição arquitetural e caso de usos
            # Diagrama da arquitetura geral do sistema 

        Implementacao/

            App/ 

                # Implementação do aplicativo móvel
                # README com dependências, instruções e como rodar o projeto 

            Arduino/ 
                
                # Implementação inserida no sensor para captar dados do acelerômetro e giroscópio
                # README com dependências, instruções e como rodar o projeto 
                # Diagrama da conexão do Hardware

            Gateway/

                # Implementação da comunicação via MQTT
                # README com dependências, instruções, observações e como rodar o projeto 

        Slides/

            # Apresentação do projeto AligMe

# 👥 Equipe

| Nome              | Função     | Usuário Git                                                                      |
|-------------------|------------|-------------------------------------------------------------------|
| Guilherme Abraão  | Arquiteto de software e desenvolvedor backend | [Guilherme-Abraao](https://github.com/Guilherme-Abraao)		 |
| Abraão    | Devops e desenvolvedor mobile				    | Link  |
| Luiz Felipe    | Arquiteto de software		    | Link	  	 |
| André   | ....				    | Link		 |

