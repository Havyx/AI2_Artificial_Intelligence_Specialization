from flask import Flask, make_response, request, render_template

from processing import process_data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])

def file_summer_page():
    if request.method == "POST":
        input_file = request.files["input_file"]
        input_data = input_file.stream.read().decode("utf-8")
        output_data = process_data(input_data)
        response = make_response(output_data)
        response.headers["Content-Disposition"] = "attachment; filename=result.csv"
        return response

    return '''
        <html>
            <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" integrity="sha512-dTfge/zgoMYpP7QbHy4gWMEGsbsdZeCXz7irItjcC3sPUFtf0kuFbDz/ixG7ArTxmDjLXDmezHubeNikyKGVyQ==" crossorigin="anonymous">

            </head>
                <body>

                <nav class="navbar navbar-inverse">
                <div class="container">

                <div class="navbar-header">

                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="https://www.github.com/Havyx" ><img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/60436-22967c4ce89dbdbd4a8d49b090509a78-medium_jpg.jpg?buster=1517982458" width="25" heigh="25"></a>
                <a class="navbar-brand" href="#">HUB AI - Fiep SENAI</a>
                </div>
                </div>
                </nav>

            <div class="container">

            <div class="row">
                <h2>Desafio 03</h2>
                <h3>Integrantes: </h3>E. Sávio, Rafael, Lucas, Felipe<BR>
            </div>

            <div class="row">
                <h3>Descrição do problema: <H3>
                <h5><i><b>Greg</b> quer construir uma String <b>S</b>, de comprimento <b>N</b>. Começando com uma string vazia, ele pode executar operações:<br>
                Adicione um caractere ao final de <b> S </b> por <b> A</b> dólares.<BR>Copie qualquer substring de <b>S</b> e adicione-o ao final de por <b>B</b> dólares. <br><br> Calcule a quantidade mínima de dinheiro que Greg precisa construir. <br><br>Formato de entrada:<br> A primeira linha contém o número de casos de teste. As linhas subseqüentes descrevem um caso de teste em duas linhas: A primeira linha contém 3 números inteiros separados por espaço, N , A, e B, respectivamente. A segunda linha contém S (a string que Greg deseja construir).</i><h5>
            </div>



</div>

            <div class="container">

                <div>Selecione o arquivo <i>(.txt)</i> que se deseja calcular o valor para se construir a <i>string</i>: </div><br>

                <form method="post" action="." enctype="multipart/form-data">
                <div>
                    <p><input type="file" name="input_file" class="btn btn-success" /></p> </div>
                <div><p><input type="submit" value="Processar o arquivo" class="btn btn-primary" /></p></div>

                </form>
            </div>
            </div><!-- /.container -->

            </body>
        </html>
    '''

