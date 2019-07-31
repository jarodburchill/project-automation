function New-React {
  param (
    [string]$projectName
  )

  Set-Location -Path L:\Projects
  npx create-react-app $projectName
  Set-Location $projectName

  pip install -r $PSScriptRoot\Requirements.txt
  python $PSScriptRoot\GitHub.py    

  git remote add origin https://github.com/$username/$repoName
  git push origin master

  code .
  npm start
}