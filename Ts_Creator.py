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
    <!--CSS-->
    <link rel="Stylesheet" href="Css/style.css">
    <!--JS Script-->
    <script src="script.js" defer></script>
</head>

<body>

</body>

</html>'''

cssf = '''*{  
    margin:0;
    padding: 0;
    border: 0;
}'''

scriptTs = ''''''

##############################################################################################################################################################

os.mkdir(projectName)
os.chdir(f"./{projectName}/")

os.mkdir(f"./{projectName}/dist")
os.chdir(f"./{projectName}/dist")
index = open("index.html","x")
index.write(html)
index.close

os.chdir('..')

os.mkdir(f"./{projectName}/Css")
os.chdir(f"./{projectName}/Css")
css = open("style.css","x")
css.write(cssf)
css.close

os.chdir('..')

os.mkdir(f"./{projectName}/src")
os.chdir(f"./{projectName}/src")
ts = open("script.ts","x")
ts.write(scriptTs)
ts.close

os.chdir('..')

print("Diretórios e arquivos criados")
input("Press Enter to continue...")


