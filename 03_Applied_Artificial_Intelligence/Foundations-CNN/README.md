# introducao-CNN

## Exercício:

* Abra a imagem figs/messi5.jpg
* recorte a bola
* copie em outra parte da imagem
* rotacione a imagem em 60 graus
* Altere o tamanho da imagem mantendo a proporção

## Exercício 2:

* Avalie o uso de filtros para eliminar ruídos e detectar contornos na imagem figs/11.jpg
* Utilize os padrões definidos em https://github.com/opencv/opencv/tree/master/data/haarcascades para criar dois classificadores, teste os classificadores com imagens aleatórias

## Exercício 3:

* Montar o ambiente para executar tensorflow com gpu (tensorflow-gpu)
* Executar código do mnist
* Fazer teste com uma rede treinada (VGG16)
* Utilizar a mesma topologia de rede neural usada para o problema minist, aplicando para o problema das abelhas
* Compare o tempo de treino da rede neural CNN usando CPUxGPU

## Exercício 4:
* Utilize o script Py-Torch-Basico.ipynb na rede neural CNN para utilizar outro dataset do Pytorch (Por Exemplo Fashion Mnist)
* Altere os dados de entrada da rede neural mlp desse script para fazer predição nos dados da Veltec
* Execute a rede neural CNN com as imagens de gatos e cachorros
  * Altere o dataloader de entrada
  * Altere o tamanho da saída da última camada de 1 para 10
