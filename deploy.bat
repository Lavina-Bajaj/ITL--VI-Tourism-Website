@echo off
echo Starting Deployment...

git add .
git commit -m "Updated website"
git push origin main

echo Deployment Completed
pause