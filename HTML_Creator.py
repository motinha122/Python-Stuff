import os

projectName = input("Digite o nome do projeto: ")

#############################################################################################################################################################

html = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, user-scalable = no">
    <title>'''+projectName+'''</title>
    <!--Font-->
    <link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet">
    <!--Bootstrap-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!--Bootstrap Script-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>
    <!--CSS-->
    <link rel="Stylesheet" href="Css/sass.css">
    <link rel="icon" href="/images/favicon.ico">
    <!--JS Script-->
    <script src="script.js" defer></script>
</head>

<body>
    <h1>A</h1>
</body>

</html>'''

css = '''/* Mixins */

@mixin center-div{
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Body */

body {
    text-align: center;
    flex-direction: column;
    font-family: 'Righteous', sans-serif;
    height: 100vh;
}'''

scriptjs = '''console.log("teste")'''

##############################################################################################################################################################

os.mkdir(projectName)

os.chdir(f"./{projectName}/")

index = open("index.html","x")
index.write(html)
index.close

os.chdir('..')

os.mkdir(f"./{projectName}/images")
os.mkdir(f"./{projectName}/Css")

os.chdir(f"./{projectName}/Css")
sass = open("sass.scss","x")
sass.write(css)
sass.close

os.chdir('..')

js = open("script.js","x")
js.write(scriptjs)
js.close

print("Diretórios e arquivos criados")
input("Press Enter to continue...")
