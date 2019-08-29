@ECHO OFF
cd /D %~dp0..
pip install -r requirements.txt
python automate_project.py