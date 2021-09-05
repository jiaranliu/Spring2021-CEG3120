Setup:
Newrepo can be add by using bash git init followed with git add commit and push Or simply using github website to create a new repo
AWS get the keypaire first. And set the permission to 600  chmod 600 .pem. Run the aws enveriment. ssh -i .pem ubuntu@IP-address to get on the server
SSH key is in the .ssh/ folder

Usage:
git init --bare repo
git clone --berbose ubuntu@IP-address:repo
git add Project1
git commit (Comments adn ^X)
git push (With token)

Proof:

