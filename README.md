# chicago_bikeshare
 Utilizando Python para explorar dados relacionados aos sistemas de compartilhamento de bicicletas nas três maiores cidades dos Estados Unidos: Chicago, Nova Iorque e Washington. Importando dados e respondendo a algumas perguntas sobre a base de dados. Utilizando computação de estatísticas descritivas.
 
## Dados sobre compartilhamento de bicicletas
Na última década, os sistemas de compartilhamento de bicicletas têm crescido em número e popularidade nas cidades de todo o mundo. Sistemas de compartilhamento de bicicletas permitem que os usuários aluguem bicicletas por um período curtíssimo, por um preço específico. Isso permite que pessoas retirem uma bicicleta do ponto A e a devolvam no ponto B, embora também possam devolvê-la no mesmo local, caso queiram apenas sair para um passeio. Independentemente disso, cada bicicleta pode servir vários usuários por dia.

Graças à ascensão das tecnologias de informação, é fácil para um usuário acessar uma estação dentro do sistema para desbloquear ou devolver as bicicletas. Essas tecnologias também fornecem uma riqueza de dados que podem ser utilizados para explorar como esses sistemas de compartilhamento de bicicletas são usados.

Neste projeto, foram utilizados dados fornecidos pelo Motivate, um provedor de sistema de bicicletas compartilhadas para diversas grandes cidades dos Estados Unidos, para descobrir os padrões de uso do compartilhamento de bicicletas. Foram analisados o uso do sistema de uma das maiores cidades dos Estados Unidos: Chicago.

## Os conjuntos de dados
Os dados para os primeiros seis meses de 2017 são fornecidos. O arquivo de dados contêm seis (6) colunas principais:

- Horário de início (ex., 2017-01-01 00:07:57)
- Horário de término (ex., 2017-01-01 00:20:53)
- Duração da viagem (em segundos, ex., 776)
- Estação inicial (ex., Broadway & Barry Avenue)
- Estação final (ex., Sedgwick St & do North Ave)
- Tipo de usuário (assinante ou cliente)
- Gênero do usuário
- Ano de nascimento do usuário

## Observação
Os arquivos originais tinham mais colunas, e elas diferiam em formato em muitos casos. Alguns processos de data wrangling foram realizados para condensar esses arquivos nas seis colunas principais citadas acima, para simplificar sua análise e a avaliação em Python. 
