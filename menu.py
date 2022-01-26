print('manin menu')
print('hello')

git config --global user.email "ratthaslip.booster@gmail.com"
git config --global user.email "iotinvationlab"

echo "# test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/iotinvationlab/test.git
git push -u origin main



