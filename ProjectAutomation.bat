set projectName="test"
set localPath="L:/Projects/"

cd /D %localPath%
npx create-react-app %projectName%
cd %projectName%
git init

pip install -r %~dp0Requirements.txt
python %~dp0GitHub.py %localPath% %projectName%    

git add *
git commit -m "initial commit"
git push origin master

PAUSE

code .
npm start


