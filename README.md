O QUE BAIXAR

Necessário baixar python e bibliotecas compatíveis de c++ para o ambiente rodar.

O QUE USAR
1 Extrair Frames do Vídeo

Execute o script de extração de frames. Ele cria uma pasta com imagens retiradas do vídeo na mesma criada, capturando um frame a cada intervalo de segundos definido.
2 Reconhecer e Filtrar o Fundo
Coloque na pasta de referência as imagens que representam o fundo que você quer identificar. Depois, execute o script de reconhecimento de fundo.

As imagens que forem consideradas semelhantes ao fundo serão copiadas para uma nova pasta para análise posterior.
3 Reconhecer e Contar Rostos

Execute o script de reconhecimento de rostos na pasta onde estão as imagens filtradas com o fundo correto.
O sistema vai identificar rostos únicos e contar quantas vezes cada um aparece nas imagens.

📂 Estrutura Recomendada de Pastas
Pasta com o vídeo original.
Pasta onde serão salvos os frames extraídos.
Pasta com imagens de fundo de referência.
Pasta final com os frames validados (com fundo correto) para análise dos rostos.
