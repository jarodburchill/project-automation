@ECHO OFF
cd /D %~dp0..
pip install PyGithub >NUL
python automate-project.py