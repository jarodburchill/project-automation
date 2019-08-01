function New-React {
  param (
    [string]$projectName
  )

  $path = "L:/Projects/"
  Set-Location -Path $path
  npx create-react-app $projectName
  Set-Location $projectName
  git init

  pip install -r $PSScriptRoot\Requirements.txt
  python $PSScriptRoot\GitHub.py $path $projectName    

  git add *
  git commit -m "initial commit"
  git push origin master

  code .
  npm start
}