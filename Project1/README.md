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
![image](https://user-images.githubusercontent.com/70781915/132114945-d44446ef-1734-4330-9efa-4674aded5279.png)

![image](https://user-images.githubusercontent.com/70781915/132114915-e0546e31-bbf0-40e0-aad2-771812028e93.png)
