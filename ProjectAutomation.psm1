function New-React {
  param (
    [string]$projectName
  )

  $username = "jarodburchill" #GitHub username here

  $secured = Read-Host "Enter GitHub password" -AsSecureString
  $bstr = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secured)
  $password = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($bstr)

  $repoName = Read-Host "GitHub repository name"

  Set-Location -Path L:\Projects
  npx create-react-app $projectName
  Set-Location $projectName

  pip install -r requirements.txt
  python $PSScriptRoot\GitHub.py $username $password $repoName

  git remote add origin https://github.com/$username/$repoName
  git push origin master

  code .
  npm start
}